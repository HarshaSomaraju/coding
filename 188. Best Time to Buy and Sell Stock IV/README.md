# 188. Best Time to Buy and Sell Stock IV

This problem is about finding the maximum profit you can make by buying and selling a stock.
You are given an array of stock prices and a number `k`.
`k` is the maximum number of transactions you can complete.
A transaction means buying one stock and then selling it.
You can't do multiple transactions at the same time. You must sell the stock before buying again.
The goal is to find the highest profit possible with at most `k` transactions.

## Approaches

# Greedy approach
Buy small and sell next big value. It does not work for all the test cases

# Recursive approach (Top Down)
At any point we can either buy/sell or do nothing. So based on this we can do recursion.
If today we are buying, then the profitLoss will be substracted by today stock price. 
Then we can calculated the max profitloss from next day onwards starting with a sell.

Similarly we can do selling.

We compare this with max profitLoss if we not do anything.

We can save this using memoization (storing intermediate results in memory so it can be used in repeatable steps)

# Tabulation (Bottom Up)
Now that we have recursive approach, we can switch it to bottom up approach by just going from last day to first day
Instead of recursive call, we directly used the memoized array which we use as `dp` variable

# Tabulation with Ahead for space optimization
In the loop, we only use the n+1 array values each time, so we can just store `ahead` and `curr` 2D arrays instead