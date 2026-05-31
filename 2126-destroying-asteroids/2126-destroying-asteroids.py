class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for at in asteroids:
            if mass >= at:
                mass += at
            else:
                return False
        return True