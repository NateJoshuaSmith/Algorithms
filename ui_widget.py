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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGraphicsView, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(650, 704)
        Widget.setMinimumSize(QSize(650, 704))
        Widget.setMaximumSize(QSize(650, 60))
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.array_size_label = QLabel(Widget)
        self.array_size_label.setObjectName(u"array_size_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.array_size_label.sizePolicy().hasHeightForWidth())
        self.array_size_label.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.array_size_label)

        self.spin_box = QSpinBox(Widget)
        self.spin_box.setObjectName(u"spin_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.spin_box.sizePolicy().hasHeightForWidth())
        self.spin_box.setSizePolicy(sizePolicy1)
        self.spin_box.setMinimum(1)
        self.spin_box.setMaximum(100)

        self.horizontalLayout_3.addWidget(self.spin_box)

        self.create_array_button = QPushButton(Widget)
        self.create_array_button.setObjectName(u"create_array_button")

        self.horizontalLayout_3.addWidget(self.create_array_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bubble_sort_checkbox = QCheckBox(Widget)
        self.bubble_sort_checkbox.setObjectName(u"bubble_sort_checkbox")

        self.horizontalLayout_2.addWidget(self.bubble_sort_checkbox)

        self.insertion_sort_checkbox = QCheckBox(Widget)
        self.insertion_sort_checkbox.setObjectName(u"insertion_sort_checkbox")

        self.horizontalLayout_2.addWidget(self.insertion_sort_checkbox)

        self.merge_sort_checkbox = QCheckBox(Widget)
        self.merge_sort_checkbox.setObjectName(u"merge_sort_checkbox")

        self.horizontalLayout_2.addWidget(self.merge_sort_checkbox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.quick_sort_checkbox = QCheckBox(Widget)
        self.quick_sort_checkbox.setObjectName(u"quick_sort_checkbox")

        self.horizontalLayout_4.addWidget(self.quick_sort_checkbox)

        self.heap_sort_checkbox = QCheckBox(Widget)
        self.heap_sort_checkbox.setObjectName(u"heap_sort_checkbox")

        self.horizontalLayout_4.addWidget(self.heap_sort_checkbox)

        self.counting_sort_checkbox = QCheckBox(Widget)
        self.counting_sort_checkbox.setObjectName(u"counting_sort_checkbox")

        self.horizontalLayout_4.addWidget(self.counting_sort_checkbox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.radix_sort_checkbox = QCheckBox(Widget)
        self.radix_sort_checkbox.setObjectName(u"radix_sort_checkbox")

        self.horizontalLayout_5.addWidget(self.radix_sort_checkbox)

        self.bucket_sort_checkbox = QCheckBox(Widget)
        self.bucket_sort_checkbox.setObjectName(u"bucket_sort_checkbox")

        self.horizontalLayout_5.addWidget(self.bucket_sort_checkbox)

        self.quick_select_checkbox = QCheckBox(Widget)
        self.quick_select_checkbox.setObjectName(u"quick_select_checkbox")

        self.horizontalLayout_5.addWidget(self.quick_select_checkbox)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.graph_view = QGraphicsView(Widget)
        self.graph_view.setObjectName(u"graph_view")
        self.graph_view.setMaximumSize(QSize(632, 16777215))

        self.verticalLayout.addWidget(self.graph_view)

        self.text_view = QTextEdit(Widget)
        self.text_view.setObjectName(u"text_view")
        sizePolicy1.setHeightForWidth(self.text_view.sizePolicy().hasHeightForWidth())
        self.text_view.setSizePolicy(sizePolicy1)
        self.text_view.setMinimumSize(QSize(571, 41))
        self.text_view.setMaximumSize(QSize(632, 60))
        self.text_view.setReadOnly(True)

        self.verticalLayout.addWidget(self.text_view)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.start_button = QPushButton(Widget)
        self.start_button.setObjectName(u"start_button")

        self.horizontalLayout.addWidget(self.start_button)

        self.pause_button = QPushButton(Widget)
        self.pause_button.setObjectName(u"pause_button")

        self.horizontalLayout.addWidget(self.pause_button)

        self.reset_button = QPushButton(Widget)
        self.reset_button.setObjectName(u"reset_button")

        self.horizontalLayout.addWidget(self.reset_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Widget)

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
        self.pause_button.setText(QCoreApplication.translate("Widget", u"Pause", None))
        self.reset_button.setText(QCoreApplication.translate("Widget", u"Reset", None))
    # retranslateUi

