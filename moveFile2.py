# -*- coding: utf-8 -*-
# @Time    : 2024/6/20 
# @Author  : machao
# @Email   : 13731634379@163.com
# @File    : moveFile.py
# @Software: PyCharm
# 作用      :1.txt文件中的名单是每行一个文件名（不包含文件扩展名），并且你需要根据这些名单将A文件夹内的名字相同的文件（包括扩展名）转移到B文件夹中

import os
import shutil

import shutil
import os

# 获取路径
#1.txt
file_list_path = 'D:/project/dataset/RTTS/images/1.txt'
#A文件夹
src_folder_path = 'D:/project/dataset/RTTS/images/train_dehaze'
#B文件夹
dest_folder_path = 'D:/project/dataset/RTTS/images/2'


# 确保目标文件夹存在
os.makedirs(dest_folder_path, exist_ok=True)

# 读取1.txt中的文件名
with open(file_list_path, 'r') as file:
    files_to_move = file.read().splitlines()  # 读取所有行并分割成列表

# 遍历文件名列表
for filename in files_to_move:
    # 构建完整的源文件路径和目标文件路径
    for src_file in os.listdir(src_folder_path):
        if src_file.startswith(filename):
            src_file_path = os.path.join(src_folder_path, src_file)
            dest_file_path = os.path.join(dest_folder_path, src_file)

            # 检查文件是否存在
            if os.path.isfile(src_file_path):
                # 移动文件
                shutil.move(src_file_path, dest_file_path)
                print(f"文件 {src_file} 已成功移动到 {dest_folder_path}")
            else:
                print(f"文件 {src_file} 在 {src_folder_path} 中不存在，无法移动。")
            break  # 找到匹配的文件后跳出循环
    else:
        print(f"没有找到匹配 {filename} 的文件。")