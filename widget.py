from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget
import random

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Sort Algorithms")

        self.start_button.clicked.connect(self.start_sort)

    # On Start, creates array from spin box and generates a random array. 
    def start_sort(self):
        array_size = self.spin_box.value()

        self.array = [random.randint(1,100) for i in range(array_size)]

        # display text in text_view
        self.text_view.setText(", ".join(map(str, self.array)))