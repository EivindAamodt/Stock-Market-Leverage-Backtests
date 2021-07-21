# Big backtest on daily resetting leverage on the S&P 500 index

### "Leveraged ETFs Are Not a Long-Term Bet" myth

[Daily resetting ETFs are often called a poor long term investment.](https://www.investopedia.com/articles/financial-advisors/082515/why-leveraged-etfs-are-not-longterm-bet.asp) This is mainly because of volatility decay, also called beta decay. The most common example I see is that whenever the underlying index drops 10% then gains 10% the next day, a leveraged portfolio would lose a lot more value compared to the underlying.


Underlying: 100 -> 90 -> 99 - 1% loss

3x Leverage: 100 -> 70 -> 91 - 9% loss

A 9% loss is not a 3x of 1% loss!

A plot showing what it means in practice:

![Volatility decay](volatility_decay.png)

What is often forgotten, is that the daily resetting also helps and serves as protection in some cases. Let's take an example where the underlying drops 10% four days in a row:

Underlying: 100 -> 90 -> 81 -> 73 -> 65 - 35% loss

3x Leverage: 100 -> 70 -> 49 -> 35 -> 24 - 76% loss

A 76% loss is a lot less than 3x of 35% loss. If it did not reset daily, the leveraged portfolio would be wiped out as 35*3 = 105% loss!

The same is also true when the underlying increases multiple days in a row:

Underlying: 100 -> 110 -> 121 -> 133 -> 146 - 46% gain

3x Leverage: 100 -> 130 -> 169 -> 220 -> 286 - 186% gain

A 186% gain is a lot better than the expected 46*3 = 138% gain.

## Backtests

### 5k lump sum + 500/month DCA:

###¤ Lots of data - mean, median, percentiles, probabilities etc:
250 trading days = 1 year

![DCA](Logs%20output/DCA.png)


#### Plots 

| End value compared to SPY  |  Raw end values   |
:-------------------------:|:-------------------------:
|![DCA125](DCA/DCA125.png)  |  ![ValueDCA125](ValueDCA/ValueDCA125.png)|
|![DCA250](DCA/DCA250.png)  |  ![ValueDCA250](ValueDCA/ValueDCA250.png)|
|![DCA500](DCA/DCA500.png)  |  ![ValueDCA500](ValueDCA/ValueDCA500.png)|
|![DCA750](DCA/DCA750.png)  |  ![ValueDCA750](ValueDCA/ValueDCA750.png)|
|![DCA1000](DCA/DCA1000.png)  |  ![ValueDCA1000](ValueDCA/ValueDCA1000.png)|
|![DCA1500](DCA/DCA1500.png)  |  ![ValueDCA1500](ValueDCA/ValueDCA1500.png)|
|![DCA2500](DCA/DCA2500.png)  |  ![ValueDCA2500](ValueDCA/ValueDCA2500.png)|
|![DCA5000](DCA/DCA5000.png)  |  ![ValueDCA5000](ValueDCA/ValueDCA5000.png)|
|![DCA7500](DCA/DCA7500.png)  |  ![ValueDCA7500](ValueDCA/ValueDCA7500.png)|
|![DCA1000](DCA/DCA10000.png)  |  ![ValueDCA1000](ValueDCA/ValueDCA10000.png)|



### 10k lump sum no DCA:

#### LOTS OF NUMBERS - mean, median, percentiles, probabilities etc:

![Lumpsum](Logs%20output/LumpSum.png)

#### Plots

| End value compared to SPY  |  Raw end values   |
:-------------------------:|:-------------------------:
|![LumpSum125](LumpSum/LumpSum125.png)  |  ![ValueLumpsum125](ValueLumpsum/ValueLumpsum125.png)|
|![LumpSum250](LumpSum/LumpSum250.png)  |  ![ValueLumpsum250](ValueLumpsum/ValueLumpsum250.png)|
|![LumpSum500](LumpSum/LumpSum500.png)  |  ![ValueLumpsum500](ValueLumpsum/ValueLumpsum500.png)|
|![LumpSum750](LumpSum/LumpSum750.png)  |  ![ValueLumpsum750](ValueLumpsum/ValueLumpsum750.png)|
|![LumpSum1000](LumpSum/LumpSum1000.png)  |  ![ValueLumpsum1000](ValueLumpsum/ValueLumpsum1000.png)|
|![LumpSum1500](LumpSum/LumpSum1500.png)  |  ![ValueLumpsum1500](ValueLumpsum/ValueLumpsum1500.png)|
|![LumpSum2500](LumpSum/LumpSum2500.png)  |  ![ValueLumpsum2500](ValueLumpsum/ValueLumpsum2500.png)|
|![LumpSum5000](LumpSum/LumpSum5000.png)  |  ![ValueLumpsum5000](ValueLumpsum/ValueLumpsum5000.png)|
|![LumpSum7500](LumpSum/LumpSum7500.png)  |  ![ValueLumpsum7500](ValueLumpsum/ValueLumpsum7500.png)|
|![LumpSum1000](LumpSum/LumpSum10000.png)  |  ![ValueLumpsum1000](ValueLumpsum/ValueLumpsum10000.png)|