from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget, QDialog, QFileDialog
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyVidMan")
        layout = QVBoxLayout()
        title = QLabel("Welcome to PyVidMan. Click the button to open a project")
        layout.addWidget(title)
        self.button = QPushButton("Load Project")
        self.button.clicked.connect(self.load)
        layout.addWidget(self.button)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    def load(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Project", "", "Project configurations (project.toml)")

app = QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle("PyVidMan")
window.resize(800, 600)
window.show()
app.exec()
