"""
    python 操作 redis set 无序集合类型数据
"""

import redis

if __name__ == '__main__':
    # 连接 redis 数据库
    redis_conn = redis.StrictRedis(host="localhost", port=6379, db=3)
    # 集合添加数据
    redis_conn.sadd("set", "郭鹏涛", "张佳琪", "陈欣妮", "索月雅")
    # 获取集合所有数据, 返回值为 list, 数据为字节形式, 需调用 decode() 方法解码
    data_list = redis_conn.smembers("set")
    for data in data_list:
        print(data.decode())
    # 删除集合元素
    redis_conn.srem("set", "付乔央", "秦明欣", "陶静", "张雪", "张莉莉")
    # 释放资源
    redis_conn.close()
