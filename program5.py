# Shuffle the Array
# link -> https://leetcode.com/problems/shuffle-the-array/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        li=[]

        for i in range(n):
            li.append(nums[i])
            li.append(nums[n+i])
        return li
