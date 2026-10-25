# mission_1

## diagnosis
In the normal_1 images, the detector was able to place the bounding box around the mug because the lighting gives enough color saturation and contrast for the HSV to isolate the different color surfaces. Dim_1, however, the lower light made the pixel values of the mug fall below the threshold, causing an empty mask. As a result no contours meet the minimum area and circularity requirements making the detector to return nothing.

## limitations
Adjusting the upper hue boundary or lowering the min value threshold allowed the mask to capture more of the mug's shadow, but it caused the wooden table surface to pass the color rule. The main issue with this detection style is that it relies on static color rather than shape.
