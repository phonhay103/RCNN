def bb_intersection_over_union(boxA, boxB):
    '''
    Calculate IOU (Intersection over Union) on bounding boxes

    Parameters
    ----------
        boxA, boxB: (x0, y0, x1, y1)
            Bounding boxes

    Returns
    -------
        IoU: float
            IoU of bounding boxes
    '''
    # determine the (x, y) - coordinates of the intersection rectangle
    x0 = max(boxA[0], boxB[0])
    y0 = max(boxA[1], boxB[1])
    x1 = min(boxA[2], boxB[2])
    y1 = min(boxA[3], boxB[3])

    # compute the area of intersection rectangle
    interArea = max(0, x1 - x0) * max(0, y1 - y0)

    if interArea == 0:
        return 0.0

    # compute the area of both the prediction and ground-truth rectangles
    boxA_area = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxB_area = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])

    # compute the intersection over union by taking the intersection
	# area and dividing it by the sum of prediction + ground-truth
	# areas - the interesection area
    return interArea / float(boxA_area + boxB_area - interArea)