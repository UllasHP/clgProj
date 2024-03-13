import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import serial

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Crack Detection UI")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label = QLabel("Crack Detection System")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label)

        self.detect_button = QPushButton("Detect Cracks")
        self.detect_button.clicked.connect(self.detect_cracks)
        self.layout.addWidget(self.detect_button)

        # Initialize serial connection
        try:
            self.serial = serial.Serial('COM3', 9600)  # Change 'COM3' to your Arduino's port
        except serial.SerialException:
            print("Serial connection failed. Make sure Arduino is connected.")

    def detect_cracks(self):
        if self.serial.is_open:
            self.serial.write(b'D')  # Send command to Arduino to start crack detection
            response = self.serial.readline().decode().strip()
            print("Response from Arduino:", response)
            # Update image label based on crack detection result
            if "Crack detected" in response:
                pixmap = QPixmap("crack_detected.png")  # Load image for crack detected
            else:
                pixmap = QPixmap("no_crack.png")  # Load image for no crack detected
            self.image_label.setPixmap(pixmap.scaledToWidth(400))

    def closeEvent(self, event):
        if self.serial.is_open:
            self.serial.close()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
