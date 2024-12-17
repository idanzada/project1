# drowning_detection_simulation.py

import matplotlib.pyplot as plt
from drowning_detection_algorithm import calculate_optimal_throwing_point

def simulate_drowning_detection():
    # Mock data for simulation
    person_location = (100, 200)  # Example coordinates
    wind_speed = 5.0  # m/s
    wave_height = 1.5  # meters
    environmental_factors = {
        'current_speed': 2.0,  # m/s
        'current_direction': 45  # degrees
    }

    # Calculate the optimal throwing point
    optimal_point = calculate_optimal_throwing_point(person_location, wind_speed, wave_height, environmental_factors)

    # Visualize the simulation
    plt.figure(figsize=(8, 6))
    plt.plot(person_location[0], person_location[1], 'bo', label='Person Location')
    plt.plot(optimal_point[0], optimal_point[1], 'ro', label='Optimal Throwing Point')
    plt.arrow(person_location[0], person_location[1], 
              optimal_point[0] - person_location[0], 
              optimal_point[1] - person_location[1], 
              head_width=5, head_length=10, fc='k', ec='k', label='Throwing Direction')
    
    plt.title('Drowning Detection Simulation')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    simulate_drowning_detection()
