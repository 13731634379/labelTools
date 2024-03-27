# -*- coding: utf-8 -*-
# @Time    : 2024/3/24 
# @Author  : machao
# @Email   : 13731634379@163.com
# @File    : xml2yolo.py
# @Software: PyCharm
# 作用      :批量处理xml数据标注文件，转为yolo模式标注文件
import xml.etree.ElementTree as ET
import os

def convert_coordinates(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[2]) / 2.0
    y = (box[1] + box[3]) / 2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

def convert_annotation(xml_file, classes):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    if w == 0 or h == 0:
        print(f"Skipping {xml_file}: width or height is 0.")
        return None

    annotations = []
    for obj in root.findall('object'):
        class_name = obj.find('name').text
        if class_name not in classes:
            continue
        class_id = classes.index(class_name)
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)
        box = (xmin, ymin, xmax, ymax)
        converted_box = convert_coordinates((w, h), box)
        annotations.append(f"{class_id} {' '.join([str(i) for i in converted_box])}")

    return annotations

def main(xml_folder, classes, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    xml_files = [f for f in os.listdir(xml_folder) if f.endswith('.xml')]
    for xml_file in xml_files:
        annotations = convert_annotation(os.path.join(xml_folder, xml_file), classes)
        if annotations is not None:
            with open(os.path.join(output_folder, os.path.splitext(xml_file)[0] + '.txt'), 'w') as f:
                f.write('\n'.join(annotations))

# 示例用法
# xml_folder = input("Enter the path to the folder containing XML files: ")
xml_folder = "D:/project/dataset/mcUAVdateset/search/img/020/xml"

# output_folder = input("Enter the path to the output folder: ")
output_folder = "D:/project/dataset/mcUAVdateset/search/img/020/label"

classes = ["UAV"]  # 替换成您的类别名称列表
main(xml_folder, classes, output_folder)

