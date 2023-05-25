"""
    python 操作 redis hash 类型数据
"""

import redis

if __name__ == '__main__':
    # 连接 redis 数据库
    redis_conn = redis.StrictRedis(host="localhost", port=6379, db=1)
    # 添加 hash 对象并添加单个属性
    redis_conn.hset("user", "user_name", "郭鹏涛")
    # 为 hash 对象设置多个属性
    redis_conn.hmset("user", {"user_id": 1, "user_sex": "男", "user_email": "1729992141@qq.com"})
    # 获取指定对象的所有属性名, 返回一个 list
    keys = redis_conn.hkeys("user")
    print(type(keys))
    for key in keys:
        print(key)
    print("=====================================")
    # 根据指定键名获取单个属性值, 返回值为字节数据, 需调用 decode() 方法解码
    print(redis_conn.hget("user", "user_name").decode())
    # 指定键名获取多个属性值, 返回值为 list
    values = redis_conn.hmget("user", "user_name", "user_id", "user_sex")
    print(type(values))
    for value in values:
        print(value.decode())
    print("=====================================")
    # 获取指定对象所有属性值, 返回值为 list
    value_all = redis_conn.hvals("user")
    for value in value_all:
        print(value.decode())
    print("=====================================")
    # 删除指定对象的指定属性
    redis_conn.hdel("user", "user-id")
    # 释放资源
    redis_conn.close()
