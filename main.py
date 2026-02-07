# Project: Simulated Drone Flight Data Analysis
# Author: [Y K MADHAVA SAI]
# Purpose: To visualize the correlation between Drone Altitude and Battery Usage

import pandas as pd
import matplotlib.pyplot as plt

# 1. Creating Dummy Drone Data (Simulating a Flight Log)
data = {
    'Time_Seconds': [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    'Altitude_Meters': [0, 5, 15, 30, 50, 80, 120, 100, 60, 20, 0],
    'Battery_Percent': [100, 98, 95, 91, 88, 82, 75, 70, 65, 62, 60],
    'Speed_KmH': [0, 5, 10, 12, 15, 18, 20, 15, 10, 5, 0]
}

# 2. Converting to a Table (DataFrame)
df = pd.DataFrame(data)

# 3. Display the Data
print("--- UAV FLIGHT TELEMETRY DATA ---")
print(df)

# 4. Visualization (Plotting the Graphs)
plt.figure(figsize=(10, 5))

# Graph 1: Altitude vs Time
plt.plot(df['Time_Seconds'], df['Altitude_Meters'], marker='o', color='blue', label='Altitude (m)')

# Graph 2: Battery vs Time (Secondary Axis)
plt.plot(df['Time_Seconds'], df['Battery_Percent'], marker='x', color='red', linestyle='--', label='Battery (%)')

plt.title('Drone Flight Analysis: Altitude vs Battery Drain')
plt.xlabel('Time (Seconds)')
plt.ylabel('Values')
plt.legend()
plt.grid(True)

# Show the Graph
plt.show()
