# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cvdlhw2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1265, 943)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Load_Image_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Load_Image_pushButton.setGeometry(QtCore.QRect(20, 180, 131, 41))
        self.Load_Image_pushButton.setObjectName("Load_Image_pushButton")
        self.Load_Video_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Load_Video_pushButton.setGeometry(QtCore.QRect(20, 240, 131, 41))
        self.Load_Video_pushButton.setObjectName("Load_Video_pushButton")
        self.Background_Subtraction_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.Background_Subtraction_groupBox.setGeometry(QtCore.QRect(170, 50, 281, 111))
        self.Background_Subtraction_groupBox.setObjectName("Background_Subtraction_groupBox")
        self.Background_Subtraction_pushButton = QtWidgets.QPushButton(self.Background_Subtraction_groupBox)
        self.Background_Subtraction_pushButton.setGeometry(QtCore.QRect(40, 40, 201, 41))
        self.Background_Subtraction_pushButton.setObjectName("Background_Subtraction_pushButton")
        self.Optical_Flow_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.Optical_Flow_groupBox.setGeometry(QtCore.QRect(170, 200, 281, 191))
        self.Optical_Flow_groupBox.setObjectName("Optical_Flow_groupBox")
        self.Preprocessing_pushButton = QtWidgets.QPushButton(self.Optical_Flow_groupBox)
        self.Preprocessing_pushButton.setGeometry(QtCore.QRect(40, 50, 201, 41))
        self.Preprocessing_pushButton.setObjectName("Preprocessing_pushButton")
        self.Video_tracking_pushButton = QtWidgets.QPushButton(self.Optical_Flow_groupBox)
        self.Video_tracking_pushButton.setGeometry(QtCore.QRect(40, 110, 201, 41))
        self.Video_tracking_pushButton.setObjectName("Video_tracking_pushButton")
        self.PCA_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.PCA_groupBox.setGeometry(QtCore.QRect(170, 430, 281, 131))
        self.PCA_groupBox.setObjectName("PCA_groupBox")
        self.Dimension_Reduction_pushButton = QtWidgets.QPushButton(self.PCA_groupBox)
        self.Dimension_Reduction_pushButton.setGeometry(QtCore.QRect(40, 50, 201, 41))
        self.Dimension_Reduction_pushButton.setObjectName("Dimension_Reduction_pushButton")
        self.MNIST_Classifier_using_VGG19_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.MNIST_Classifier_using_VGG19_groupBox.setGeometry(QtCore.QRect(510, 40, 661, 341))
        self.MNIST_Classifier_using_VGG19_groupBox.setObjectName("MNIST_Classifier_using_VGG19_groupBox")
        self.Show_Model_Structure_VGG19_pushButton = QtWidgets.QPushButton(self.MNIST_Classifier_using_VGG19_groupBox)
        self.Show_Model_Structure_VGG19_pushButton.setGeometry(QtCore.QRect(50, 40, 191, 31))
        self.Show_Model_Structure_VGG19_pushButton.setObjectName("Show_Model_Structure_VGG19_pushButton")
        self.Show_Accuracy_and_Loss_pushButton = QtWidgets.QPushButton(self.MNIST_Classifier_using_VGG19_groupBox)
        self.Show_Accuracy_and_Loss_pushButton.setGeometry(QtCore.QRect(40, 90, 211, 31))
        self.Show_Accuracy_and_Loss_pushButton.setObjectName("Show_Accuracy_and_Loss_pushButton")
        self.Predict_pushButton = QtWidgets.QPushButton(self.MNIST_Classifier_using_VGG19_groupBox)
        self.Predict_pushButton.setGeometry(QtCore.QRect(70, 140, 151, 31))
        self.Predict_pushButton.setObjectName("Predict_pushButton")
        self.Reset_pushButton = QtWidgets.QPushButton(self.MNIST_Classifier_using_VGG19_groupBox)
        self.Reset_pushButton.setGeometry(QtCore.QRect(70, 190, 151, 31))
        self.Reset_pushButton.setObjectName("Reset_pushButton")
        self.VGG19_graphicsView = QtWidgets.QGraphicsView(self.MNIST_Classifier_using_VGG19_groupBox)
        self.VGG19_graphicsView.setGeometry(QtCore.QRect(290, 30, 351, 271))
        self.VGG19_graphicsView.setObjectName("VGG19_graphicsView")
        self.ResNet50_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.ResNet50_groupBox.setGeometry(QtCore.QRect(510, 430, 661, 361))
        self.ResNet50_groupBox.setObjectName("ResNet50_groupBox")
        self.Load_Image_ResNet50_pushButton = QtWidgets.QPushButton(self.ResNet50_groupBox)
        self.Load_Image_ResNet50_pushButton.setGeometry(QtCore.QRect(40, 40, 181, 31))
        self.Load_Image_ResNet50_pushButton.setObjectName("Load_Image_ResNet50_pushButton")
        self.Show_Images_pushButton = QtWidgets.QPushButton(self.ResNet50_groupBox)
        self.Show_Images_pushButton.setGeometry(QtCore.QRect(40, 90, 181, 31))
        self.Show_Images_pushButton.setObjectName("Show_Images_pushButton")
        self.Show_Model_Structure_ResNet50_pushButton = QtWidgets.QPushButton(self.ResNet50_groupBox)
        self.Show_Model_Structure_ResNet50_pushButton.setGeometry(QtCore.QRect(30, 140, 201, 31))
        self.Show_Model_Structure_ResNet50_pushButton.setObjectName("Show_Model_Structure_ResNet50_pushButton")
        self.Show_Comparison_pushButton = QtWidgets.QPushButton(self.ResNet50_groupBox)
        self.Show_Comparison_pushButton.setGeometry(QtCore.QRect(30, 190, 201, 31))
        self.Show_Comparison_pushButton.setObjectName("Show_Comparison_pushButton")
        self.Inference_pushButton = QtWidgets.QPushButton(self.ResNet50_groupBox)
        self.Inference_pushButton.setGeometry(QtCore.QRect(50, 240, 161, 31))
        self.Inference_pushButton.setObjectName("Inference_pushButton")
        self.ResNet50_graphicsView = QtWidgets.QGraphicsView(self.ResNet50_groupBox)
        self.ResNet50_graphicsView.setGeometry(QtCore.QRect(290, 40, 351, 271))
        self.ResNet50_graphicsView.setObjectName("ResNet50_graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1265, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Load_Image_pushButton.setText(_translate("MainWindow", "Load Image"))
        self.Load_Video_pushButton.setText(_translate("MainWindow", "Load Video"))
        self.Background_Subtraction_groupBox.setTitle(_translate("MainWindow", "1. Background Subtraction"))
        self.Background_Subtraction_pushButton.setText(_translate("MainWindow", "1. Background Subtraction"))
        self.Optical_Flow_groupBox.setTitle(_translate("MainWindow", "2. Optical Flow"))
        self.Preprocessing_pushButton.setText(_translate("MainWindow", "2.1 Preprocessing"))
        self.Video_tracking_pushButton.setText(_translate("MainWindow", "2.2 Video tracking"))
        self.PCA_groupBox.setTitle(_translate("MainWindow", "3. PCA"))
        self.Dimension_Reduction_pushButton.setText(_translate("MainWindow", "3. Dimension Reduction"))
        self.MNIST_Classifier_using_VGG19_groupBox.setTitle(_translate("MainWindow", "4. MNIST Classifier Using VGG19"))
        self.Show_Model_Structure_VGG19_pushButton.setText(_translate("MainWindow", "1. Show Model Structure"))
        self.Show_Accuracy_and_Loss_pushButton.setText(_translate("MainWindow", "2. Show Accuracy and Loss"))
        self.Predict_pushButton.setText(_translate("MainWindow", "3. Predict"))
        self.Reset_pushButton.setText(_translate("MainWindow", "4. Reset"))
        self.ResNet50_groupBox.setTitle(_translate("MainWindow", "5. ResNet50"))
        self.Load_Image_ResNet50_pushButton.setText(_translate("MainWindow", "Load Image"))
        self.Show_Images_pushButton.setText(_translate("MainWindow", "5.1 Show Images"))
        self.Show_Model_Structure_ResNet50_pushButton.setText(_translate("MainWindow", "5.2 Show Model Structure"))
        self.Show_Comparison_pushButton.setText(_translate("MainWindow", "5.3 Show Comparison"))
        self.Inference_pushButton.setText(_translate("MainWindow", "5.4 Inference"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
