"""
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


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""
from typing import List
from unittest import TestCase, main


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        if len(prices) < 2:
            return result
        buy_day, sell_day = 0, 1
        while buy_day < sell_day < len(prices):
            current_profit = prices[sell_day] - prices[buy_day]
            if current_profit > result:
                result = current_profit
            if prices[sell_day] < prices[buy_day]:
                buy_day = sell_day
            sell_day += 1



        return result


class PriceTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.obj = Solution()

    def test1(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(self.obj.maxProfit(prices), 5)

    def test2(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(self.obj.maxProfit(prices), 0)


if __name__ == "__main__":
    main()
