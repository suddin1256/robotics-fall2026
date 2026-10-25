# pillar_search

## diagnosis
I looked at the settings and made sure the steering gain stayed at 1.2 and that the four pillars were listed. As a result of this attempt, there was smooth error correction without any overcorrections or oscillations.

## evidence
All four colors were centered, with just the blue being slightly off. The timeline shows valid contour detections leading to a clean hold across each target. However, a centered color mask and stable hold do not prove object identity or distance because the pipeline relies mainly on static color thresholds and image-space contour centroids, meaning any identically colored surface or reflection would produce the exact same steering response without verifying physical depth or category.
