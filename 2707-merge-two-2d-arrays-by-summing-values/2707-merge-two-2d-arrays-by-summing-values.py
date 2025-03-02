class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums1.sort()
        nums2.sort()
        ans=[]
        i,j=0,0
        n,m=len(nums1),len(nums2)
        while i<n and j<m:
            if nums1[i][0]<nums2[j][0]:
                ans.append(nums1[i])
                i+=1
                continue
            elif nums1[i][0]>nums2[j][0]:
                ans.append(nums2[j])
                j+=1
                continue
            else:
                ans.append([nums1[i][0],nums1[i][1]+nums2[j][1]])
                i+=1
                j+=1
        if i<n:
            ans+=nums1[i:]
        elif j<m:
            ans+=nums2[j:]
        return ans