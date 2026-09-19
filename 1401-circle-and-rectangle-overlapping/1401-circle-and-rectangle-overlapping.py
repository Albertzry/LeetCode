class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:

        def distance(ux, uy, vx, vy):
            return (ux - vx)**2 + (uy - vy)**2

        """
        圆心在矩形内部
        """
        if x1 <= xCenter <= x2 and y1 <= yCenter <= y2:
            return True

        """
        圆心在矩形上部
        """
        if x1 <= xCenter <= x2 and y2 <= yCenter <= y2 + radius:
            return True

        """
        圆心在矩形下部
        """
        if x1 <= xCenter <= x2 and y1 - radius <= yCenter <= y1:
            return True

        """
        圆心在矩形左部
        """
        if x1 - radius <= xCenter <= x1 and y1 <= yCenter <= y2:
            return True

        """
        圆心在矩形右部
        """
        if x2 <= xCenter <= x2 + radius and y1 <= yCenter <= y2:
            return True

        """
        矩形左上角
        """
        if distance(xCenter, yCenter, x1, y2) <= radius**2:
            return True

        """
        矩形左下角
        """
        if distance(xCenter, yCenter, x1, y1) <= radius**2:
            return True

        """
        矩形右上角
        """
        if distance(xCenter, yCenter, x2, y2) <= radius**2:
            return True

        """
        矩形右下角
        """
        if distance(xCenter, yCenter, x1, y2) <= radius**2:
            return True

        """
        无交点
        """
        return False
