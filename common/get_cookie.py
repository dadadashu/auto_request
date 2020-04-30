# coding:utf-8
import os


cur = os.path.dirname(os.path.realpath(__file__))

def cookie(yamlName="cookie.yaml"):
    '''
    从token.yaml读取token值
    :param yamlName: 配置文件名称
    :return: token值
    '''

    p = os.path.join(cur, yamlName)
    f = open(p)
    a = f.read()
    f.close()
    return a