from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QApplication
from pyqtgraph import ImageView

import cv2
import numpy as np
import pyrealsense2 as rs


class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QWidget()
        self.button_min = QPushButton('Get Minimum', self.central_widget)
        self.button_max = QPushButton('Get Maximum', self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.button_min)
        self.layout.addWidget(self.button_max)

        self.setCentralWidget(self.central_widget)

        self.image_view = ImageView()
        self.layout.addWidget(self.image_view)

        self.button_max.clicked.connect(self.update_image)

    def camera_init(self):
        # Configure depth and color streams
        pipeline = rs.pipeline()
        config = rs.config()

        # config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 60)

        # # Start streaming
        pipeline.start(config)
        frames = pipeline.wait_for_frames()
        # depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()

        self.color_image = np.asanyarray(color_frame.get_data())

        # images = np.hstack((color_image, color_image))

        # print(color_image)
        # print(np.min(color_image))
        # print(np.max(color_image))
        #
        # gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)


    def update_image(self):
        self.camera_init()
        self.image_view.setImage(self.color_image.T)

    def button_clicked(self):
        print('Button Clicked')

if __name__ == '__main__':
    app = QApplication([])
    window = StartWindow()
    window.show()
    app.exit(app.exec_())