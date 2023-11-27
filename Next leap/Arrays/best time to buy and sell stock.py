'''
Problem Description
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''


def besttime(prices):
    profit = 0
    min_buy = float('inf')
    for i in prices:
        profit = max(profit,i-min_buy)
        min_buy = min(min_buy,i)
    return profit
print("approach1:",besttime([7,1,5,3,6,4]))
print("approach1:",besttime([7,6,4,3,1]))

def approach2(prices):
    m = float('-inf')
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            m = max(m,prices[j]-prices[i])
    return m if m>0 else 0
print("approach2:",approach2([7,1,5,3,6,4]))
print("approach2:",approach2([7,6,4,3,1]))

'''
Approach1:
1.intilaize max value to a variable
2.iterate through list
3.update the profit if sub of element and min_buy is greater
4.update the min_buy if elemnt is smaller
5.repeat 2 to 4 steps till the end of list
Time complexity O(n)

Approach2:
1.intilaize min value to a variable m
2.iterate through the list till second last element
3.iterate through the list from i and till end
4.update m if sub of two elements is greater 
'''