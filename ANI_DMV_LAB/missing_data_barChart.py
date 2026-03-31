import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("Anagrams.csv")

# Extract columns
categories = data["Category"]
values = data["Value"]

# Create bar chart
plt.bar(categories, values)

# Add labels and title
plt.xlabel("Category")
plt.ylabel("Value")
plt.title("Bar Chart from CSV Data")

# Show the chart
plt.show()