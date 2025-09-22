#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   Icons.py
@Time    :   2025/09/22
@Author  :   XuMing
@Version :   v1.1
@Contact :   920972751@qq.com
@License :   Copyright (c) 2021-2025 XuMing. All Rights Reserved.
@Desc    :   图标管理类，自动扫描 icons 文件夹中的 PNG 文件，生成 QIcon 对象。
"""

from PyQt5.QtGui import QIcon, QPixmap
import os

# 全局单例实例
icons_instance = None

def get_icon(name):
    """
    全局获取图标函数，如果没有实例化 Icons 类则先创建
    :param name: 图标名称（不带 .png 后缀）
    :return: QIcon 对象
    """
    global icons_instance
    if not icons_instance:
        icons_instance = Icons()
    return icons_instance.icon(name)


class Icons(object):
    """
    图标管理类
    扫描指定文件夹下的 PNG 文件并生成 QIcon 对象
    提供默认图标 fallback
    """

    def __init__(self):
        self._icons = {}  # 存放 {图标名: QIcon} 键值对
        # 扫描 icons 文件夹并生成图标
        self.set_all_icons_name()
        # 手动添加一些常用图标
        self.make_icon("default", "./src/icons/folder.png")
        self.make_icon("folder", "./src/icons/folder.png")
        self.make_icon("open", "./src/icons/folder.png")
        self.make_icon("save", "./src/icons/save.png")
        self.make_icon("icon", "./src/icons/icon.png")
        self.make_icon("exit", "./src/icons/exit.png")
        self.make_icon("paste", "./src/icons/paste.png")
        self.make_icon("zoom", "./src/icons/zoom.png")
        self.make_icon("copy", "./src/icons/copy.png")
        self.make_icon("about", "./src/icons/about.png")
        self.make_icon("license", "./src/icons/license.png")
        self.make_icon("sketch", "./src/icons/direct_sketch.2l.png")

    def set_all_icons_name(self, path="./src/icons"):
        """
        扫描指定目录下的 PNG 文件，并生成图标
        :param path: 图标目录
        """
        if not os.path.exists(path):
            print(f"图标目录不存在: {path}")
            return

        for filename in os.listdir(path):
            if filename.endswith(".png"):
                icon_name = filename.replace(".png", "")
                icon_path = os.path.join(path, filename)
                self.make_icon(icon_name, icon_path)

    def make_icon(self, name, path):
        """
        创建单个图标并加入 _icons 字典
        :param name: 图标名称
        :param path: 图标路径
        """
        if not os.path.exists(path):
            print(f"警告: 图标文件不存在: {path}")
            return

        icon = QIcon()
        icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)
        self._icons[name] = icon

    def icon(self, name):
        """
        获取指定名称的 QIcon
        :param name: 图标名称
        :return: QIcon 对象，如果不存在返回 default
        """
        icon = self._icons.get("default", QIcon())
        try:
            icon = self._icons[name]
        except KeyError:
            print(f"icon '{name}' not found, fallback to default")
        return icon


# ===============================
# 测试部分
# ===============================
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)  # ✅ 必须先创建

    icons = Icons()
    print("默认图标:", icons.icon("default"))
    print("folder 图标:", icons.icon("folder"))
    print("不存在的图标:", icons.icon("non_exist"))
    print("icon 图标:", icons.icon("icon"))
    print("save 图标:", icons.icon("save"))