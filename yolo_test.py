import cv2
import matplotlib.pyplot as plt
from darkflow.net.build import TFNet
option = {
    'metaLoad':"built_graph/yolov2-tiny-2.meta",
    'pbLoad':"built_graph/yolov2-tiny-2.pb",
    'threshold': 0.2,
    'gpu': 1
}
tfnet = TFNet(option)
img = cv2.imread('A42.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# use YOLO to predict the image
result = tfnet.return_predict(img)
print(result)
img.shape
tl = (result[0]['topleft']['x'], result[0]['topleft']['y'])
print(tl)
br = (result[0]['bottomright']['x'], result[0]['bottomright']['y'])
label = result[0]['label']


# add the box and label and display it
img = cv2.rectangle(img, tl, br, (0, 0, 255), 4)
img = cv2.putText(img, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
plt.imshow(img)
plt.show()