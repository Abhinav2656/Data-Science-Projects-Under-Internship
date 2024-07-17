import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'uber-raw-data-sep14.csv'
data = pd.read_csv(file_path)

# Convert the Date/Time column to datetime
data['Date/Time'] = pd.to_datetime(data['Date/Time'], format='%m/%d/%Y %H:%M:%S')

# Set the style
sns.set(style="white")

# Plot the scatter plot
plt.figure(figsize=(10, 10))

# Use hexbin to show density of points
hb = plt.hexbin(data['Lon'], data['Lat'], gridsize=100, cmap='Blues', mincnt=1)

# Add a color bar
cb = plt.colorbar(hb, shrink=0.5, aspect=5)
cb.set_label('Number of Pickups')

# Set titles and labels
plt.title('Uber Pickups in September 2014', fontsize=16)
plt.xlabel('Longitude', fontsize=14)
plt.ylabel('Latitude', fontsize=14)

# Add a grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Set axis limits for a closer view of NYC
plt.xlim(-74.05, -73.75)
plt.ylim(40.60, 40.90)

# Add annotations for well-known areas
plt.annotate('Manhattan', xy=(-73.98, 40.75), xytext=(-74.00, 40.85),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, ha='center')

plt.annotate('Brooklyn', xy=(-73.95, 40.65), xytext=(-73.85, 40.70),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, ha='center')

plt.annotate('Queens', xy=(-73.85, 40.75), xytext=(-73.80, 40.80),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, ha='center')

# Show plot
plt.tight_layout()
plt.show()
