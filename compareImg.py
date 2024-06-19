# -*- coding: utf-8 -*-
# @Time    : 2024/3/28 
# @Author  : machao
# @Email   : 13731634379@163.com
# @File    : compareImg.py
# @Software: PyCharm
# 作用      :比较两文件夹中图片是否存在相同的
import os
import filecmp

def find_duplicate_images(folder1, folder2):
    # 获取文件夹1和文件夹2中的所有图片文件
    images1 = [f for f in os.listdir(folder1) if (os.path.isfile(os.path.join(folder1, f)) and (f.endswith('.jpg') or f.endswith('.png')))]
    images2 = [f for f in os.listdir(folder2) if (os.path.isfile(os.path.join(folder2, f)) and (f.endswith('.jpg') or f.endswith('.png')))]

    # 比较两个文件夹中的图片文件是否相同
    found_duplicates = False
    for img1 in images1:
        for img2 in images2:
            if filecmp.cmp(os.path.join(folder1, img1), os.path.join(folder2, img2)):
                print(f"相同图片的名字：{img1}（在文件夹A中）和 {img2}（在文件夹B中）")
                found_duplicates = True

    if not found_duplicates:
        print("未找到相同的图片。")

# 示例用法
# folder_A = "/path/to/folder/A"
folder_A = "D:/project/dataset/mcUAVdateset/img/train"
# folder_B = "/path/to/folder/B"
# folder_B = "D:/project/dataset/mcUAVdateset/search/test2017"
folder_B = "D:/project/dataset/movies/pic"
find_duplicate_images(folder_A, folder_B)

