from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

class send_email:
    def __init__(self):
        self.from_addr = "yanlinyyds@qq.com"
        self.password = "xywevwzhxcaubajj"
        self.to_addr = "1730933627@qq.com"
        self.smtp_server = "smtp.qq.com"

    def _format_addr(self,s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def send_out(self,par):
        html_body = """
                    <html>
                        <head>
                            <style>
                                .data{
                                    min-width: 300px;
                                    display: block;
                                    float: left;
                                    background-color: #F8F8FF;
                                    border-radius: 10px;
                                    margin: 20px 15px 20px 15px;
                                    padding: 20px 50px;
                                    box-shadow: 0 0 5px white;
                                    transform: scale(1);
                                    transition-property: transform box-shadow;
                                    transition-duration: 0.5s;
                                    transition-timing-function: ease-in-out;
                                }
                                .data:hover{
                                    transform: scale(1.02);
                                    box-shadow: 0 0 5px #00BFFF;
                                    transition-property: transform box-shadow;
                                    transition-duration: 0.5s;
                                    transition-timing-function: ease-in-out;
                                }
                                .data #title{
                                    user-select: none;
                                    width: 100px;
                                    font-size: 24px;
                                    font-weight: bold;
                                    display: inline-block;
                                    padding: 2px 0;
                                }
                                .data #word{
                                    padding: 2px 0;
                                    font-size: 20px;
                                    display: inline-block;
                                }
                            </style>
                        </head>
                        <body>
                            <div class="data">
                                <div id="title">类型：</div><div id="word"><p>%s</p></div><br>
                                <div id="title">名称：</div><div id="word"><p>%s</p></div><br>
                                <div id="title">邮箱：</div><div id="word"><p>%s</p></div><br>
                                <div id="title">文本：</div><div id="word"><p>%s</p></div><br>
                                <div id="title">时间：</div><div id="word"><p>%s</p></div><br>
                            </div>
                        </body>
                    </html>
                    """ % (par[0],par[1],par[2],par[3],par[4])
        msg = MIMEText(html_body, _subtype='html', _charset='utf-8')
        msg['From'] = send_email()._format_addr('Blog_Mail <%s>' % self.from_addr)
        msg['To'] = send_email()._format_addr('管理员 <%s>' % self.to_addr)
        msg['Subject'] = Header('来自{}的信息~'.format(par[2]), 'utf-8').encode()
            
        server = smtplib.SMTP_SSL(self.smtp_server, 465)
        server.set_debuglevel(1)
        try:
            server.login(self.from_addr, self.password)
            server.sendmail(self.from_addr, [self.to_addr], msg.as_string())
        except:
            print("邮件发送失败!")
            return 404
        server.quit()
