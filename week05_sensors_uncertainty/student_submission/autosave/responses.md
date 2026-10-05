# Week 5: Sensors, Noise, and Uncertainty

- course_id: 24101093
- email: shadib.uddin93@login.cuny.edu
- name: Shadib Uddin

## concepts.observation

Bias moves the whole reading up or down from the truth, whereas noise adds in more random values that mess with the final measurement. Bias shifts the distribution, whereas noise makes the distribution harder to read since it adds more scattered data.

## final.course_reflection

This activity showed me how deeply low-level sensor noise and filtering choices impact real-world robotic decision-making. Working through the trade-offs between moving-average lag and median outlier rejection made these signal processing concepts tangible. Connecting technical filtering choices to real-world consequences, like comparing warehouse efficiency against human safety in assistive settings, showed me the importance of designing failure-tolerant software.

## final.synthesis

Sensor characterization in Mission 1 revealed that Sensor A exhibits high sample variance and outlier spikes, while Sensor B suffers from dropouts and bias offset from ground truth. These unique failure modes directly influenced the filter design decisions in Mission 2. Using a window-3 median filter effectively eliminates Sensor A's extreme values without the bad lag caused by larger moving-average windows, keeping max error down to 1.49 m and RMSE near 0.16 m. Fusing Sensor A with a 0.45 weight balanced high-frequency update responsiveness against Sensor B's stability. In Mission 3, translating these outputs into vehicle control decisions shows how deployment context alters safety tolerances. The assistive setting required a higher stopping threshold and caution margin to make sure there are no dangerous commands near humans, trading off minor efficiency. On the other hand, the warehouse policy prioritized throughput with a 0.75 m threshold and 1 confirmation cycle to maintain low detection delay. Together, these missions show that effective autonomous control relies on aligning hardware characterization, strong signal filtering, and context-biased safety thresholds.

## mission_1.bias

-0.004

## mission_1.bias_vs_variance

Bias measures the systematic calibration offset that shifts the averages away from the 2.00m ground truth. However, variance measures the spread or random dispersion of individual measurements around the sample mean regardless of accuracy.

## mission_1.dropouts

10

## mission_1.mean

1.997

## mission_1.median

1.99

## mission_1.more_samples

No, taking more samples will not eliminate the 28 outliers or the 10 dropped data points. While adding samples reduces random error from noise, the spikes will continue to distort the sample variance of 0.0996 m2 compared to the stable median of 1.99m.

## mission_1.outliers

28

## mission_1.prediction

A biased sensor will have a non-zero average offset relative to the 2.00m ground truth, but low variance. A noisy sensor will have an average close to 2.00m but high variance spread across the 240 readings.

## mission_1.prediction_draft

A biased sensor will have a non-zero average offset relative to the 2.00m ground truth, but low variance. A noisy sensor will have an average close to 2.00m but high variance spread across the 240 readings.

## mission_1.profile

outlier_prone

## mission_1.robot_consequence

An unexpected downward outlier measuring about 0.80 m instead of 2.00 m could trigger emergency braking on an autonomous delivery robot in transit, risking a rear-end collision with commuters or pedestrians.

## mission_1.variance

0.0996

## mission_2.comparison

Expanding moving-average windows from 3 to 11 evens out noise but increases the step response delay. Switch to a window-3 median filter to eliminate outlier spikes without inflating the max error of 1.49 or introducing heavy lag, keeping RMSE around 0.16 m.

## mission_2.fusion_choice

Sensor A updates quickly at 20 Hz with high noise, while Sensor B updates slowly at 5 Hz with lower noise but bias. A weight of 0.45 on Sensor A can balance quick updates with stability, giving a 0.16 m RMSE and 100% data availability without excessive jitter or step lag.

## mission_2.manual_average

4.17

## mission_2.manual_fusion

2.25

## mission_2.manual_median

2.30

## mission_2.prediction_draft

A moving average with a window of 9 provides smoother filtering and reduces random noise variance, but it increases response delay and smears single outlier spikes across multiple samples.

## mission_2.responsiveness

Larger filter windows increase signal smoothing but degrade responsiveness, introducing up to a 1.30 s delay following distance changes. For a nearby robot or vehicle, a 1.30 s delay means traveling several meters on stale distance data before reacting, risking a very bad collision.

## mission_2.selected

3

## mission_3.Assistive.prediction_draft

Increasing the stopping threshold to 0.85 m and adding a 0.25 m margin minimizes the risky command events near humans while maintaining low detection delay.

## mission_3.Warehouse.prediction_draft

Adding a margin and confirmation count will eliminate false-safe triggers from isolated spikes while maintaining a good detection delay.

## mission_3.context_comparison

The assistive policy sets a larger stopping threshold and caution margin than the warehouse policy. This conservative tuning drops dangerous commands to 0 and avoids false-safe errors around people, trading off minor operational speed for user safety.

## mission_3.error_costs

In warehouse settings, false-safe errors risk equipment collision costs borne by facility managers, while unnecessary stops cause minor workflow delays. In assistive settings, false-safe errors risk direct physical injury to humans, making safety incredibly important, whereas unnecessary stops reduce user convenience and mobility.

## mission_3.limitations

These tests prove how policies handle synthetic step changes and sensor dropouts, but they don't cover real-world dynamic movement or physical braking distances. Before launching, consult human safety officers and run hardware braking tests at full speed and under heavy load.
