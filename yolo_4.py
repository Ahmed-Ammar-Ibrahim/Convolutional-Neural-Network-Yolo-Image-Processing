import cv2
import matplotlib.pyplot as plt
from darkflow.net.build import TFNet
import numpy as np
option = {
    'metaLoad':"built_graph/yolov2-tiny-2.meta",
    'pbLoad':"built_graph/yolov2-tiny-2.pb",
    'threshold': 0.2,
    'gpu': 1
}
tfnet = TFNet(option)
img = cv2.imread('A48.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# use YOLO to predict the image
results = tfnet.return_predict(img)  
colors = [tuple(255 * np.random.rand(3)) for i in range(5)]

for color, result in zip(colors, results):
    tl = (result['topleft']['x'], result['topleft']['y'])
    br = (result['bottomright']['x'], result['bottomright']['y'])
    label = result['label']
    img = cv2.rectangle(img, tl, br, color, 7)
    img = cv2.putText(img, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

plt.imshow(img)
plt.show()




