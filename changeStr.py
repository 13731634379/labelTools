# -*- coding: utf-8 -*-
# @Time    : 2024/6/24 
# @Author  : machao
# @Email   : 13731634379@163.com
# @File    : changeStr.py
# @Software: PyCharm
# 作用      :python实现：将A.txt只中的B字符串替换为C字符串，A由地址指定


def replace_all_occurrences(file_path, target, replacement):
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 替换所有目标字符串
        updated_content = content.replace(target, replacement)

        # 将更新后的内容写回文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        print(f"所有 '{target}' 已被替换为 '{replacement}'。")

    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 未找到。")
    except Exception as e:
        print(f"发生错误：{e}")

# 指定文件路径
file_path = 'D:/project/dataset/RTTS/labels/rtts_rt.txt'  # 替换为实际文件路径
# 指定要替换的目标字符串
target = '"category_id": 0'
# 指定替换后的字符串
replacement = '"category_id": 5'

# 调用函数执行替换
replace_all_occurrences(file_path, target, replacement)