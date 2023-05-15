"""
    json模块:
        python数据和json数据相互转换
        1. python数据转换为json格式的字符串
            data = json.dumps(data)
        2. python的数据类型转为json格式的字符串并存入文件
            json.dump(python_data, file_name, ensure_ascii=False)
                python_data: python类型的数据(字典, 列表等)
                file_name: 文件对象
                ensure_ascii: ensure_ascii=False 序列化时编码
        3. json格式的字符串转换为python数据
            data = json.loads(data)
        4. 读取json文件, 并将数据转为python类型
            data = json.load(json格式的文件对象)
"""
import json


if __name__ == '__main__':
    # 读取json文件数据
    with open('$1_app.js', 'r', encoding='utf-8') as file_js:
        js_data = file_js.read()
        # json格式数据转换为Python数据
        js_data = json.loads(js_data)
        print(type(js_data))
        # 将python格式数据转为json格式并存入文件
        json.dump(js_data, open('$1_app_test.js', 'w', encoding='utf-8'), ensure_ascii=False)
        # python数据转换为json格式字符串
        js_data = json.dumps(js_data)
        print(type(js_data))
        print(js_data)