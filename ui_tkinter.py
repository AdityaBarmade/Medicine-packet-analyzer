from PyQt5 import QtWidgets, QtGui, QtCore
import sys
from analyzer import analyze_medicine_packet

class ModernMedicineUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🩺 Medicine Packet Analyzer")
        self.setGeometry(200, 100, 850, 600)
        self.setStyleSheet("""
            QWidget {
                background-color: #f8fbfd;
                font-family: 'Segoe UI', sans-serif;
            }
            QLabel#titleLabel {
                font-size: 26px;
                font-weight: bold;
                color: #1a5276;
                padding: 15px;
            }
            QPushButton {
                background-color: #2e86c1;
                color: white;
                padding: 10px 18px;
                border-radius: 8px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #1b4f72;
            }
            QTextEdit {
                background-color: white;
                padding: 12px;
                border: 1px solid #d6eaf8;
                border-radius: 6px;
                font-size: 15px;
                color: #34495e;
            }
        """)
        self.setup_ui()

    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout()

        self.titleLabel = QtWidgets.QLabel("Medicine Packet Analyzer 🧾")
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.titleLabel)

        self.imageLabel = QtWidgets.QLabel("📷 Drop Image or Click 'Browse'")
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setFixedHeight(200)
        self.imageLabel.setStyleSheet("border: 2px dashed #2e86c1; border-radius: 12px; font-size: 15px;")
        self.imageLabel.setAcceptDrops(True)
        layout.addWidget(self.imageLabel)

        self.browseButton = QtWidgets.QPushButton("📁 Browse Image")
        self.browseButton.clicked.connect(self.browse_image)
        layout.addWidget(self.browseButton)

        self.analyzeButton = QtWidgets.QPushButton("🧪 Analyze")
        self.analyzeButton.clicked.connect(self.analyze_image)
        layout.addWidget(self.analyzeButton)

        self.resultBox = QtWidgets.QTextEdit()
        self.resultBox.setReadOnly(True)
        layout.addWidget(self.resultBox)

        self.setLayout(layout)

    def browse_image(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            self.selected_image = file_path
            pixmap = QtGui.QPixmap(file_path).scaled(300, 200, QtCore.Qt.KeepAspectRatio)
            self.imageLabel.setPixmap(pixmap)
            self.imageLabel.setText("")

    def analyze_image(self):
        if hasattr(self, 'selected_image'):
            self.resultBox.setText("Analyzing image... Please wait.")
            QtWidgets.QApplication.processEvents()
            result = analyze_medicine_packet(self.selected_image)
            self.resultBox.setText(result)
        else:
            QtWidgets.QMessageBox.warning(self, "No Image", "Please select an image first.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ModernMedicineUI()
    window.show()
    sys.exit(app.exec_())
