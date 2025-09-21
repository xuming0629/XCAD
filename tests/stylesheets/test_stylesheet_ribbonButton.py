#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_stylesheet_ribbonButton.py
@Time    :   2025/09/21
@Author  :   XuMing
@Version :   v1.0
@Contact :   920972751@qq.com
@Desc    :   PyQt5 测试 Ribbon QToolButton 样式
"""

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QToolButton, QVBoxLayout, QLabel

# 获取项目根目录（假设 XCAD 下 src 和 tests 同级）

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# CSS 文件路径
CSS_PATH = os.path.join(ROOT_DIR, "src", "stylesheets", "ribbonButton.css")

def main():
    # 检查 CSS 文件是否存在
    if not os.path.exists(CSS_PATH):
        print(f"CSS 文件不存在: {CSS_PATH}")
        return

    # 创建 QApplication
    app = QApplication(sys.argv)

    # 创建主窗口
    window = QWidget()
    window.setWindowTitle("Ribbon QToolButton 样式测试")
    window.resize(400, 300)
    layout = QVBoxLayout(window)

    # 创建示例按钮
    btn1 = QToolButton()
    btn1.setText("普通按钮")

    btn2 = QToolButton()
    btn2.setText("可选中按钮")
    btn2.setCheckable(True)  # 支持选中状态

    btn3 = QToolButton()
    btn3.setText("悬停/按下按钮")

    # 添加按钮到布局
    layout.addWidget(QLabel("测试 QToolButton 样式效果"))
    layout.addWidget(btn1)
    layout.addWidget(btn2)
    layout.addWidget(btn3)

    # 读取并应用 CSS
    with open(CSS_PATH, "r", encoding="utf-8") as f:
        css = f.read()
    window.setStyleSheet(css)
    window.ensurePolished()

    # 输出提示
    if "QToolButton" in css:
        print("CSS 文件中包含 QToolButton 样式")
    else:
        print("CSS 文件未定义 QToolButton 样式")

    # 显示窗口
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
