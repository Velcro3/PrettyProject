from PySide6.QtCore import QSize, Qt, Signal, QObject
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget, QDialog, QFileDialog
import sys
import tomllib
import os
class TomlSignal(QObject):
    toml_loaded = Signal(dict)
TomlSignalInstance = TomlSignal()
class ManagmentWindow(QMainWindow):
    def __init__(self, signal_bus):
        super().__init__()
        self.setWindowTitle("PyVidMan Project: Unknown")
        self.label = QLabel("Waiting for input")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        signal_bus.toml_loaded.connect(self.gottoml)
    def gottoml(self, data: dict):
        self.setWindowTitle("PyVidMan Project: " + data["project"]["name"])
        self.label.setText(str(data))
        self.show()
class MainWindow(QMainWindow):
    def __init__(self, signal_bus):
        super().__init__()
        self.signal_bus = signal_bus
        self.setMinimumSize(800, 600)
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
        if os.path.exists(filename):
            with open(filename, "rb") as conf:
                data = tomllib.load(conf)
            self.signal_bus.toml_loaded.emit(data)
            self.close()
app = QApplication(sys.argv)
mgmtWindow = ManagmentWindow(TomlSignalInstance)
window = MainWindow(TomlSignalInstance)
window.setWindowTitle("PyVidMan")
window.resize(800, 600)
window.show()
app.exec()
