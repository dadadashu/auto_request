__author__ ="peishuheng"
import unittest
import requests
from common.get_cookie import cookie
from os.path import abspath, dirname
import configparser as cparser
from common.globalparam import now,past_time,base_url


# ======== Reading payload_config.ini setting ===========
base_dir = dirname(dirname(abspath(__file__)))
base_dir = base_dir.replace('\\', '/')
config = base_dir + "/common/payload_config.ini"
#ConfigParser 是用来读取配置文件的包
cf = cparser.ConfigParser()
cf.read(config,encoding='UTF-8')
WWJEquipmentId = cf.get("WWJEquipmentId", "WWJEquipmentId")
WWJGroupId = cf.get("WWJGroupId", "WWJgroupId")
DBJEquipmentId = cf.get("DBJEquipmentId", "DBJEquipmentId")
DBJGroupId = cf.get("DBJGroupId", "DBJgroupId")
SHJEquipmentId = cf.get("SHJEquipmentId", "SHJEquipmentId")
SHJGroupId = cf.get("SHJGroupId", "SHJGroupId")



class onlinePayDetail(unittest.TestCase):
    ''' 在线支付统计 '''
    def setUp(self):
        self.cookie=cookie()

    def tearDown(self):
        print(self.result)

    def test_1_onlinePayDetail(self):
        '''在线支付明细'''
        url = base_url+"/rest/benefitAnalysis/onlinePayDetail"
        payload={
            "startDate":past_time,
            "endDate":now,
            "groupId":WWJGroupId,
            "equipmentIds":WWJEquipmentId,
            "pageIndex":1,
            "pageSize":10
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
        self.assertEqual(self.result['data']['items'][0]['status'], 'SUCCESS')

class onlinepayment(unittest.TestCase):
    ''' 在线收益 '''
    def setUp(self):
        self.cookie=cookie()

    def tearDown(self):
        print(self.result)

    def test_1_dbjpayment(self):
        '''获取兑币机在线支付详情'''
        url = base_url+"/rest/benefitAnalysis/group/equipment/benefit/dbj/payment"
        payload={
            "startDate":past_time,
            "endDate":now,
            "groupId":DBJGroupId,
            "equipmentIds":DBJEquipmentId,
            "pageIndex":1,
            "pageSize":10
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_2_dbjcoins(self):
        '''获取兑币机收益明细'''
        url = base_url+"/rest/benefitAnalysis/group/equipment/benefit/dbj/coins"
        payload={
            "startDate":past_time,
            "endDate":now,
            "groupId":DBJGroupId,
            "equipmentIds":DBJEquipmentId,
            "pageIndex":1,
            "pageSize":10
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_3_benefitonline(self):
        '''获取在线收益（在线支付 + 广告收益）'''
        url = base_url+"/rest/benefitAnalysis/group/equipment/benefit/online"
        payload={
            "startDate":past_time,
            "endDate":now,
            "groupId":WWJGroupId,
            "equipmentIds":WWJEquipmentId,
            "pageIndex":1,
            "pageSize":10
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
        self.assertNotEqual(self.result['data']['income_count'], None)

    def test_4_benefit_undbj(self):
        '''获取非兑币机收益明细-广告收益'''
        url = base_url+"/rest/benefitAnalysis/group/equipment/benefit/undbj"
        payload={
            "startDate":past_time,
            "endDate":now,
            "groupId":WWJGroupId,
            "equipmentIds":WWJEquipmentId,
            "pageIndex":1,
            "pageSize":10,
            "type":"AD"
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
        self.assertNotEqual(self.result['data']['items'][0]["income"], None)

    def test_5_benefit_undbj(self):
        '''获取非兑币机收益明细-在线支付'''
        url = base_url+"/rest/benefitAnalysis/group/equipment/benefit/undbj"
        payload={
            "startDate":past_time,
            "endDate":now,
            "groupId":WWJGroupId,
            "equipmentIds":WWJEquipmentId,
            "pageIndex":1,
            "pageSize":10,
            "type":"PAY"
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
        self.assertNotEqual(self.result['data']['items'][0]["title"], None)

    def test_6_benefit_undbj(self):
        '''获取仓位在线收益-广告收益'''
        url = base_url+"/rest/benefitAnalysis/group/equipment/benefit/mb"
        payload={
            "startDate":past_time,
            "endDate":now,
            "groupId":SHJGroupId,
            "equipmentIds":SHJEquipmentId,
            "pageIndex":1,
            "pageSize":10,
            "type":"AD",
            "positionId":1
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_7_benefit_undbj(self):
        '''获取仓位在线收益-游戏支付'''
        url = base_url+"/rest/benefitAnalysis/group/equipment/benefit/mb"
        payload={
            "startDate":past_time,
            "endDate":now,
            "groupId":SHJGroupId,
            "equipmentIds":SHJEquipmentId,
            "pageIndex":1,
            "pageSize":10,
            "type":"GAME",
            "positionId":1
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_8_benefit_undbj(self):
        '''获取仓位在线收益-购买支付'''
        url = base_url+"/rest/benefitAnalysis/group/equipment/benefit/mb"
        payload={
            "startDate":past_time,
            "endDate":now,
            "groupId":SHJGroupId,
            "equipmentIds":SHJEquipmentId,
            "pageIndex":1,
            "pageSize":10,
            "type":"BUY",
            "positionId":1
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

class benefitAnalysis_ad(unittest.TestCase):
    ''' 广告收益统计 '''
    def setUp(self):
        self.cookie=cookie()


    def tearDown(self):
        print(self.result)

    def test_1_benefitAnalysis_ad(self):
        '''广告收益明细'''
        url = base_url+"/rest/benefitAnalysis/adIncomeDetail"
        payload={
            "startDate":past_time,
            "endDate":now,
            "groupId":WWJGroupId,
            "equipmentIds":WWJEquipmentId,
            "pageIndex":1,
            "pageSize":10,
            "type":"PAY"
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
        self.assertNotEqual(self.result['data']['items'][0]["total_fee"], None)

class coins_statistical(unittest.TestCase):
    ''' 现金兑币统计 '''
    def setUp(self):
        self.cookie=cookie()

    def tearDown(self):
        print(self.result)

    def test_1_coinstotal(self):
        '''现金兑币总次数'''
        url = base_url+"/rest/benefitAnalysis/coins/total"
        payload={
            "startDate":past_time,
            "endDate":now,
            "groupId":DBJGroupId,
            "equipmentIds":DBJEquipmentId
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
        self.assertNotEqual(self.result['data'], None)

    def test_2_coins_details(self):
        '''现金兑币明细'''
        url = base_url+"/rest/benefitAnalysis/coins/details"
        payload={
            "startDate":past_time,
            "endDate":now,
            "groupId":DBJGroupId,
            "equipmentIds":DBJEquipmentId,
            "pageIndex":1,
            "pageSize":10,
            "type":"PAY"
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
        self.assertNotEqual(self.result['data']['items'][0]["total_fee"], None)

    def test_3_coins_sum(self):
        '''获取现金兑币总金额'''
        url = base_url+"/rest/benefitAnalysis/coins/sum"
        payload={
            "startDate":past_time,
            "endDate":now,
            "groupId":DBJGroupId,
            "equipmentIds":DBJEquipmentId
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
        self.assertNotEqual(self.result['data'], None)

class coins_statistical(unittest.TestCase):
    ''' 礼品消耗统计 '''
    def setUp(self):
        self.cookie=cookie()

    def tearDown(self):
        print(self.result)

    def test_1_giftConsume(self):
        '''获取礼品消耗'''
        url = base_url+"/rest/benefitAnalysis/giftConsume"
        payload={
            "startDate":past_time,
            "endDate":now,
            "groupId":WWJGroupId,
            "equipmentIds":WWJEquipmentId
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_2_transaction(self):
        '''获取礼品消耗明细（新）'''
        url = base_url+"/rest/benefitAnalysis/group/equipment/material/transaction"
        payload={
            "startDate":past_time,
            "endDate":now,
            "groupId":WWJGroupId,
            "equipmentIds":WWJEquipmentId,
            "pageSize":1,
            "pageIndex":10
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

class onlineStart_statistical(unittest.TestCase):
    ''' 线上启动统计 '''
    def setUp(self):
        self.cookie=cookie()

    def tearDown(self):
        print(self.result)

    def test_1_onlineStart_details(self):
        '''线上启动记录明细'''
        url = base_url+"/rest/benefitAnalysis/onlineStart/details"
        payload={
            "startDate":past_time,
            "endDate":now,
            "groupId":WWJGroupId,
            "equipmentIds":WWJEquipmentId,
            "pageSize":1,
            "pageIndex":1
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
    @unittest.skip("未调试完成")
    def test_2_onlineStartCount(self):
        '''获取线上启动次数'''
        url = base_url+"/rest/benefitAnalysis/onlineStartCount"
        payload={
            "startDate":past_time,
            "endDate":now,
            "groupId":WWJGroupId,
            "equipmentIds":WWJEquipmentId
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
    @unittest.skip("未调试完成")
    def test_3_equipmentStartDetail(self):
        '''设备启动详情'''
        url = base_url+"/rest/group/distributor/equipmentStartDetail"
        payload={
            "startDate":past_time,
            "endDate":now,
            "id":WWJGroupId,
            "type":"WWJ",
            "pageSize":1,
            "pageIndex":1
            }
        header = {'cookie': self.cookie}
        r = requests.get(url,headers=header,params=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

class benefitAnalysis_coins_online(unittest.TestCase):
    ''' 获取线上投币统计 '''
    def setUp(self):
        self.cookie=cookie()

    def tearDown(self):
        print(self.result)

    def test_1_coins_online(self):
        '''获取线上投币明细'''
        url = base_url+"/rest/benefitAnalysis/group/equipment/coins/online"
        payload={
            "startDate":past_time,
            "endDate":now,
            "groupId":WWJGroupId,
            "equipmentIds":WWJEquipmentId,
            "pageSize":10,
            "pageIndex":1
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

class benefitAnalysis_coins_benefit(unittest.TestCase):
    ''' 获取线下投币统计 '''
    def setUp(self):
        self.cookie=cookie()

    def tearDown(self):
        print(self.result)

    def test_1_coins_benefit(self):
        '''获取现金收益记录'''
        url = base_url+"/rest/benefitAnalysis/group/equipment/benefit/coins"
        payload={
            "startDate":past_time,
            "endDate":now,
            "groupId":DBJGroupId,
            "equipmentIds":DBJEquipmentId,
            "pageSize":10,
            "pageIndex":1
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_1_coins_online(self):
        '''获取线下投币记录'''
        url = base_url+"/rest/benefitAnalysis/coins/details"
        payload={
            "startDate":past_time,
            "endDate":now,
            "groupId":WWJGroupId,
            "equipmentIds":WWJEquipmentId,
            "pageSize":10,
            "pageIndex":1
            }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)



if __name__ == '__main__':
    unittest.main()