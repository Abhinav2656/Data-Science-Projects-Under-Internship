import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
file_path = 'uber-raw-data-sep14.csv'
data = pd.read_csv(file_path)

# Convert the Date/Time column to datetime with a specified format
data['Date/Time'] = pd.to_datetime(data['Date/Time'], format='%m/%d/%Y %H:%M:%S')

# Extract the hour from the Date/Time column
data['Hour'] = data['Date/Time'].dt.hour

# Group by hour and count the number of rides for each hour
rides_per_hour = data.groupby('Hour').size()

# Set the style
sns.set(style="whitegrid")

# Plot the number of rides per hour
plt.figure(figsize=(12, 6))
sns.lineplot(x=rides_per_hour.index, y=rides_per_hour.values, marker='o', linestyle='-')
plt.title('Number of Uber Rides per Hour in September 2014', fontsize=16)
plt.xlabel('Hour of the Day', fontsize=14)
plt.ylabel('Number of Rides', fontsize=14)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.xticks(np.arange(0, 24, 1))
plt.tight_layout()
plt.show()
