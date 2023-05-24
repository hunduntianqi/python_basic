"""
    pymongo ==> python中操作MongoDB数据库的第三方包
    pymongo模块使用:
        创建数据库连接对象: mongo_conn = pymongo.MongoClient("mongodb://localhost:27017/") ==> 连接到本地数据库
            获取所有数据库名列表 ==> mongo_conn.list_database_names()
        获取指定数据库对象: database_name = mongo_conn["database_name"] ==> 数据库如果不存在会新建数据库, 但在程序结束后未插入集合会
                                                                         删除空数据库
            获取数据库中所有集合名列表 ==> database_name.list_collection_names()
        获取指定集合对象: collections_name = database_name["collections_name"] ==> 集合如果不存在会新建集合, 但在程序结束后未插入
                                                                         文档会删除空集合
        删除集合: database_name.drop_collection(collections_name)
        断开数据库连接: mongo_conn.close()
        文档操作:
            增 ==> 添加文档:
                添加一条文档 ==> collections_name.insert_one(document)
                    该方法返回一个 InsertOneResult 对象, 包含插入文档的 ObjectId, InsertOneResult.inserted_id 可以获取文档 '_id'
                添加多条文档 ==> collections_name.insert_many([document1, document2, ...]])
                    该方法返回一个 InsertManyResult 对象, InsertManyResult.inserted_ids 可以获取文档 '_id' 的列表
            删 ==> 删除文档:
                删除一条满足指定条件的文档 ==> collections_name.delete_one(condition)
                删除多条满足指定条件的文档 ==> collections_name.delete_many(condition)
            改 ==> 修改文档数据:
                修改一条满足查询条件的数据 ==> collections_name.update_one(condition, new_values), 例:
                    collection_name.update_one({"name":"Taobao"}, {"$set":{"name":"知乎"}})
                修改所有满足查询条件的数据 ==> collections_name.update_many(condition, new_values), 例:
                    collection_name.update_many({"name":"Taobao"}, {"$set":{"name":"知乎"}})
            查 ==> 查询文档数据:
                查询集合中的一条满足条件的数据 ==> collection_name.find_one(condition)
                查询集合中的所有数据 ==> collection_name.find()
                查询集合中的所有满足条件的数据 ==> collection_name.find(condition)
"""
import pymongo


# 定义函数, 添加文档数据
def insert_document(collection: pymongo.collection.Collection):
    # 向集合中插入一条数据
    object_id = collection.insert_one({"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"})
    # 打印添加文档数据 _id
    print(object_id.inserted_id)
    # 向集合中插入多条数据
    object_id_list = collection.insert_many([
        {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
        {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
        {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
        {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
        {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
    ])
    # 获取包含文档 _id 的列表
    id_list = object_id_list.inserted_ids
    # 遍历列表
    for id_document in id_list:
        print(id_document)
    pass


# 定义函数, 删除文档数据
def delete_document(collection: pymongo.collection.Collection):
    # 删除一条 name 值为 RUNOOB 的文档
    collection.delete_one({"name": "RUNOOB"})
    # 删除所有 name 值为 Taobao 的文档
    collection.delete_many({"name": "Taobao"})
    # 删除所有文档, 相当于删除整个集合
    # my_mongo.drop_collection(collection)
    pass


# 定义函数, 修改文档数据
def update_document(collection: pymongo.collection.Collection):
    # 修改第一条 name 为 Facebook 的 name 为 百度, 网址为 https://www.baidu.com
    collection.update_one({"name": "Facebook"}, {"$set": {"name": "百度", "url": "https://www.baidu.com"}})
    # 修改所有 alexa 不为 10 的 alexa 为 0
    collection.update_many({"alexa": {"$ne": "10"}}, {"$set": {"alexa": "0"}})


# 定义函数, 查询文档数据
def select_document(collection: pymongo.collection.Collection):
    # 查询集合中的一条数据
    data_one = collection.find_one({"name": "Github"})
    print(data_one)
    # # 获取集合中的所有数据
    # data_list = collection.find()
    # for data in data_list:
    #     print(data)
    # 获取集合中的所有 alexa = 0 的数据
    data_list = collection.find({"alexa": "0"})
    for data in data_list:
        print(data)


if __name__ == '__main__':
    # 连接 MongoDB 数据库
    mongo_conn = pymongo.MongoClient("mongodb://localhost:27017")
    # 获取当前系统中所有数据库名
    database_name_list = mongo_conn.list_database_names()
    print(database_name_list)
    # 获取指定数据库对象
    my_mongo = mongo_conn['python_study']
    # 获取指定集合对象
    my_collection = my_mongo["my_collection"]
    # 调用函数, 执行文档操作
    # insert_document(my_collection)
    # delete_document(my_collection)
    # update_document(my_collection)
    select_document(my_collection)
    # 释放资源
    mongo_conn.close()
