import pandas as pd
import matplotlib.pyplot as plt

data_dict = {
    'Cause': ['Alzheimers', 'Chronic Respiratory Disease', 'Diabetes', 'Heart Disease', 'Influenza/Pneumonia', 'Malignant Neoplasms', 'Accidents', 'Nephritis/Nephrosis', 'Septicemia', 'Stroke'],
    'Num': [7.2, 12.5, 7.2, 63.2, 5.6, 56.0, 12.2, 4.5, 3.4, 13.7]
}

df = pd.DataFrame(data_dict)
total = df['Num'].sum()
df['Cumulative_Percentage'] = df['Num'].cumsum() / total * 100

fig, ax1 = plt.subplots()
ax1.bar(df['Cause'], df['Num'], color='blue')
ax1.set_ylabel('Num (x 10,000)', color='blue')

ax2 = ax1.twinx()
ax2.plot(df['Cause'], df['Cumulative_Percentage'], color='red', marker='D')
ax2.set_ylabel('Cumulative_Percentage (%)', color='red')

plt.title('Pareto Chart:deaths due to diseases in year 2006 in US ')
ax1.set_xticklabels(df['Cause'], rotation=60)
plt.show()
