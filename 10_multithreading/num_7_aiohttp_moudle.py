"""
    aiohttp模块:
        异步http请求模块, 类似于requests模块, 支持异步操作
        创建异步请求对象:
            request_object = aiohttp.ClientSession()
            aiohttp模块创建请求对象, 对象方法支持异步操作, 可以使用await关键字修饰
            发送请求:
                response = await request_object.get(url)
            获取文本内容:
                data = await response.text()
            获取二进制数据:
                data = await response.content.read()

"""
import asyncio
import aiohttp

urls = [
    'http://kr.shanghai-jiuxin.com/file/2021/0106/bb2624394073427fc3104b52b160bc83.jpg',
    'http://kr.shanghai-jiuxin.com/file/2021/0709/e79feeb471cecfcc0ca4fffec3d96137.jpg',
    'http://kr.shanghai-jiuxin.com/file/2021/0106/af5bf84ba13d20af37d9ffb01181c109.jpg'
]


# async关键词定义异步执行函数
async def down_load(url: str):
    name = url.rsplit('/', 1)[1]
    async with aiohttp.ClientSession() as s:
        async with s.get(url) as res:
            # # 获取文本
            # print(await res.text())
            # # 转换为字节数据
            # print(await res.content.read())
            with open('{}'.format(name), 'wb') as file:
                file.write(await res.content.read())
    # # s = aiohttp.ClientSession()  # s相当于原来的requetst
    # res = s.get(url)
    # print(res.text())
    #
    # # pass


async def main():
    tasks = []  # 创建任务列表
    for url in urls:
        # 创建任务对象
        task = asyncio.create_task(down_load(url))
        tasks.append(task) # 任务对象添加列表
    await asyncio.wait(tasks)


if __name__ == '__main__':
    # 列表推导式创建包含协程对象的列表
    task_list: list = [down_load(url) for url in urls]
    asyncio.get_event_loop().run_until_complete(asyncio.wait(task_list))
