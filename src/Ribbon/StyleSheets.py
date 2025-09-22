#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   StyleSheets.py
@Time    :   2025/09/22 22:59:27
@Author  :   XuMing
@Version :   v1.0
@Contact :   920972751@qq.com
@License :   Copyright (c) 2021-2025 XuMing. All Rights Reserved.
@Desc    :   样式表管理模块，支持通过 name 获取对应 QSS 文件内容
'''

# 单例实例
stylesheet_instance = None


def get_stylesheet(name):
    """
    全局获取指定样式表
    """
    global stylesheet_instance
    if not stylesheet_instance:
        stylesheet_instance = Stylesheets()
    return stylesheet_instance.get_stylesheet(name)


class Stylesheets(object):
    """管理所有样式表的类"""

    def __init__(self):
        self._stylesheets = {}

        # 初始化并加载所有样式表
        self.make_stylesheet("main", "src/stylesheets/main.css")
        self.make_stylesheet("ribbon", "src/stylesheets/ribbon.css")
        self.make_stylesheet("ribbonPane", "src/stylesheets/ribbonPane.css")
        self.make_stylesheet("ribbonButton", "src/stylesheets/ribbonButton.css")
        self.make_stylesheet("ribbonSmallButton", "src/stylesheets/ribbonSmallButton.css")
        self.make_stylesheet("tittlebarButton", "src/stylesheets/tittlebarButton.css")
        self.make_stylesheet("tittlebarButtonWindown", "src/stylesheets/tittlebarButtonWindown.css")
        self.make_stylesheet("ViewLeaderButton", "src/stylesheets/ViewLeaderButton.css")
        self.make_stylesheet("ViewLeader", "src/stylesheets/ViewLeader.css")

    def make_stylesheet(self, name, path):
        """
        读取指定路径的 CSS/QSS 文件，并存储到字典中
        :param name: 样式表名称
        :param path: 样式表文件路径
        """
        try:
            with open(path, encoding="utf-8") as data_file:
                stylesheet = data_file.read()
            self._stylesheets[name] = stylesheet
        except FileNotFoundError:
            print(f"⚠️ 样式表文件不存在: {path}")
            self._stylesheets[name] = ""

    def get_stylesheet(self, name):
        """
        获取指定名称的样式表内容
        :param name: 样式表名称
        :return: 样式表字符串
        """
        stylesheet = ""
        try:
            stylesheet = self._stylesheets[name]
        except KeyError:
            print(f"⚠️ 样式表 {name} 未找到")
        return stylesheet
