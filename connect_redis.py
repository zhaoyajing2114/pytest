import redis
import json
conn = redis.Redis(host="172.16.100.112",port=6379,password='Gmck7X02')
a = conn.mget('0922.lvluoyun.com')
print(a)
