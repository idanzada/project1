# environmental_factors.py

import math
import datetime

def simulate_wind_speed():
    """
    Simulate wind speed in meters per second.
    
    Returns:
    - wind_speed (float): Simulated wind speed.
    """
    # For simplicity, use a random value or a fixed pattern for wind speed
    # In a real scenario, this could be based on historical data or a complex model
    # Example fixed wind speed; in a real scenario, this could vary
    wind_speed = 5.0
    return wind_speed

def simulate_wave_height():
    """
    Simulate wave height in meters.
    
    Returns:
    - wave_height (float): Simulated wave height.
    """
    # For simplicity, use a random value or a fixed pattern for wave height
    # Example fixed wave height; in a real scenario, this could vary
    wave_height = 1.5
    return wave_height

def simulate_day_night_cycle():
    """
    Determine if it is day or night based on the current time.
    
    Returns:
    - is_day (bool): True if it is day, False if it is night.
    """
    current_hour = datetime.datetime.now().hour
    # Assume day is from 6 AM to 6 PM
    is_day = 6 <= current_hour < 18
    # This could be adjusted for different seasons or locations
    return is_day

def simulate_environmental_factors():
    """
    Simulate all environmental factors affecting the marine environment.
    
    Returns:
    - environmental_factors (dict): A dictionary containing wind speed, wave height, and day/night status.
    """
    wind_speed = simulate_wind_speed()
    wave_height = simulate_wave_height()
    is_day = simulate_day_night_cycle()
    
    environmental_factors = {
        'wind_speed': wind_speed,
        'wave_height': wave_height,
        'is_day': is_day
    }
    
    return environmental_factors
    # This function aggregates all environmental factors into a single dictionary

# Example usage
if __name__ == "__main__":
    factors = simulate_environmental_factors()
    print(f"Environmental Factors: {factors}")