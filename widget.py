from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget
import algo
import random

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Sort Algorithms")

        self.create_array_button.clicked.connect(self.create_sort)

        self.start_button.clicked.connect(self.start_clicked)

    # When clicking create_button, creates array from spin box and generates a random array. 
    def create_sort(self):
        array_size = self.spin_box.value()

        self.array = [random.randint(1,100) for i in range(array_size)]

        # display text in text_view
        self.text_view.setText("Unsorted: [" + ", ".join(map(str, self.array)) + "]")
    
    def start_clicked(self):
        algorithm = self.combo_box.currentText()
        if algorithm == "Merge Sort":
            sorted_array = algo.merge_sort(self.array)
            self.text_view.setText(f"Sorted: {str(sorted_array)}")
        