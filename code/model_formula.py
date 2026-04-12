import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('../data/model_data.csv')

# Extract parameters
R = data['R_avg']
gap = data['gap']
width = data['width']
thickness = data['thickness']
f_actual = data['frequency']

# Your formula
f_pred = 64.28 * (R ** -1.17) * (gap ** 0.025) * (width ** 0.05) * (thickness ** 0.001)

# Add predictions to dataframe
data['f_predicted'] = f_pred

# Error calculation
data['error (%)'] = abs((f_actual - f_pred) / f_actual) * 100

# Print results
print("\n--- Model Performance ---")
print(data[['frequency', 'f_predicted', 'error (%)']])

print("\nAverage Error (%): ", data['error (%)'].mean())

# Plot comparison
plt.figure()
plt.plot(f_actual.values, label='CST (Actual)', marker='o')
plt.plot(f_pred.values, label='Model (Predicted)', marker='x')
plt.xlabel('Sample Index')
plt.ylabel('Frequency (GHz)')
plt.title('CST vs Model Prediction')
plt.legend()
plt.grid()

# Save plot
plt.savefig('../figures/model_vs_cst.png')

plt.show()
