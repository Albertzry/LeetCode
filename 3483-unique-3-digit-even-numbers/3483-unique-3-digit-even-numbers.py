class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        st = set()
        for i, a in enumerate(digits):  # 个位数
            if a % 2:
                continue
            for j, b in enumerate(digits):  # 十位数
                if j == i:
                    continue
                for k, c in enumerate(digits):  # 百位数
                    if c == 0 or k == i or k == j:
                        continue
                    st.add(c * 100 + b * 10 + a)
        return len(st)