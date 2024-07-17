import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import pearsonr

# Load the dataset
file_path = 'uber-raw-data-sep14.csv'
data = pd.read_csv(file_path)

# Convert the Date/Time column to datetime
data['Date/Time'] = pd.to_datetime(data['Date/Time'], format='%m/%d/%Y %H:%M:%S')

# Extract the hour from the Date/Time column
data['Hour'] = data['Date/Time'].dt.hour

# Group by hour and count the number of rides for each hour
rides_per_hour = data.groupby('Hour').size()

# Calculate the correlation coefficient
correlation, _ = pearsonr(rides_per_hour.index, rides_per_hour.values)

# Plot the scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x=rides_per_hour.index, y=rides_per_hour.values, color='blue', alpha=0.7)
plt.title('Correlation between Time of Day and Number of Rides\nCorrelation Coefficient: {:.2f}'.format(correlation), fontsize=16)
plt.xlabel('Hour of the Day', fontsize=14)
plt.ylabel('Number of Rides', fontsize=14)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.xticks(np.arange(0, 24, 1))
plt.tight_layout()
plt.show()
