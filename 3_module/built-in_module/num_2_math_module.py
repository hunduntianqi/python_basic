# 数学模块-math
import math

#  math.ceil() 向上取整
print(math.ceil(10.3))  # 11

# math.floor() 向下取整
print(math.floor(10.3))  # 10

# math.pow(x, n) 计算数字的n次方
print(math.pow(2, 4))  # 16.0

# math.sqrt() 开平方运算
print(math.sqrt(3))  # 1.732

# math.fabs() 计算绝对值
print(math.fabs(-5))  # 5.0

# math.modf() 把一个数值拆分成整数和小数组成的元组(小数在前, 整数在后)
print(math.modf(2.5))  # (0.5, 2.0)

# math.copysign(x, y) 把第二个参数的正负符合拷贝给第一个参数
print(math.copysign(1, -2.3))  # -1.0
print(math.copysign(1, 2.3))  # 1.0

# math.fsum() 将一个容器类型数据中的元素进行一个求和运算
print(math.fsum([1, 2, 3]))  # 6

# math.factorial() 返回一个数的阶乘
print(math.factorial(5))  # 5 * 4 * 3 * 2 * 1 = 120

# 常量pi 数学常数 Π = 3.1415926..., 精确到可用精度
print(math.pi)  # 3.141592653589793

# 常量e 数学常数e, 精确到可用精度
print(math.e)  # 2.718281828459045

# 常量 tau, 数学常数 τ = 6.283185...，精确到可用精度。Tau 是一个圆周常数，等于 2π，圆的周长与半径之比
print(math.tau)  # 6.283185307179586
