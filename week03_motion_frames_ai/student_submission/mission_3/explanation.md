# Mission 3

## Ai Disclosure

I've used the free version of ChatGPT because it was free. However, I've had to look through the code many times and prompt it to fix errors. I had to personally redo the indents and import the libaries that it used.

## Assigned Pattern

alternating_arcs

## Assumptions

The AI assumed that there would be no wheel slip, perfect traction, and that the robot would maintain a perfect arc with the exact radius. It assumed the linear variable is in meters per second, angular velocity is in rads per second, and duration is in seconds. The ai also assumed that there will be no lag between commands that the motions will happen exactly back to back.

## Evidence Analysis

The 9  tests tells us that build_pattern is following the  assigned geometry, it maintains the alternating turn sequence order [+0.40, -0.40, +0.40, -0.40], it stays within our velocity limits, and it returns to a 0.0 rad heading. However, it does not test the physical execution accuracy, real-world wheel slip, or actual checkpoint markers in Gazebo.

## Live Pending

True

## Modifications

Added import math to fix missing library imports in the code. The AI referenced math.pi for calculating arc durations but forgot the import statement.

## Original Output

segments = build_pattern(name)
validate(segments)
for segment in segments:
    repeatedly_publish(segment.linear_x, segment.angular_z, segment.duration)
publish_zero_velocity()
record_path_and_stop_evidence()
The wrapper does not decide your geometry. Your segment list determines the path. The course guard separately checks and forwards the commands.

Use an AI assistant of your choice. Include your saved specification and this interface in your prompt:

This is a ROS 2 Jazzy Python package. Implement only build_pattern(pattern_name: str) -> list[Segment] for 'alternating_arcs' in the existing pattern.py.
The course-provided pattern_node.py calls this function, publishes the returned segments repeatedly through /student_cmd_vel, and sends the final zero command.
Use the existing Segment class with linear_x (m/s), angular_z (rad/s), and duration (s).
Return the ordered segments for the assigned specification and raise ValueError for an unknown pattern name.
Stay within 0.22 m/s, 0.80 rad/s, 30 seconds per segment, and 60 seconds total.
Do not replace the wrapper or course checks. Explain assumptions and propose tests.

## Original Prompt

segments = build_pattern(name)
validate(segments)
for segment in segments:
    repeatedly_publish(segment.linear_x, segment.angular_z, segment.duration)
publish_zero_velocity()
record_path_and_stop_evidence()
The wrapper does not decide your geometry. Your segment list determines the path. The course guard separately checks and forwards the commands.

Use an AI assistant of your choice. Include your saved specification and this interface in your prompt:

This is a ROS 2 Jazzy Python package. Implement only build_pattern(pattern_name: str) -> list[Segment] for 'alternating_arcs' in the existing pattern.py.
The course-provided pattern_node.py calls this function, publishes the returned segments repeatedly through /student_cmd_vel, and sends the final zero command.
Use the existing Segment class with linear_x (m/s), angular_z (rad/s), and duration (s).
Return the ordered segments for the assigned specification and raise ValueError for an unknown pattern name.
Stay within 0.22 m/s, 0.80 rad/s, 30 seconds per segment, and 60 seconds total.
Do not replace the wrapper or course checks. Explain assumptions and propose tests.

## Original Source

```python
"""AI-assisted motion pattern implementation.

Preserve the original AI response in Streamlit. Review it, then implement a safe
version here. The node accepts only segments returned by ``build_pattern``.
"""
from __future__ import annotations
from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Segment:
    linear_x: float
    angular_z: float
    duration: float


def build_pattern(pattern_name: str) -> list[Segment]:
    """Return ordered, bounded motion segments for the assigned pattern.

    Supported assignments are ``rounded_rectangle``, ``l_path``, and
    ``alternating_arcs``. Do not include the final stop; the ROS wrapper always
    publishes it and the evaluator verifies it.
    """
    if pattern_name != "alternating_arcs":
        raise ValueError(f"Unknown pattern: {pattern_name}")

    linear_x = 0.12
    angular_z = 0.40

    # Each arc turns 45 degrees.
    # duration = angle / angular velocity.
    duration = (math.pi / 4.0) / angular_z

    return [
        Segment(linear_x, +angular_z, duration),
        Segment(linear_x, -angular_z, duration),
        Segment(linear_x, +angular_z, duration),
        Segment(linear_x, -angular_z, duration),
    ]
```


## Problems

It had many syntax error especially with indentations, my vs code was showing alot of errors becasue of it

## Saved Specification

The robot will do four alternating 45-degree arcs, alternating between left first, then right, with a radius R = 0.30m at a speed of v = 0.12m/s and a turn rate of  0.40 rad/s for about 2 sec per segment. After about 8 s total elapsed time, the controller sends (0.0, 0.0) to /student_cmd_vel to come to a complete stop, keeping speeds down to under 0.22(m/s) and 0.80 rad/s. The robot should complete the four alternating arcs within a 2 m by 2 m area and finish facing its original orientation within these course tolerances.

## Specification

The robot will do four alternating 45-degree arcs, alternating between left first, then right, with a radius R = 0.30m at a speed of v = 0.12m/s and a turn rate of  0.40 rad/s for about 2 sec per segment. After about 8 s total elapsed time, the controller sends (0.0, 0.0) to /student_cmd_vel to come to a complete stop, keeping speeds down to under 0.22(m/s) and 0.80 rad/s. The robot should complete the four alternating arcs within a 2 m by 2 m area and finish facing its original orientation within these course tolerances.

## Test Plan

when build_pattern("alternating_arcs") is run, it will make sure that the 4 segments are reading the correct values, linear_x = 0.12 m/s, duration ≈ 1.9635 s, and alternating angular_z = [+0.40, -0.40, +0.40, -0.40] rad/s. The expected result is a .30m radius arc, then 0.0 rad heading; the stop command will output linear.x = 0.0 m/s and angular.z = 0.0 rad/s and send it to /student_cmd_vel to bring the robot to a complete stop within tolerance.

## Live Issue

I am not too sure; all the other tests passed, but the live verification isn't. The simulation is running at half speed, and my Docker container is using maxed-out CPU. My laptop is also overheating which could play a factor.
