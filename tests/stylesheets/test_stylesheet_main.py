#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_stylesheet_main.py
@Time    :   2025/09/21 21:35:07
@Author  :   XuMing
@Version :   v1.1
@Contact :   920972751@qq.com
@License :   Copyright (c) 2021-2025 XuMing. All Rights Reserved.
@Desc    :   PyQt5 CSS 测试脚本（直接运行）
'''

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QColor

# 获取项目根目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



# CSS 文件路径
CSS_PATH = os.path.join(ROOT_DIR, "src", "stylesheets", "main.css")



def main():
    # 检查 CSS 文件是否存在
    if not os.path.exists(CSS_PATH):
        print(f"CSS 文件不存在: {CSS_PATH}")
        return

    # 创建 QApplication
    app = QApplication(sys.argv)

    # 创建 QWidget
    w = QWidget()
    
    # 读取 CSS 文件
    with open(CSS_PATH, "r", encoding="utf-8") as f:
        css = f.read()
    
    # 应用 CSS
    w.setStyleSheet(css)
    
    # 强制刷新样式
    w.ensurePolished()
    
    # 获取样式表中定义的背景色（#dfe9f5 -> RGB 223, 233, 245）
    expected_color = QColor(223, 233, 245)
    bg_color = w.palette().color(w.backgroundRole())
    
    # 简单验证 CSS 是否包含预期背景色
    if "#dfe9f5" in css:
        print("CSS 文件中包含预期的背景色：#dfe9f5")
    else:
        print("CSS 文件未定义预期背景色")
    
    # 设置窗口标题和大小，并显示
    w.setWindowTitle("CSS 背景色测试")
    w.resize(400, 300)
    w.show()
    
    # 进入 Qt 事件循环
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
