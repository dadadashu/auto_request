__author__ ="peishuheng"
import unittest
import requests
import json
from common.get_cookie import cookie
from os.path import abspath, dirname
import configparser as cparser
from common.globalparam import base_url


# ======== Reading payload_config.ini setting ===========
base_dir = dirname(dirname(abspath(__file__)))
base_dir = base_dir.replace('\\', '/')
config = base_dir + "/common/payload_config.ini"
#ConfigParser 是用来读取配置文件的包
cf = cparser.ConfigParser()
cf.read(config,encoding='UTF-8')
WWJGroupId = cf.get("WWJGroupId", "WWJgroupId")
WWJGroupIds= cf.get("WWJGroupIds", "WWJGroupIds")
DBJGroupIds= cf.get("DBJGroupIds", "DBJGroupIds")
CDZGroupIds= cf.get("CDZGroupIds", "CDZGroupIds")
ETLGroupIds= cf.get("ETLGroupIds", "ETLGroupIds")
AMYGroupIds= cf.get("AMYGroupIds", "AMYGroupIds")
SHJgroupIds= cf.get("SHJgroupIds", "SHJgroupIds")

class Discount(unittest.TestCase):
    ''' 优惠设置 '''

    def setUp(self):
        self.cookie=cookie()

    def tearDown(self):
        print(self.result)

    def test_1_saveBatchDiscount(self):
        '''娃娃机保存批量优惠设置'''
        url = base_url+"/rest/discount/saveBatchDiscount"
        payload={
            "groupList":eval(WWJGroupIds),
            "type":3,
            "isBatch":False,
            "lyyEquipmentTypeId":[1000001],
            "consumeMode":1,
            "WWJRuleData":[{
                "adClientId":1000001,
                "coins":1,
                "isactive":"Y",
                "payAmount": 0.01,
                "type": 3
                },
                {
                "adClientId":1000001,
                "coins":2,
                "isactive":"Y",
                "payAmount": 0.02,
                "type": 3
                },
                {
                "adClientId":1000001,
                "coins":10,
                "isactive":"Y",
                "payAmount": 10,
                "type": 3
                    }]
            }
        header = {'cookie': self.cookie,"Content-Type":"application/json"}
        r = requests.post(url,headers=header,data=json.dumps(payload))
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_2_saveBatchDiscount(self):
        '''兑币机保存批量优惠设置'''
        url = base_url+"/rest/discount/saveBatchDiscount"
        payload={
            "groupList":eval(DBJGroupIds),
            "type":1,
            "isBatch":False,
            "lyyEquipmentTypeId":[1000058],
            "consumeMode":1,
            "DBJRuleData":[{
                "adClientId":1000001,
                "coins":1,
                "isactive":"Y",
                "payAmount": 1
                },
                {
                "adClientId":1000001,
                "coins":2,
                "isactive":"Y",
                "payAmount":2
                },
                {
                "adClientId":1000001,
                "coins":10,
                "isactive":"Y",
                "payAmount": 10
                    }]
            }
        header = {'cookie': self.cookie,"Content-Type":"application/json"}
        r = requests.post(url,headers=header,data=json.dumps(payload))
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_3_saveBatchDiscount(self):
        '''充电桩保存批量优惠设置'''
        url = base_url+"/rest/discount/saveBatchDiscount"
        payload={
            "groupList":eval(CDZGroupIds),
            "type":2,
            "isBatch":False,
            "lyyEquipmentTypeId":[1000078],
            "SHLRuleData":[{
                "adClientId":1000001,
                "coins":1,
                "isactive":"Y",
                "payAmount": 1
                },
                {
                "adClientId":1000001,
                "coins":2,
                "isactive":"Y",
                "payAmount":2
                },
                {
                "adClientId":1000001,
                "coins":10,
                "isactive":"Y",
                "payAmount": 10
                    }],
            "SHLServiceData":[{
                "adClientId":1000001,
                "price":0.01,
                "isactive":"Y",
                "serviceTime": 3
                },
                {
                "adClientId":1000001,
                "price":0.02,
                "isactive":"Y",
                "serviceTime": 6
                }]
            }
        header = {'cookie': self.cookie,"Content-Type":"application/json"}
        r = requests.post(url,headers=header,data=json.dumps(payload))
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_4_saveBatchDiscount(self):
        '''儿童类保存批量优惠设置'''
        url = base_url+"/rest/discount/saveBatchDiscount"
        payload={
            "groupList":eval(ETLGroupIds),
            "type":6,
            "isBatch":False,
            "lyyEquipmentTypeId":[1001211],
            "offlineCoinsType":1,
            "ETLRuleData":[{
                "adClientId":1000001,
                "coins":2,
                "isactive":"Y",
                "payAmount": 2
                },
                {
                "adClientId":1000001,
                "coins":4,
                "isactive":"Y",
                "payAmount":4
                },
                {
                "adClientId":1000001,
                "coins":6,
                "isactive":"Y",
                "payAmount": 6
                    }]
            }
        header = {'cookie': self.cookie,"Content-Type":"application/json"}
        r = requests.post(url,headers=header,data=json.dumps(payload))
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_5_saveBatchDiscount(self):
        '''按摩椅保存批量优惠设置'''
        url = base_url+"/rest/discount/saveBatchDiscount"
        payload={
            "groupList":eval(AMYGroupIds),
            "type":2,
            "isBatch":False,
            "lyyEquipmentTypeId":[1001081],
            "consumeMode":1,
            "SHLRuleData":[{
                "adClientId":1000001,
                "coins":1,
                "isactive":"Y",
                "payAmount": 1
                },
                {
                "adClientId":1000001,
                "coins":2,
                "isactive":"Y",
                "payAmount":2
                },
                {
                "adClientId":1000001,
                "coins":10,
                "isactive":"Y",
                "payAmount": 10
                    }],
            "SHLServiceData":[{
                "adClientId":1000001,
                "price":0.01,
                "description":"test1",
                "isactive":"Y",
                "serviceTime": 3
                },
                {
                "adClientId":1000001,
                "price":0.02,
                "description":"test2",
                "isactive":"Y",
                "serviceTime": 6
                }]
            }
        header = {'cookie': self.cookie,"Content-Type":"application/json"}
        r = requests.post(url,headers=header,data=json.dumps(payload))
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_6_saveBatchDiscount(self):
        '''售货机保存批量优惠设置'''
        url = base_url+"/rest/discount/saveBatchDiscount"
        payload={
            "groupList":eval(SHJgroupIds),
            "type":8,
            "isBatch":False,
            "lyyEquipmentTypeId":[1001131],
            "offlineCoinsType":1,
            "SHJRuleData":[{
                "adClientId":1000001,
                "coins":2,
                "isactive":"Y",
                "payAmount": 2
                },
                {
                "adClientId":1000001,
                "coins":4,
                "isactive":"Y",
                "payAmount":4
                },
                {
                "adClientId":1000001,
                "coins":6,
                "isactive":"Y",
                "payAmount": 6
                    }]
            }
        header = {'cookie': self.cookie,"Content-Type":"application/json"}
        r = requests.post(url,headers=header,data=json.dumps(payload))
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_5_batchInsert(self):
        '''洗衣机保存批量优惠设置'''
        url = base_url+"/rest/discount/batchInsert"

        payload={"equipmentCategoryType":{"type":1},
                 "factory":{
                     "direction":1,
                     "loginFlag":601,
                     "mainboardServicePackageId":100300,
                     "productNumber":""
                     },
                 "lyyEquipmentGroupIds":[1045328],
                 "lyyEquipmentTypeId": 1000028,
                  "lyyGroupServices":[{
                      "coins":1,
                      "description":"大物件",
                      "isactive":"Y",
                      "pattern":"大物洗",
                      "price":4,
                      "serviceTime":42
                  },{
                      "coins":2,
                      "description":"标准洗",
                      "isactive":"Y",
                      "pattern":"标准洗",
                      "price":3,
                      "serviceTime":33
                  },{
                      "coins":3,
                      "description":"快速洗",
                      "isactive":"Y",
                      "pattern":"快速洗",
                      "price":2,
                      "serviceTime":20
                  },{
                      "coins":4,
                      "description":"单脱水",
                      "isactive":"Y",
                      "pattern":"单脱水",
                      "price":1,
                      "serviceTime":5
                  }]
                 }

        header = {'cookie': self.cookie}

        r = requests.post(url,headers=header,json=payload)

        self.result = r.json()

        self.assertEqual(self.result['result'], 0)
    def test_5_editGroupService(self):
        '''编辑保存洗衣机套餐'''
        url = base_url+"/rest/discount/equipment/editGroupServiceByEquipmentId"

        payload={"description":"测试","equipmentModeType":"CKF", "isValid":"Y","lyyGroupServiceId": 1036129,
                  'price':0.01,'serviceTime':3,"value":"82213601"}

        header = {'cookie': self.cookie}

        r = requests.post(url,headers=header,json=payload)

        self.result = r.json()

        self.assertEqual(self.result['result'], 0)

if __name__ == '__main__':
    unittest.main()