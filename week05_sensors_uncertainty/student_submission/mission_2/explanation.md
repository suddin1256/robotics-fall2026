# Mission 2

## comparison

Expanding moving-average windows from 3 to 11 evens out noise but increases the step response delay. Switch to a window-3 median filter to eliminate outlier spikes without inflating the max error of 1.49 or introducing heavy lag, keeping RMSE around 0.16 m.

## fusion_choice

Sensor A updates quickly at 20 Hz with high noise, while Sensor B updates slowly at 5 Hz with lower noise but bias. A weight of 0.45 on Sensor A can balance quick updates with stability, giving a 0.16 m RMSE and 100% data availability without excessive jitter or step lag.

## manual_average

4.17

## manual_fusion

2.25

## manual_median

2.30

## prediction_draft

A moving average with a window of 9 provides smoother filtering and reduces random noise variance, but it increases response delay and smears single outlier spikes across multiple samples.

## responsiveness

Larger filter windows increase signal smoothing but degrade responsiveness, introducing up to a 1.30 s delay following distance changes. For a nearby robot or vehicle, a 1.30 s delay means traveling several meters on stale distance data before reacting, risking a very bad collision.

## selected

3
