class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        re = dict()

        def rle(n):
            if n == 1:
                return ["1"]
            else:
                if n-1 not in re.keys():
                    re[n-1] = rle(n-1)
                temp=re[n-1][0]
                num = 0
                result = []
                for i in range(len(re[n-1])):
                    if re[n-1][i] == temp:
                        num += 1
                    else:
                        result.append(str(num))
                        result.append(temp)
                        num = 1
                        temp = re[n-1][i]
                result.append(str(num))
                result.append(temp)
                return result


        return ''.join(rle(n))

                    
                    
                    
