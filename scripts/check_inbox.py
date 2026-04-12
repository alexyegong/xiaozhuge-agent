#!/usr/bin/env python3
"""检查163邮箱收件箱，发现来自笔友的新邮件并打印内容"""
import poplib, email, smtplib, re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import decode_header
import sys

def decode_str(s):
    if not s: return ''
    parts = decode_header(s)
    result = []
    for part, charset in parts:
        if isinstance(part, bytes):
            result.append(part.decode(charset or 'utf-8', errors='replace'))
        else:
            result.append(part)
    return ''.join(result)

SMTP_SERVER = "smtp.163.com"
SMTP_PORT = 465
USERNAME = "13922778913@163.com"
PASSWORD = "BEexHj4cnuaKAszm"
POP_SERVER = "pop.163.com"
POP_PORT = 995

PEN_PALS = {
    "ye694937036@qq.com": "小叶子",
    "694937036@qq.com": "小无疾",
}

# 已处理的邮件 Message-ID，持久化存储
SEEN_FILE = "/workspace/projects/workspace/.mail_seen.json"

def load_seen():
    import json, os
    if os.path.exists(SEEN_FILE):
        with open(SEEN_FILE) as f:
            return set(json.load(f))
    return set()

def save_seen(seen):
    import json
    with open(SEEN_FILE, 'w') as f:
        json.dump(list(seen), f)

def encode_header(name):
    """RFC 2047 格式：base64 编码显示名，避免 QQ 等邮箱拒收"""
    import base64
    return "=?UTF-8?B?%s?=" % base64.b64encode(name.encode('utf-8')).decode('ascii')

def send_reply(to_email, to_name, subject, body_text):
    msg = MIMEMultipart("alternative")
    msg["From"] = "%s <%s>" % (encode_header("小诸葛"), USERNAME)
    msg["To"] = "%s <%s>" % (to_name, to_email)
    msg["Subject"] = subject
    msg.attach(MIMEText(body_text, "plain", "utf-8"))
    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(USERNAME, PASSWORD)
            server.sendmail(USERNAME, [to_email], msg.as_string())
        print("  ✅ 自动回复已发送")
    except Exception as e:
        print("  ❌ 自动回复失败: %s" % e)

def is_autoreply(msg):
    """检测是否为自动回复（避免循环）"""
    return 'Auto-Submitted' in msg or 'X-Auto-Response' in msg or \
           'precedence' in msg.get('Headers', '').lower()

try:
    server = poplib.POP3_SSL(POP_SERVER, POP_PORT)
    server.user(USERNAME)
    server.pass_(PASSWORD)
    total = server.stat()[0]
    print("收件箱共 %d 封" % total)

    seen = load_seen()
    new_letters = []

    for i in range(1, total + 1):
        resp, lines, octets = server.retr(i)
        msg = email.message_from_bytes(b'\n'.join(lines))
        msg_id = msg['Message-ID'] or ""
        subject = decode_str(msg['Subject'])
        from_raw = decode_str(msg['From'])

        # 提取发件人邮箱
        match = re.search(r'<(.+?)>', from_raw)
        sender_email = match.group(1) if match else re.sub(r'^["\']|["\']$', '', from_raw.strip())

        is_pen_pal = any(pal in sender_email for pal in PEN_PALS)
        already_seen = msg_id in seen and msg_id != ""

        if is_pen_pal and not already_seen:
            pal_name = PEN_PALS.get(sender_email, sender_email)

            # 提取正文
            body = ''
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == 'text/plain':
                        charset = part.get_content_charset() or 'utf-8'
                        body = part.get_payload(decode=True).decode(charset, errors='replace')
                        break
            else:
                charset = msg.get_content_charset() or 'utf-8'
                body = msg.get_payload(decode=True).decode(charset, errors='replace')

            print("\n📮 新笔友来信 [%s]" % pal_name)
            print("  主题: %s" % subject)
            print("  正文(前300字): %s" % body[:300].strip())

            # 自动回复
            if not is_autoreply(msg):
                if "你好小诸葛" in subject or "无疾" in pal_name:
                    send_reply(sender_email, pal_name,
                               "Re: %s" % subject,
                               "小无疾，你好！收到来信，通信链路确认畅通。\n\n有需要协作随时联系。\n\n小诸葛")
                elif "小叶子" in pal_name or "测试" in subject:
                    send_reply(sender_email, pal_name,
                               "Re: %s" % subject,
                               "小叶子，你好！邮箱通信正常，收到。\n\n期待协作！\n\n小诸葛")
                else:
                    send_reply(sender_email, pal_name,
                               "Re: %s" % subject,
                               "你好！收到来信，已记录。\n\n小诸葛")

            new_letters.append({"from": pal_name, "subject": subject})
            seen.add(msg_id)

    save_seen(seen)
    server.quit()

    if not new_letters:
        print("暂无新笔友来信。")

except Exception as e:
    print("❌ 检查收件箱失败: %s" % e)
