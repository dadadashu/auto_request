#coding:utf-8

import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.log import Log
from common import globalparam

# 测试报告的路径
reportPath = globalparam.report_path
logger = Log()
# 配置收发件人
recvaddress =['test1@xxx.com','test2@xxx.com']

# 发件人的用户名和密码
sendaddr_name = 'aaa@xxx.com'
sendaddr_pswd = 'xxxx'

class SendMail:
	def __init__(self,recver=None):
		"""接收邮件的人：list or tuple"""
		if recver is None:
			self.sendTo = recvaddress
		else:
			self.sendTo = recver

	def __get_report(self):
		"""获取最新测试报告"""
		dirs = os.listdir(reportPath)
		dirs.sort()
		newreportname = dirs[-1]
		print('The new report name: {0}'.format(newreportname))
		return newreportname

	def __take_messages(self):
		"""生成邮件的内容，和html报告附件"""
		now = time.strftime("%Y-%m-%d %H_%M_%S")
		newreport = self.__get_report()
		self.msg = MIMEMultipart()
		self.msg['Subject'] = 'Request_Report_B '+now
		self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

		with open(os.path.join(reportPath,newreport), 'rb') as f:
			mailbody = f.read()
		html = MIMEText(mailbody,_subtype='html',_charset='utf-8')
		self.msg.attach(html)

		# html附件
		now = time.strftime("%Y-%m-%d %H_%M_%S")
		att1 = MIMEText(mailbody, 'base64', 'gb2312')
		att1["Content-Type"] = 'application/octet-stream'
		att1["Content-Disposition"] = 'attachment; filename="Request_Report_B {t}.html"'.format(t=now)
		#这里的filename可以任意写，写什么名字，邮件中显示什么名字
		self.msg.attach(att1)

	def send(self):
		"""发送邮件"""
		self.__take_messages()
		self.msg['from'] = sendaddr_name
		try:
			smtp = smtplib.SMTP('imap.exmail.qq.com',25)
			smtp.login(sendaddr_name,sendaddr_pswd)
			smtp.sendmail(self.msg['from'], self.sendTo,self.msg.as_string())
			smtp.close()
			logger.info("发送邮件成功")
		except Exception:
			logger.error('发送邮件失败')
			raise

if __name__ == '__main__':
	sendMail = SendMail()
	sendMail.send()

        
