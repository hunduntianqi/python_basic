"""
    pymongo ==> python中操作MongoDB数据库的第三方包
    pymongo模块使用:
        1. 创建连接对象: conn = pymongo.MongoClient('localhost', 27017)
        2. 创建库对象: db = conn['库名']
        3. 创建集合对象: myset = db['集合名']
        4. 在集合中插入文档: myset.insert_one({})
        5. 在集合中插入文档2:myset.insert_many([{}, {}, {}, {}.....{}])
"""
import pymongo

if __name__ == '__main__':
    # 创建连接对象
    conn = pymongo.MongoClient('localhost', 27017)
    # 创建库对象
    db = conn['test_database']
    # 创建集合对象
    myset = db['message']
    # 在集合中插入一条文档
    myset.insert_one({'name': '郭鹏涛', 'age': '23', 'sex': '男'})
    # 在集合中插入多条文档
    myset.insert_many([{'name': '郭鹏涛', 'age': '23', 'sex': '男'},
                       {'name': '郭鹏强', 'age': '22', 'sex': '男'}]
                      )
