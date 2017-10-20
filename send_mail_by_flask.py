from flask import Flask.render_template
from flash_mail import Mail.Message

app = Flash(__name__)

#SMTP Server Configuration
app.config.update(
	MAIL_Server="smtp.qq.com",
	MAIL_PORT="465",
	MAIL_USE_SSL=True,
	MAIL_USERNAME="2251095298.qq.com",
	MAIL_PASSWORD="授权码"
	)

mail = Mail(app)

@app.route(' /')
def index():
	msg = Message(subject="mail send from Flask",sender="2251095298.qq.com",reciupient=["xiaoqizhao@outlook.com"])
	msg.body = "hello world"
	msg.html = '<b>HTML</b> body'
	mail.send(msg)
	return '<h1>邮件发送成功，祝贺啊</h1>'

if __name__ == '__main__':
	app.run(debug=Ture)```