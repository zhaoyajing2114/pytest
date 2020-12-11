
import redis
import configparser
import os
def get_redis_connection():
    try:
        conf = configparser.ConfigParser()
        conf.read(r'D:\workspace\pytest1\conf\test_conf.ini',encoding='utf-8')
    except BaseException as e:
        print('打开配置文件失败')
    host1 = conf.get('redis','host')
    port1 = conf.getint('redis','port')
    password1 = conf.get('redis','password')
    db1 = conf.getint('redis','db')
    try:
        conn = redis.Redis(host=host1, port=port1, password=password1, db=db1)
        return conn
    except BaseException as e:
        print(str(e))