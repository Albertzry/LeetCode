class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        from collections import deque, defaultdict

        if source == target:
            return 0 
            
        station = defaultdict(set)
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                station[routes[i][j]].add(i)

        if source not in station or target not in station:
            return -1
        
        queue = deque([(source,0)])
        path = set()
        visited=set()
        while queue:
            current_station,n= queue.popleft()
            if current_station == target:
                return n
            elif current_station in visited:
                continue
            visited.add(current_station)
            for route in station[current_station]:
                if route not in path:
                    path.add(route)
                    for possible_station in routes[route]:
                        queue.append((possible_station,n+1))
        return -1

        



