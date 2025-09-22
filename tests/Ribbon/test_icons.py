#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_icon.py
@Time    :   2025/09/22
@Author  :   XuMing
@Desc    :   手动测试 Icons 模块（不用 pytest）
"""

import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QIcon

# 获取项目根目录（XCAD）
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
SRC_DIR = os.path.join(ROOT_DIR, "src")
sys.path.insert(0, SRC_DIR)

from src.Ribbon.Icons import Icons, get_icon


def run_basic_tests():
    """在终端打印 Icons 功能测试结果"""
    icons = Icons()

    # 测试默认图标
    default_icon = icons.icon("default")
    print("默认图标是否有效:", not default_icon.isNull())

    # 遍历所有图标
    icons_dir = os.path.join(SRC_DIR, "icons")
    print(f"扫描图标目录: {icons_dir}")
    if not os.path.exists(icons_dir):
        print("❌ 图标目录不存在")
        return

    png_files = [f.replace(".png", "") for f in os.listdir(icons_dir) if f.endswith(".png")]
    for name in png_files:
        icon = icons.icon(name)
        status = "✅ OK" if not icon.isNull() else "❌ 失败"
        print(f"图标 {name}: {status}")


def run_gui_preview():
    """GUI 窗口展示所有图标"""
    app = QApplication(sys.argv)

    icons = Icons()

    window = QWidget()
    window.setWindowTitle("Icons 测试预览")
    layout = QVBoxLayout(window)

    icons_dir = os.path.join(SRC_DIR, "icons")
    png_files = [f.replace(".png", "") for f in os.listdir(icons_dir) if f.endswith(".png")]

    if not png_files:
        layout.addWidget(QLabel("未找到任何图标"))
    else:
        for name in png_files:
            btn = QPushButton(name)
            btn.setIcon(icons.icon(name))
            layout.addWidget(btn)

    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    print("=== Icons 模块测试开始 ===")
    run_basic_tests()
    print("=== 打开 GUI 窗口预览图标 ===")
    run_gui_preview()
