# Daily resetting leverage

import matplotlib.pyplot as plt
import yfinance as yf
import statistics
import time
import numpy as np


tic = time.time()

SPX = yf.Ticker("%5EGSPC")
QQQ = yf.Ticker("QQQ")

hist = SPX.history(period="max")

startValue = 5000


value1 = startValue
value2 = startValue
value3 = startValue
invested = startValue

# Comparison
x1, y1, x2, y2, x3, y3 = [], [], [], [], [], []
# Raw values
x4, y4, x5, y5, x6, y6, x7, y7 = [], [], [], [], [], [], [], []

LastValue = 0
total = 0

print()
print("SPY - 5k lump sum + 500/month hold X number of days")
print()

# 1 year ~ 250 trading days
for days in [125, 250, 500, 750, 1000, 1500, 2500, 5000, 7500, 10000]:
    count = 0

    doubleHigher = 0
    tripleHigher = 0

    doubleHalf = 0
    tripleHalf = 0

    doubleQuarter = 0
    tripleQuarter = 0

    doubleDouble = 0
    tripleDouble = 0

    doubleQuadruple = 0
    tripleQuadruple = 0


    for i in range(len(hist) - days):
        for j in range(days):
            value = hist.Close.values[i + j]

            # DCA every month. 21 trading days = 1 month
            if j % 21 == 0:
                value1 += 500
                value2 += 500
                value3 += 500
                invested += 500

            if j > 0:
                change = value / hist.Close.values[i + j - 1]
                leveragechange = change * 2 - 1
                leveragethree = change * 3 - 2
                value1 = value1 * change
                value2 = value2 * leveragechange
                value3 = value3 * leveragethree

        # print("End values:")
        # print(f"{1}: {value1:10.0f}")
        # print(f"{2}: {value2:10.0f} Increase over 1x: {value2/value1:5.5f}")
        # print(f"{3}: {value3:10.0f} Increase over 1x: {value3/value1:5.5f}")
        # print()

        # Comparison to 1x SPY graph
        x1.append(hist.index.date[i])
        y1.append(value2/value1)
        x2.append(hist.index.date[i])
        y2.append(value3/value1)
        x3.append(hist.index.date[i])
        y3.append(1)

        # Raw value graph
        x4.append(hist.index.date[i])
        y4.append(value2)
        x5.append(hist.index.date[i])
        y5.append(value3)
        x6.append(hist.index.date[i])
        y6.append(value1)
        x7.append(hist.index.date[i])
        y7.append(invested)

        if value2 > value1:
            doubleHigher += 1
        if value3 > value1:
            tripleHigher += 1

        if value2 > 2 * value1:
            doubleDouble += 1
        if value3 > 2 * value1:
            tripleDouble += 1

        if value2 > 4 * value1:
            doubleQuadruple += 1
        if value3 > 4 * value1:
            tripleQuadruple += 1

        if value2 < 0.5 * value1:
            doubleHalf += 1
        if value3 < 0.5 * value1:
            tripleHalf += 1

        if value2 < 0.25 * value1:
            doubleQuarter += 1
        if value3 < 0.25 * value1:
            tripleQuarter += 1

        count += 1

        value1 = startValue
        value2 = startValue
        value3 = startValue
        invested = startValue


    # Numpy arrays for percentiles
    a = np.array(y1)
    b = np.array(y2)

    # Print information
    print(f"Number of trading days: {days}")
    print(f"2x end value compared to 1x: Higher than 1x: {doubleHigher / count:3.5f}. Mean 2x/1x: {statistics.mean(y1):3.5f}. Median 2x/1x: {statistics.median(y1):3.5f}. More than double: {doubleDouble / count:3.5f}. More than 4x: {doubleQuadruple / count:3.5f}. Less than half: {doubleHalf / count:3.5f}. Less than 1/4: {doubleQuarter / count:3.5f}")
    print(f"2x end value compared to 1x percentiles: 10%: {np.percentile(a, 10):.3f}. 20%: {np.percentile(a, 20):.3f}. 30%: {np.percentile(a, 30):.3f}. 40%: {np.percentile(a, 40):.3f}. 50%: {np.percentile(a, 50):.3f}. 60%: {np.percentile(a, 60):.3f}. 70%: {np.percentile(a, 70):.3f}. 80%: {np.percentile(a, 80):.3f}. 90%: {np.percentile(a, 90):.3f}. 100%: {np.percentile(a, 100):.3f}.")
    print(f"3x end value compared to 1x: Higher than 1x: {tripleHigher / count:3.5f}. Mean 3x/1x: {statistics.mean(y2):3.5f}. Median 3x/1x: {statistics.median(y2):3.5f}. More than double: {tripleDouble / count:3.5f}. More than 4x: {tripleQuadruple / count:3.5f}. Less than half: {tripleHalf / count:3.5f}. Less than 1/4: {tripleQuarter / count:3.5f}")
    print(f"3x end value compared to 1x percentiles: 10%: {np.percentile(b, 10):.3f}. 20%: {np.percentile(b, 20):.3f}. 30%: {np.percentile(b, 30):.3f}. 40%: {np.percentile(b, 40):.3f}. 50%: {np.percentile(b, 50):.3f}. 60%: {np.percentile(b, 60):.3f}. 70%: {np.percentile(b, 70):.3f}. 80%: {np.percentile(b, 80):.3f}. 90%: {np.percentile(b, 90):.3f}. 100%: {np.percentile(b, 100):.3f}.")
    print()

    # Comparison graphs
    plt.plot(x3, y3, label="1x", color='r')
    plt.plot(x1, y1, label="2x")
    plt.plot(x2, y2, label="3x")

    plt.yticks(fontsize=8)
    plt.xlabel('BuyDate')
    plt.ylabel('End value compared to holding SPY')
    plt.title(f"SPY - 5k lump sum + 500/month holding {days} days")
    plt.legend()
    filename = f"DCA{days}"
    plt.savefig(filename)
    plt.close()

    plt.plot(x3, y3, label="1x", color='r')
    plt.plot(x1, y1, label="2x")
    plt.plot(x2, y2, label="3x")

    plt.yticks(fontsize=8)
    plt.xlabel('BuyDate')
    plt.ylabel('End value compared to holding SPY')
    plt.title(f"SPY - 5k lump sum + 500/month holding {days} days - zoomed in")
    plt.legend()
    plt.ylim(0, 2)
    filename = f"DCA{days}Zoom"
    plt.savefig(filename)
    plt.close()

    # Raw value graphs

    plt.plot(x6, y6, label="1x", color='r')
    plt.plot(x4, y4, label="2x")
    plt.plot(x5, y5, label="3x")
    plt.plot(x7, y7, label="Invested")

    plt.yticks(fontsize=8)
    plt.xlabel('BuyDate')
    plt.ylabel('Raw end value')
    plt.title(f"SPY - 5k lump sum + 500/month holding {days} days - value")
    plt.legend()
    filename = f"ValueDCA{days}"
    plt.savefig(filename)
    plt.close()

    plt.plot(x6, y6, label="1x", color='r')
    plt.plot(x4, y4, label="2x")
    plt.plot(x5, y5, label="3x")
    plt.plot(x7, y7, label="Invested")

    plt.yticks(fontsize=8)
    plt.xlabel('BuyDate')
    plt.ylabel('Raw end value')
    plt.title(f"SPY - 5k lump sum + 500/month holding {days} days - value - zoomed in")
    plt.legend()
    plt.ylim(0, max(y6)*1.1)
    filename = f"ValueDCA{days}Zoom"
    plt.savefig(filename)
    plt.close()

    x1, y1, x2, y2, x3, y3 = [], [], [], [], [], []
    x4, y4, x5, y5, x6, y6, x7, y7 = [], [], [], [], [], [], [], []

toc = time.time()

print(f"Time taken: {toc - tic:.0f}")
