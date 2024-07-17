#Using Scatter plot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'uber-raw-data-sep14.csv'
data = pd.read_csv(file_path)

# Convert the Date/Time column to datetime
data['Date/Time'] = pd.to_datetime(data['Date/Time'], format='%m/%d/%Y %H:%M:%S')

# Sort the data by base and Date/Time
data = data.sort_values(by=['Base', 'Date/Time'])

# Calculate the time difference between consecutive pickups
data['Time_Diff'] = data.groupby('Base')['Date/Time'].diff().dt.total_seconds().dropna()

# Filter out extremely large time differences to focus on more common intervals
data = data[data['Time_Diff'] < 3600]  # Only consider differences less than an hour

# Set the style
sns.set(style="whitegrid")

# Plot the distribution of time differences using a scatter plot
plt.figure(figsize=(12, 6))
sns.scatterplot(x=data.index, y='Time_Diff', data=data, color='blue', alpha=0.5)
plt.title('Distribution of Time Differences Between Consecutive Pickups', fontsize=16)
plt.xlabel('Index', fontsize=14)
plt.ylabel('Time Difference (seconds)', fontsize=14)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Add informative text annotations
plt.text(0.5, 0.95, 'Time Differences less than 1 hour', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

plt.tight_layout()
plt.show()
