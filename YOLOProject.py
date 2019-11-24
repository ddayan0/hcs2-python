#Dennis Dayan, Cole Zucosky
#YOLOProject.py
#this script has more confidence than us
import numpy as np
import argparse
import time
import cv2
import os




#Below allows you to parse arguments through a terminal command, although this is essentiallty disabled for ease of use
#DO NOT DELETE!
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default="dinner.jpg",
	help="path to input image")
ap.add_argument("-y", "--yolo", default="./yolo-coco",
	help="base path to YOLO directory")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
	help="minimum probability to filter weak detections")
ap.add_argument("-t", "--threshold", type=float, default=0.3,
	help="threshold when applying non-maxima suppression")
args = vars(ap.parse_args())

#Gets object labels
labelsPath = os.path.sep.join([args["yolo"], "coco.names"])
LABELS = open(labelsPath).read().strip().split("\n")
#Gets label color
np.random.seed(42)
COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
	dtype="uint8")

#Setting the paths for the weights and the cvg into a variable
weightsPath = os.path.sep.join([args["yolo"], "yolov3.weights"])
configPath = os.path.sep.join([args["yolo"], "yolov3.cfg"])

#friendly print message
print('''[INFO] loading YOLO from disk...


     _____        ___                 ___          ___          ___          ___          ___
    /  /::\      /  /\        ___    /  /\        /__/\        /  /\        /  /\        /  /\    ___
   /  /:/\:\    /  /::\      /__/|  /  /::\       \  \:\      /  /:/_      /  /::\      /  /:/_  /  /\
  /  /:/  \:\  /  /:/\:\    |  |:| /  /:/\:\       \  \:\    /  /:/ /\    /  /:/\:\    /  /:/ /\/  /:/
 /__/:/ \__\:|/  /:/~/::\   |  |:|/  /:/~/::\  _____\__\:\  /  /:/ /::\  /  /:/  \:\  /  /:/ /:/  /:/
 \  \:\ /  /:/__/:/ /:/\:\__|__|:/__/:/ /:/\:\/__/::::::::\/__/:/ /:/\:\/__/:/ \__\:\/__/:/ /:/  /::\
  \  \:\  /:/\  \:\/:/__\/__/::::\  \:\/:/__\/\  \:\~~\~~\/\  \:\/:/~/:/\  \:\ /  /:/\  \:\/:/__/:/\:\
   \  \:\/:/  \  \::/       ~\~~\:\  \::/      \  \:\  ~~~  \  \::/ /:/  \  \:\  /:/  \  \::/\__\/  \:\
    \  \::/    \  \:\         \  \:\  \:\       \  \:\       \__\/ /:/    \  \:\/:/    \  \:\     \  \:\
     \__\/      \  \:\         \__\/\  \:\       \  \:\        /__/:/      \  \::/      \  \:\     \__\/
                 \__\/        ___    \__\/        \__\/        \__\/   ___  \__\/ _____  \__\/ ___          ___                 ___                   ___          ___
     _____       _____       /  /\    /  /\                ___        /__/\      /  /::\      /__/\        /  /\        ___    /  /\      ___        /  /\        /  /\
    /  /::\     /  /::\     /  /::\  /  /::\              /  /\       \  \:\    /  /:/\:\     \  \:\      /  /:/_      /  /\  /  /::\    /  /\      /  /:/_      /  /:/_
   /  /:/\:\   /  /:/\:\   /  /:/\:\/  /:/\:\            /  /:/        \  \:\  /  /:/  \:\     \  \:\    /  /:/ /\    /  /:/ /  /:/\:\  /  /:/     /  /:/ /\    /  /:/ /\
  /  /:/~/::\ /  /:/~/::\ /  /:/~/:/  /:/~/::\          /__/::\    _____\__\:\/__/:/ \__\:|___  \  \:\  /  /:/ /::\  /  /:/ /  /:/~/:/ /__/::\    /  /:/ /:/_  /  /:/ /::\
 /__/:/ /:/\:/__/:/ /:/\:/__/:/ /:/__/:/ /:/\:\         \__\/\:\__/__/::::::::\  \:\ /  /:/__/\  \__\:\/__/:/ /:/\:\/  /::\/__/:/ /:/__\__\/\:\__/__/:/ /:/ /\/__/:/ /:/\:\`
 \  \:\/:/~/:|  \:\/:/~/:|  \:\/:/\  \:\/:/__\/            \  \:\/\  \:\~~\~~\/\  \:\  /:/\  \:\ /  /:/\  \:\/:/~/:/__/:/\:\  \:\/:::::/  \  \:\/\  \:\/:/ /:/\  \:\/:/~/:/
  \  \::/ /:/ \  \::/ /:/ \  \::/  \  \::/                  \__\::/\  \:\  ~~~  \  \:\/:/  \  \:\  /:/  \  \::/ /:/\__\/  \:\  \::/~~~~    \__\::/\  \::/ /:/  \  \::/ /:/
   \  \:\/:/   \  \:\/:/   \  \:\   \  \:\                  /__/:/  \  \:\       \  \::/    \  \:\/:/    \__\/ /:/      \  \:\  \:\        /__/:/  \  \:\/:/    \__\/ /:/
    \  \::/     \  \::/     \  \:\   \  \:\                 \__\/    \  \:\       \__\/      \  \::/       /__/:/        \__\/\  \:\       \__\/    \  \::/       /__/:/
     \__\/       \__\/       \__\/    \__\/                           \__\/                   \__\/        \__\/               \__\/                 \__\/        \__\/










''')
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

