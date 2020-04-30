import sys, time
sys.path.append('../db_fixture')
try:
    from postgresql_db import consumption
except ImportError:
    from .postgresql_db import consumption
from db_fixture.postgresql_db import lyy_cmember
from db_fixture.postgresql_db import lyy_prod

# # 定义过去时间
# past_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()-100000))
#
# # 定义将来时间
# future_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()+10000))


#
def lyy_clear():
    consumption().lyy_clear('lyy_grant_coins',"description='接口数据初始化'")#初始化会员派币记录
    # lyy_cmember().lyy_clear('lyy_distributor_coupon',"valid_fee=1.01 and pay_valid_fee=1.01")#初始化优惠券-售货机
    # lyy_cmember().lyy_clear('lyy_distributor_coupon_group',"111111111111")

# #
# def lyy_query():
#     consumption().lyy_query_order("lyy_distributor_coupon_id","lyy_distributor_coupon","created DESC")
#     lyy_prod().lyy_query_order("amount","lyy_grant_coins","created DESC")


if __name__ == '__main__':
    lyy_clear()



