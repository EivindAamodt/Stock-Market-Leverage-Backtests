import matplotlib.pyplot as plt
import yfinance as yf

SPX = yf.Ticker("%5EGSPC")

SPX.info

hist = SPX.history(period="max")




plus1 = 101 / 100
minus1 = 100/101

pluss2 = plus1 * 2 - 1
minus2 = minus1*2-1

pluss3 = plus1 * 3 - 2
minus3 = minus1*3-2

startvalue = 100000

value1 = startvalue
value2 = startvalue
value3 = startvalue


x1 = []
y1 = []

x2 = []
y2 = []

x3 = []
y3 = []

pluss = False
teller = 0

for i in range(250):
    if pluss:
        value1 = value1 * plus1
        value2 = value2 * pluss2
        value3 = value3 * pluss3

        x1.append(i)
        y1.append(value1)
        x2.append(i)
        y2.append(value2)
        x3.append(i)
        y3.append(value3)
        teller = teller +1
        pluss = False
    else:
        value1 = value1 * minus1
        value2 = value2 * minus2
        value3 = value3 * minus3

        x1.append(i)
        y1.append(value1)
        x2.append(i)
        y2.append(value2)
        x3.append(i)
        y3.append(value3)
        teller = teller + 1
        pluss = True


plt.plot(x1, y1, label="1x")
plt.plot(x2, y2, label="2x")
plt.plot(x3, y3, label="3x")

plt.grid(axis='y')
plt.yticks(fontsize=8)
plt.ylim(min(y3)*0.9, max(y3)*1.1)
plt.xlabel('Day')
plt.ylabel('Value')
plt.title('Volatility decay simulation')
plt.legend()
plt.show()
