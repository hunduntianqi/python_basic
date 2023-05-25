"""
    1. 安装包-redis:
        pip install redis
    2. 引入模块:
        from redis import *
        该模块中提供了StrictRedis对象, 用于连接redis服务器, 并按照不同类型提供了不同方法
        连接数据库:
            redis_conn = redis.StrictRedis(host, port, db)
                host ==> 连接的 redis 主机地址, 如果是本机是 'localhost' / '127.0.0.1'
                port ==> 连接的 redis 主机端口, 一般为 6379
                db ==> 指定要操作的数据库, 0~15, 默认为 0
        释放资源, 断开数据库连接 ==> redis_conn.close()
    3. 常用方法:
        redis_conn.info() ==> 查看 Redis 信息
        redis_conn.flushdb() ==> 清空当前操作的数据库
        redis_conn.flushall() ==> 清空所有数据库
        redis_conn.time() ==> 返回当前 Redis 服务器的时间
        redis_conn.dbsize() ==> 获取当前操作数据库中 key 的数量
        redis_conn.keys("regex") ==> 根据正则表达式匹配获取符合条件的键名集合, 返回一个 list
        redis_conn.type("key_name") ==> 查看对应键的值的数据类型
        redis_conn.exists("key_name") ==> 判断对应键名是否存在, 存在返回 1, 不存在返回 0
        redis_conn.expire("key_name", time) ==> 设置键的过期时间, 单位是秒
        redis_conn.ttl("key_name") ==> 查看键的过期时间
        redis_conn.delete("key_name1", "key_name2", ...) ==> 删除键值对
    4. 各类型数据增删改查操作:
        string 类型数据:
            redis_conn.keys("*") ==> 获取数据库中所有的键名, 返回值为 list
            redis_conn.get("key_name") ==> 根据键名获取对应值, 返回值为字节数据, 需调用 decode() 方法解码
            redis_conn.mget("key_name1", "key_name2", ...) ==> 根据键名获取多个值, 返回值为存储每个键对应值的字节数据的列表
            redis_conn.set("key_name", value) ==> 新增一组键值对, 如果键已存在会修改原来的数据
            redis_conn.mset({"key_name1":values1, "key_name2": value2, ...}) ==> 新增多组键值对, 如果键已存在会修改原来的值
            redis_conn.append("key_name", add_value) ==> 指定键名追加数据
            redis_conn.delete("key_name1", "key_name2", ...) ==> 删除指定键值对
        hash 类型数据:
            redis_conn.hset("object_name", "field_name", value) ==> 为指定 hash 对象添加单个属性, 属性名已存在会修改原来的值
            redis_conn.hmset("object_name", {"field_name1":value, "field_name2":value}, ....)
                ==> 为指定 hash 对象添加多个属性, 属性名已存在会修改原来的值
            redis_conn.hkeys("object_name") ==> 获取指定 hash 对象所有属性名, 返回一个 list
            redis_conn.hget("object_name", "key_name") ==> 根据指定属性名获取对应属性值, 返回值为字节数据, 需调用decode()方法解码
            redis_conn.hmget("object_name", "key_name1", "key_name2", ...) ==> 根据指定属性名获取多个对应属性值, 返回一个 list
            redis_conn.hvals("object_name") ==> 获取指定对象所有属性值, 返回一个 list
            redis_conn.hdel("object_name", "field_name1", "field_name2", ...) ==> 删除指定对象的指定属性
        list 类型数据:
            redis_conn.lpush("list_name", value1, value2, value3, ...) ==> 从列表左侧插入数据
            redis_conn.rpush("list_name", value1, value2, value3, ...) ==> 从列表右侧插入数据
            redis_conn.linsert("list_name", "before", old_value, new_value) ==> 在指定数据前插入数据
            redis_conn.linsert("list_name", "after", old_value, new_value) ==> 在指定数据后插入数据
            redis_conn.llen("list_name") ==> 获取指定列表中的元素个数
            redis_conn.lrange("list_name", start_index, end_index) ==> 获取列表中指定范围的元素, 返回值为列表, 数据为字节形式,
                                                                       需调用 decode() 方法解码
            redis_conn.lset("list_name", index, new_value) ==> 修改指定索引位置的元素值
            redis_conn.lrem("list_name", count, value) ==> 删除指定元素
                count = 0 ==> 删除所有指定元素
                count > 0 ==> 从左到右删除指定个数的元素
                count < 0 ==> 从右到左删除指定个数的元素
        set 无序集合类型数据:
            redis_conn.sadd("set_name", value1, value2, ...) ==> 集合添加数据
            redis_conn.smembers("set_name") ==> 获取集合所有数据, 返回值为 list, 数据为字节形式, 需调用 decode() 方法解码
            redis_conn.srem("set_name", value1, value2, ...) ==> 删除集合指定数据
        zset 有序集合数据:
            redis_conn.zadd("zset_name", {"value1": score1, "valie2": score2, ...}) ==> 集合添加数据
            redis_conn.zrange("zset_name", start_index, end_index) ==> 获取指定索引范围的元素, 返回一个 list, 数据为字节形式,
                                                                       需调用 decode() 方法解码
            redis_conn.zrangebyscore("zset_name", min_score, max_score) ==> 获取指定权重范围的元素, 返回一个 list, 数据为字节形式,
                                                                       需调用 decode() 方法解码
            redis_conn.zscore("zset_name", "value") ==> 获取指定元素的权重值, 返回值为 float 类型
            redis_conn.zrem("zset_name", "value") ==> 删除指定元素
            redis_conn.zremrangebyscore("zset_name", min_score, max_score) ==> 删除指定权重范围的元素
"""
from redis import *

if __name__ == '__main__':
    # 连接redis数据库
    redis_conn = StrictRedis(host="localhost", port=6379, db=0)
    # 查看 Redis 信息
    print(redis_conn.info())
    # 清空当前操作数据库
    # redis_conn.flushdb()
    # 清空所有数据库
    # redis_conn.flushall()
    # 查看当前连接的 Redis 服务器时间
    print(redis_conn.time())
    # 查看数据库中键的个数
    print(redis_conn.dbsize())
    # 根据正则表达式获取指定的键名列表
    print(redis_conn.keys("*"))
    # 查看对应键的值的数据类型
    print(redis_conn.type("Name"))
    # 判断键名是否存在
    print(redis_conn.exists("sex"))
    # 设置键的过期时间
    redis_conn.expire("Age", 10)
    # 查看键的过期时间
    print(redis_conn.ttl("Age"))
    # 删除键值对
    redis_conn.delete("age")
    # 释放资源
    redis_conn.close()
