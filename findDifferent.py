# -*- coding: utf-8 -*-
# @Time    : 2024/9/1 
# @Author  : machao
# @Email   : 13731634379@163.com
# @File    : findDifferent.py
# @Software: PyCharm
# 作用      :找出文件夹A，B中名称不同的文件

import os


def find_different_files(folder_a, folder_b):
    # 获取两个文件夹中的文件名列表
    files_in_a = set(os.listdir(folder_a))
    files_in_b = set(os.listdir(folder_b))

    # 找出只存在于A中的文件
    only_in_a = files_in_a - files_in_b
    # 找出只存在于B中的文件
    only_in_b = files_in_b - files_in_a

    # 输出结果
    for file in only_in_a:
        print(f"File '{file}' is only in folder A.")
    for file in only_in_b:
        print(f"File '{file}' is only in folder B.")


# 指定文件夹路径
folder_a_path = 'D:/project/dataset/RTTS/images/train_dehaze2'  # 替换为你的文件夹A路径
folder_b_path = 'D:/project/dataset/RTTS/images/train'  # 替换为你的文件夹B路径

# 调用函数
find_different_files(folder_a_path, folder_b_path)
