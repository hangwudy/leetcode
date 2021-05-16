from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if k * m > len(bloomDay):
            return -1

        def can_make(days):
            flowers = 0
            bouquet = 0
            for i, bloom in enumerate(bloomDay):
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquet += 1
                        if bouquet == m:
                            break
                        flowers = 0
                else:
                    flowers = 0
            return bouquet == m

        low, high = 1, max(bloomDay),
        while low < high:
            days = low + (high - low) // 2
            if can_make(days):
                high = days
            else:
                low = days + 1

        return low
