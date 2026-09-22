from PySide6.QtWidgets import QApplication

from assisted.window import Window


def main() -> None:
    app = QApplication([])

    window = Window()
    window.resize(400, 200)
    window.show()

    app.exec()


if __name__ == "__main__":
    main()