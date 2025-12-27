import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Data from the dataset
labels = ['Services', 'Government', 'Telecom', 'Universities', 'Industrial', 
          'Energy', 'Pharmaceutical', 'Transportation', 'Other', 'Healthy', 'Finance_Insurance']
values = [9, 12, 1, 2, 3, 3, 1, 1, 7, 1, 8]
colors = plt.cm.tab20(np.linspace(0, 1, len(labels)))  # Distinct colors for each sector

# Create a figure and 3D axis
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Create the pie chart
ax.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, 
       wedgeprops=dict(width=0.3, edgecolor='w'))  # Width controls the 3D depth

# Set title
plt.title('3D Pie Chart of Sector Distribution')

# Display the chart
plt.show()