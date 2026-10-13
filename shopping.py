import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QListWidget, QPushButton, QLabel,
    QVBoxLayout, QHBoxLayout, QMessageBox,
)

PRODUCTS = {
    "Apple": 30,
    "Bread": 40,
    "Milk": 55,
    "Eggs (6)": 45,
    "Rice 1kg": 70,
    "Chocolate": 50,
}


class Shop(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Shop")
        self.resize(500, 350)
        self.cart = []

        self.product_list = QListWidget()
        for name, price in PRODUCTS.items():
            self.product_list.addItem(f"{name} - ₹{price}")

        self.cart_list = QListWidget()
        self.total_label = QLabel("Total: ₹0")

        add_btn = QPushButton("Add to Cart")
        add_btn.clicked.connect(self.add_to_cart)
        remove_btn = QPushButton("Remove")
        remove_btn.clicked.connect(self.remove_from_cart)
        checkout_btn = QPushButton("Checkout")
        checkout_btn.clicked.connect(self.checkout)

        left = QVBoxLayout()
        left.addWidget(QLabel("Products"))
        left.addWidget(self.product_list)
        left.addWidget(add_btn)

        right = QVBoxLayout()
        right.addWidget(QLabel("Cart"))
        right.addWidget(self.cart_list)
        right.addWidget(self.total_label)
        right.addWidget(remove_btn)
        right.addWidget(checkout_btn)

        layout = QHBoxLayout(self)
        layout.addLayout(left)
        layout.addLayout(right)

    def add_to_cart(self):
        row = self.product_list.currentRow()
        if row < 0:
            return
        name = list(PRODUCTS)[row]
        self.cart.append(name)
        self.update_cart()

    def remove_from_cart(self):
        row = self.cart_list.currentRow()
        if row < 0:
            return
        self.cart.pop(row)
        self.update_cart()

    def update_cart(self):
        self.cart_list.clear()
        for name in self.cart:
            self.cart_list.addItem(f"{name} - ₹{PRODUCTS[name]}")
        total = sum(PRODUCTS[name] for name in self.cart)
        self.total_label.setText(f"Total: ₹{total}")

    def checkout(self):
        if not self.cart:
            QMessageBox.information(self, "Cart", "Your cart is empty.")
            return
        total = sum(PRODUCTS[name] for name in self.cart)
        QMessageBox.information(self, "Thank you", f"Order placed!\nTotal paid: ₹{total}")
        self.cart.clear()
        self.update_cart()


app = QApplication(sys.argv)
window = Shop()
window.show()
sys.exit(app.exec_())