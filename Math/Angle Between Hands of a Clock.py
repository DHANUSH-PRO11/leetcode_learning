class Solution:
    def angleClock(self, ho: int, mi: int) -> float:
        ho %= 12
        h = ho * 30 + mi * 0.5
        m = mi * 6
        angle = abs(h - m)
        return min(angle, 360 - angle)