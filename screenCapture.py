# -*- coding: utf-8 -*-
# @Time    : 2024/3/19 
# @Author  : machao
# @Email   : 13731634379@163.com
# @File    : screenCapture.py
# @Software: PyCharm
# 作用      :视频截屏并输出

import cv2
import os

def extract_frames(video_path, output_folder,num_frames_per_sec,pre_name, start_time=None, end_time=None):
    # 创建输出文件夹
    os.makedirs(output_folder, exist_ok=True)

    # 打开视频文件
    cap = cv2.VideoCapture(video_path)

    # 获取视频帧率和总帧数
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # 计算起始帧和结束帧
    start_frame = int(start_time * fps) if start_time is not None else 0
    end_frame = int(end_time * fps) if end_time is not None else total_frames

    # 计算每秒截图的间隔
    interval = int(fps / num_frames_per_sec)

    # 计数器，用于命名截图文件
    count = 0

    # 设置读取视频的起始位置
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    # 读取视频
    while cap.isOpened():
        # 读取视频帧
        ret, frame = cap.read()

        if not ret or count > end_frame:
            break

        # 每间隔interval帧截图一次
        if count % interval == 0:
            # 构建截图文件路径
            image_path = os.path.join(output_folder, f"{pre_name}frame_{count:04d}.jpg")
            # 保存截图
            cv2.imwrite(image_path, frame)
            print(f"保存截图: {image_path}")

        count += 1

    # 释放视频资源
    cap.release()


# 使用示例
if __name__ == "__main__":
    # 输入视频文件路径
    # video_path = input("请输入视频文件路径: ")
    # video_path = "D:\project\dataset\movies\\12.mp4"
    video_path = "D:/project/dataset/movies/side_switch/test4.mp4"

    #名字前缀
    pre_name = "val"
    print(video_path)

    # 输入截图保存的文件夹路径
    # output_folder = input("请输入截图保存的文件夹路径: ")
    # output_folder = "D:\project\dataset\movies\pic"
    output_folder = "D:/project/dataset/movies/pic"
    print(output_folder)

    # 输入开始截图的时间（秒），如果不指定则为None
    start_time_input = 0
    # start_time_input = None
    start_time = float(start_time_input) if start_time_input else None

    # 输入结束截图的时间（秒），如果不指定则为None
    end_time_input = 100
    # end_time_input=None
    end_time = float(end_time_input) if end_time_input else None

    # 每秒截图的次数
    num_frames_per_sec = 2

    # 提取视频帧并保存截图
    extract_frames(video_path, output_folder,num_frames_per_sec,pre_name, start_time, end_time,)


