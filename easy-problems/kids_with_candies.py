class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results = list()
        max_candies = sorted(candies)[-1]
        for val in candies:
            if val + extraCandies >= max_candies:
                results.append(True)
            else:
                results.append(False)
        return results