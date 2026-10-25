# Lab 7 saved answers

## mission_1.diagnosis
In the normal_1 images, the detector was able to place the bounding box around the mug because the lighting gives enough color saturation and contrast for the HSV to isolate the different color surfaces. Dim_1, however, the lower light made the pixel values of the mug fall below the threshold, causing an empty mask. As a result no contours meet the minimum area and circularity requirements making the detector to return nothing.

## mission_1.limitations
Adjusting the upper hue boundary or lowering the min value threshold allowed the mask to capture more of the mug's shadow, but it caused the wooden table surface to pass the color rule. The main issue with this detection style is that it relies on static color rather than shape.

## mission_2.comparison
Under normal, dim, and occluded conditions, the learned detector produces accurate bounding boxes with fewer false positives, whereas the classical color-threshold detector struggles and fails to detect the mug due to lighting changes. Using normal-1, the classical detector finds no valid contours, while the learned model makes the correct box

## mission_2.choice
I would recommend the learned detector for its robustness. For normal_1, the foreground mask achieves a Dice score of 0.7306 and a mask IoU of  0.5756. Detailed masks only segment contiguous shapes by low-level features without semantic category labels, meaning background desk equipment is often included. The primary limitation of this small image test is its reliance on a tiny static dataset, which fails to capture diverse real-world lighting angles and clutter.

## pillar_search.diagnosis
I looked at the settings and made sure the steering gain stayed at 1.2 and that the four pillars were listed. As a result of this attempt, there was smooth error correction without any overcorrections or oscillations.

## pillar_search.evidence
All four colors were centered, with just the blue being slightly off. The timeline shows valid contour detections leading to a clean hold across each target. However, a centered color mask and stable hold do not prove object identity or distance because the pipeline relies mainly on static color thresholds and image-space contour centroids, meaning any identically colored surface or reflection would produce the exact same steering response without verifying physical depth or category.

## line_following.comparison
I have uses the same settings for both tracks; I have lowered the gain and speed to .15 and .14. This made the straight track perfect, where the robot was tracking exactly on the centerline the whole length. For the curve track, the robot was able to traverse the whole track; however, I noticed on the curves the robot would almost travel wide, while the camera detection did successfully detect the true center. The robot's angular velocity error correction wasn't aggressive enough to maintain the robot on the center line, causing it to take wider turns.

## line_following.limits
While both of my tests were successful, I did notice that on the curves the robot would almost travel wide, while the camera detection successfully detected the true center. The robot's angular velocity error correction wasn't aggressive enough to maintain the robot on the center line, causing it to take wider turns.

## final.synthesis
Across all three missions, turning visual evidence into reliable robot behavior requires balancing sensor data with control tuning. Classical HSV thresholding stopped working under dim lighting, whereas the learned detector maintained better resilience, achieving a mask IoU of 0.5756 on normal. The error correction successfully centered four colored pillars in sequence; however, static color masks couldn't verify true object depth or identity. Furthermore, tuning the line-following steering gain to 0.15 and speed to 0.14 provided decent proportional response to navigate tight curves without bad oscillation or even kicking the robot off course. Ultimately, closed-loop vision pipelines are great for tracking, but are limited by static color guesses, small datasets, and a lack of depth sensing.

## final.course_reflection
Building and testing computer vision systems for the turtle robot highlighted how software, sensors, and control systems connect in real-world engineering. Working through classical computer vision, learned detection, and proportional control significantly boosted my motivation to pursue advanced design challenges in robotics and automation. This has motivated me to use the things I’ve learn from this lab into our autonomous drone flying project where we have a basic computer vision setup barely working. With the additional knowledge gained from this lab, I am confident that my group members and I can build a more optimised, low-latency vision system that can aid in planning the flight line a drone is supposed to take in an environment.
