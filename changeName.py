# -*- coding: utf-8 -*-
# @Time    : 2024/3/19 
# @Author  : machao
# @Email   : 13731634379@163.com
# @File    : changeName.py
# @Software: PyCharm
# 作用      :修改文件名称,待修改文件按名称依次进行名称修改
import os
import datetime

def batch_rename_files(directory, start_number,name_pre,log_txt):
    # 设置初始数字
    number = start_number
    log_file = open(log_txt, 'a+')
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file.write('\n')
    log_file.write(current_time + '\n')
    # 遍历目录中的所有文件
    for filename in sorted(os.listdir(directory)):
        # 构建完整的文件路径
        old_filepath = os.path.join(directory, filename)
        # 如果是文件
        if os.path.isfile(old_filepath):
            # 构建新的文件名
            new_filename = str(name_pre)+str(number).zfill(5) + os.path.splitext(filename)[1]
            new_filepath = os.path.join(directory, new_filename)
            try:
                # 重命名文件
                os.rename(old_filepath, new_filepath)
                print(f"文件 {filename} 重命名为 {new_filename}")
                log_file.write(str(f"{directory}中文件 {filename} 重命名为 {new_filename}") + '\n')
            except Exception as e:
                print(f"无法重命名文件 {filename}: {e}")
            # 增加数字
            number += 1
    log_file.close()


# 使用示例
if __name__ == "__main__":
    # 输入要处理的目录路径
    # directory = input("请输入要处理的目录路径: ")
    # directory = "D:\project\dataset\mcUAVdateset\search\lab\\val"
    directory = "D:\project\dataset\movies\pic"
    # directory = "D:\project\dataset\mcUAVdateset\search\img\\test"
    # directory = "D:\project\dataset\mcUAVdateset\img"
    # directory = "D:\project\dataset\mcUAVdateset\search\lab"
    # directory = "D:\project\dataset\mcUAVdateset\label"

    print(directory)

    # 输入起始数字
    start_number = int(input("请输入起始数字: "))

    name_pre="test_";

    # log_txt="D:/project/dataset/mcUAVdateset/changeNameLog.txt"
    log_txt="D:/project/dataset/movies/pic/changeNameLog.txt"

    # 调用函数批量重命名文件
    batch_rename_files(directory, start_number,name_pre,log_txt)
