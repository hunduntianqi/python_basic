# 随机模块-random
# 随机数应用场景: 数字验证码, 高并发下的订单号

import random

# random.random() 返回0-1之间的随机小数
print(random.random())

# random.randrange(开始值, 结束值, 步进值) 随机获取指定范围内的整数
print(random.randrange(5))
print(random.randrange(1, 6))
print(random.randrange(1, 6, 2))

# 随机产生指定范围内的整数
print(random.randint(1, 100))

# random.uniform() 获取指定范围内的随即小数
print(random.uniform(1, 12))

# random.choice() 随机获取容器类型中的值
print(random.choice([1, 2, 4, 5, 8]))

# random.shuffle() 随机打乱当前列表的值
list = [1, 2, 3, 4, 5, 6]
random.shuffle(list)
print(list)
