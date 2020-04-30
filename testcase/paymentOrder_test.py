__author__ ="peishuheng"
import unittest
import requests
from common.get_cookie import cookie
from os.path import abspath, dirname
import configparser as cparser
from common.globalparam import base_url,now,past_time_threeday


# ======== Reading payload_config.ini setting ===========
base_dir = dirname(dirname(abspath(__file__)))
base_dir = base_dir.replace('\\', '/')
config = base_dir + "/common/payload_config.ini"
#ConfigParser 是用来读取配置文件的包
cf = cparser.ConfigParser()
cf.read(config,encoding='UTF-8')
WWJGroupId = cf.get("WWJGroupId", "WWJgroupId")
WWJEquipmentId = cf.get("WWJEquipmentId", "WWJEquipmentId")

class paymentOrder(unittest.TestCase):
    ''' 订单查询 '''

    def setUp(self):
        self.cookie=cookie()

    def tearDown(self):
        print(self.result)

    def test_1_paymentOrderRecords(self):
        '''获取订单详情-交易成功'''
        url = base_url+"/rest/orderRecord/paymentOrderRecords"
        payload={
            "type":"Pay",
            "dateEnd":past_time_threeday,
            "endDate":now,
            "pageIndex":1,
            "pageSize":10,
            "noTimeRestrict":"N"
        }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_2_paymentOrderRecords(self):
        '''获取订单详情-退款'''
        url = base_url+"/rest/orderRecord/paymentOrderRecords"
        payload={
            "type":"Refund",
            "dateEnd":past_time_threeday,
            "endDate":now,
            "pageIndex":1,
            "pageSize":1,
            "noTimeRestrict":"N"
        }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_3_paymentOrderRecords(self):
        '''获取订单详情-全部'''
        url = base_url+"/rest/orderRecord/paymentOrderRecords"
        payload={
            "type":"",
            "dateEnd":past_time_threeday,
            "endDate":now,
            "pageIndex":1,
            "pageSize":10,
            "noTimeRestrict":"N"
        }
        header = {'cookie': self.cookie}
        r = requests.post(url,headers=header,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

if __name__ == '__main__':
    unittest.main()