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
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSlider,
    QSpinBox, QTextEdit, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(591, 576)
        Widget.setMinimumSize(QSize(591, 576))
        Widget.setMaximumSize(QSize(591, 16777215))
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.algorithm_label = QLabel(Widget)
        self.algorithm_label.setObjectName(u"algorithm_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.algorithm_label.sizePolicy().hasHeightForWidth())
        self.algorithm_label.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.algorithm_label)

        self.combo_box = QComboBox(Widget)
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.setObjectName(u"combo_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.combo_box.sizePolicy().hasHeightForWidth())
        self.combo_box.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.combo_box)

        self.array_size_label = QLabel(Widget)
        self.array_size_label.setObjectName(u"array_size_label")
        sizePolicy.setHeightForWidth(self.array_size_label.sizePolicy().hasHeightForWidth())
        self.array_size_label.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.array_size_label)

        self.spin_box = QSpinBox(Widget)
        self.spin_box.setObjectName(u"spin_box")
        sizePolicy1.setHeightForWidth(self.spin_box.sizePolicy().hasHeightForWidth())
        self.spin_box.setSizePolicy(sizePolicy1)
        self.spin_box.setMinimum(1)
        self.spin_box.setMaximum(100)

        self.horizontalLayout_2.addWidget(self.spin_box)

        self.create_array_button = QPushButton(Widget)
        self.create_array_button.setObjectName(u"create_array_button")

        self.horizontalLayout_2.addWidget(self.create_array_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.graph_view = QGraphicsView(Widget)
        self.graph_view.setObjectName(u"graph_view")

        self.verticalLayout.addWidget(self.graph_view)

        self.text_view = QTextEdit(Widget)
        self.text_view.setObjectName(u"text_view")
        sizePolicy1.setHeightForWidth(self.text_view.sizePolicy().hasHeightForWidth())
        self.text_view.setSizePolicy(sizePolicy1)
        self.text_view.setMinimumSize(QSize(571, 41))
        self.text_view.setMaximumSize(QSize(574, 41))
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

        self.speed_label = QLabel(Widget)
        self.speed_label.setObjectName(u"speed_label")

        self.horizontalLayout.addWidget(self.speed_label)

        self.slider = QSlider(Widget)
        self.slider.setObjectName(u"slider")
        self.slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout.addWidget(self.slider)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.time_label = QLabel(Widget)
        self.time_label.setObjectName(u"time_label")

        self.verticalLayout.addWidget(self.time_label)

        self.status_label = QLabel(Widget)
        self.status_label.setObjectName(u"status_label")

        self.verticalLayout.addWidget(self.status_label)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.algorithm_label.setText(QCoreApplication.translate("Widget", u"Algorithm:", None))
        self.combo_box.setItemText(0, QCoreApplication.translate("Widget", u"Bubble Sort", None))
        self.combo_box.setItemText(1, QCoreApplication.translate("Widget", u"Insertion Sort", None))
        self.combo_box.setItemText(2, QCoreApplication.translate("Widget", u"Merge Sort", None))
        self.combo_box.setItemText(3, QCoreApplication.translate("Widget", u"Quick Sort", None))
        self.combo_box.setItemText(4, QCoreApplication.translate("Widget", u"Heap Sort", None))
        self.combo_box.setItemText(5, QCoreApplication.translate("Widget", u"Counting Sort", None))
        self.combo_box.setItemText(6, QCoreApplication.translate("Widget", u"Radix Sort", None))
        self.combo_box.setItemText(7, QCoreApplication.translate("Widget", u"Bucket Sort", None))
        self.combo_box.setItemText(8, QCoreApplication.translate("Widget", u"Quick Select Sort", None))

        self.array_size_label.setText(QCoreApplication.translate("Widget", u"Array Size:", None))
        self.create_array_button.setText(QCoreApplication.translate("Widget", u"Create Array", None))
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
        self.speed_label.setText(QCoreApplication.translate("Widget", u"Speed:", None))
        self.time_label.setText(QCoreApplication.translate("Widget", u"Time: ", None))
        self.status_label.setText(QCoreApplication.translate("Widget", u"Status: ", None))
    # retranslateUi

