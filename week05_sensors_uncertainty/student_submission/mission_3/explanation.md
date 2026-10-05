# Mission 3

## Assistive.prediction_draft

Increasing the stopping threshold to 0.85 m and adding a 0.25 m margin minimizes the risky command events near humans while maintaining low detection delay.

## Warehouse.prediction_draft

Adding a margin and confirmation count will eliminate false-safe triggers from isolated spikes while maintaining a good detection delay.

## context_comparison

The assistive policy sets a larger stopping threshold and caution margin than the warehouse policy. This conservative tuning drops dangerous commands to 0 and avoids false-safe errors around people, trading off minor operational speed for user safety.

## error_costs

In warehouse settings, false-safe errors risk equipment collision costs borne by facility managers, while unnecessary stops cause minor workflow delays. In assistive settings, false-safe errors risk direct physical injury to humans, making safety incredibly important, whereas unnecessary stops reduce user convenience and mobility.

## limitations

These tests prove how policies handle synthetic step changes and sensor dropouts, but they don't cover real-world dynamic movement or physical braking distances. Before launching, consult human safety officers and run hardware braking tests at full speed and under heavy load.
