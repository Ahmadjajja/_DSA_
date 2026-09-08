# class StockSpanner:
#     def __init__(self):
#         self.stockPrices = []
#         self.output = []

#     def next(self, price: int) -> int:
#         curSpan = 1
#         i = len(self.stockPrices) - 1
#         while i >= 0 and self.stockPrices[i] <= price:
#             curSpan += self.output[i]
#             i = i - self.output[i]
#         self.stockPrices.append(price)
#         self.output.append(curSpan)
#         return curSpan

class StockSpanner:

    def __init__(self):
        self.stack = []  # pair: (price, span)

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span
    # [7, 3, 2, 1, 2], 5
    # [1, 1, 1, 1, 3], 3 + 1 = 4

    # 1 + 3 + 1

    # 5 - 2 = 3 values (3, 4, 5)

    # [7, 34, 1, 2], 8







