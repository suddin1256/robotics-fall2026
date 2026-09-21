import math
import os
import unittest
from week03_pattern.pattern import build_pattern

class MyPatternTests(unittest.TestCase):
    def test_my_pattern_geometry(self):
        """Verify segment count, arc radius, and turn angle geometry."""
        segments = build_pattern(os.environ.get("WEEK03_ASSIGNED_PATTERN", "alternating_arcs"))
        
        # Assert expected number of segments for alternating arcs
        self.assertEqual(len(segments), 4)
        
        for seg in segments:
            # Assert forward velocity and speed bounds (v <= 0.22 m/s, |w| <= 0.80 rad/s)
            self.assertGreater(seg.linear_x, 0.0)
            self.assertLessEqual(seg.linear_x, 0.22)
            self.assertLessEqual(abs(seg.angular_z), 0.80)
            
            # Assert arc radius R = |v / w| is approximately 0.30 m
            radius = seg.linear_x / abs(seg.angular_z)
            self.assertAlmostEqual(radius, 0.30, places=2)
            
            # Assert segment angle |w * t| is approximately 45 degrees (pi / 4 rad)
            angle = abs(seg.angular_z) * seg.duration
            self.assertAlmostEqual(angle, math.pi / 4.0, places=2)

    def test_my_pattern_order(self):
        """Verify alternating turn directions and net zero heading change."""
        segments = build_pattern(os.environ.get("WEEK03_ASSIGNED_PATTERN", "alternating_arcs"))
        
        # Verify alternating turning signs: [+0.40, -0.40, +0.40, -0.40]
        expected_signs = [1, -1, 1, -1]
        for seg, expected_sign in zip(segments, expected_signs):
            actual_sign = 1 if seg.angular_z > 0 else -1
            self.assertEqual(actual_sign, expected_sign)
            
        # Verify net orientation change delta_theta equals 0.0 rad
        net_heading_change = sum(seg.angular_z * seg.duration for seg in segments)
        self.assertAlmostEqual(net_heading_change, 0.0, places=4)

if __name__ == "__main__":
    unittest.main()