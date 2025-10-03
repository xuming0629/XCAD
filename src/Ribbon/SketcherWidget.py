# -*- coding: utf-8 -*-
#!/usr/bin/env python
# ****************************************************
# @FileName      :   SketcherWidget.py
# @Time          :   2025/10/03 07:58:45
# @Author        :   XuMing
# @Version       :   1.0
# @Email         :   920972751@qq.com
# @Description   :   自定义草图绘制工具窗口，提供矩形绘制按钮
# @Copyright     :   XuMing. All Rights Reserved.
# ****************************************************

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from src.Ribbon.SketcherButton import SketcherButton


class SketcherWidget(QtWidgets.QMainWindow):
    """
    自定义草图绘制窗口类
    -----------------------
    提供多个矩形绘制按钮，方便在绘图环境中选择绘制工具。
    支持居中显示，并可绑定父窗口的草图操作接口。
    """

    def __init__(self, parent=None, mode=None):
        """
        初始化 SketcherWidget

        :param parent: 父窗口对象
        :param mode: 可选模式参数（目前未使用）
        """
        super(SketcherWidget, self).__init__(parent)
        self.parent = parent

        # 初始化 UI
        self.setupUi(parent)

        # 居中显示窗口
        if parent and hasattr(parent, "geometry"):
            geo = parent.geometry()
            x = geo.x() + geo.width() / 2 - 120  # 水平居中
            y = geo.y() + geo.height() / 2 - 75  # 垂直居中
            self.setGeometry(int(x), int(y), 240, 150)
        else:
            self.resize(240, 150)

        self.setWindowTitle('绘制矩形')

    def setupUi(self, parent):
        """
        初始化 UI 布局和控件
        :param parent: 父窗口对象
        """
        # 主控件容器
        self.widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.widget)

        # 主布局（垂直布局）
        main_layout = QVBoxLayout(self.widget)

        # 上方用于放置其他控件（如 combo box）
        combo_layout = QVBoxLayout()
        main_layout.addLayout(combo_layout)

        # 下方用于放置按钮
        button_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)

        # 循环添加矩形绘制按钮
        for idx, name in enumerate(["矩形1", "矩形2", "矩形3"]):
            btn = QtWidgets.QPushButton()
            icon = QtGui.QIcon(f"./src/icons/{name}.png")  # 加载图标
            btn.setIcon(icon)
            btn.setIconSize(QtCore.QSize(35 if idx == 0 else 30, 35 if idx == 0 else 30))  # 设置按钮图标大小
            button_layout.addWidget(btn)

    def ok(self):
        """
        确认操作
        调用父窗口的 Sketcher.uptoplane 方法（如果存在），然后关闭窗口
        """
        if hasattr(self.parent, "Sketcher"):
            self.parent.Sketcher.uptoplane()
        self.close()

    def cancel(self):
        """
        取消操作，关闭窗口
        """
        self.close()

    def Show(self):
        """
        显示窗口
        """
        self.show()


if __name__ == "__main__":
    """
    测试入口
    -----------------------
    独立运行 SketcherWidget，用于调试和开发
    """
    import sys

    app = QtWidgets.QApplication(sys.argv)

    # 创建主窗口作为父窗口
    main_window = QtWidgets.QWidget()
    main_window.setGeometry(200, 200, 800, 600)
    main_window.setWindowTitle("主窗口")

    # 创建并显示 SketcherWidget
    sketcher_widget = SketcherWidget(main_window)
    sketcher_widget.show()

    sys.exit(app.exec_())
