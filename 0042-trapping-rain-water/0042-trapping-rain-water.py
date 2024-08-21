class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        left_max=0
        right_max=0
        result=0
        while left<right:
            if height[left]<height[right]:
                if height[left]<left_max:
                    result+=left_max-height[left]
                else:
                    left_max=height[left]
                left+=1
            else:
                if height[right]<right_max:
                    result+=right_max-height[right]
                else:
                    right_max=height[right]
                right-=1
        return result

#上面是采用双指针，下面采用动态规划
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_max=[]
        right_max=[]
        left = 0
        right = 0
        result = 0
        for i in range(len(height)):
            left=max(height[i],left)
            left_max.append(left)
        for i in range(len(height)-1,-1,-1):
            right=max(height[i],right)
            right_max.append(right)
        right_max.reverse()
        for i in range(len(height)):
            if min(left_max[i],right_max[i])==height[i]:
                continue
            else:
                result+=min(left_max[i],right_max[i])-height[i]
        return result
            
