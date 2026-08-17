from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        # Step 1: number -> frequency
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Step 2: frequency -> numbers
        for n, c in count.items():
            freq[c].append(n)

        # Step 3: highest frequency se start karo
        res = []

        for c in range(len(freq) - 1, 0, -1):
            for n in freq[c]:
                res.append(n)

                if len(res) == k:
                    return res