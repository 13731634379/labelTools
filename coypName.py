# -*- coding: utf-8 -*-
# @Time    : 2024/7/22 
# @Author  : machao
# @Email   : 13731634379@163.com
# @File    : coypName.py
# @Software: PyCharm
# 作用      :将文件夹A中的文件名称添加道B.txt文件中，要求每个文件在B中占据一行，并在每行前添加字符串，要求字符串根据输入给出，并按输入判断在B中是否保留A中文件的后缀名

import os

# 文件夹A的路径
# folder_a = 'path/to/folder/A'
folder_a = 'D:/project/dataset/RTTS/images/train'
# B.txt文件的路径
b_txt_path = 'D:/project/1/B.txt'

# 获取用户输入的前缀字符串
prefix = "train/"

# 询问用户是否保留文件扩展名
end_name = False

# 获取文件夹A中的所有文件名称
files_in_a = [f for f in os.listdir(folder_a) if os.path.isfile(os.path.join(folder_a, f))]

# 打开B.txt文件准备写入
with open(b_txt_path, 'w') as b_file:
    # 遍历文件名列表
    for filename in files_in_a:
        # 根据用户选择决定是否保留扩展名
        if not end_name:
            # 去掉文件名的扩展名
            filename = os.path.splitext(filename)[0]

        # 格式化每行的内容：在文件名前添加用户输入的前缀
        line = f'{prefix}{filename}\n'
        # 写入B.txt文件
        b_file.write(line)

print(f'文件名已添加到{b_txt_path}')