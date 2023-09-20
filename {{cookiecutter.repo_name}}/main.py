import sys

from PyQt5.QtWidgets import QApplication

from src.main_window import MainWindow


def main():
    app = QApplication([])
    app.setApplicationName("{{cookiecutter.project_name}}")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
