# -*- coding: utf-8 -*-
# @Time    : 2024/3/23 
# @Author  : machao
# @Email   : 13731634379@163.com
# @File    : copyFileByPic.py
# @Software: PyCharm
# 作用      :根据图片名称，复制标签文件到其他文件夹

import os
import shutil


def copy_files_if_exists(folder_A, folder_B, folder_C):
    # 获取文件夹 A 中的所有文件名（不考虑后缀名）
    files_in_A = [os.path.splitext(file)[0] for file in os.listdir(folder_A)]

    # 获取文件夹 B 中的所有文件名（不考虑后缀名）
    files_in_B = [os.path.splitext(file)[0] for file in os.listdir(folder_B)]

    # 遍历文件夹 A 中的文件
    for file_name in files_in_A:
        # 检查文件夹 B 中是否存在同名文件（不考虑后缀名）
        if file_name in files_in_B:
            # 构建文件的完整路径（包括后缀名）
            file_path_A = os.path.join(folder_A, file_name + os.path.splitext(os.listdir(folder_A)[0])[1])
            file_path_B = os.path.join(folder_B, file_name + os.path.splitext(os.listdir(folder_B)[0])[1]).replace("\\", "/")
            # file_path_B = folder_B+"/"+file_name+".txt"

            # 构建文件 C 的完整路径（包括后缀名）
            file_path_C = os.path.join(folder_C, file_name + os.path.splitext(os.listdir(folder_B)[0])[1]).replace("\\", "/")
            # file_path_C = folder_C + "/" + file_name + ".txt"

            # 将文件夹 B 中的文件复制到文件夹 C
            shutil.copy(file_path_B, file_path_C)


# 示例用法
# folder_A = input("Enter the path to folder A: ")
# folder_A = "D:/project/dataset/mcUAVdateset/search/val2017"
folder_A = "D:/project/dataset/mcUAVdateset/search/img/020"

# folder_B = input("Enter the path to folder B: ")
# folder_B = "D:/project/dataset/mcUAVdateset/search/label-all/val2017"
folder_B = "D:/project/dataset/mcUAVdateset/search/img/020/xml"

# folder_C = input("Enter the path to folder C: ")
# folder_C = "D:/project/dataset/mcUAVdateset/search/val_label"
folder_C = "D:/project/dataset/mcUAVdateset/search/img/020/xml2"

copy_files_if_exists(folder_A, folder_B, folder_C)

