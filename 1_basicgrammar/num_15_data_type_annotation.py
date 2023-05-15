"""
    类型注解:
        变量类型注解:
            格式: variable_name : data_type
            例: num : int = 10
        各种变量类型注解格式:
            int ==> variable_name: int
            float ==> variable_name: float
            bool == variable_name:bool
            complex ==> variable_name:complex
            str ==> variable_name:str
            list ==> variable_name:list
            tuple ==> variable_name:tuple
            set ==> variable_name:set
            dict ==> variable_name:dict
        容器类型变量详细注解:
            list ==> variable_name:list[data_type]
            tuple ==> variable_name:tuple[type1, type2, type3...]
                元组类型设置类型详细注解, 需要将每个元素的数据类型标记出来
            set ==> variable_name:set[data_type]
            dict ==> variable_name:dict[key_type, value_type]: 字典设置类型详细注解, 需要指定键与值的数据类型
        变量注解还可以使用注释来定义:
            格式:
                variable_name = start_value  # type: data_type
        注意: 类型注解仅仅是提示作用, 对于变量的根本类型无决定作用
        函数和方法类型注解:
            格式:
                def func_name (variable:data_type) -> return_type:
                    pass
"""

if __name__ == '__main__':
    # 通过类型注解定义仅存放数字的列表
    list_num = [1, 2, 3]  # type: list[int]
    print(list_num)
