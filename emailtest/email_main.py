import email


def parse_eml_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        msg = email.message_from_file(f)

        # 获取邮件头信息  
        subject = msg.get('Subject')
        from_email = msg.get('From')

        # 获取邮件正文  
        # 注意：可能需要检查邮件的MIME类型来决定如何解析正文  
        body = ''
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=True).decode('utf-8')
                    # 如果邮件包含HTML部分，你也可以选择解析HTML
                elif part.get_content_type() == 'text/html':
                    # 使用HTML解析库如BeautifulSoup等  
                    pass
        else:
            body = msg.get_payload(decode=True).decode('utf-8')

        print(f"Subject: {subject}")
        print(f"From: {from_email}")
        print(f"Body: {body}")

    # 使用函数


parse_eml_file('ATT_003DF7.eml')