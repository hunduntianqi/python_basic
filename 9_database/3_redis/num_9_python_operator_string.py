"""
    python 操作 redis string 类型数据
"""

import redis

if __name__ == '__main__':
    # 连接 redis 数据库
    redis_conn = redis.StrictRedis(host="localhost", port=6379, db=0)
    # 获取数据库中所有键名
    key_names = redis_conn.keys("*")
    print(type(key_names))
    for key_name in key_names:
        print(key_name)
        # 根据键名获取对应值
        print(redis_conn.get(key_name).decode())
    # 根据键名获取多个值
    values = redis_conn.mget("age", "name", "sex")
    print(type(values))
    for value in values:
        print(value.decode())
    # 新增一组键值对, 如果键已存在会修改原来的值
    redis_conn.set("email", "1729992141@qq.com")
    # 新增多组键值对, 如果键已存在会修改原来的值
    redis_conn.mset({"id": "01", "phone": "17320101759", "address": "江苏省苏州市昆山市锦溪镇"})
    # 指定键追加数据
    redis_conn.append("name", "and 陈欣妮")
    # 删除键值对
    redis_conn.delete("address", "id", "email")
    # 释放资源
    redis_conn.close()
