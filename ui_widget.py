# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGraphicsView,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpinBox, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(650, 800)
        Widget.setMinimumSize(QSize(650, 704))
        Widget.setMaximumSize(QSize(650, 800))
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(650, 800))
        self.tabWidget.setMaximumSize(QSize(650, 800))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.array_size_label = QLabel(self.tab)
        self.array_size_label.setObjectName(u"array_size_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.array_size_label.sizePolicy().hasHeightForWidth())
        self.array_size_label.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.array_size_label)

        self.spin_box = QSpinBox(self.tab)
        self.spin_box.setObjectName(u"spin_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.spin_box.sizePolicy().hasHeightForWidth())
        self.spin_box.setSizePolicy(sizePolicy1)
        self.spin_box.setMinimum(1)
        self.spin_box.setMaximum(5000)

        self.horizontalLayout_11.addWidget(self.spin_box)

        self.create_array_button = QPushButton(self.tab)
        self.create_array_button.setObjectName(u"create_array_button")

        self.horizontalLayout_11.addWidget(self.create_array_button)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.bubble_sort_checkbox = QCheckBox(self.tab)
        self.bubble_sort_checkbox.setObjectName(u"bubble_sort_checkbox")

        self.horizontalLayout_12.addWidget(self.bubble_sort_checkbox)

        self.insertion_sort_checkbox = QCheckBox(self.tab)
        self.insertion_sort_checkbox.setObjectName(u"insertion_sort_checkbox")

        self.horizontalLayout_12.addWidget(self.insertion_sort_checkbox)

        self.merge_sort_checkbox = QCheckBox(self.tab)
        self.merge_sort_checkbox.setObjectName(u"merge_sort_checkbox")

        self.horizontalLayout_12.addWidget(self.merge_sort_checkbox)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.quick_sort_checkbox = QCheckBox(self.tab)
        self.quick_sort_checkbox.setObjectName(u"quick_sort_checkbox")

        self.horizontalLayout_13.addWidget(self.quick_sort_checkbox)

        self.heap_sort_checkbox = QCheckBox(self.tab)
        self.heap_sort_checkbox.setObjectName(u"heap_sort_checkbox")

        self.horizontalLayout_13.addWidget(self.heap_sort_checkbox)

        self.counting_sort_checkbox = QCheckBox(self.tab)
        self.counting_sort_checkbox.setObjectName(u"counting_sort_checkbox")

        self.horizontalLayout_13.addWidget(self.counting_sort_checkbox)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.radix_sort_checkbox = QCheckBox(self.tab)
        self.radix_sort_checkbox.setObjectName(u"radix_sort_checkbox")

        self.horizontalLayout_14.addWidget(self.radix_sort_checkbox)

        self.bucket_sort_checkbox = QCheckBox(self.tab)
        self.bucket_sort_checkbox.setObjectName(u"bucket_sort_checkbox")

        self.horizontalLayout_14.addWidget(self.bucket_sort_checkbox)

        self.quick_select_checkbox = QCheckBox(self.tab)
        self.quick_select_checkbox.setObjectName(u"quick_select_checkbox")

        self.horizontalLayout_14.addWidget(self.quick_select_checkbox)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.graph_view = QGraphicsView(self.tab)
        self.graph_view.setObjectName(u"graph_view")
        self.graph_view.setMaximumSize(QSize(632, 16777215))

        self.verticalLayout.addWidget(self.graph_view)

        self.text_view = QTextEdit(self.tab)
        self.text_view.setObjectName(u"text_view")
        sizePolicy1.setHeightForWidth(self.text_view.sizePolicy().hasHeightForWidth())
        self.text_view.setSizePolicy(sizePolicy1)
        self.text_view.setMinimumSize(QSize(571, 41))
        self.text_view.setMaximumSize(QSize(632, 120))
        self.text_view.setReadOnly(True)

        self.verticalLayout.addWidget(self.text_view)

        self.start_button = QPushButton(self.tab)
        self.start_button.setObjectName(u"start_button")

        self.verticalLayout.addWidget(self.start_button)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.graph_view_2 = QGraphicsView(self.tab_2)
        self.graph_view_2.setObjectName(u"graph_view_2")
        self.graph_view_2.setGeometry(QRect(0, 70, 626, 481))
        self.graph_view_2.setMaximumSize(QSize(632, 16777215))
        self.text_view_2 = QTextEdit(self.tab_2)
        self.text_view_2.setObjectName(u"text_view_2")
        self.text_view_2.setGeometry(QRect(0, 560, 626, 120))
        sizePolicy1.setHeightForWidth(self.text_view_2.sizePolicy().hasHeightForWidth())
        self.text_view_2.setSizePolicy(sizePolicy1)
        self.text_view_2.setMinimumSize(QSize(571, 41))
        self.text_view_2.setMaximumSize(QSize(632, 120))
        self.text_view_2.setReadOnly(True)
        self.widget = QWidget(self.tab_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 362, 26))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.algo_label = QLabel(self.widget)
        self.algo_label.setObjectName(u"algo_label")

        self.horizontalLayout.addWidget(self.algo_label)

        self.combo_box = QComboBox(self.widget)
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.setObjectName(u"combo_box")

        self.horizontalLayout.addWidget(self.combo_box)

        self.array_size_label_2 = QLabel(self.widget)
        self.array_size_label_2.setObjectName(u"array_size_label_2")
        sizePolicy.setHeightForWidth(self.array_size_label_2.sizePolicy().hasHeightForWidth())
        self.array_size_label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.array_size_label_2)

        self.spin_box_2 = QSpinBox(self.widget)
        self.spin_box_2.setObjectName(u"spin_box_2")
        sizePolicy1.setHeightForWidth(self.spin_box_2.sizePolicy().hasHeightForWidth())
        self.spin_box_2.setSizePolicy(sizePolicy1)
        self.spin_box_2.setMinimum(1)
        self.spin_box_2.setMaximum(5000)

        self.horizontalLayout.addWidget(self.spin_box_2)

        self.create_array_button_2 = QPushButton(self.widget)
        self.create_array_button_2.setObjectName(u"create_array_button_2")

        self.horizontalLayout.addWidget(self.create_array_button_2)

        self.widget1 = QWidget(self.tab_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(60, 700, 239, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.visual_button = QPushButton(self.widget1)
        self.visual_button.setObjectName(u"visual_button")

        self.horizontalLayout_2.addWidget(self.visual_button)

        self.stop_button = QPushButton(self.widget1)
        self.stop_button.setObjectName(u"stop_button")

        self.horizontalLayout_2.addWidget(self.stop_button)

        self.reset_button = QPushButton(self.widget1)
        self.reset_button.setObjectName(u"reset_button")

        self.horizontalLayout_2.addWidget(self.reset_button)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.array_size_label.setText(QCoreApplication.translate("Widget", u"Array Size:", None))
        self.create_array_button.setText(QCoreApplication.translate("Widget", u"Create Array", None))
        self.bubble_sort_checkbox.setText(QCoreApplication.translate("Widget", u"Bubble Sort", None))
        self.insertion_sort_checkbox.setText(QCoreApplication.translate("Widget", u"Insertion Sort", None))
        self.merge_sort_checkbox.setText(QCoreApplication.translate("Widget", u"Merge Sort", None))
        self.quick_sort_checkbox.setText(QCoreApplication.translate("Widget", u"Quick Sort", None))
        self.heap_sort_checkbox.setText(QCoreApplication.translate("Widget", u"Heap Sort", None))
        self.counting_sort_checkbox.setText(QCoreApplication.translate("Widget", u"Counting Sort", None))
        self.radix_sort_checkbox.setText(QCoreApplication.translate("Widget", u"Radix Sort", None))
        self.bucket_sort_checkbox.setText(QCoreApplication.translate("Widget", u"Bucket Sort", None))
        self.quick_select_checkbox.setText(QCoreApplication.translate("Widget", u"Quick Select", None))
        self.text_view.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.start_button.setText(QCoreApplication.translate("Widget", u"Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Time Comparison", None))
        self.text_view_2.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.algo_label.setText(QCoreApplication.translate("Widget", u"Algorithms:", None))
        self.combo_box.setItemText(0, QCoreApplication.translate("Widget", u"Bubble Sort", None))
        self.combo_box.setItemText(1, QCoreApplication.translate("Widget", u"Insertion Sort", None))
        self.combo_box.setItemText(2, QCoreApplication.translate("Widget", u"Merge Sort", None))
        self.combo_box.setItemText(3, QCoreApplication.translate("Widget", u"Quick Sort", None))
        self.combo_box.setItemText(4, QCoreApplication.translate("Widget", u"Heap Sort", None))
        self.combo_box.setItemText(5, QCoreApplication.translate("Widget", u"Counting Sort", None))
        self.combo_box.setItemText(6, QCoreApplication.translate("Widget", u"Radix Sort", None))
        self.combo_box.setItemText(7, QCoreApplication.translate("Widget", u"Bucket Sort", None))

        self.array_size_label_2.setText(QCoreApplication.translate("Widget", u"Array Size:", None))
        self.create_array_button_2.setText(QCoreApplication.translate("Widget", u"Create Array", None))
        self.visual_button.setText(QCoreApplication.translate("Widget", u"Start", None))
        self.stop_button.setText(QCoreApplication.translate("Widget", u"Stop", None))
        self.reset_button.setText(QCoreApplication.translate("Widget", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"Visualization", None))
    # retranslateUi

