import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
import numpy as np
import os


class filedialogdemo(QWidget):

    def __init__(self, parent=None):
        super(filedialogdemo, self).__init__(parent)
        layout = QVBoxLayout()

        self.btn = QPushButton()
        self.btn.clicked.connect(self.loadFile)
        self.btn.setText("选择图片")
        layout.addWidget(self.btn)

        self.label = QLabel()
        layout.addWidget(self.label)

        self.btn_2 = QPushButton()
        self.btn_2.clicked.connect(self.function)
        self.btn_2.setText("开始检测")
        layout.addWidget(self.btn_2)

        self.label_2 = QLabel()
        layout.addWidget(self.label_2)

        self.content = QTextEdit()
        layout.addWidget(self.content)

        self.setWindowTitle("编织布的瑕疵检测")

        self.setLayout(layout)

    def loadFile(self):
        print("load--file")
        fname, _ = QFileDialog.getOpenFileName(self, '选择图片', 'c:\\', 'Image files(*.jpg *.gif *.png)')
        print(fname)
        img = cv2.imread(fname, 0)
        height, width = img.shape[:2]
        reSize2 = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_CUBIC)  # 缩放
        self.img = reSize2
        img2 = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        self.QtImg = QImage(img2.data,
                            img2.shape[1],
                            img2.shape[0],
                            img2.shape[1]*3,
                            QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(self.QtImg))

    def QImageToCvMat(self, incomingImage):  # 将QImage转换为numpyarray
        incomingImage = incomingImage.convertToFormat(4)
        width = incomingImage.width()
        height = incomingImage.height()
        ptr = incomingImage.constBits()
        arr = np.array(ptr).reshape(height, width, 4)
        return arr

    def function(self):
        img2 = cv2.cvtColor(self.img, cv2.IMREAD_GRAYSCALE)

        res = cv2.medianBlur(img2, 3)  # 中值滤波 核大小3*3

        res = cv2.Canny(res, 40, 140)  # Canny算子边缘检测

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 8))  # 定义矩形结构元素

        res = cv2.morphologyEx(res, cv2.MORPH_CLOSE, kernel)  # 通过闭运算填充瑕疵轮廓内部

        ans = 0  # 统计瑕疵所占空间大小
        for i in range(len(res)):
            for j in range(len(res[i])):
                if res[i][j] > 50:
                    ans += 1

        if 500 >= ans > 0:
            data = "缺陷尺寸大小：%d\n品类：二等品" % (ans)
            os.system('say "a flaw has been detected"')  # 声音提醒
        elif ans > 500:
            data = "缺陷尺寸大小：%d\n品类：次品" % (ans)
            os.system('say "a flaw has been detected"')  # 声音提醒
        else:
            data = "缺陷尺寸大小：%d\n品类：一等品" % (ans)
        self.content.setText(data)

        self.QtImg = QImage(res.data,
                            res.shape[1],
                            res.shape[0],
                            res.shape[1] * 1,
                            QImage.Format_Grayscale8)  # 将numpyarray转换为QImage
        self.label_2.setPixmap(QPixmap.fromImage(self.QtImg))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fileload = filedialogdemo()
    fileload.show()
    sys.exit(app.exec_())
