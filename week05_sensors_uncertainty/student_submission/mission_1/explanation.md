# Mission 1

## bias

-0.004

## bias_vs_variance

Bias measures the systematic calibration offset that shifts the averages away from the 2.00m ground truth. However, variance measures the spread or random dispersion of individual measurements around the sample mean regardless of accuracy.

## dropouts

10

## mean

1.997

## median

1.99

## more_samples

No, taking more samples will not eliminate the 28 outliers or the 10 dropped data points. While adding samples reduces random error from noise, the spikes will continue to distort the sample variance of 0.0996 m2 compared to the stable median of 1.99m.

## outliers

28

## prediction

A biased sensor will have a non-zero average offset relative to the 2.00m ground truth, but low variance. A noisy sensor will have an average close to 2.00m but high variance spread across the 240 readings.

## prediction_draft

A biased sensor will have a non-zero average offset relative to the 2.00m ground truth, but low variance. A noisy sensor will have an average close to 2.00m but high variance spread across the 240 readings.

## profile

outlier_prone

## robot_consequence

An unexpected downward outlier measuring about 0.80 m instead of 2.00 m could trigger emergency braking on an autonomous delivery robot in transit, risking a rear-end collision with commuters or pedestrians.

## variance

0.0996
