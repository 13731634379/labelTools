# -*- coding: utf-8 -*-
# @Time    : 2024/6/20 
# @Author  : machao
# @Email   : 13731634379@163.com
# @File    : moveFile.py
# @Software: PyCharm
# 作用      :A文件夹中名字中含有dehaze字段的文件移动到B文件夹

import os
import shutil

# 给定的文件夹地址
folder_A = 'D:/download/BaiduNetdiskDownload/数据集/RTTS_yolov8/labels/train1'
folder_B = 'D:/download/BaiduNetdiskDownload/数据集/RTTS_yolov8/labels/train-dehaze'

# 遍历A文件夹中的所有文件和文件夹
for filename in os.listdir(folder_A):
    # 检查文件名是否包含'dehaze'
    if 'dehaze' in filename:
        # 构造完整的文件路径
        file_path = os.path.join(folder_A, filename)
        # 移动文件到B文件夹
        shutil.move(file_path, os.path.join(folder_B, filename))

print("文件移动完成。")