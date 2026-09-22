from PySide6.QtWidgets import QStackedWidget, QLineEdit, QLabel, QWidget
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import QTimer, Signal, Qt


class Stack(QStackedWidget):
    time_stopped = Signal(bool)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter time in seconds")

        validator = QIntValidator(1, 999999, self)
        self.input.setValidator(validator)

        self.counter = QLabel("00:00")
        self.counter.setAlignment(Qt.AlignCenter)

        self.addWidget(self.input)
        self.addWidget(self.counter)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._decrement)

        self.remaining_seconds = 0

    def start_counter(self) -> None:
        if self.currentWidget() == self.input:
            if not self.input.text():
                return

            self.remaining_seconds = int(self.input.text())
            self.setCurrentWidget(self.counter)

        self.timer.start(1000)

        self.time_stopped.emit(False)

    def _decrement(self) -> None:
        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1

            minutes = self.remaining_seconds // 60
            seconds = self.remaining_seconds % 60

            self.counter.setText(f"{minutes:02d}:{seconds:02d}")

        if self.remaining_seconds == 0:
            self.timer.stop()
            self.reset()
            self.time_stopped.emit(True)

    def reset(self) -> None:
        self.timer.stop()

        self.remaining_seconds = 0

        self.counter.setText("00:00")
        self.input.clear()

        self.setCurrentWidget(self.input)

    def pause(self) -> None:
        self.timer.stop()
        self.time_stopped.emit(True)