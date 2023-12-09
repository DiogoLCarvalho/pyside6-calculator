from PySide6.QtWidgets import QWidget, QVBoxLayout, QMainWindow, QMessageBox

# main window
class AppWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.central_widget = QWidget()
        self.layoutWindow = QVBoxLayout()
        self.central_widget.setLayout(self.layoutWindow)
        self.setCentralWidget(self.central_widget)

    def titleAplication(self, text: str) -> None:
        self.setWindowTitle(text)

    def adjustWindowSize(self):
        self.adjustSize()

        self.setFixedSize(self.width(), self.height())

    def addWidgetToWindow(self, widget: QWidget):
        self.layoutWindow.addWidget(widget)

    def addLayoutToWindow(self, layout):
        self.layoutWindow.addLayout(layout)

    def setMsgBox(self):
        return QMessageBox(self)