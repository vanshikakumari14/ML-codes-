# -*- coding: utf-8 -*-
"""ttest on random dataset

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X7YQuFzzKIKu5S8M9To1euZwL-HgZ__8
"""

import numpy as np
from scipy.stats import ttest_ind

#Creating sample datasets
data1 = np.array([23, 25, 29, 31, 35, 36, 40, 42, 44, 48])
data2 = np.array([18, 20, 24, 26, 30, 32, 34, 38, 40, 42])

#Perform the t-test
t_statistic, p_value = ttest_ind(data1, data2)

print("T-statistic:", t_statistic)
print("P-value:", p_value)

if p_value < 0.05:
    print("Reject null hypothesis: The means are different.")
else:
    print("Fail to reject null hypothesis: The means are not significantly different.")

import matplotlib.pyplot as plt
plt.boxplot([data1, data2], labels=['Data 1', 'Data 2'])          # Create  box plot
plt.title('Box Plot of Sample Datasets')
plt.ylabel('Values')
plt.xlabel('Groups')


plt.text(3, 30, f'T-statistic: {t_statistic:.2f}\nP-value: {p_value:.4f}', bbox=dict(facecolor='pink', alpha=0.6))

plt.show()