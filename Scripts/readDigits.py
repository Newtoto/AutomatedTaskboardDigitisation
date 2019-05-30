import cv2
import numpy as np

# Read image files
digits = cv2.imread("../Images/digits.png", cv2.IMREAD_GRAYSCALE)
test_digits = cv2.imread("../Images/test_digits.png", cv2.IMREAD_GRAYSCALE)

# Split training image into rows
rows = np.vsplit(digits, 50)
# Split training rows into cells
cells = []
for row in rows:
    row_cells = np.hsplit(row, 50)
    for cell in row_cells:
        cell = cell.flatten()
        cells.append(cell)
cells = np.array(cells, dtype=np.float32)
 
k = np.arange(10)
cells_labels = np.repeat(k, 250)
 

test_digits = np.vsplit(test_digits, 50)
test_cells = []
for d in test_digits:
    d = d.flatten()
    test_cells.append(d)
test_cells = np.array(test_cells, dtype=np.float32)
 
 
# KNN
knn = cv2.ml.KNearest_create()
knn.train(cells, cv2.ml.ROW_SAMPLE, cells_labels)
ret, result, neighbours, dist = knn.findNearest(test_cells, k=3)
 
 
print(result)