__author__ = 'lee0530'

import unittest
import requests
from common.get_cookie import cookie
from os.path import abspath, dirname
from db_fixture.postgresql_db import lyy_prod
import configparser as cparser
import urllib3
from common.globalparam  import base_url
urllib3.disable_warnings()

autotestgroupid = '1040816'

class Valurcard(unittest.TestCase) :
    '''超值卡测试'''
    def setUp(self):
        self.cookie=cookie()

    def tearDown(self):
        print(self.result)

    def test_1_create(self):
        '''保存超值卡'''
        url = base_url+'/rest/valueCard/saveValueCard'
        header = {'Content-Type': 'application/json', 'cookie': self.cookie}
        body = {'validFee':"50",'coinsImmediate':"50",'coinsPerDay': "5",'days': "3", 'startDate': '2019-08-01','endDate':'2019-08-31' ,'groupIds': autotestgroupid, 'isRepeatBuy': 1, 'coinsEffectiveTimeType':1 }
        r = requests.post(url=url,headers=header,json=body,verify=False)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
        # 数据库检查已建的活动
        self.sql = lyy_prod().lyy_query_where('A.lyy_distributor_value_card_id','lyy_distributor_value_card A LEFT JOIN lyy_distributor_value_card_group B ON A.lyy_distributor_value_card_id=B.lyy_distributor_value_card_id',
                                       'status=1 AND B.lyy_equipment_group_id=%s'%(autotestgroupid))
        self.assertIsNotNone(self.sql)
        globals()["valuecardid"] = self.sql
        print(globals()["valuecardid"])

    def test_2_create(self):
        '''建过超值卡的场地不能再建'''
        url = base_url+'/rest/valueCard/saveValueCard'
        header = {'Content-Type': 'application/json', 'cookie': self.cookie}
        body = {'validFee':"50",'coinsImmediate':"50",'coinsPerDay': "5",'days': "3", 'startDate': '2019-08-01','endDate':'2019-08-31' ,'groupIds': autotestgroupid, 'isRepeatBuy': 1, 'coinsEffectiveTimeType':1 }
        r = requests.post(url=url,headers=header,json=body,verify=False)
        self.result = r.json()
        self.assertEqual(self.result['result'], 102)
        self.assertEqual(self.result['description'], '有部分场地已开展活动')

    def test_3_delete(self):
        '''终止活动'''
        url = base_url+'/rest/valueCard/updateCardActivity'
        header = {'Content-Type': 'application/x-www-form-urlencoded', 'cookie': self.cookie}
        body = {'valueCardId':globals()["valuecardid"],'status':2}
        r = requests.post(url=url,headers=header,data=body,verify=False)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
        # 数据库检查活动已删除
        self.sql = lyy_prod().lyy_query_where('status','lyy_distributor_value_card','lyy_distributor_value_card_id=%s'%(globals()["valuecardid"]))
        self.assertEqual(self.sql,2)

    def test_4_delete(self):
        '''删除活动'''
        url = base_url+'/rest/valueCard/updateCardActivity'
        header = {'Content-Type': 'application/x-www-form-urlencoded', 'cookie': self.cookie}
        body = {'valueCardId':globals()["valuecardid"],'status':0}
        r = requests.post(url=url,headers=header,data=body,verify=False)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
        # 数据库检查活动已删除
        self.sql = lyy_prod().lyy_query_where('status','lyy_distributor_value_card','lyy_distributor_value_card_id=%s'%(globals()["valuecardid"]))
        self.assertEqual(self.sql,0)

if __name__ == '__main__':
    unittest.main()