# -*- coding: utf-8 -*-
# @Time    : 2023/12/8 19:37
# @Author  : longfei Kang
# @File    : draw_fans.py
# 预测前进行ini文件批量处理图像边框裁剪

import os
import numpy as np
import matplotlib.pyplot as plt

# 读取 ini 文件夹中的所有 ini 文件
ini_folder = './ini_test'  # 此处是需要进行预测动液面位置的ini文件存放的目录
ini_files = [f for f in os.listdir(ini_folder) if f.endswith('.ini')]

# 遍历 ini 文件夹中的所有 ini 文件
for ini_file in ini_files:
    # 读取 ini 文件中的数据
    ini_data = np.loadtxt(os.path.join(ini_folder, ini_file))

    # 使用 matplotlib 将 ini 文件中的数据绘制成图像
    fig, ax = plt.subplots()
    ax.plot(ini_data)

    # 关闭坐标轴
    ax.axis('off')

    # 手动调整子图的边距
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

    # 保存图像到文件中，并裁剪空白区域
    img_folder = './img'  # 这里是处理好的图片保存路径
    img_name = os.path.splitext(ini_file)[0] + '.png'
    img_path = os.path.join(img_folder, img_name)
    fig.savefig(img_path, bbox_inches='tight', pad_inches=0)
