class Solution(object):
    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        """
        :type buses: List[int]
        :type passengers: List[int]
        :type capacity: int
        :rtype: int
        """
        buses.sort()
        passengers.sort()
        pos = 0

        for arrive in buses:
            space = capacity
            while space > 0 and pos < len(passengers) and passengers[pos] <= arrive:
                space -= 1
                pos += 1

        pos -= 1
        last_catch_time = buses[-1] if space > 0 else passengers[pos]
        while pos >= 0 and passengers[pos] == last_catch_time:
            pos -= 1
            last_catch_time -= 1

        return last_catch_time

            