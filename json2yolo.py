# -*- coding: utf-8 -*-
# @Time    : 2024/3/23 
# @Author  : machao
# @Email   : 13731634379@163.com
# @File    : json2yolo.py
# @Software: PyCharm
# 作用      :将json标签文件转为yolo标签
import os
import json

def convert_to_yolo(json_file, output_dir, class_map):
    with open(json_file, 'r') as f:
        data = json.load(f)

    images = {img['id']: img for img in data['images']}
    annotations = {ann['id']: ann for ann in data['annotations']}
    categories = {cat['id']: cat for cat in data['categories']}

    for img_id, ann in annotations.items():
        image_info = images[ann['image_id']]
        image_name = image_info["file_name"]
        image_name_without_ext = os.path.splitext(image_name)[0]
        output_file = os.path.join(output_dir, image_name_without_ext + ".txt")

        with open(output_file, 'w') as f:
            category_id = ann['category_id']
            category_name = categories[category_id]['name']
            if category_name not in class_map:
                raise ValueError(f"Class '{category_name}' not found in class map!")
            class_id = class_map[category_name]
            bbox = ann['bbox']
            x_center = (bbox[0] + bbox[2] / 2) / image_info['width']
            y_center = (bbox[1] + bbox[3] / 2) / image_info['height']
            width = bbox[2] / image_info['width']
            height = bbox[3] / image_info['height']
            f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")

# Example usage
# json_file = input("Enter the path to the JSON file: ")
# json_file = "D:\project\dataset\mcUAVdateset\test\instances_test2017.json"
json_file = "D:/project/dataset/mcUAVdateset/search/val2017/instances_val2017.json"
print(json_file)

# output_dir = input("Enter the output directory path for YOLO labels: ")
# output_dir = "D:/project/dataset/mcUAVdateset/test"
output_dir = "D:/project/dataset/mcUAVdateset/search/val2017/label"
print(output_dir)

class_map = {"UAV": 0}  # Mapping class names to class IDs

convert_to_yolo(json_file, output_dir, class_map)

