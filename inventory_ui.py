import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

SERVER_URL = "http://127.0.0.1:5000"

class InventoryApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inventory Management")
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.inventory_label = QLabel("Inventory: Loading...", self)
        self.layout.addWidget(self.inventory_label)

        self.add_button = QPushButton("Add Item", self)
        self.add_button.clicked.connect(self.add_item)
        self.layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Remove Item", self)
        self.remove_button.clicked.connect(self.remove_item)
        self.layout.addWidget(self.remove_button)

        self.setLayout(self.layout)

        self.update_inventory()

    def add_item(self):
        requests.post(f"{SERVER_URL}/add-item", json={"name": "Item1", "quantity": 5})
        self.update_inventory()

    def remove_item(self):
        requests.post(f"{SERVER_URL}/remove-item", json={"name": "Item1"})
        self.update_inventory()

    def update_inventory(self):
        response = requests.get(f"{SERVER_URL}/inventory")
        if response.status_code == 200:
            self.inventory_label.setText(f"Inventory: {response.json()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryApp()
    window.show()
    sys.exit(app.exec_())
