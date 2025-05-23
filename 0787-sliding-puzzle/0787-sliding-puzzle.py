class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 邻近点
        neighbors = {0: (1, 3), 1: (0, 2, 4), 2: (1, 5), 3: (0, 4), 4: (1, 3, 5), 5: (2, 4)}

        # 曼哈顿距离
        def ManhattanDist(p1, p2):
            return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

        # State状态
        class State:
            def __init__(self, b=None, cost=0):
                self.board = b
                self.h = self.heuristic()
                self.g = cost
                # A*, f=h+g
                self.f = self.h + self.g
                self.hash = hash(tuple(self.board))

            def __lt__(self, other):
                return self.f < other.f

            def __eq__(self, other):
                return self.hash == other.hash or self.board == other.board

            def __hash__(self):
                return self.hash

            # 两种启发式
            def heuristic(self):
                # h1
                return sum(1 for i in range(6) if self.board[i] and self.board[i] != i + 1)
                # h2
                # return sum(
                #     ManhattanDist((i // 3, i % 3), ((num - 1) // 3, (num - 1) % 3))
                #     for i, num in enumerate(self.board) if num)

            # 下一个状态为和0的各种交换
            def successor(self):
                idx = self.board.index(0)
                successors = []
                for ng in neighbors[idx]:
                    temp = self.board[:]
                    temp[idx] = temp[ng]
                    temp[ng] = 0
                    successors.append(State(temp, self.g + 1))
                return successors

        board = board[0] + board[1]
        # n*m puzzle中，m为奇数时,逆序数对奇偶性要和最终奇偶性相同，否则无解
        if sum(1 for i in range(6) for j in range(i+1, 6) if board[j] and board[i] > board[j]) % 2 == 1:
            return -1
        initState = State(board)
        pq = [initState]
        explored = {initState}
        # 优先队列以f=h+g进行了排序
        while pq:
            state = heapq.heappop(pq)
            if state.board == [1, 2, 3, 4, 5, 0]:
                return state.g
            for successor in state.successor():
                if successor not in explored:
                    explored.add(successor)
                    heapq.heappush(pq, successor)
        return -1
