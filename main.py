import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from modules import *;
from utils import *;

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # theme of application
    setupTheme()

    # main window
    window = AppWindow()
    window.titleAplication("Epic Calculator")
    
    # alternative text above display
    info_operations = OperationsText("")
    window.addWidgetToWindow(info_operations)

    # display screen
    display = Display("0")
    window.addWidgetToWindow(display)

    # buttons of calculator
    gridButtons = GridButtons(display, window, info_operations)
    window.addLayoutToWindow(gridButtons)

    # icon of application
    icon = QIcon(str(ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # set window width and height fixed
    window.adjustWindowSize()

    window.show()
    app.exec()