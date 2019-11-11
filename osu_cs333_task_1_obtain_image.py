import cv2
import numpy as np
import pyrealsense2 as rs


# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()

# config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 60)

# # Start streaming
pipeline.start(config)


while(True):
    frames = pipeline.wait_for_frames()
    # depth_frame = frames.get_depth_frame()
    color_frame = frames.get_color_frame()
    color_frame = frames.get_color_frame()

    color_image = np.asanyarray(color_frame.get_data())

    # images = np.hstack((color_image, color_image))

    print(color_image)
    print(np.min(color_image))
    print(np.max(color_image))

    gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
    luv = cv2.cvtColor(color_image, cv2.COLOR_RGB2Luv)

    # images = np.hstack((bgr555, gray))

    cv2.imshow('color_image', luv)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

print(np.size(gray))
print(np.size(luv))

pipeline.stop()
cv2.destroyAllWindows()