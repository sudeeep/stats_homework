import numpy as np
import datetime


def calculate_mode(arr):
    values, counts = np.unique(arr, return_counts=True)
    max_count = np.max(counts)
    mode_values = values[counts == max_count]
    return mode_values

data = [
    11, 14, 15, 15, 16, 16, 17, 18, 19, 21, 25, 36,
    12, 14, 15, 15, 16, 16, 17, 18, 19, 21, 25, 39,
    13, 14, 15, 15, 16, 17, 17, 18, 20, 22, 26, 43,
    13, 14, 15, 15, 16, 17, 17, 18, 20, 22, 26, 46,
    13, 14, 15, 16, 16, 17, 17, 18, 20, 22, 27, 50,
    13, 14, 15, 16, 16, 17, 17, 19, 20, 23, 27, 54,
    13, 14, 15, 16, 16, 17, 18, 19, 20, 23, 29, 59,
    13, 15, 15, 16, 16, 17, 18, 19, 20, 23, 30, 67,
    14, 15, 15, 16, 16, 17, 18, 19, 21, 24, 31,
    14, 15, 15, 16, 16, 17, 18, 19, 21, 24, 34
]


median = np.median(data)


mode = calculate_mode(data)

q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)

p10 = np.percentile(data, 10)
p95 = np.percentile(data, 95)

print(f"Date: {datetime.datetime.today()}")
print("Median:", median)
print("Mode:", mode)
print("Q1 (25th percentile):", q1)
print("Q3 (75th percentile):", q3)
print("P10 (10th percentile):", p10)
print("P95 (95th percentile):", p95)
