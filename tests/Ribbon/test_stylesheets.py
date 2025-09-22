#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_stylesheets.py
@Time    :   2025/09/22
@Author  :   XuMing
@Desc    :   手动测试 StyleSheets 模块（不用 pytest）
"""

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from src.Ribbon.StyleSheets import get_stylesheet

def main():
    # 检查样式表是否能正确加载
    names = ["main", "ribbon", "ribbonPane", "ribbonButton", "ViewLeader"]
    for name in names:
        css = get_stylesheet(name)
        if css:
            print(f"✅ 样式表 '{name}' 加载成功，长度: {len(css)}")
        else:
            print(f"❌ 样式表 '{name}' 加载失败或为空")

    # GUI 预览 main 样式表
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("StyleSheets 测试窗口")
    w.resize(400, 300)

    # 应用 main 样式
    w.setStyleSheet(get_stylesheet("main"))

    layout = QVBoxLayout()
    layout.addWidget(QLabel("这是一个测试标签"))
    w.setLayout(layout)

    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
