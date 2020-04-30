__author__ ="peishuheng"
import requests,unittest
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
username = cf.get("login", "username")
password = cf.get("login", "password")
# username  = '13326475209'
# password  = 'e10adc3949ba59abbe56e057f20f883e'

class login(unittest.TestCase):
    ''' 登录B端 '''

    def setUp(self):
        pass

    def tearDown(self):
        print(self.result)
    def test_login(self):
        '''登录B端'''
        url = base_url+"/rest/group/distributor/login"
        header = {'content-type':'application/x-www-form-urlencoded'}
        payload = {'userName':username,'password':password}
        r = requests.post(url=url,headers=header,data=payload)
        self.result=r.json()

        cookie = r.headers['Set-Cookie'].split(';')[0]
        filename_cookie = base_dir+'/common/cookie.yaml'
        with open(filename_cookie, 'w') as f:  # 如果filename不存在会自动创建，
                                             #  'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(cookie)

        userid = r.json()['data']['userId']
        filename_userid = base_dir+'/common/userid.yaml'
        with open(filename_userid, 'w') as f:  # 如果filename不存在会自动创建，
                                            # 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(userid)


if __name__ == '__main__':
    unittest.main()