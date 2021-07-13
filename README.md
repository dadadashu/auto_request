# auto_request
基于unittest+requests+HTMLTestRunner搭建的接口自动化测试框架
技术栈：python 3.7 + requests + unittest

依赖库：
pip3 install requests==2.22.0
另外还要安装你项目对应的数据库依赖

包含功能:
  * 对数据的查询和删除做了封装，用于验证数据和测试数据初始化。
      * unittest单元测试框架运行测试
  * HTMLTestRunner生成接口测试报告
  * 邮件发送html测试报告

目录说明：

--common

  db_config.ini 数据库配置文件
  get_cookie.py 获取登录的cookie.yaml，用于测试用例的调用
  get_userid.py 获取登录的userid.yaml，用于测试用例的调用
  globalparam.py 定义全局变量
  log.py 日志配置文件
  payload_config.ini 测试用例参数配置文件
  sendmail.py 发送邮件配置文件

--db_fixture

  postgresql_db.py 数据库的连接和基本操作的封装
  test_data.py 数据库的清除方法

--report 

html测试报告和邮件发送成功与否日志

--testcase 

测试用例


--run_tests.py 

运行主文件
