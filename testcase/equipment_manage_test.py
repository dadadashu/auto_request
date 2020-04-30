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


dbj_uniqueCode = '0000000000241318'
dbj_value = '241318'
dbj_equipmentId= '1221954'
groupId = '1040816'
amount = '1'
dbj_typeId = '1000058'
dbj_href = 'https://sb.leyaoyao.com/group/device-dbj-reg.html?eid=%s'%(dbj_value)
ruleData = []
other =  '自动化测试'

wwj_uniqueCode = '0000000000155215'
wwj_value = '155215'
wwj_typeId = '1000001'
wwj_equipmentId= '1132215'
wwj_href='https://sb.leyaoyao.com/group/device-reg.html?eid=155215&machineType=wwj&isChangeableType=false&equipmentTypeId=1000001&price=1&typeId=&groupId=1040816&address=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95'

etl_uniqueCode = '0000000000030131'
etl_value = '30131'
etl_typeId = '1001211'
etl_equipmentId= '1046196'
etl_href = 'https://sb.leyaoyao.com/group/device/pages/register-child-machine.html?eid=%s&machineType=children&typeId=%s'%(etl_value,etl_typeId)

cdz_uniqueCode = '0000000000127959'
cdz_value = '127959'
cdz_equipmentId= '1108857'
cdz_typeId = '1000078'
cdz_href = 'https://sb.leyaoyao.com/group/device-reg.html?eid=%s&machineType=life&isChangeableType=true&equipmentTypeId=1000078&typeId=1000078&address='%(cdz_value)
cdz_serviceData = [{
		"serviceId": 0,
		"price": 0.15,
		"coins": 1,
		"serviceTime": 1,
		"description": "快充"
	}]
cdz_xyjRuleData =[{
		"ruleId": 1,
		"payAmount": 10,
		"coins": 10
	}]

lyyEquipmentIdList = wwj_equipmentId+','+etl_equipmentId+','+cdz_equipmentId

class Equipment(unittest.TestCase) :
    '''设备管理'''
    def setUp(self):
        self.cookie=cookie()

    def tearDown(self):
        print(self.result)

    def test_1_equipment_check(self):
        '''查询设备'''
        url = base_url+'/rest/equipment/register/check'
        header = {'cookie':self.cookie}
        payload = {'uniqueCode':dbj_uniqueCode}
        r = requests.get(url=url,headers=header,params=payload,verify=False)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_2_equipment_register(self):
        '''兑币机注册'''
        url = base_url + '/rest/equipment/registerEquipment'
        header = {'Content-Type': 'application/json', 'cookie': self.cookie}
        body = {'value': dbj_value, 'groupId': groupId, 'typeId': dbj_typeId, 'href': dbj_href ,'ruleData':ruleData}
        r = requests.post(url=url, headers=header, json=body,verify=False)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
    #    数据库查询已经注册成功,场地正确
        self.sql = lyy_prod().lyy_query_where("DISTINCT(lyy_equipment_group_id)","lyy_equipment","value='%s'"%(dbj_value))
        self.assertEqual(str(self.sql),groupId)

    def test_3_equipment_register(self):
        '''娃娃机注册'''
        url = base_url + '/rest/equipment/registerEquipment'
        header = {'Content-Type': 'application/json', 'cookie': self.cookie}
        body = {'value': wwj_value, 'groupId': groupId, 'typeId': wwj_typeId, 'amount': amount ,'groupNumber':10, 'serviceData':[], 'xyjRuleData':[], 'href':wwj_href}
        r = requests.post(url=url, headers=header, json=body,verify=False)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
        self.sql = lyy_prod().lyy_query_where("DISTINCT(lyy_equipment_group_id)","lyy_equipment","value='%s'"%(wwj_value))
        self.assertEqual(str(self.sql),groupId)

    def test_4_equipment_register(self):
        '''充电桩注册'''
        url = base_url + '/rest/equipment/registerEquipment'
        header = {'Content-Type': 'application/json', 'cookie': self.cookie}
        body = {'value': cdz_value, 'groupId': groupId, 'groupNumber': 1,'typeId': cdz_typeId, 'amount': amount, 'serviceData': cdz_serviceData,  'xyjRuleData': cdz_xyjRuleData, 'href': cdz_href}
        r = requests.post(url=url, headers=header, json=body,verify=False)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
        self.sql = lyy_prod().lyy_query_where("DISTINCT(lyy_equipment_group_id)","lyy_equipment","value='%s'"%(cdz_value))
        self.assertEqual(str(self.sql),groupId)

    def test_5_equipment_register(self):
        '''儿童类注册'''
        url = base_url + '/rest/equipment/registerEquipment'
        header = {'Content-Type': 'application/json', 'cookie': self.cookie}
        body = {'value': etl_value, 'groupId': groupId, 'typeId': etl_typeId, 'amount': amount, 'groupNumber': 10, 'type': 6, 'href': etl_href, 'ruleData': ruleData}
        r = requests.post(url=url, headers=header, json=body,verify=False)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
        self.sql = lyy_prod().lyy_query_where("DISTINCT(lyy_equipment_group_id)","lyy_equipment","value='%s'"%(etl_value))
        self.assertEqual(str(self.sql),groupId)

    def test_6_equipment_already_register(self):
        '''设备已注册'''
        url = base_url + '/rest/equipment/registerEquipment'
        header = {'Content-Type': 'application/json', 'cookie': self.cookie}
        body = {'value': etl_value, 'groupId': groupId, 'typeId': etl_typeId, 'amount': amount, 'groupNumber': 10, 'type': 6, 'href': etl_href, 'ruleData': ruleData}
        r = requests.post(url=url, headers=header, json=body,verify=False)
        self.result = r.json()
        self.assertEqual(self.result['result'], 2)
        self.assertEqual(self.result['description'],'设备已注册')

    def test_7_equipment_codeerror_register(self):
        '''设备唯一码无效'''
        url = base_url + '/rest/equipment/registerEquipment'
        header = {'Content-Type': 'application/json', 'cookie': self.cookie}
        body = {'value': 'abcd', 'groupId': groupId, 'typeId': etl_typeId, 'amount': amount, 'groupNumber': 10, 'type': 6, 'href': etl_href, 'ruleData': ruleData}
        r = requests.post(url=url, headers=header, json=body,verify=False)
        self.result = r.json()
        self.assertEqual(self.result['result'], -1)
        self.assertEqual(self.result['description'],'设备唯一码错误')

    def test_8_equipment_unbind(self):
        '''设备解绑'''
        url = base_url + '/rest/equipment/unbundling'
        header = {'Content-Type':'application/json','cookie':self.cookie}
        body = {'lyyEquipmentId':dbj_equipmentId,'other':other}
        r = requests.post(url=url,headers=header,json=body,verify=False)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)

    def test_9_equipment_batchUnbundling(self):
        '''批量解绑'''
        url = base_url + '/rest/equipment/batchUnbundling'
        header = {'Content-Type': 'application/json', 'cookie': self.cookie}
        body = {'lyyEquipmentIdList': lyyEquipmentIdList,'other':other}
        r = requests.post(url=url, headers=header, json=body,verify=False)
        self.result = r.json()
        self.assertEqual(self.result['result'], 0)
        #数据库校验解绑成功
        self.sql=lyy_prod().lyy_query_where("DISTINCT(name)","lyy_equipment","lyy_equipment_id in (%s)"%(lyyEquipmentIdList))
        self.assertEqual(self.sql,'已解绑')

if __name__ == '__main__':
    unittest.main()

