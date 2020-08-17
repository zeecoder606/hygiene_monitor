import numpy as np
import cv2
import os

def iou(box, clusters):
    x = np.minimum(clusters[:, 0], box[0])
    y = np.minimum(clusters[:, 1], box[1])

    intersection = x * y
    box_area = box[0] * box[1]
    cluster_area = clusters[:, 0] * clusters[:, 1]

    iou_ = intersection / (box_area + cluster_area - intersection)

    return iou_

def kmeans(boxes, k, dist=np.median):
	rows = boxes.shape[0]

	distances = np.empty((rows, k))
	last_clusters = np.zeros((rows,))

	np.random.seed()

	clusters = boxes[np.random.choice(rows, k, replace=False)]
	loop = 0

	while True:
		loop += 1
		print (loop)
		for row in range(rows):
		    distances[row] = 1 - iou(boxes[row], clusters)

		nearest_clusters = np.argmin(distances, axis=1)

		if (last_clusters == nearest_clusters).all():
		    break

		for cluster in range(k):
		    clusters[cluster] = dist(boxes[nearest_clusters == cluster], axis=0)

		last_clusters = nearest_clusters
	return clusters

boxes = np.empty((0,2))
for file in os.listdir("labels/"):
	file_ = os.path.join("labels",file)
	f = open(file_, "r")
	L = f.readlines()
	for L1 in L:
		L1 = L[0].rstrip().split(" ")
		if (len(L1)==1):
			continue
		w_h = L1[3:]
		w_h[0] = float(w_h[0])
		w_h[1] = float(w_h[1])
		boxes = np.append(boxes, [w_h], axis = 0)

anchors = kmeans(boxes, 9)
print(anchors*416)


