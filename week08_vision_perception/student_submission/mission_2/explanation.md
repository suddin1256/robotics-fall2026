# mission_2

## comparison
Under normal, dim, and occluded conditions, the learned detector produces accurate bounding boxes with fewer false positives, whereas the classical color-threshold detector struggles and fails to detect the mug due to lighting changes. Using normal-1, the classical detector finds no valid contours, while the learned model makes the correct box

## choice
I would recommend the learned detector for its robustness. For normal_1, the foreground mask achieves a Dice score of 0.7306 and a mask IoU of  0.5756. Detailed masks only segment contiguous shapes by low-level features without semantic category labels, meaning background desk equipment is often included. The primary limitation of this small image test is its reliance on a tiny static dataset, which fails to capture diverse real-world lighting angles and clutter.
