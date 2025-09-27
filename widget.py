from PySide6.QtWidgets import QWidget, QVBoxLayout, QMessageBox, QInputDialog
from ui_widget import Ui_Widget
import algo
import algo_anim
import random
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.animation import FuncAnimation
# For scientific notation formatting
import matplotlib.ticker



class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Sort Algorithms")

        # Setting up connections for buttons in the Widget
        self.create_array_button.clicked.connect(self.create_sort)
        self.start_button.clicked.connect(self.start_clicked)
        self.visual_button.clicked.connect(self.start_animation)
        self.stop_button.clicked.connect(self.stop_animation)  # optional stop button
        self.reset_button.clicked.connect(self.reset_animation)  # optional reset button
        self.create_array_button_2.clicked.connect(self.create_sort_2)


        self.figure = plt.figure(figsize=(6,4))
        self.canvas = FigureCanvas(self.figure)

        # creates a QGraphicScene and sets it to graph_view
        layout = QVBoxLayout(self.graph_view)
        layout.addWidget(self.canvas)

        # setsup visualization
        self.anim_fig = plt.figure(figsize=(6, 4))
        self.anim_canvas = FigureCanvas(self.anim_fig)
        layout = QVBoxLayout(self.graph_view_2)  # graph_view_2 is your target
        layout.addWidget(self.anim_canvas)
        self.anim_ax = self.anim_fig.add_subplot(111)

        self.anim = None
        self.anim_running = False



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

        any_checked = False # to see if any of the checkboxes are checked
    
        for name, (checkbox, func) in algos.items():
            if checkbox.isChecked():
                any_checked = True
                arr = array_copy.copy()
                start = time.perf_counter() # starts the timer
                sorted_array = func(arr)
                end = time.perf_counter() # ends the timer
                elapsed = end - start
                results.append((name, elapsed))
                # shows all the sorted arrays and the time elapsed for each selected checkbox algo
                self.text_view.append(f"{name}: {str(sorted_array)}\nTime: {elapsed:.6f} secs\n")

        # case for quickselect, since it takes a value of k
        if self.quick_select_checkbox.isChecked():
            any_checked = True
            arr = array_copy.copy()
            k, ok = QInputDialog.getInt(
                self,
                "Quick Select",
                f"Enter k (1 to {len(arr)}):",
                1,
                1,
                len(arr)
            )
            if ok:
                start = time.perf_counter() # starts the timer
                result = algo.quick_select(arr, 0, len(arr) - 1, k - 1)
                end = time.perf_counter() # ends the timer
                elapsed = end - start
                self.text_view.append(f"Quick Select: {k}-th smallest element: {result} \nOriginal Array: {self.array} \nPartially Sorted Array: {arr} \nTime: {elapsed:.6f} secs")
                results.append(("Quick Select", elapsed)) # returns result
        
        # case where if no checkboxes are selected, displays warning
        if not any_checked:
            message = QMessageBox(self)
            message.setMinimumSize(700, 200)
            message.setWindowTitle("Select Algorithm!")
            message.setText("You must select at least one sorting algorithm.")
            message.setIcon(QMessageBox.Critical)
            message.setStandardButtons(QMessageBox.Ok)
            message.exec()
            return

        # creates graph from results of algo and time
        if results:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.yaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())
            ax.ticklabel_format(style='plain', axis='y')
            names = [r[0] for r in results]
            times = [r[1] for r in results]
            ax.bar(names, times, color='blue')
            ax.set_ylabel("Time(s)")
            ax.set_title("Sorting Algorithm Time Comparison")
        ax.set_xticklabels(names, fontsize=5.5)  # fontsize for labels
        self.figure.tight_layout()
        self.canvas.draw()
        
    # reused code to create a new array
    def create_sort_2(self):
        array_size = self.spin_box_2.value()
        self.array_2 = [random.randint(1, 100) for _ in range(array_size)]
        self.text_view_2.setText("Unsorted: [" + ", ".join(map(str, self.array_2)) + "]")


    def start_animation(self):
        # stop previous animation if running
        self.stop_animation()

        arr = self.array_2.copy()
        algo_name = self.combo_box.currentText()  # get algorithm from combo box

        # dictionary of algo anim
        algo_funcs = {
            "Bubble Sort": algo_anim.bubble_sort_anim,
            "Insertion Sort": algo_anim.insertion_sort_anim,
            "Merge Sort": algo_anim.merge_sort_anim,
            "Quick Sort": algo_anim.quick_sort_anim,
            "Heap Sort": algo_anim.heap_sort_anim,
            "Counting Sort": algo_anim.counting_sort_anim,
            "Radix Sort": algo_anim.radix_sort_anim,
            "Bucket Sort": algo_anim.bucket_sort_anim
        }

        # reusing code from start_button to show output result
        algos = {
            "Bubble Sort": algo.bubble_sort,
            "Insertion Sort": algo.insertion_sort,
            "Merge Sort": algo.merge_sort,
            "Quick Sort": algo.quick_sort,
            "Heap Sort": algo.heap_sort,
            "Counting Sort": algo.counting_sort,
            "Radix Sort": algo.radix_sort,
            "Bucket Sort": algo.bucket_sort
        }
        
        # clearing text to make sure text_edit is empty
        self.text_view_2.setText("")

        gen = algo_funcs[algo_name](arr.copy())
        start = time.perf_counter()
        last_frame = None
        for frame in gen:
            last_frame = frame
        end = time.perf_counter()
        elapsed = end - start
        self.text_view_2.append(f"{algo_name}: {last_frame}\nTime: {elapsed:.6f} seconds")

        # generator for new algo
        gen = algo_funcs[algo_name](arr.copy())
        if algo_name not in algo_funcs:
            return

        gen = algo_funcs[algo_name](arr)

        self.anim_ax.clear()
        self.anim_ax.set_title(algo_name)
        self.anim_ax.xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))
        self.anim_ax.yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))
        self.bar_rects = self.anim_ax.bar(range(len(arr)), arr, color="blue")

        # update each frame
        def update(frame):
            for rect, val in zip(self.bar_rects, frame):
                rect.set_height(val if val is not None else 0)
            return self.bar_rects
        self.anim = FuncAnimation(
            self.anim_fig,
            func=update,
            frames=gen,
            interval=50,
            repeat=False
        )
        self.anim_running = True
        self.anim_canvas.draw()
    
    def stop_animation(self):
        if self.anim is not None:
            if hasattr(self.anim, "event_source") and self.anim.event_source is not None:
                self.anim.event_source.stop()
            self.anim = None
        self.anim_running = False
    
    # resets the animation 
    def reset_animation(self):
        if self.anim is not None:
            self.anim.event_source.stop()
            self.anim = None
        self.anim_running = False
        self.anim_ax.clear()
        self.anim_canvas.draw()