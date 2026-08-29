class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        print(prices)
        total_money = 0
        own_stock = False
        stock_value = 0
        if len(prices) <= 1:
            return 0
        for i in range(0,len(prices)-1):
            # Do i own a stock?
            if own_stock == True:
                if prices[i+1]<prices[i]:
                    #Sell
                    total_money +=prices[i]
                    own_stock = False

            if own_stock == False:
                if prices[i+1]>prices[i]:
                    total_money -=prices[i]
                    own_stock = True
        print(total_money)


        if own_stock:
            total_money = prices[-1] + total_money
        return total_money



