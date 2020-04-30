__author__ ="peishuheng"
import unittest
import requests
from common.get_cookie import cookie
from os.path import abspath, dirname
import configparser as cparser
from common.globalparam import now,future_time,base_url
import json
from db_fixture.postgresql_db import lyy_prod
from db_fixture.postgresql_db import lyy_cmember

# ======== Reading payload_config.ini setting ===========
base_dir = dirname(dirname(abspath(__file__)))
base_dir = base_dir.replace('\\', '/')
config = base_dir + "/common/payload_config.ini"
#ConfigParser 是用来读取配置文件的包
cf = cparser.ConfigParser()
cf.read(config,encoding='UTF-8')
SHJgroupIds = cf.get("SHJgroupIds", "SHJgroupIds")
WWJGroupIds = cf.get("WWJGroupIds", "WWJgroupIds")



class Discount(unittest.TestCase):
    ''' 商户自建支付优惠活动 '''

    def setUp(self):
        self.cookie=cookie()

    def tearDown(self):
        print(self.result)

    def test_0_updateDistributorDiscountStatus(self):
        '''更新娃娃机用户活动任务状态-随机币(已终止)（初始化）'''
        url = base_url+"/rest/distributor_discount/updateDistributorDiscountStatus"
        lyy_distributor_discount_id=lyy_prod().lyy_query_order('lyy_distributor_discount_id',
                                                              'lyy_distributor_discount','created desc')
        payload={
            "lyy_distributor_discount_id":lyy_distributor_discount_id,
            "status":3
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_1_saveDistributorDiscount(self):
        '''保存娃娃机用户活动任务-随机币'''
        url = base_url+"/rest/distributor_discount/saveDistributorDiscount"
        payload={
            "minusMin":1,
            "minusMax":10,
            "validFee":1,
            "total":200,
            "beginTimeStr":now,
            "endTimeStr":future_time,
             "discountType":3,
            "discountSecondType":2,
            "userDiscountCount":"",
            "groups":eval(WWJGroupIds)
            }
        header = {'cookie': self.cookie,'Content-Type':'application/json'}
        r = requests.post(url,headers=header,data=json.dumps(payload))
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_2_saveDistributorDiscount(self):
        '''保存娃娃机用户活动任务-随机币-已存在'''
        url = base_url+"/rest/distributor_discount/saveDistributorDiscount"
        payload={
            "minusMin":1,
            "minusMax":10,
            "validFee":1,
            "total":200,
            "beginTimeStr":now,
            "endTimeStr":future_time,
             "discountType":3,
            "discountSecondType":2,
            "userDiscountCount":"",
            "groups":eval(WWJGroupIds)
            }
        header = {'cookie': self.cookie,'Content-Type':'application/json'}
        r = requests.post(url,headers=header,data=json.dumps(payload))
        self.result = r.json()
        self.assertEqual(self.result['result'],102)
        self.assertEqual(self.result['description'],"已有部分场地开展活动")

    def test_3_updateDistributorDiscountStatus(self):
        '''更新娃娃机用户活动任务状态-随机币(已终止)'''
        url = base_url+"/rest/distributor_discount/updateDistributorDiscountStatus"
        lyy_distributor_discount_id=lyy_prod().lyy_query_order('lyy_distributor_discount_id',
                                                              'lyy_distributor_discount','created desc')
        payload={
            "lyy_distributor_discount_id":lyy_distributor_discount_id,
            "status":3
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_4_updateDistributorDiscountStatus(self):
        '''更新娃娃机用户活动任务状态-随机币(已删除)'''
        url = base_url+"/rest/distributor_discount/updateDistributorDiscountStatus"
        lyy_distributor_discount_id=lyy_prod().lyy_query_order('lyy_distributor_discount_id',
                                                              'lyy_distributor_discount','created desc')
        payload={
            "lyy_distributor_discount_id":lyy_distributor_discount_id,
            "status":4
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_5_discountupdateStatus(self):
        '''更新售货机用户活动任务状态(已终止)（初始化）'''
        url = base_url+"/marketing/distributor/discount/updateStatus"
        lyyDistributorDiscountId=lyy_cmember().lyy_query_order('lyy_distributor_discount_id',
                                                              'lyy_distributor_discount','created desc')
        payload={
            "lyyDistributorDiscountId":lyyDistributorDiscountId,
            "status":3
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_6_saveDistributorDiscount(self):
        '''保存娃娃机用户活动任务-固定币'''
        url = base_url+"/rest/distributor_discount/saveDistributorDiscount"
        payload={
            "minusMin":0,
            "minusMax":10,
            "validFee":1,
            "total":200,
            "beginTimeStr":now,
            "endTimeStr":future_time,
             "discountType":3,
            "discountSecondType":1,
            "userDiscountCount":"",
            "groups":eval(WWJGroupIds)
            }
        header = {'cookie': self.cookie,'Content-Type':'application/json'}
        r = requests.post(url,headers=header,data=json.dumps(payload))
        self.result = r.json()
        self.lyy_distributor_discount_id=lyy_prod().lyy_query_order('lyy_distributor_discount_id',
                                                              'lyy_distributor_discount','created desc')
        globals()["lyy_distributor_discount_id"] = self.lyy_distributor_discount_id
        self.assertEqual(self.result['result'], 0)

    def test_7_saveDistributorDiscount(self):
        '''保存娃娃机用户活动任务-固定币-已存在'''
        url = base_url+"/rest/distributor_discount/saveDistributorDiscount"
        payload={
            "minusMin":0,
            "minusMax":10,
            "validFee":1,
            "total":200,
            "beginTimeStr":now,
            "endTimeStr":future_time,
             "discountType":3,
            "discountSecondType":1,
            "userDiscountCount":"",
            "groups":eval(WWJGroupIds)
            }
        header = {'cookie': self.cookie,'Content-Type':'application/json'}
        r = requests.post(url,headers=header,data=json.dumps(payload))
        self.result = r.json()
        self.assertEqual(self.result['result'],102)
        self.assertEqual(self.result['description'],"已有部分场地开展活动")


    def test_8_updateDistributorDiscountStatus(self):
        '''更新娃娃机用户活动任务状态-固定币(已终止)'''
        url = base_url+"/rest/distributor_discount/updateDistributorDiscountStatus"

        payload={
            "lyy_distributor_discount_id":globals()["lyy_distributor_discount_id"],
            "status":3
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_9_updateDistributorDiscountStatus(self):
        '''更新娃娃机用户活动任务状态-固定币(已删除)'''
        url = base_url+"/rest/distributor_discount/updateDistributorDiscountStatus"
        payload={
            "lyy_distributor_discount_id":globals()["lyy_distributor_discount_id"],
            "status":4
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_a_discountsave(self):
        '''保存售货机用户活动任务'''
        url = base_url+"/marketing/distributor/discount/save"
        payload={
            "minusMin":1,
            "minusMax":10,
            "validFee":11,
            "total":200,
            "beginTimeStr":now,
            "endTimeStr":future_time,
             "discountType":1,
            "discountSecondType":2,
            "userDiscountCount":"",
            "groupIds":eval(SHJgroupIds),
            "lyyEquipmentTypeIds":[]
            }
        header = {'cookie': self.cookie,'Content-Type':'application/json'}
        r = requests.post(url,headers=header,data=json.dumps(payload))
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_b_discountupdateStatus(self):
        '''更新售货机用户活动任务状态(已终止)'''
        url = base_url+"/marketing/distributor/discount/updateStatus"
        lyyDistributorDiscountId=lyy_cmember().lyy_query_order('lyy_distributor_discount_id',
                                                              'lyy_distributor_discount','created desc')
        payload={
            "lyyDistributorDiscountId":lyyDistributorDiscountId,
            "status":3
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

if __name__ == '__main__':
    unittest.main()