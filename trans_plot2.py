# -*- coding: utf-8 -*-
# @Time    : 2023/12/8 20:40
# @Author  : longfei Kang
# @File    : trans_plot2.py
# yolo框定位映射数据程序

import numpy as np
import matplotlib.pyplot as plt

# 读取 ini 文件中的数据
ini_data = np.loadtxt('ini_test/166911126250312_OriData_20220719063838_1275.ini')

# 使用 matplotlib 将 ini 文件中的数据绘制成图像
fig, ax = plt.subplots()
ax.plot(ini_data)

# 关闭坐标轴
ax.axis('off')

# 手动调整子图的边距
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

# 计算图像的宽度
# image_width = fig.get_size_inches()[0] * fig.dpi
image_width = 585
# 计算缩放比例
scale = len(ini_data) / image_width
print(scale)
# 将图像上的横坐标转换为 ini 文件中的数据索引
x1, x2 = 243-28, 215-28  # 此处输入框图两个横坐标位置，一定要减28，是为了减去图像白边干扰。
index1 = int(x1 * scale)
index2 = int(x2 * scale)
print(index1, index2)
# index1 = index1 + 200
# index2 = index2 + 200

# 获取数据区间内的数据

data = ini_data[index2+1:index1]

# 计算最大值和最小值
# max_value = np.max(data)
min_value = np.min(data)
print(min_value)
# 计算最小值所在的索引
min_index = np.argmin(data)

# 计算最小值在 ini 文件中的行号
point = index2 + min_index + 1

print(point)