#Sets up handling for images arguments
#Gives the image to cv2
image = cv2.imread(args["image"])
(H, W) = image.shape[:2]

#imma be real with u i have no definite idea
#Pulls layer name from coco.names?
ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

#Sets image to a simplified template
#cv2 processes the simplified image

blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
	swapRB=True, crop=False)
net.setInput(blob)
start = time.time()
layerOutputs = net.forward(ln)
end = time.time()

#Print statement
print("[INFO] YOLO took {:.6f} seconds".format(end - start))

#Sets list for boxes, confidences and classIDs
boxes = []
confidences = []
classIDs = []

#Confidence module taken from https://www.pyimagesearch.com/2018/11/12/yolo-object-detection-with-opencv/
# loop over each of the layer outputs
for output in layerOutputs:
	# loop over each of the detections
	for detection in output:
		# extract the class ID and confidence (i.e., probability) of
		# the current object detection
		scores = detection[5:]
		classID = np.argmax(scores)
		confidence = scores[classID]

		# filter out weak predictions by ensuring the detected
		# probability is greater than the minimum probability
		if confidence > args["confidence"]:
			# scale the bounding box coordinates back relative to the
			# size of the image, keeping in mind that YOLO actually
			# returns the center (x, y)-coordinates of the bounding
			# box followed by the boxes' width and height
			box = detection[0:4] * np.array([W, H, W, H])
			(centerX, centerY, width, height) = box.astype("int")

			# use the center (x, y)-coordinates to derive the top and
			# and left corner of the bounding box
			x = int(centerX - (width / 2))
			y = int(centerY - (height / 2))

			# update our list of bounding box coordinates, confidences,
			# and class IDs
			boxes.append([x, y, int(width), int(height)])
			confidences.append(float(confidence))
			classIDs.append(classID)

#Uses confidence to prevent excessive detection and overlapping boxes
idxs = cv2.dnn.NMSBoxes(boxes, confidences, args["confidence"],
	args["threshold"])

# ensure at least one detection exists
if len(idxs) > 0:
	# loops over boxes
	for i in idxs.flatten():
		# extracts box coordinates
		(x, y) = (boxes[i][0], boxes[i][1])
		(w, h) = (boxes[i][2], boxes[i][3])

		# draw a bounding box rectangle and label on the image
		color = [int(c) for c in COLORS[classIDs[i]]]
		cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
		text = "{}: {:.4f}".format(LABELS[classIDs[i]], confidences[i])
		cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
			0.5, color, 2)

# shows the actual image
#woo hoo!
cv2.imshow("Image", image)
cv2.waitKey(0)

