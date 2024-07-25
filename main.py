from generate_module import generating
from slice_by_length_module import slicing_by_length
from clean_module import cleanning
from slice_by_title_module import slicing_by_title
from txt2md import generate_md

import os
import time


def main(dir):
    names = os.listdir(dir)  # 获取指定目录下的OCR识别后的TXT文档
    num = len(names)  # 统计TXT文档数量
    print('***********************************************************************************************************')
    for i, name in zip(range(1, num + 1), names):  # 循环，批量处理
        if 'txt' in name:  # 确认是TXT文档

            #path = 'D:\coding\workingspace\myprojects\qa_generator_tool\input\\' + name
            path = 'C:\\Users\Lenovo\Desktop\\test\\' + name  # 目录

            start = time.time()  # 计时开始

            length_slices = slicing_by_length(path, name)  # 1. 将OCR识别后文本根据长度切片
            md = generate_md(path)                         # 2. 将OCR识别后文本转换为Markdown类型文档
            titles_slices = slicing_by_title(md)           # 3. 将转换后的Markdown文档根据标题切片
            slices = length_slices + titles_slices         # 4. 将长度切片和标题切片合并
            qas = generating(slices, name)                 # 5. 根据切片调用GPT生成问答
            cleanning(slices, qas, name)                   # 6. 将问答统一格式，增加主语，删除部分无用内容

            end = time.time()  # 计时结束
            cost = int(end - start) / 60  # 转换为分钟单位

            size = os.path.getsize(path) / 1024  # 计算文件大小，转换为kb单位
            print(f'[{i}/{num}]    成功生成《{name}》的问答文档, 原文本体积为{size:.1f}KB,生成耗时约{cost:.1f}分钟')


if __name__ == "__main__":
    dir = 'C:\\Users\Lenovo\Desktop\\test\\'

    start = time.time()
    main(dir)
    end = time.time()
    cost = int(end - start) / 60
    print('***********************************************************************************************************')
    print(f'已生成所有问答文档，总耗时{cost:.1f}分钟')
    print('***********************************************************************************************************')
