class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        idx = list(range(n))
        idx.sort(key=lambda i: positions[i])

        alive = []
        for i in idx:
            curIdx, curHp, curDir = i, healths[i], directions[i]
            while alive:
                prevIdx, prevHp, prevDir = alive[-1]
                if prevDir == "R" and curDir == "L":
                    alive.pop()
                    if prevHp > curHp:
                        curIdx, curHp, curDir = prevIdx, prevHp - 1, prevDir
                    elif prevHp < curHp:
                        curHp -= 1
                    else:
                        curIdx = -1
                        break
                else:
                    break
            if curIdx != -1:
                alive.append((curIdx, curHp, curDir))

        alive.sort(key=lambda o: o[0])
        return list(o[1] for o in alive)

