# this is taken from https://takeuforward.org/data-structure/subset-sum-sum-of-all-subsets/
# I tried to use this for t4 to try to generate the subset sums faster
# but it was too slow too, and the process was killed

from typing import List
class Solution:
    def subsetSums(self, arr: List[int], n: int) -> List[int]:
        ans = []


        def subsetSumsHelper(ind: int, sum: int):
            if ind == n:
                ans.append(sum)
                return
            # element is picked
            subsetSumsHelper(ind + 1, sum + arr[ind])
            # element is not picked
            subsetSumsHelper(ind + 1, sum)
        subsetSumsHelper(0, 0)
        return ans

if __name__ == "__main__":
    arr = [3, 1, 2,5,6,7]
    ans = Solution().subsetSums(arr, len(arr))
    print(ans)
