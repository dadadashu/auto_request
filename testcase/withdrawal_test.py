__author__ ="peishuheng"
import unittest
import requests
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

class withdrawal(unittest.TestCase):
    ''' 我的钱包 '''
    def setUp(self):
        self.cookie=cookie()

    def tearDown(self):
        print(self.result)

    def test_1_withdrawal(self):
        '''提现记录-支付收益'''
        url = base_url+"/rest/group/distributor/withdrawalsHistoryList"
        payload={
            "pageSize":1,
            "pageIndex":1,
            "type":1
            }
        header = {'cookie': self.cookie}
        r = requests.get(url,headers=header,params=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 1)

    def test_2_withdrawal(self):
        '''提现记录-广告收益'''
        url = base_url+"/rest/group/distributor/withdrawalsHistoryList"
        payload={
            "pageSize":1,
            "pageIndex":1,
            "type":2
            }
        header = {'cookie': self.cookie}
        r = requests.get(url,headers=header,params=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], 1)

if __name__ == '__main__':
    unittest.main()