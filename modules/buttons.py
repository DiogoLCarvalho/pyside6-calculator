from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from utils.functions import isNumOrDot, isEmpty, isACorrectNumber, convertTypeNumber
from PySide6.QtCore import Slot
from math import pow
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules import Display
    from modules import OperationsText
    from modules import AppWindow

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(20)
        self.setFont(font)
        self.setMinimumSize(60, 60)

# organize buttons
class GridButtons(QGridLayout):
    def __init__(self, display: 'Display', appWindow: 'AppWindow', operationsText: 'OperationsText', parent: QWidget | None = None) -> None:
        super().__init__(parent)

        # texts that will appear on the buttons
        self._gridTemplate = [
            ['C', '✖', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['+/-', '0', '.', '='],
        ]

        self.display = display
        self._putButtonsOnGrid()

        # Message box
        self.mainWindowApp = appWindow

        # store text of operations
        self.operationsText = operationsText
        self._finalOperationsText = ''

        # attributes to get the result
        self.numberLeft = None
        self.numberRight = None
        self.operation = None

        # change number when number is clicked
        self.isFirstOperationNumber = False

    @property
    def finalOperationsText(self):
        return self._finalOperationsText

    @finalOperationsText.setter
    def finalOperationsText(self, value: str):
        self._finalOperationsText = value
        self.operationsText.setText(value)

    # slots of keyboard keys
    def _keyboardKeySignals(self):
        self.display.myEnterSignal.connect(self._finalResul)
        self.display.myDeleteSignal.connect(self._backspace)
        self.display.myEspaceSignal.connect(self._clearDisplay)
        self.display.myNumberSignal.connect(self._addToDisplay)
        self.display.myOperationsSignal.connect(self._operationClicked)

    def _putButtonsOnGrid(self):
        self._keyboardKeySignals()
        
        for i, row in enumerate(self._gridTemplate):
            for j, textButton in enumerate(row):
                button = Button(textButton)

                # add styles to the buttons
                if not isNumOrDot(textButton) and not isEmpty(textButton):

                    # borderButton is config on utils\theme.py
                    button.setProperty('cssClass', 'borderButton')
                    self._configSpecialButtons(button)

                # resultButton is config on utils\theme.py
                if textButton in "=":
                    button.setProperty('cssClass', 'resultButton')

                if isNumOrDot(textButton) and not isEmpty(textButton):
                    self._configNumberButtons(button)

                # add button
                self.addWidget(button, i, j)

                # button click
                self._clickButton(
                    button,
                    self._loadButtonText(self._addToDisplay, textButton)
                )

    def _configSpecialButtons(self, button):
        buttonText = button.text()

        if buttonText == "C":
            self._clickButton(button, self._clearDisplay)

        if buttonText == "+/-":
            self._clickButton(button, self._invertNumber)

        if buttonText in "+-/*^":
            self._clickButton(button, self._loadButtonText(self._operationClicked, buttonText))

        if buttonText == "=":
            self._clickButton(button, self._finalResul)

        if buttonText == "✖":
            self._clickButton(button, lambda _ : self.display.backspace())

    # Slots
    def _loadButtonText(self, function, button, *args, **kwargs):
        @Slot()
        def inner():
            function(button, *args, **kwargs)
        return inner
    
    @Slot()
    def _clearDisplay(self):
        self.numberLeft = None
        self.numberRight = None
        self.operation = None
        self.finalOperationsText = ''

        self.display.setText("0")
        self.display.setFocus()
        self.isFirstOperationNumber = False

    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()

        if not isACorrectNumber(displayText):
            return 

        newNumber = convertTypeNumber(displayText) * -1

        self.display.setText(str(newNumber))

    @Slot()
    def _operationClicked(self, text):
        buttonText = text
        displayText = self.display.text()
        self.display.setFocus()

        if not isACorrectNumber(displayText) and self.numberLeft is None:
            return

        if self.numberLeft is None:
            self.numberLeft = convertTypeNumber(displayText)

        self.operation = buttonText
        self.finalOperationsText = f'{self.numberLeft} {self.operation} '

    @Slot()
    def _finalResul(self):
        displayText = self.display.text()

        if self.operation is None:
            self.showDialogError("Enter an operation!")
            return
        
        if not isACorrectNumber(displayText):
            self.showDialogError("Type one more number!")
            return
        
        self.numberRight = convertTypeNumber(displayText)

        self.finalOperationsText = f'{self.numberLeft} {self.operation} {self.numberRight}'
        result = 'Erro'

        try: 
            if "^" in self.finalOperationsText and isinstance(self.numberLeft, int | float):
                result = pow(self.numberLeft, self.numberRight)
                result = convertTypeNumber(str(result))
            else:
                result = eval(self.finalOperationsText)
        except ZeroDivisionError:
            self.showDialogError("It's not possible to divide a number by zero  !")
        except OverflowError:
            self.showDialogError("The result is too large!")
            
        self.display.setText(str(result))
        self.operationsText.setText(f'{self.finalOperationsText} = {result}')
        self.numberLeft = result
        self.numberRight = None
        self.isFirstOperationNumber = False
        self.display.setFocus()

        if result == 'Erro':
            self.numberLeft = None

    @Slot()
    def _addToDisplay(self, text):
        
        displayText = self.display.text() + text

        if not isACorrectNumber(displayText):
            return
        
        if self.display.text() == "0":
            self.display.setText(text)
        else:
            self.display.insert(text)

        self.display.setFocus()

    @Slot()
    def _backspace(self):
        self.display.backspace
        self.display.setFocus()

    def _clickButton(self, button, slot):
        button.clicked.connect(slot)

    def _changeLoadNumber(self):
        if self.display.text() != "":

            if self.numberLeft is not None and self.isFirstOperationNumber is False:
                self.display.clear()
                self.isFirstOperationNumber = True

    def _configNumberButtons(self, button):
        buttonText = button.text()

        if buttonText in "0123456789":
            self._clickButton(button, lambda _ : self._changeLoadNumber())

    def showDialogError(self, text):
        msgBox = self.mainWindowApp.setMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.setStandardButtons(msgBox.StandardButton.Ok)
        msgBox.exec()
