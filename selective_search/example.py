import skimage
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from selective_search import selective_search, box_filter

# Load image
image = skimage.data.rocket()

# Propose boxes using selective search
boxes = selective_search(image, mode='fast')

# Filter box proposals
# Feel free to change parameters`
boxes_filter = box_filter(boxes, min_size=20, topN=80)

# draw rectangles on the original image
fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(image)
for x1, y1, x2, y2 in boxes_filter:
    bbox = mpatches.Rectangle(
        (x1, y1), (x2-x1), (y2-y1), fill=False, edgecolor='red', linewidth=1)
    ax.add_patch(bbox)

plt.axis('off')
plt.show()