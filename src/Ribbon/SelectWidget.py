#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ****************************************************
# @FileName      :   SelectWidget.py
# @Time          :   2025/10/03 07:44:58
# @Author        :   XuMing
# @Version       :   1.0
# @Email         :   920972751@qq.com
# @Description   :   草图平面选择窗口
# @Copyright     :   XuMing. All Rights Reserved.
# ****************************************************

from PyQt5 import QtCore, QtWidgets


class SelectWidget(QtWidgets.QMainWindow):
    """
    草图平面选择窗口类
    --------------------
    用于选择草图平面（XY、XZ、YZ）。
    包含确认和取消按钮，点击确认会触发父窗口的相关方法。
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi()

        # 设置窗口大小
        self.resize(250, 80)

        # 窗口居中显示
        if parent:
            parent_geo = parent.geometry()
            x = parent_geo.x() + (parent_geo.width() - self.width()) / 2
            y = parent_geo.y() + (parent_geo.height() - self.height()) / 2
            self.move(int(x), int(y))

        self.setWindowTitle('创建草图')

        # 按钮信号绑定
        self.pushbutton_ok.clicked.connect(self.ok)
        self.pushbutton_cancel.clicked.connect(self.cancel)

    def setupUi(self):
        """初始化界面布局"""
        self.widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.widget)

        # 布局
        main_layout = QtWidgets.QVBoxLayout(self.widget)
        combo_layout = QtWidgets.QVBoxLayout()
        button_layout = QtWidgets.QHBoxLayout()

        main_layout.addLayout(combo_layout)
        main_layout.addLayout(button_layout)

        # 下拉选择框
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItems(["XY平面", "XZ平面", "YZ平面"])
        combo_layout.addWidget(self.comboBox, 0, QtCore.Qt.AlignTop)

        # 按钮
        self.pushbutton_ok = QtWidgets.QPushButton("确定")
        self.pushbutton_cancel = QtWidgets.QPushButton("取消")
        button_layout.addWidget(self.pushbutton_ok)
        button_layout.addWidget(self.pushbutton_cancel)

        # 状态栏提示
        if hasattr(self.parent, "statusBar"):
            self.parent.statusBar().showMessage("请选择草绘平面")

    def ok(self):
        """点击确定按钮的响应方法"""
        if hasattr(self.parent, "Sketcher"):
            self.parent.Sketcher.uptoplane()
        if hasattr(self.parent, "change_ribbon"):
            self.parent.change_ribbon(init_name="Ribbon_sketcher")
        self.close()

    def cancel(self):
        """点击取消按钮的响应方法"""
        self.close()


if __name__ == "__main__":
    """
    测试 SelectWidget 的运行入口
    """

    import sys

    class TestMainWindow(QtWidgets.QMainWindow):
        def __init__(self):
            super().__init__()
            self.resize(600, 400)
            self.setWindowTitle("测试主窗口")

            # 显示状态栏信息
            self.statusBar().showMessage("准备就绪")

            # 主窗口布局
            self.central_widget = QtWidgets.QWidget()
            self.setCentralWidget(self.central_widget)
            layout = QtWidgets.QVBoxLayout(self.central_widget)

            # 打开选择窗口按钮
            self.btn_open = QtWidgets.QPushButton("打开选择窗口")
            layout.addWidget(self.btn_open)

            self.btn_open.clicked.connect(self.open_select_widget)

            # 模拟父窗口的方法
            self.Sketcher = type("SketcherObj", (), {"uptoplane": lambda: print("Sketcher: uptoplane called")})()
            self.change_ribbon = lambda init_name=None: print(f"Ribbon changed to: {init_name}")

        def open_select_widget(self):
            """打开 SelectWidget 窗口"""
            self.select_widget = SelectWidget(self)
            self.select_widget.show()

    # 创建应用并运行
    app = QtWidgets.QApplication(sys.argv)
    main_win = TestMainWindow()
    main_win.show()
    sys.exit(app.exec_())
