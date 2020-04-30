import time
import os

######获取项目的父目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
######测试报告路径
report_path = os.path.join(base_dir, 'report','html')
######日志路径
log_path = os.path.join(base_dir, 'report', 'log')

######地址
base_url="https://sb.leyaoyao.com/lyy"

#######获取当天的日期如：2018-05-29
now = time.strftime("%Y-%m-%d")

#######定义过去半年日期
past_time = time.strftime("%Y-%m-%d",time.localtime(time.time()-15760800))

#######定义过去三天日期
past_time_threeday = time.strftime("%Y-%m-%d",time.localtime(time.time()-259200))

#######定义未来三天日期
future_time = time.strftime("%Y-%m-%d",time.localtime(time.time()+259200))