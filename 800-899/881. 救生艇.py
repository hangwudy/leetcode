from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        left, right = 0, len(people) - 1,
        people.sort(reverse=True)
        while left < right:
            if people[left] + people[right] > limit:
                left += 1
            else:
                left += 1
                right -= 1
            ans += 1
        return ans
