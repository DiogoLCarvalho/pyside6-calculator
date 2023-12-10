from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from utils.functions import isEmpty, isNumOrDot

# display screen
class Display(QLineEdit):
    myEnterSignal = Signal()
    myDeleteSignal = Signal()
    myEspaceSignal = Signal()
    myNumberSignal = Signal(str)
    myOperationsSignal = Signal(str)

    def __init__(self, *args, **kwags):
        super().__init__(*args, **kwags)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(
            """
            font-size:45px;
            font-weight:600;
            """
        )
        
        self.setMinimumHeight(20 * 2)
        self.setMinimumWidth(300)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(5,10,5,10)

    # keyboard keys 
    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isDelete = key in [KEYS.Key_Delete, KEYS.Key_Backspace, KEYS.Key_D]
        isEscape = key in [KEYS.Key_Escape, KEYS.Key_C]
        myPotencialSignal = key in [KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash, KEYS.Key_Asterisk, KEYS.Key_P]

        if isEnter: 
            self.myEnterSignal.emit()
            return event.ignore()

        if isDelete:
            self.myDeleteSignal.emit()
            return event.ignore()
        
        if isEscape:
            self.myEspaceSignal.emit()
            return event.ignore()

        if isEmpty(text):
            return event.ignore()
        
        if myPotencialSignal:
            if text.lower() == "p":
                text = "^"
            self.myOperationsSignal.emit(text)
            return event.ignore()    

        if isNumOrDot(text):
            self.myNumberSignal.emit(text)
            return event.ignore()
