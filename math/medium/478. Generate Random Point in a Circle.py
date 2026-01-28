import random, math
from typing import List

# 1. Polar
class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        theta = random.uniform(0.0, 2.0 * math.pi) # 각도
        rad = self.r * math.sqrt(random.random())  # sqrt가 핵심
        return [self.x + rad * math.cos(theta), self.y + rad * math.sin(theta)]
    
    
## 2. Rejection Sampling
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        while True:
            dx = random.uniform(-self.r, self.r)
            dy = random.uniform(-self.r, self.r)
            if dx*dx + dy*dy <= self.r*self.r:
                return [self.x + dx, self.y + dy]
