
import random
import matplotlib.pyplot as plt
import datetime

def random_numbers():
    numbers = []
    for i in range(0,500):
        num = random.uniform(-20, 20)
    numbers.append(round(num,2))
    return numbers

def mean(num):
    sum=0
    for i in num:
       sum=sum + i
    mean=sum/len(num)
    return mean

def median(num):
    num.sort()
    n=len(num)
    if n%2==1:
        index=(n//2)
        median=num[index]
    else:
        median_index=n//2
        median=(num[index]+num[(index-1)])/2
    return median 

def get_standard_deviation(num):
    n=len(num)
    m=mean
    van=0 
    for i in num:
        van=int(int(i)-mean)**2
        standard_deviation=(van/n)**0.5
        return standard_deviation
        

def plot_histogram(list, num_bins=10):
  
     plt.hist(list, bins=num_bins)
     plt.xlabel("Value")
     plt.ylabel("Frequency")
     plt.title(f"Date: {datetime.datetime.today()}\nHistogram of Random Numbers")
     plt.show()
    


list = random_numbers()

mean=mean(list)
print("your mean is:",(mean))

median=median(list)
print("your median is:",(median))

standard_deviation=get_standard_deviation(list)
print("your standard deviation is:",(standard_deviation))

plot_histogram(list)