#!/usr/local/bin/python3.7
import glob,os
import time, sys
sys.path.append('./testcase')
sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader
from db_fixture import test_data
from common import sendmail
from common import globalparam
from os.path import abspath, dirname


# 指定测试用例为当前文件夹下的 testcase 目录
test_dir = './testcase'
#TestLoader 类中提供的discover（）方法可以自动识别测试用例
#test_dir：要测试的测试用例目录
#pattern='test*.py'：表示用例文件名的匹配原则。此处匹配以“test”开头的.py 类型的文件，* 表示任意多个字符
testsuit = defaultTestLoader.discover(test_dir, pattern='*_test.py')
# 测试报告路径
reportPath = globalparam.report_path
logpath=globalparam.log_path

def delhtml(reportPath):
    '''删除旧的html报告'''
    #读取文件夹下的所有文件
    fileNames = glob.glob(reportPath + r'/*')
    for fileName in fileNames:
        try:
            #删除文件
            os.remove( fileName)
        except:
            try:
                #删除空文件夹
                os.rmdir( fileName)
            except:
                #文件夹不为空，删除文件夹下的文件
                delhtml( fileName)
                #文件夹为空之后，删除文件夹
                os.rmdir( fileName)

def dellog(logpath):
    '''删除旧的log'''
    #读取文件夹下的所有文件
    fileNames = glob.glob(logpath + r'/*')
    for fileName in fileNames:
        try:
            #删除文件
            os.remove( fileName)
        except:
            try:
                #删除空文件夹
                os.rmdir( fileName)
            except:
                #文件夹不为空，删除文件夹下的文件
                dellog( fileName)
                #文件夹为空之后，删除文件夹
                os.rmdir( fileName)

def run():
    '''运行测试用例、生成报告并发送邮件'''
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    reportname = reportPath + '\\' + 'Request_Report_B '+ now+ '.html'
    reportname=reportname.replace('\\', '/')
    fp = open(reportname, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='B端接口自动化测试',
                            description='运行环境：PostgreSQL(psycopg2), Requests, unittest ')
    # discover（）方法会自动根据测试目录test_dir匹配查找测试用例文件，并将查找到的测试用例组装到测试套件中，
    # 因此，可以直接通过run()方法执行testsuit，大大简化了测试用例的查找与执行
    runner.run(testsuit)
    fp.close()
    time.sleep(2)
    # 发送邮件
    mail = sendmail.SendMail()
    mail.send()

if __name__ == "__main__":
    delhtml(reportPath)
    dellog(logpath)
    test_data.lyy_clear()#清除测试数据
    run()
    # test_data.lyy_clear()#清除测试数据