from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QToolButton
from PyQt5 import QtGui
from src.Ribbon import gui_scale
from src.Ribbon.StyleSheets import get_stylesheet


class TittleBarButton(QToolButton):
    def __init__(self, parent=None, object_name=None, icon_name=None, icon_size=None, action_tip=None, action=None):
        super().__init__(parent)
        sc = gui_scale()
        self.setFixedSize(int(25 * sc), int(50 * sc))
        self.setStyleSheet(get_stylesheet("tittlebarButton"))
        self.setToolButtonStyle(Qt.ToolButtonIconOnly)

        # 默认图标大小
        if icon_size is None:
            icon_size = [int(32 * sc), int(32 * sc)]
        elif isinstance(icon_size, QSize):
            icon_size = [icon_size.width(), icon_size.height()]

        self.setIconSize(QSize(icon_size[0], icon_size[1]))
        self._create_icon_button(object_name, icon_name, action_tip, action, icon_size)

    def _create_icon_button(self, object_name, icon_name, action_tip, action, icon_size):
        self.setObjectName(object_name or "tittlebar_btn")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"./Win64/icons/{icon_name}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)
        self.setIconSize(QSize(icon_size[0], icon_size[1]))
        if action_tip:
            self.setToolTip(action_tip)
        if action:
            self.clicked.connect(action)


class TittleBarButton_windown(QToolButton):
    def __init__(self, parent=None, object_name=None, icon_name=None, icon_size=None, action=None, action2=None):
        super().__init__(parent)
        self.checked = 1
        sc = gui_scale()
        self.setFixedSize(int(30 * sc), int(50 * sc))
        self.setStyleSheet(get_stylesheet("tittlebarButtonWindown"))
        self.setToolButtonStyle(Qt.ToolButtonIconOnly)

        if icon_size is None:
            icon_size = [int(32 * sc), int(32 * sc)]
        elif isinstance(icon_size, QSize):
            icon_size = [icon_size.width(), icon_size.height()]

        self.setIconSize(QSize(icon_size[0], icon_size[1]))
        self._create_icon_button(object_name, icon_name, icon_size)
        self._add_action(action, action2)

    def _create_icon_button(self, object_name, icon_name, icon_size):
        self.setObjectName(object_name or "tittlebar_wnd_btn")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"./Win64/icons/{icon_name}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)
        self.setIconSize(QSize(icon_size[0], icon_size[1]))

    def _add_action(self, action1=None, action2=None):
        if action1 and action2:
            def toggle_action():
                if self.checked == 1:
                    action1()
                else:
                    action2()
                self.checked *= -1
            self.clicked.connect(toggle_action)
        elif action1:
            self.clicked.connect(action1)


if __name__ == "__main__":
    import sys

    def on_click():
        print("按钮被点击！")

    app = QApplication(sys.argv)

    window = QWidget()
    layout = QHBoxLayout(window)

    btn1 = TittleBarButton(window, "btn1", "folder", [32, 32], "打开", on_click)
    btn2 = TittleBarButton_windown(window, "btn2", "windowclose", [32, 32], on_click)

    layout.addWidget(btn1)
    layout.addWidget(btn2)

    window.setWindowTitle("TittleBarButton 测试")
    window.show()

    sys.exit(app.exec_())
