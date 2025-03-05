# -*- coding: utf-8 -*-
# @Time    : 2024/9/1 
# @Author  : machao
# @Email   : 13731634379@163.com
# @File    : reName.py
# @Software: PyCharm
# 作用      :将文件夹中所有文件的名称中含有的字符串A全部该为字符串B
import os

def rename_files_in_folder(folder_path, old_string, new_string):
    # 遍历指定文件夹
    for filename in os.listdir(folder_path):
        # 构建完整的文件路径
        file_path = os.path.join(folder_path, filename)
        # 检查是否为文件
        if os.path.isfile(file_path):
            # 替换文件名中的字符串A为字符串B
            new_filename = filename.replace(old_string, new_string)
            # 构建新的文件路径
            new_file_path = os.path.join(folder_path, new_filename)
            # 重命名文件
            os.rename(file_path, new_file_path)
            print(f'Renamed "{filename}" to "{new_filename}"')

# 指定文件夹路径
folder_path = 'D:/project/dataset/RTTS/images/val_dehaze2'  # 替换为你的文件夹路径
old_string = '_MSBDN'  # 要替换的字符串
new_string = ''  # 替换后的字符串

# 调用函数
rename_files_in_folder(folder_path, old_string, new_string)