"""
    python 操作 redis list 类型数据
"""

import redis

if __name__ == '__main__':
    # 连接 redis 数据库
    redis_conn = redis.StrictRedis(host="localhost", port=6379, db=2)
    # 创建一个 list 并从左侧插入数据
    # redis_conn.lpush("list", 1, 2, 3)
    # 从列表右侧插入数据
    # redis_conn.rpush("list", 4, 5, 6)
    # 在指定元素前插入数据
    # redis_conn.linsert("list", "before", 1, 7)
    # 在指定元素后插入数据
    # redis_conn.linsert("list", "after", 7, 8)
    # 获取指定列表元素个数
    element_num = redis_conn.llen("list")
    print(element_num)
    print("==================================")
    # 获取列表中指定范围的元素, 返回值为列表, 数据为字节形式, 需调用 decode() 方法解码
    element_range = redis_conn.lrange("list", 0, 5)
    for element in element_range:
        print(element.decode())
    print("==================================")
    # 修改指定索引位置的元素值
    redis_conn.lset("list", 0, "郭鹏涛")
    # 删除指定元素值
    redis_conn.lrem("list", 0, 7)
    # 释放资源
    redis_conn.close()
