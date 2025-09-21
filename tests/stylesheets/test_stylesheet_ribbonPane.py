#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_stylesheet_ribbonPane.py
@Time    :   2025/09/21
@Author  :   XuMing
@Version :   v1.0
@Contact :   920972751@qq.com
@Desc    :   PyQt5 测试 Ribbon Pane QWidget 样式
"""

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

# 获取项目根目录（假设 XCAD 下 src 和 tests 同级）
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# CSS 文件路径
CSS_PATH = os.path.join(ROOT_DIR, "src", "stylesheets", "ribbonPane.css")

def main():
    # 检查 CSS 文件是否存在
    if not os.path.exists(CSS_PATH):
        print(f"CSS 文件不存在: {CSS_PATH}")
        return

    # 创建 QApplication
    app = QApplication(sys.argv)

    # 创建主窗口
    window = QWidget()
    window.setWindowTitle("Ribbon Pane 样式测试")
    window.resize(400, 300)

    layout = QVBoxLayout(window)

    # 创建一些示例子控件
    label1 = QLabel("这是一个测试标签")
    label2 = QLabel("看看字体是否应用为微软雅黑 9pt")
    layout.addWidget(label1)
    layout.addWidget(label2)

    # 读取并应用 CSS
    with open(CSS_PATH, "r", encoding="utf-8") as f:
        css = f.read()
    window.setStyleSheet(css)
    window.ensurePolished()

    # 简单验证 CSS 是否包含字体设置
    if "微软雅黑" in css:
        print("CSS 文件中包含字体设置：微软雅黑")
    else:
        print("CSS 文件未定义字体设置")

    # 显示窗口
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
