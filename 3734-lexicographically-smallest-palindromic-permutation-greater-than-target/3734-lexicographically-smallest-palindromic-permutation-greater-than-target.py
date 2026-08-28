class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        # 特殊情况：长度为1
        if n == 1:
            return s if s > target else ""
        
        # 统计每个字符的出现次数
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        
        # 检查是否能构成回文串，并记录奇数个的字符
        odd_char = ''
        for i in range(26):
            if cnt[i] % 2 == 1:
                # 超过一个字符出现奇数次，无法构成回文
                if odd_char != '':
                    return ""
                odd_char = chr(ord('a') + i)
            cnt[i] //= 2  # 只需要一半的字符来构造左半部分
        
        prefix = []
        
        def check(c):
            left = prefix.copy()
            left.append(c)
            for i in range(25, -1, -1):
                left.extend([chr(ord('a') + i)] * cnt[i])
                
            palindrome = left + [odd_char] + left[::-1]
            
            return ''.join(palindrome) > target
        
        # 贪心构造左半部分的每一位
        for i in range(n // 2):
            found = False
            # 尝试放置字典序最小的字符
            for j in range(26):
                if cnt[j] == 0:
                    continue
                
                cnt[j] -= 1
                if check(chr(ord('a') + j)):
                    # 如果构造的回文串大于target，则选择该字符
                    prefix.append(chr(ord('a') + j))
                    found = True
                    break
                else:
                    cnt[j] += 1  # 不满足条件，恢复计数
            if not found:
                return ""  # 无法构造出大于target的回文串

            if prefix[i] > target[i]:  # prefix已经大于target
                left = prefix[:]
                for j in range(26): 
                    left.extend([chr(ord('a') + j)] * cnt[j])
                palindrome = left + [odd_char] + left[::-1]
                return ''.join(palindrome)

        # 构造最终的回文串
        ans = prefix + [odd_char] + prefix[::-1]
        return ''.join(ans)
