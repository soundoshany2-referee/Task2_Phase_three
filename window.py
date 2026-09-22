from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from assisted.buttons import Buttons
from assisted.stack import Stack


class Window(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Countdown Timer")

        self.stack = Stack()
        self.buttons = Buttons()

        central_widget = QWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        layout.addWidget(self.buttons)

        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

        self.buttons.start.connect(self.stack.start_counter)
        self.buttons.pause.connect(self.stack.pause)
        self.buttons.reset.connect(self.stack.reset)

        self.stack.time_stopped.connect(self._switch_buttons)

    def _switch_buttons(self, state: bool) -> None:
        if state:
            self.buttons.b1.setText("Start")
            self.buttons.timer_paused = False
        else:
            self.buttons.b1.setText("Pause")
            self.buttons.timer_paused = True