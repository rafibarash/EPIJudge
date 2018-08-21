from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    myMax, buy = 0, float('inf')
    for p in prices:
        diff = p - buy
        myMax = max(myMax, diff)
        buy = min(buy, p)
    return myMax


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
