import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('weight-height.csv')

# Extract lengths (in inches) and weights (in pounds)
length_inches = data['Height']
weight_pounds = data['Weight']

# Convert lengths from inches to centimeters (1 inch = 2.54 cm)
length_cm = length_inches * 2.54

# Convert weights from pounds to kilograms (1 pound = 0.453592 kg)
weight_kg = weight_pounds * 0.453592

# Calculate means of lengths and weights
mean_length_cm = length_cm.mean()
mean_weight_kg = weight_kg.mean()

# Print means
print("Mean Length (cm):", mean_length_cm)
print("Mean Weight (kg):", mean_weight_kg)

# Draw a histogram of lengths
plt.hist(length_cm, bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Lengths (cm)')
plt.xlabel('Length (cm)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
