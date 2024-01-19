from PyQt6.QtWidgets import QSpinBox, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class Spinbox(QSpinBox):
    def __init__(self, read_noly, starting_value) -> None:
        super().__init__()
        self.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.setValue(starting_value)
        self._init_set_style(read_noly)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setAutoFillBackground(True)
        self.setReadOnly(read_noly)
        self.set_font()

    def _init_set_style(self, read_only):
        if read_only == True:
            self.setStyleSheet(
                """
                QSpinBox { 
                    border: none; 
                    background-color: transparent; 
                    selection-background-color: transparent; 
                    color: "#A19292";
                    }
                """
            )
        else:
            self.setStyleSheet(
                """
                QSpinBox { 
                    border: none; 
                    background-color: transparent; 
                    selection-background-color: transparent; 
                    color: "#FFFFFF";
                    }
                """
            )

    def set_font(self, value=20):
        font = QFont()
        font.setPointSize(value)
        self.setFont(font)

    def update_upper(self, value, spin_box2):
        if value <= 0:
            value = 60
        spin_box2.setValue(value - 1)

    def update_middle(self, value):
        if value > 59:
            value = 0
        if value < 0:
            value = 59
        self.setValue(value)

    def update_lower(self, value, spin_box2):
        value += 1
        if value == 60:
            value = 0
        if value > 60:
            value = 1
        spin_box2.setValue(value)

    def update_all(self, spinbox0, spinbox2):
        self.valueChanged.connect(
            lambda value: self.update_upper(value, spinbox0))
        self.valueChanged.connect(lambda value: self.update_middle(value))
        self.valueChanged.connect(
            lambda value: self.update_lower(value, spinbox2))
