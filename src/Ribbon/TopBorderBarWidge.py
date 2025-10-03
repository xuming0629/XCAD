from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QToolBar, QHBoxLayout, QMainWindow, QWidget,QApplication
from PyQt5 import QtWidgets, QtCore, QtGui, Qt

from src.Ribbon.RibbonTab import RibbonTab
from src.Ribbon import gui_scale
from src.Ribbon.StyleSheets import get_stylesheet
from src.Ribbon.TittleBarButton import TittleBarButton, TittleBarButton_windown


class TopBorderBarWidget(QToolBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.setStyleSheet(get_stylesheet("ribbon"))
        self.setObjectName("TittleWidget")
        self.setWindowTitle("Tittle")

        self._Tittle_widget = QtWidgets.QWidget(self)
        self._Tittle_widget.setMaximumHeight(37)
        self._Tittle_widget.setMinimumHeight(37)
        self.setMovable(False)
        self.addWidget(self._Tittle_widget)

        self.HBOX_LeftlLayoutWidget = QtWidgets.QWidget(self._Tittle_widget)
        self.HBOX_LeftlLayoutWidget.setGeometry(QtCore.QRect(0, 0, 500, 40))

        HBOX = QHBoxLayout()
        HBOX_Logo = QHBoxLayout()
        HBOX_Left = QHBoxLayout()
        HBOX_Center = QHBoxLayout()
        HBOX_Right = QHBoxLayout()

        self._Tittle_widget.setLayout(HBOX)
        HBOX.addLayout(HBOX_Logo)
        HBOX.addLayout(HBOX_Left, 0)
        HBOX.addLayout(HBOX_Center, 280)
        HBOX.addLayout(HBOX_Right, 0)

        # 按钮示例
        self.view_top_pushButton = TittleBarButton(self._Tittle_widget, "view_top_pushButton", "view_top", [32, 32], "俯视图",
                                                    self.parent.Displayshape_core_dict[self.parent.current_window_name].canva._display.View_Top)
        HBOX_Left.addWidget(self.view_top_pushButton, 0)

        self.view_tfr_tri_pushButton = TittleBarButton(self._Tittle_widget, "view_tfr_tri_pushButton", "view_tfr_tri", [32, 32],
                                                        "正三轴视图",
                                                        self.parent.Displayshape_core_dict[self.parent.current_window_name].canva._display.View_Rear)
        HBOX_Left.addWidget(self.view_tfr_tri_pushButton, 0)

        self.view_tfr_iso_pushButton = TittleBarButton(self._Tittle_widget, "view_tfr_iso_pushButton", "view_tfr_iso", [32, 32],
                                                        "轴测图",
                                                        self.parent.Displayshape_core_dict[self.parent.current_window_name].canva._display.View_Iso)
        HBOX_Left.addWidget(self.view_tfr_iso_pushButton, 0)

        self.view_right_pushButton = TittleBarButton(self._Tittle_widget, "view_right_pushButton", "view_right", [32, 32],
                                                      "右视图",
                                                      self.parent.Displayshape_core_dict[self.parent.current_window_name].canva._display.View_Right)
        HBOX_Left.addWidget(self.view_right_pushButton, 0)

        self.view_left_pushButton = TittleBarButton(self._Tittle_widget, "view_left", "view_left", [32, 32], "左视图",
                                                     self.parent.Displayshape_core_dict[self.parent.current_window_name].canva._display.View_Left)
        HBOX_Left.addWidget(self.view_left_pushButton, 0)

        self.view_front_pushButton = TittleBarButton(self._Tittle_widget, "view_front", "view_front", [32, 32], "前视图",
                                                      self.parent.Displayshape_core_dict[self.parent.current_window_name].canva._display.View_Front)
        HBOX_Left.addWidget(self.view_front_pushButton, 0)

        self.view_bottom_pushButton = TittleBarButton(self._Tittle_widget, "view_bottom", "view_bottom", [32, 32], "仰视图",
                                                       self.parent.Displayshape_core_dict[self.parent.current_window_name].canva._display.View_Bottom)
        HBOX_Left.addWidget(self.view_bottom_pushButton, 0)

        HBOX_Left.setSpacing(5)

    def reset_triggered_connect(self):
        self.view_top_pushButton.Add_Action(
            self.parent.Displayshape_core_dict[self.parent.current_window_name].canva._display.View_Top)
        self.view_tfr_tri_pushButton.Add_Action(
            self.parent.Displayshape_core_dict[self.parent.current_window_name].canva._display.View_Rear)
        self.view_tfr_iso_pushButton.Add_Action(
            self.parent.Displayshape_core_dict[self.parent.current_window_name].canva._display.View_Iso)
        self.view_right_pushButton.Add_Action(
            self.parent.Displayshape_core_dict[self.parent.current_window_name].canva._display.View_Right)
        self.view_left_pushButton.Add_Action(
            self.parent.Displayshape_core_dict[self.parent.current_window_name].canva._display.View_Left)
        self.view_front_pushButton.Add_Action(
            self.parent.Displayshape_core_dict[self.parent.current_window_name].canva._display.View_Front)
        self.view_bottom_pushButton.Add_Action(
            self.parent.Displayshape_core_dict[self.parent.current_window_name].canva._display.View_Bottom)


if __name__ == "__main__":
    import sys

    class MockDisplay:
        def __init__(self):
            self._display = self

        def View_Top(self): print("View_Top triggered")
        def View_Rear(self): print("View_Rear triggered")
        def View_Iso(self): print("View_Iso triggered")
        def View_Right(self): print("View_Right triggered")
        def View_Left(self): print("View_Left triggered")
        def View_Front(self): print("View_Front triggered")
        def View_Bottom(self): print("View_Bottom triggered")

    class MockParent(QMainWindow):
        def __init__(self):
            super().__init__()
            self.current_window_name = "main"
            self.Displayshape_core_dict = {
                self.current_window_name: type("obj", (), {"canva": MockDisplay()})()
            }

    app = QApplication(sys.argv)
    main_window = MockParent()
    top_bar = TopBorderBarWidget(main_window)

    main_window.setCentralWidget(QWidget())
    main_window.addToolBar(top_bar)
    main_window.setWindowTitle("TopBorderBarWidget 测试")
    main_window.resize(900, 100)
    main_window.show()

    sys.exit(app.exec_())
