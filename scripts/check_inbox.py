#!/usr/bin/env python3
"""检查163邮箱收件箱，发现来自笔友的新邮件并打印内容"""
import poplib, email
from email.header import decode_header
from datetime import datetime

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
    else:
        print("\n暂无笔友新来信。")

except Exception as e:
    print(f"❌ 检查收件箱失败: {e}")
