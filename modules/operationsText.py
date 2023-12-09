from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt

# alternative text above display
class OperationsText(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet("font-size:14px")
        self.setAlignment(Qt.AlignmentFlag.AlignRight)

