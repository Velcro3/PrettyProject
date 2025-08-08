from PySide6.QtCore import QSize, Qt, Signal, QObject # Import some QtCore stuff
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget, QDialog, QFileDialog, QTabWidget, QListWidget, QListWidgetItem, QMessageBox # Import Qt widgets
import sys # Import OS libraries  like exit
import tomllib # Import TOML parser
import os # Import filesystem management
import re # Regex lib.
import subprocess # For starting files on *Nix, so Mac, Linux, Unix, BSD- I think you get it just for Posix compliant systems.
class TomlSignal(QObject):
    toml_loaded = Signal(dict, str) # Create a signal bus to carry TOML between classes.
TomlSignalInstance = TomlSignal() # Create an instance of the signal bus.
def openFile(path):
    if sys.platform.startswith("darwin"): # I see, a man of wisdom. (MacOS)
        subprocess.run(["open", path])
    elif os.name == "nt": # Oh, you sweet summer child. (Windows)
        os.startfile(path)
    elif os.name == "posix": # This deals with most OSes. (Posix Compliant except Mac.)
        subprocess.run(["xdg-open", path])
    else: # If you get this, what the heck are you running?
        QMessageBox.warning(None, "I don't recognize this OS! This script can't run files on your machine.")
def itemSelect(item):
    path = item.data(256)
    if path and os.path.exists(path):
        openFile(path)
    else:
        QMessageBox.warning(None, "404 Not Found.", f"Can't find file:\n{path}")
class ManagmentWindow(QMainWindow): # Create a window to operate in.
    def __init__(self, signal_bus):
        super().__init__()
        self.setWindowTitle("PyVidMan Project: Unknown") # Placeholder title.
        self.label = QLabel("Waiting for input") 
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        signal_bus.toml_loaded.connect(self.gottoml)
    def gottoml(self, data: dict, path: str):
        self.setWindowTitle("PyVidMan Project: " + data["project"]["name"])
        self.loadtoml(data, path)
        self.show()
    def loadtoml(self, data: dict, path: str):
        fileMatcher = {}
        dir = os.path.dirname(path)
        for type in data.get("type"):
            name = type["name"]
            regexMatch = type["regex"]["match"]
            regexMode = type["regex"]["mode"]
            fileMatcher[name] = []
            if regexMode == "some":
                compiledRegex = re.compile(regexMatch)
                for dirname, _, files in os.walk(dir):
                    for file in files:
                        if compiledRegex.search(file):
                            fileMatcher[name].append(os.path.join(dirname, file))
            else:
                compiledRegex = re.compile(regexMatch)
                for dirname, _, files in os.walk(dir):
                    for file in files:
                        if compiledRegex.fullmatch(file):
                            fileMatcher[name].append(os.path.join(dirname, file))
        self.createUI(fileMatcher, dir)
    def createUI(self, files: dict, basepath: str):
        self.uiWidget = QTabWidget()
        for key, value in files.items():
            tab = QWidget()
            layout = QVBoxLayout(tab)
            widget = QListWidget()
            for path in value:
                smallPath = os.path.relpath(path, basepath)
                item = QListWidgetItem(smallPath)
                item.setData(256, path)
                widget.addItem(item)
            widget.itemDoubleClicked.connect(itemSelect)
            layout.addWidget(widget)
            self.uiWidget.addTab(tab, key)
            self.setCentralWidget(self.uiWidget)


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
            self.signal_bus.toml_loaded.emit(data, filename)
            self.close()
app = QApplication(sys.argv)
mgmtWindow = ManagmentWindow(TomlSignalInstance)
window = MainWindow(TomlSignalInstance)
window.setWindowTitle("PyVidMan")
window.resize(800, 600)
window.show()
app.exec()
