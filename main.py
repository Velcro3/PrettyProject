from PySide6.QtWidgets import QApplication, QWidget
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("PyVidMan")
window.resize(800, 600)
window.show()
app.exec()