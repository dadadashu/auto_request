__author__ ="peishuheng"
import unittest
import requests
from common.get_cookie import cookie
from os.path import abspath, dirname
import configparser as cparser
from db_fixture.postgresql_db import lyy_cmember
from db_fixture.postgresql_db import lyy_prod
from common.globalparam import now,future_time,base_url


# ======== Reading payload_config.ini setting ===========
base_dir = dirname(dirname(abspath(__file__)))
base_dir = base_dir.replace('\\', '/')
config = base_dir + "/common/payload_config.ini"
#ConfigParser 是用来读取配置文件的包
cf = cparser.ConfigParser()
cf.read(config,encoding='UTF-8')
SHJgroupIds = cf.get("SHJgroupIds", "SHJgroupIds")
WWJGroupId = cf.get("WWJGroupId", "WWJgroupId")

class Coupon(unittest.TestCase):
    ''' 商户优惠券 '''

    def setUp(self):
        self.cookie=cookie()

    def tearDown(self):
        print(self.result)

    def test_0_deleteOrStop(self):
        '''停止优惠券-售货机（初始化）'''
        url = base_url+"/marketing/distributor/coupon/deleteOrStop"

        couponId= lyy_cmember().lyy_query_order("lyy_distributor_coupon_id","lyy_distributor_coupon",
                                       "created DESC")
        payload={"flag":"s","couponId":couponId}
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_1_saveCoupon(self):
        '''优惠券保存与更新-售货机'''
        url = base_url+"/marketing/distributor/coupon/save"
        payload={
            "lyyDistributorCouponId":"",
            "type":1,
            "validFee":1.01,
            "amount":0.5,
            "payValidFee":1.01,
            "startDate":now,
            "endDate":future_time,
            "groupIds":eval(SHJgroupIds),
            "lyyEquipmentTypeId":[]
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,json=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
        self.assertEqual(self.result['description'], '保存成功')

    def test_2_saveCoupon(self):
        '''优惠券保存与更新-售货机-已存在'''
        url = base_url+"/marketing/distributor/coupon/save"
        payload={
            "lyyDistributorCouponId":"",
            "type":1,
            "validFee":1.01,
            "amount":0.5,
            "payValidFee":1.01,
            "startDate":now,
            "endDate":future_time,
            "groupIds":eval(SHJgroupIds),
            "lyyEquipmentTypeId":[]
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,json=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 102)
        self.assertEqual(self.result['description'], "包含不可用场地")


    def test_3_deleteOrStop(self):
        '''停止优惠券-售货机'''
        url = base_url+"/marketing/distributor/coupon/deleteOrStop"

        couponId= lyy_cmember().lyy_query_order("lyy_distributor_coupon_id","lyy_distributor_coupon",
                                       "created DESC")
        payload={"flag":"s","couponId":couponId}
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    # def test_9_deleteOrStop(self):
    #     '''删除优惠券-售货机'''
    #     url = base_url+"/marketing/distributor/coupon/deleteOrStop"
    #
    #     couponId= lyy_cmember().lyy_query_order("lyy_distributor_coupon_id","lyy_distributor_coupon",
    #                                    "created DESC")
    #     payload={"flag":"d","couponId":couponId}
    #     header = {'cookie': self.cookie,}
    #     r = requests.post(url,headers=header,data=payload)
    #     self.result = r.json()
    #     self.assertEqual(self.result['result'], 0)
    def test_4_deleteOrStopCoupon(self):
        '''删除优惠券-娃娃机（初始化）'''
        url = base_url+"/rest/distributorCoupon/deleteOrStopCoupon"
        couponId = lyy_prod().lyy_query_order("lyy_distributor_coupon_id","lyy_distributor_coupon","created DESC")
        print(couponId)
        payload={"flag":"d","couponId":couponId}
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_5_saveCoupon(self):
        '''优惠券保存与更新-娃娃机'''
        url = base_url+"/rest/distributorCoupon/saveCoupon"
        payload={
            "lyyDistributorCouponId":"",
            "equipmentGroupIds":WWJGroupId,
            "type":1,
            "validFee":1,
            "amount":2,
            "payValidFee":1,
            "startDate":now,
            "endDate":future_time
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,json=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
        self.assertEqual(self.result['description'], '保存成功')

    def test_6_saveCoupon(self):
        '''优惠券保存与更新-娃娃机-已存在'''
        url = base_url+"/rest/distributorCoupon/saveCoupon"
        payload={
            "lyyDistributorCouponId":"",
            "equipmentGroupIds":WWJGroupId,
            "type":1,
            "validFee":1,
            "amount":2,
            "payValidFee":1,
            "startDate":now,
            "endDate":future_time
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,json=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 102)
        self.assertEqual(self.result['description'], "包含不可用场地")

    def test_7_deleteOrStopCoupon(self):
        '''停止优惠券-娃娃机'''
        url = base_url+"/rest/distributorCoupon/deleteOrStopCoupon"
        couponId = lyy_prod().lyy_query_order("lyy_distributor_coupon_id","lyy_distributor_coupon","created DESC")
        # print(couponId)
        payload={"flag":"s","couponId":couponId}
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_8_deleteOrStopCoupon(self):
        '''删除优惠券-娃娃机'''
        url = base_url+"/rest/distributorCoupon/deleteOrStopCoupon"
        couponId = lyy_prod().lyy_query_order("lyy_distributor_coupon_id","lyy_distributor_coupon","created DESC")
        print(couponId)
        payload={"flag":"d","couponId":couponId}
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_9_deleteOrStopCoupon(self):
        '''删除现金券-娃娃机（初始化）'''
        url = base_url+"/rest/distributorCoupon/deleteOrStopCoupon"
        couponId = lyy_prod().lyy_query_order("lyy_distributor_coupon_id","lyy_distributor_coupon","created DESC")
        # print(couponId)
        payload={"flag":"d","couponId":couponId}
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_a_saveCoupon(self):
        '''现金券保存与更新-娃娃机'''
        url = base_url+"/rest/distributorCoupon/saveCoupon"
        payload={
            "lyyDistributorCouponId":"",
            "equipmentGroupIds":1045315,
            "type":2,
            "validFee":1,
            "amount":0.8,
            "payValidFee":1,
            "startDate":now,
            "endDate":future_time
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,json=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
        self.assertEqual(self.result['description'], '保存成功')

    def test_b_saveCoupon(self):
        '''现金券保存与更新-娃娃机-已存在'''
        url = base_url+"/rest/distributorCoupon/saveCoupon"
        payload={
            "lyyDistributorCouponId":"",
            "equipmentGroupIds":1045315,
            "type":2,
            "validFee":1,
            "amount":0.8,
            "payValidFee":1,
            "startDate":now,
            "endDate":future_time
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,json=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 102)
        self.assertEqual(self.result['description'], "包含不可用场地")

    def test_c_deleteOrStopCoupon(self):
        '''停止现金券-娃娃机'''
        url = base_url+"/rest/distributorCoupon/deleteOrStopCoupon"
        couponId = lyy_prod().lyy_query_order("lyy_distributor_coupon_id","lyy_distributor_coupon","created DESC")
        # print(couponId)
        payload={"flag":"s","couponId":couponId}
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_d_deleteOrStopCoupon(self):
        '''删除现金券-娃娃机'''
        url = base_url+"/rest/distributorCoupon/deleteOrStopCoupon"
        couponId = lyy_prod().lyy_query_order("lyy_distributor_coupon_id","lyy_distributor_coupon","created DESC")
        payload={"flag":"d","couponId":couponId}
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

if __name__ == '__main__':
    unittest.main()