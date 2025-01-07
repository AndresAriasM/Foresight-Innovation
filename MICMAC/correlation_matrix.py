# Correlation Matrix Visualization
# ============================

"""
Creates a heatmap visualization of correlation relationships between variables.

Requirements:
------------
- pandas
- seaborn
- matplotlib

Code Implementation:
------------------
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Calculate correlation matrix
correlation_matrix = t_data.corr()

# Create heatmap
plt.figure(figsize=(18, 16))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()

"""
Quick Guide:
-----------
1. Input (t_data):
   - pandas DataFrame
   - Numerical variables only
   - Clean data (no missing values)

2. Parameters:
   - figsize: (18, 16) - adjust for your needs
   - annot=True: shows correlation values
   - cmap='coolwarm': red (positive) to blue (negative)
   - vmin=-1, vmax=1: correlation range

3. Interpretation:
   - Red: positive correlation
   - Blue: negative correlation
   - Darker colors: stronger relationships
   - Values range from -1 to 1

"""