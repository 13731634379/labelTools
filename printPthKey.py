# -*- coding: utf-8 -*-
# @Time    : 2024/11/7 
# @Author  : machao
# @Email   : 13731634379@163.com
# @File    : printPthKey.py
# @Software: PyCharm
# 作用      :输出权重文件的键值对
import torch

# 加载 Checkpoint 文件
ckpt = torch.load(r'D:\project\pth_file\rtdetrv2_r34vd_120e_coco_ema.pth')

# 打印字典的键值对
for key, value in ckpt.items():
    print(key)