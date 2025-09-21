#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_stylesheet_ribbon.py
@Time    :   2025/09/21
@Author  :   XuMing
@Version :   v1.1
@Contact :   920972751@qq.com
@License :   Copyright (c) 2021-2025 XuMing. All Rights Reserved.
@Desc    :   PyQt5 Ribbon CSS/QSS 测试脚本（直接运行）
"""

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QToolBar, QTabWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QColor

# 获取项目根目录（XCAD），确保 src 和 tests 同级
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ribbon.css 文件路径
CSS_PATH = os.path.join(ROOT_DIR, "src", "stylesheets", "ribbon.css")


def main():
    # 检查 CSS 文件是否存在
    if not os.path.exists(CSS_PATH):
        print(f"CSS 文件不存在: {CSS_PATH}")
        return

    # 创建 QApplication
    app = QApplication(sys.argv)

    # 创建主窗口
    window = QWidget()
    window.setWindowTitle("Ribbon CSS 测试示例")
    window.resize(800, 500)

    # 布局
    layout = QVBoxLayout(window)

    # 工具栏示例
    toolbar = QToolBar("工具栏")
    toolbar.addAction("按钮1")
    toolbar.addAction("按钮2")
    layout.addWidget(toolbar)

    # 标签页示例
    tab_widget = QTabWidget()
    for i in range(1, 4):
        page = QWidget()
        page_layout = QVBoxLayout(page)
        page_layout.addWidget(QLabel(f"这是第 {i} 个标签页的内容"))
        tab_widget.addTab(page, f"标签 {i}")
    layout.addWidget(tab_widget)

    # 读取 CSS 文件
    with open(CSS_PATH, "r", encoding="utf-8") as f:
        css = f.read()

    # 应用 CSS
    window.setStyleSheet(css)
    window.ensurePolished()

    # 简单验证 CSS 是否包含预期背景色
    expected_bg_color = "#efefef"  # ribbon.css 底部渐变颜色之一
    if expected_bg_color in css:
        print(f"CSS 文件中包含预期颜色：{expected_bg_color}")
    else:
        print(f"CSS 文件未定义预期颜色：{expected_bg_color}")

    # 显示窗口
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
