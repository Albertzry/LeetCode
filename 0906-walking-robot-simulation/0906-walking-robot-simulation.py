class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        row = dict()
        column = dict()
        x, y, direction , result = 0, 0, 0, 0
        for i in range(len(obstacles)):
            if obstacles[i][0] not in row:
                row[obstacles[i][0]] = [obstacles[i][1]]
            else:
                row[obstacles[i][0]].append(obstacles[i][1])
                row[obstacles[i][0]] = sorted(row[obstacles[i][0]])
            if obstacles[i][1] not in column:
                column[obstacles[i][1]] = [obstacles[i][0]]
            else:
                column[obstacles[i][1]].append(obstacles[i][0])
                column[obstacles[i][1]] = sorted(column[obstacles[i][1]])

        def judge(x, y, direction, length):
            if direction % 4 == 0:
                if x not in row:
                    return x, y + length
                else:
                    for i in range(len(row[x])):
                        if row[x][i] <= y + length and row[x][i] > y:
                            return x, row[x][i] - 1
                    return x, y + length
            elif direction % 4 == 1:
                if y not in column:
                    return x + length, y
                else:
                    for i in range(len(column[y])):
                        if column[y][i] <= x + length and column[y][i] > x:
                            return column[y][i] - 1, y
                    return x + length, y
            elif direction % 4 == 2:
                if x not in row:
                    return x, y - length
                else:
                    for i in range(len(row[x])):
                        if row[x][i] >= y - length and row[x][i] < y:
                            return x, row[x][i] + 1
                    return x, y - length
            elif direction % 4 == 3:
                if y not in column:
                    return x - length, y
                else:
                    for i in range(len(column[y])):
                        if column[y][i] >= x - length and column[y][i] < x:
                            return column[y][i] + 1, y
                    return x - length, y

        for i in range(len(commands)):
            if commands[i] == -1:
                direction += 1
            elif commands[i] == -2:
                direction -= 1
            else:
                x, y = judge(x, y, direction, commands[i])
                result = max(result, x ** 2 + y ** 2)

        return result
        
