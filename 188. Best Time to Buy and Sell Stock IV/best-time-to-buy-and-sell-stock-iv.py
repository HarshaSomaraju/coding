from typing import List


class Solution:

    # Greedy approach
    # def maxProfit(self, k: int, prices: List[int]) -> int:
    #     pl = 0
    #     is_buy = True
    #     i = 0
    #     n = len(prices)
    #     last = -1
    #     k = 2*k
    #     while i < n - 1 and k > 0:
    #         if prices[i] > prices[i+1]:
    #             if not is_buy:
    #                 pl += prices[i]
    #                 is_buy = True
    #                 last = prices[i]
    #                 k -= 1
    #         else:
    #             if is_buy:
    #                 pl -= prices[i]
    #                 is_buy = False
    #                 last = prices[i]
    #                 k -= 1

    #         i+= 1
        
    #     if not is_buy:
    #         if k > 0 and prices[i] > last:
    #             pl += prices[i]
    #         else:
    #             pl += last
    #     return pl
    
    # Recursive approach (Top Down)
    # def maxProfit(self, k: int, prices: List[int]) -> int:
    #     memProfits = [[[None for _ in range(2)] for _ in range(k+1)] for _ in range(len(prices))]

    #     def recurSearch(currI, currK, isBuying):
    #         # print(currI, currK, isBuying, currProfit)
    #         if currI >= len(prices) or currK == 0:
    #             return 0
    #         if memProfits[currI][currK][isBuying] is not None:
    #             return memProfits[currI][currK][isBuying]
    #         stock_price = prices[currI]

    #         # Either buy or sell
    #         if isBuying:
    #             path1 = recurSearch(currI + 1, currK, False) - stock_price
    #         else:
    #             path1 = recurSearch(currI + 1, currK - 1, True) + stock_price
            
    #         # Dont do anything
    #         path2 = recurSearch(currI + 1, currK, isBuying)
            
    #         maxProfit = max(path1, path2)
    #         memProfits[currI][currK][isBuying] = maxProfit
    #         return maxProfit

    #     ans = recurSearch(0, k, True)
    #     return ans

    # Tabulation approach (Bottom Up)
    # def maxProfit(self, k: int, prices: List[int]) -> int:
    #     n = len(prices)
    #     dp = [[[0 for _ in [0, 1]] for _ in range(k+1)] for _ in range(n+1)]

    #     for day in range(n-1, -1, -1):
    #         for trans in range(1, k+1):
    #             for isBuying in [0, 1]:
    #                 stock_price = prices[day]

    #                 # Either buy or sell
    #                 if isBuying:
    #                     path1 = dp[day+1][trans][0] - stock_price
    #                 else:
    #                     path1 = dp[day+1][trans-1][1] + stock_price
                    
    #                 # Dont do anything
    #                 path2 = dp[day+1][trans][isBuying]

    #                 dp[day][trans][isBuying] = max(path1, path2)

    #     return dp[0][k][1]
    
    # Tabulation + Space complexity reduced with ahead
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        ahead = [[0 for _ in [0, 1]] for _ in range(k+1)]
        curr = [[0 for _ in [0, 1]] for _ in range(k+1)]

        for day in range(n-1, -1, -1):
            for trans in range(1, k+1):
                for isBuying in [0, 1]:
                    stock_price = prices[day]

                    # Either buy or sell
                    if isBuying:
                        path1 = ahead[trans][0] - stock_price
                    else:
                        path1 = ahead[trans-1][1] + stock_price
                    
                    # Dont do anything
                    path2 = ahead[trans][isBuying]

                    curr[trans][isBuying] = max(path1, path2)
                
            ahead = curr

        return curr[k][1]


        
# print(Solution().maxProfit(2, [2,4,1]))
print(Solution().maxProfit(2, [3,2,6,5,0,3]))
