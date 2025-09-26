from PySide6.QtWidgets import QWidget, QGraphicsScene
from ui_widget import Ui_Widget
import algo
import random
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# For scientific notation formatting
from matplotlib.ticker import ScalarFormatter


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Sort Algorithms")

        # Setting up connections for buttons in the Widget
        self.create_array_button.clicked.connect(self.create_sort)
        self.start_button.clicked.connect(self.start_clicked)

        self.figure = plt.figure(figsize=(6,4))
        self.canvas = FigureCanvas(self.figure)

        # creates a QGraphicScene and sets it to graph_view
        self.scene = QGraphicsScene()
        self.graph_view.setScene(self.scene)
        self.scene.addWidget(self.canvas)



    # When clicking create_button, creates array from spin box and generates a random array. 
    def create_sort(self):
        # Taking the Array Size from the spinbox
        array_size = self.spin_box.value()

        self.array = [random.randint(1,100) for i in range(array_size)]

        # display text in text_view
        self.text_view.setText("Unsorted: [" + ", ".join(map(str, self.array)) + "]")
        
    def start_clicked(self):
        array_copy = self.array.copy()
        results = []  # stores (algorithm_name, time)
    
        # dictionary of checkboxes (name, checkbox object name in widget, algo functions from algo.py)
        algos = {
            "Bubble Sort": (self.bubble_sort_checkbox, algo.bubble_sort),
            "Insertion Sort": (self.insertion_sort_checkbox, algo.insertion_sort),
            "Merge Sort": (self.merge_sort_checkbox, algo.merge_sort),
            "Quick Sort": (self.quick_sort_checkbox, algo.quick_sort),
            "Heap Sort": (self.heap_sort_checkbox, algo.heap_sort),
            "Counting Sort": (self.counting_sort_checkbox, algo.counting_sort),
            "Radix Sort": (self.radix_sort_checkbox, algo.radix_sort),
            "Bucket Sort": (self.bucket_sort_checkbox, algo.bucket_sort)
        }

        # clearing text to make sure text_edit is empty
        self.text_view.setText("")
    
        for name, (checkbox, func) in algos.items():
            if checkbox.isChecked():
                arr = array_copy.copy()
                start = time.perf_counter() # starts the timer
                sorted_array = func(arr)
                end = time.perf_counter() # ends the timer
                elapsed = end - start
                results.append((name, elapsed))
                # shows all the sorted arrays and the time elapsed for each selected checkbox algo
                self.text_view.append(f"{name}: {str(sorted_array)}\nTime: {elapsed:.6f} secs")
    
        if results:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.yaxis.set_major_formatter(ScalarFormatter())
            ax.ticklabel_format(style='plain', axis='y')
            names = [r[0] for r in results]
            times = [r[1] for r in results]
            ax.bar(names, times, color='blue')
            ax.set_ylabel("Time(s)")
            ax.set_title("Sorting Algorithm Time Comparison")
        ax.set_xticklabels(names, fontsize=6.5)  # fontsize for labels
        self.figure.tight_layout()
        self.canvas.draw()
        