from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget
import algo
import random
import time

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

        start = time.perf_counter() # starts timing algorithms

        if algorithm == "Bubble Sort":
            sorted_array = algo.bubble_sort(self.array)
            self.text_view.setText(f"Sorted: {str(sorted_array)}")

        if algorithm == "Insertion Sort":
            sorted_array = algo.insertion_sort(self.array)
            self.text_view.setText(f"Sorted: {str(sorted_array)}")

        if algorithm == "Merge Sort":
            sorted_array = algo.merge_sort(self.array)
            self.text_view.setText(f"Sorted: {str(sorted_array)}")

        if algorithm == "Quick Sort":
            sorted_array = algo.quick_sort(self.array)
            self.text_view.setText(f"Sorted: {str(sorted_array)}")

        if algorithm == "Heap Sort":
            sorted_array = algo.heap_sort(self.array)
            self.text_view.setText(f"Sorted: {str(sorted_array)}")

        if algorithm == "Counting Sort":
            sorted_array = algo.counting_sort(self.array)
            self.text_view.setText(f"Sorted: {str(sorted_array)}")  

        if algorithm == "Radix Sort":
            sorted_array = algo.radix_sort(self.array)
            self.text_view.setText(f"Sorted: {str(sorted_array)}")  

        if algorithm == "Bucket Sort":
            sorted_array = algo.bucket_sort(self.array)
            self.text_view.setText(f"Sorted: {str(sorted_array)}")  

        end = time.perf_counter()
        elapse = end - start

        self.time_label.setText(f"Time: {elapse:.6f} seconds")
        self.status_label.setText(f"Status: {algorithm}, Array Size: {len(self.array)}") # set status to the current algorithm selected
        