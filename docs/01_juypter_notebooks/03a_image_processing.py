from skimage.io import imread, imsave
import stackview
import pyclesperanto as cle
import numpy as np

image = imread('data/lund.tif')

# Apply top hat filter to the image
processed_image = np.asarray(cle.top_hat_box(image, radius_x=10, radius_y=10, radius_z=0))
# Segment the image using voronoi otsu labeling
label_image = cle.voronoi_otsu_labeling(processed_image, spot_sigma=2, outline_sigma=2)

print(label_image.max())

