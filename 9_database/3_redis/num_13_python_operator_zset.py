"""
    python 操作 redis zset 有序集合类型数据
"""

import redis

if __name__ == '__main__':
    # 连接 redis 数据库
    redis_conn = redis.StrictRedis(host="localhost", port=6379, db=4)
    # ZSet 集合添加数据
    redis_conn.zadd("zset", {"郭鹏涛": 1, "陈欣妮": 2, "索月雅": 3})
    # 获取指定索引范围的元素, 返回一个 list, 数据为字节形式, 需调用 decode() 方法解码
    data_list_index = redis_conn.zrange("zset", 0, 2)
    for data in data_list_index:
        print(data.decode())
    print("=====================================")
    # 获取指定权重范围的元素, 返回一个 list, 数据为字节形式, 需调用 decode() 方法解码
    data_list_score = redis_conn.zrangebyscore("zset", 1, 3)
    for data in data_list_score:
        print(data.decode())
    print("=====================================")
    # 获取指定元素的权重值, 返回值为 float 类型
    print(redis_conn.zscore("zset", "索月雅"))
    # 删除指定元素
    redis_conn.zrem("zset", "郭鹏涛")
    # 删除指定权重范围的元素
    redis_conn.zremrangebyscore("zset", 2, 3)
    # 释放资源
    redis_conn.close()
