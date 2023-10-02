import random
import numpy as np
import matplotlib.pyplot as plt
import datetime


def calculateMean(numbers):
    total = sum(numbers)
    mean = total / len(numbers)
    return mean


def calculateMedian(numbers):
    sortedNumbers = sorted(numbers)
    n = len(numbers)
    if n % 2 == 0:
        median = (sortedNumbers[n // 2 - 1] + sortedNumbers[n // 2]) / 2
    else:
        median = sortedNumbers[n // 2]
    return median

def calculateStdDev(numbers, mean):
    n = len(numbers)
    sumOfSquaredDiff = sum((x - mean) ** 2 for x in numbers)
    stdDev = (sumOfSquaredDiff / n) ** 0.5
    return stdDev


meanValue = 10
stdDevValue = 0.5
randomNumbers = np.random.normal(meanValue, stdDevValue, 500)

meanResult = calculateMean(randomNumbers)
medianResult = calculateMedian(randomNumbers)
stdDevResult = calculateStdDev(randomNumbers, meanResult)

print("Mean:", meanResult)
print("Median:", medianResult)
print("Standard Deviation:", stdDevResult)

plt.hist(randomNumbers, bins=10, color='green', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title(f'Date: {datetime.datetime.now()}\nHistogram of 500 Random Numbers (Gaussian)')
plt.grid(True)
plt.show()
