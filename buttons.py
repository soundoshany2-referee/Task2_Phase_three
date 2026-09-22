from PySide6.QtWidgets import QHBoxLayout, QPushButton, QWidget
from PySide6.QtCore import Signal


class Buttons(QWidget):
    start = Signal()
    pause = Signal()
    reset = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self._timer_paused = False

        self.b1 = QPushButton("Start")
        self.b2 = QPushButton("Reset")

        layout = QHBoxLayout()
        layout.addWidget(self.b1)
        layout.addWidget(self.b2)

        self.setLayout(layout)

        self.b1.clicked.connect(self._b1_clicked)
        self.b2.clicked.connect(self._b2_clicked)

    @property
    def timer_paused(self) -> bool:
        return self._timer_paused

    @timer_paused.setter
    def timer_paused(self, state: bool) -> None:
        self._timer_paused = state

    def _b1_clicked(self) -> None:
        if self._timer_paused:
            self.pause.emit()
        else:
            self.start.emit()

    def _b2_clicked(self) -> None:
        self.reset.emit()