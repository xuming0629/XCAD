# -*- coding: utf-8 -*-
#!/usr/bin/env python
# ****************************************************
# @FileName      :   SketcherButton.py
# @Time          :   2025/10/03 07:50:37
# @Author        :   XuMing
# @Version       :   1.0
# @Email         :   920972751@qq.com
# @Description   :   Ribbon 风格按钮（Sketcher按钮 + 标题栏按钮）
# @Copyright     :   XuMing. All Rights Reserved.
# ****************************************************

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QToolButton
from src.Ribbon import gui_scale
from src.Ribbon.StyleSheets import get_stylesheet


class SketcherButton(QToolButton):
    """
    草图工具按钮类
    --------------------
    Ribbon 风格按钮，图标在上方，文本在下方。
    支持设置图标、大小、提示信息和点击事件。
    """

    def __init__(self, parent=None, object_name=None, icon_name=None, icon_size=None, action_tip=None, action=None):
        super().__init__(parent)
        sc = gui_scale()

        # 设置按钮尺寸
        self.setMaximumWidth(int(25 * sc))
        self.setMinimumWidth(int(25 * sc))
        self.setMinimumHeight(int(50 * sc))
        self.setMaximumHeight(int(50 * sc))

        self.setStyleSheet(get_stylesheet("SketcherButton"))
        self.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.setIconSize(QSize(int(32 * sc), int(32 * sc)))

        # 初始化按钮属性
        self.create_icon_button(object_name, icon_name, icon_size, action_tip, action)

    def create_icon_button(self, object_name, icon_name, icon_size, action_tip, action):
        """
        创建按钮图标和属性
        :param object_name: 按钮对象名称
        :param icon_name: 图标文件名称
        :param icon_size: 图标大小 [宽, 高]
        :param action_tip: 鼠标悬停提示
        :param action: 点击事件回调
        """
        self.setObjectName(object_name)
        self.setAutoRaise(True)  # 替代 setFlat(True)，使按钮在悬浮时有效果

        icon = QtGui.QIcon(f"./src/icons/{icon_name}.png")
        self.setIcon(icon)
        self.setIconSize(QSize(icon_size[0], icon_size[1]))
        self.setToolTip(action_tip)

        if action:
            self.clicked.connect(action)


class TittleBarButton_windown(QToolButton):
    """
    标题栏按钮类
    --------------------
    Ribbon 风格按钮，图标在旁边，支持切换状态和点击事件。
    """

    def __init__(self, parent=None, object_name=None, icon_name=None, icon_size=None, action=None):
        super().__init__(parent)
        self.checked = 1
        sc = gui_scale()

        self.setMaximumWidth(int(30 * sc))
        self.setMinimumWidth(int(30 * sc))
        self.setMinimumHeight(int(50 * sc))
        self.setMaximumHeight(int(50 * sc))

        self.setStyleSheet(get_stylesheet("tittlebarButtonWindown"))
        self.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.setIconSize(QSize(int(32 * sc), int(32 * sc)))

        self.create_icon_button(object_name, icon_name, icon_size)

        self.add_action(action)

    def create_icon_button(self, object_name, icon_name, icon_size):
        """
        创建标题栏按钮图标和属性
        """
        self.setObjectName(object_name)
        self.setAutoRaise(True)

        icon = QtGui.QIcon(f"./src/icons/{icon_name}.png")
        self.setIcon(icon)
        self.setIconSize(QSize(icon_size[0], icon_size[1]))

    def add_action(self, action_1=None, action_2=None):
        """
        添加点击事件，可支持双状态切换。
        :param action_1: 第一次点击执行
        :param action_2: 第二次点击执行
        """
        if action_1 and action_2:
            def toggle_action():
                if self.checked == 1:
                    action_1()
                else:
                    action_2()
                self.checked *= -1

            self.clicked.connect(toggle_action)
        elif action_1:
            self.clicked.connect(action_1)


if __name__ == "__main__":
    """
    测试入口
    --------------------
    独立运行 SketcherButton 测试按钮功能。
    """
    import sys

    def test_action():
        print("按钮被点击了")

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("SketcherButton 测试")
    layout = QtWidgets.QHBoxLayout(window)

    # 创建测试按钮
    btn1 = SketcherButton(window, "sketcherBtn", "icon", [32, 32], "Sketcher按钮", test_action)
    btn2 = TittleBarButton_windown(window, "titleBtn", "icon", [32, 32], test_action)

    layout.addWidget(btn1)
    layout.addWidget(btn2)

    window.show()
    sys.exit(app.exec_())
