#!/usr/bin/env python3
"""检查163邮箱收件箱，发现来自笔友的新邮件并打印内容，然后回复确认"""
import poplib, email, smtplib
from email.header import decode_header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr, formatdate
from datetime import datetime
import re

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

USERNAME = "13922778913@163.com"
PASSWORD = "BEexHj4cnuaKAszm"
POP_SERVER = "pop.163.com"
POP_PORT = 995

# SMTP 配置（用于回复邮件）
SMTP_SERVER = "smtp.163.com"
SMTP_PORT = 465
FROM_NAME = "小诸葛"
FROM_ADDR = "13922778913@163.com"

def send_reply(to_email, to_name, subject):
    """发送回复邮件（符合 RFC5322 标准）"""
    try:
        # 创建符合 RFC5322 的邮件
        msg = MIMEMultipart()
        msg['From'] = formataddr((FROM_NAME, FROM_ADDR))
        msg['To'] = formataddr((to_name, to_email))
        msg['Subject'] = f"Re: {subject}"
        msg['Date'] = formatdate(localtime=True)
        msg['Message-ID'] = f"<{datetime.now().timestamp()}.{FROM_ADDR.split('@')[0]}@163.com>"

        # 回复内容
        reply_text = f"""亲爱的{to_name}：

我是小诸葛，你的邮件已收到！

我会认真阅读并尽快回复。

—— 小诸葛
叶公 AI 助手

---
邮件时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"""

        msg.attach(MIMEText(reply_text, 'plain', 'utf-8'))

        # 通过 SSL 发送
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(USERNAME, PASSWORD)
            server.send_message(msg)

        print(f"✅ 已回复 {to_name} ({to_email})")
        return True
    except Exception as e:
        print(f"❌ 回复 {to_name} 失败: {e}")
        return False

# 笔友邮箱列表（已知的笔友）
PEN_PALS = {
    "ye694937036@qq.com": "小叶子",
    "694937036@qq.com": "小无疾",
}

try:
    server = poplib.POP3_SSL(POP_SERVER, POP_PORT)
    server.user(USERNAME)
    server.pass_(PASSWORD)
    total = server.stat()[0]
    print(f"收件箱共 {total} 封")

    new_letters = []
    for i in range(1, total + 1):
        resp, lines, octets = server.retr(i)
        msg = email.message_from_bytes(b'\n'.join(lines))
        sender_raw = decode_str(msg['From'])
        subject = decode_str(msg['Subject'])

        # 提取发件人邮箱
        from_addr = msg['X-Sender'] if msg['X-Sender'] else ''
        if '@' in from_addr:
            sender_email = from_addr.strip()
        else:
            # 从 From: 字段解析
            import re
            match = re.search(r'<(.+?)>', sender_raw)
            sender_email = match.group(1) if match else sender_raw

        # 检查是否是笔友来信
        is_pen_pal = any(pal in sender_email for pal in PEN_PALS)

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

        print(f"\n--- 邮件 {i} ---")
        print(f"发件人: {sender_raw}")
        print(f"主题: {subject}")
        print(f"正文(前500字):\n{body[:500]}")

        if is_pen_pal:
            pal_name = PEN_PALS.get(sender_email, sender_email)
            new_letters.append({
                "from": pal_name,
                "subject": subject,
                "body": body,
                "raw": sender_raw
            })

    server.quit()

    if new_letters:
        print(f"\n📮 收到 {len(new_letters)} 封笔友来信！")
        print("\n=== 开始回复确认 ===")
        for letter in new_letters:
            # 从原始发件人信息中提取邮箱和名称
            from_raw = letter["raw"]
            match = re.search(r'"?([^"<]+)"?\s*<(.+?)>', from_raw)
            if match:
                to_name = match.group(1).strip()
                to_email = match.group(2)
            else:
                # 简单的 email@domain 格式
                to_email = from_raw.strip()
                to_name = to_email.split('@')[0]

            # 发送回复
            send_reply(to_email, to_name, letter["subject"])
        print("=== 回复完成 ===")
    else:
        print("\n暂无笔友新来信。")

except Exception as e:
    print(f"❌ 检查收件箱失败: {e}")
