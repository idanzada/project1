# drowning_detection_algorithm.py

import math

def calculate_optimal_throwing_point(person_location, wind_speed, wave_height, environmental_factors):
    """
    Calculate the optimal throwing point for a life jacket based on the person's location and environmental factors.

    Parameters:
    - person_location (tuple): A tuple (x, y) representing the person's current location in the water.
    - wind_speed (float): The speed of the wind in meters per second.
    - wave_height (float): The height of the waves in meters.
    - environmental_factors (dict): A dictionary containing other environmental factors such as current speed and direction.

    Returns:
    - throwing_point (tuple): A tuple (x, y) representing the optimal point to throw the life jacket.
    """

    # Extract environmental factors
    current_speed = environmental_factors.get('current_speed', 0)
    current_direction = environmental_factors.get('current_direction', 0)

    # Calculate the effect of wind on the throwing point
    wind_effect_x = wind_speed * math.cos(math.radians(current_direction))
    wind_effect_y = wind_speed * math.sin(math.radians(current_direction))

    # Calculate the effect of waves on the throwing point
    wave_effect_x = wave_height * 0.1  # Arbitrary factor for wave effect
    wave_effect_y = wave_height * 0.1

    # Calculate the effect of current on the throwing point
    current_effect_x = current_speed * math.cos(math.radians(current_direction))
    current_effect_y = current_speed * math.sin(math.radians(current_direction))

    # Calculate the optimal throwing point by adjusting the person's location
    throwing_point_x = person_location[0] + wind_effect_x + wave_effect_x + current_effect_x
    throwing_point_y = person_location[1] + wind_effect_y + wave_effect_y + current_effect_y

    throwing_point = (throwing_point_x, throwing_point_y)

    return throwing_point

# Example usage
if __name__ == "__main__":
    person_location = (100, 200)  # Example coordinates
    wind_speed = 5.0  # m/s
    wave_height = 1.5  # meters
    environmental_factors = {
        'current_speed': 2.0,  # m/s
        'current_direction': 45  # degrees
    }

    optimal_point = calculate_optimal_throwing_point(person_location, wind_speed, wave_height, environmental_factors)
    print(f"Optimal Throwing Point: {optimal_point}")
