from PySide6.QtWidgets import QWidget, QVBoxLayout, QMainWindow, QMessageBox
from PySide6.QtCore import Slot
from utils import setupTheme

# main window
class AppWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.central_widget = QWidget()
        self.layoutWindow = QVBoxLayout()
        self.central_widget.setLayout(self.layoutWindow)
        self.setCentralWidget(self.central_widget)
        
        # change theme
        self.menu_bar = self.menuBar()
        self.menu = self.menu_bar.addMenu("Theme")
        self.menu_light = self.menu.addAction("Light")
        self.menu_dark = self.menu.addAction("Dark")

        self.addSlotsToMenus()

    def titleAplication(self, text: str) -> None:
        self.setWindowTitle(text)

    def adjustWindowSize(self):
        self.adjustSize()

        self.setFixedSize(self.width() - 80, self.height())

    def addWidgetToWindow(self, widget: QWidget):
        self.layoutWindow.addWidget(widget)

    def addLayoutToWindow(self, layout):
        self.layoutWindow.addLayout(layout)

    def setMsgBox(self):
        return QMessageBox(self)

    @Slot()
    def changeThemeOfApp(self, theme):
        setupTheme(theme)
    
    def addSlotsToMenus(self):
        self.menu_light.triggered.connect(lambda _: self.changeThemeOfApp("light"))
        self.menu_dark.triggered.connect(lambda _: self.changeThemeOfApp("dark"))
