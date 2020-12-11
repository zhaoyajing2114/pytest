import pymysql
import json
'''
用于校验数据库中存入的值和最终生效的配置是否一致
将ADS上的配置下载下来存放到txt文档中
要求文档中的类型是json格式的

'''
file_cur = open(r'D:\workspace\pytest1\func\123.txt',encoding='utf-8')
conf_str = file_cur.read()
result = json.loads(conf_str)
# 打开数据库连接
db = pymysql.connect("rm-8vb3uun05yrxu06ldlo.mysql.zhangbei.rds.aliyuncs.com", "ads_test", "ZF_cq>&Ne7M|!)?/", "yundun_ads_prod", charset='utf8' )
cursor = db.cursor()
for item in result['data']:
    if 'dst_ip' in item:
        ip_str = result['data'][item]
        print("当前校验的机器是%s" % ip_str)
    else:
        name = item
        value = result['data'][item]
        # 使用execute方法执行SQL语句
        try:
            cursor.execute('SELECT %s FROM t_protect_template a where uuid in (select protect_template_id from t_defense_group where name like "241");' % name)
            # 使用 fetchone() 方法获取一条数据
            data = cursor.fetchone()
            data = data[0]
            if isinstance(data,bytes):
                data = int.from_bytes(data,byteorder='big',signed=False)
            if data == value:
                # print('字段一致%s'%name)
                pass
            else:
                print('[error]字段[%s]不一致 数据库%s----配置%s'%(name,data,value))
        except BaseException as e:
            print(name + '@@@@@@在数据库中没有相应的字段！')
# 关闭数据库连接
db.close()