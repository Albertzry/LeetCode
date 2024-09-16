class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        sum_distance=sum(distance)
        if start > destination:
            start, destination = destination, start
        positive = sum(distance[start:destination])
        negative = sum_distance-positive
        return min(positive,negative)