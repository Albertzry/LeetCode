class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        pos = defaultdict(list)  # 记录每个字符的第一次和最后一次出现位置

        for i, ch in enumerate(s):
            if ch not in pos:
                pos[ch] = [i, i]
            else:
                pos[ch][1] = i

        valid = []  # 所有合法的区间

        for c, (l_c, r_c) in pos.items():
            l, r = l_c, r_c

            nl = nr = l

            while nl >= l or nr <= r:
                i = nl if nl >= l else nr

                l_t, r_t = pos[s[i]] # 当前处理的是字符 s[i]

                if l_t < l: # 当前区间左侧还有该字符，需要向左扩展
                    l = l_t

                if r_t > r: # 当前区间右侧还有该字符，需要向右扩展
                    r = r_t
                
                if i == nl: # 当前处理的是左指针
                    nl -= 1

                if i == nr: # 当前处理的是右指针
                    nr += 1

            valid.append([l, r])

        # 按右端点升序排序
        valid.sort(key=lambda x: x[1])

        # 贪心选择互不重叠的区间
        ans = []
        end = -1

        for left, right in valid:
            if left > end:
                ans.append(s[left:right + 1])
                end = right

        return ans