# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        direction = 0
        i,j=0,0
        res = [[-1]*n for _ in range(m)]
        res[0][0]=head.val
        current=head.next
        while current is not None:
            if direction%4==0:
                if j+1>=n or res[i][j+1]!=-1:
                    direction+=1
                else:
                    j+=1
                    res[i][j]=current.val
                    current=current.next
            elif direction%4==1:
                if i+1>=m or res[i+1][j]!=-1:
                    direction+=1
                else:
                    i+=1
                    res[i][j]=current.val
                    current=current.next
            elif direction%4==2:
                if j-1<0 or res[i][j-1]!=-1:
                    direction+=1
                else:
                    j-=1
                    res[i][j]=current.val
                    current=current.next
            elif direction%4==3:
                if res[i-1][j]!=-1:
                    direction+=1
                else:
                    i-=1
                    res[i][j]=current.val
                    current=current.next
        return res