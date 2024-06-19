# -*- coding: utf-8 -*-
# @Time    : 2024/6/19 
# @Author  : machao
# @Email   : 13731634379@163.com
# @File    : txtContentCopyToTxt.py
# @Software: PyCharm
# 作用      :将A.txt中的内容从第x行到第y行进行剪切，并复制到B.txt中,并将选中行在A中删除掉

# 指定具体的文件路径
path_to_txt_a = 'D:\\project\\rtts.txt'  # 替换为A.txt文件的实际路径
path_to_txt_b = 'D:\\project\\lab.txt'  # 替换为B.txt文件的实际路径

# 假设x和y是你要剪切的起始和结束行号
x = 1055450  # 起始行号，从1开始计数
y = 2084899  # 结束行号

# 读取A.txt文件的所有行到一个列表中
with open(path_to_txt_a, 'r', encoding='utf-8') as file_a:
    lines = file_a.readlines()

# 检查x和y是否在数据范围内
if x < 1 or y > len(lines) or x > y:
    print("行号超出范围或起始行号大于结束行号")
else:
    # 剪切指定行的内容到B.txt文件
    cut_lines = lines[x-1:y]
    with open(path_to_txt_b, 'a', encoding='utf-8') as file_b:
        file_b.writelines(cut_lines)

    # 删除A.txt中的指定行
    # 从列表中删除指定行，重新组合剩余的行
    lines = lines[:x-1] + lines[y:]

    # 将剩余的行写回A.txt文件
    with open(path_to_txt_a, 'w', encoding='utf-8') as file_a:
        file_a.writelines(lines)

print("剪切到B.txt并从A.txt删除指定行完成")