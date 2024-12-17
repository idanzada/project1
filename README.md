# project1

## Drowning Detection System

### Project Overview

The Drowning Detection System aims to develop a system capable of locating a drowning person and calculating the optimal point to deploy a life jacket. The system is designed to be completely autonomous and considers various environmental factors such as wind, waves, and current.

### Technologies Researched

- **Sonar Sensors**: Effective in low visibility conditions but limited to underwater detection.
- **Infrared Sensors**: Useful in low light or nighttime conditions but have limited range.
- **Thermal Cameras**: Effective in darkness and fog but expensive.
- **Optical Cameras**: High resolution but ineffective in low visibility conditions.
- **Machine Learning Models**: CNNs and RNNs for image recognition and sequence prediction.

### Running the Simulation Prototype

To run the simulation prototype, follow these steps:

1. **Install Dependencies**:
   Ensure you have `matplotlib` installed for visualization.
   ```bash
   pip install matplotlib
   ```

2. **Run the Simulation**:
   Execute the `drowning_detection_simulation.py` script to visualize the detection and optimal throwing point calculation.
   ```bash
   python drowning_detection_simulation.py
   ```

### Prerequisites

- Python 3.x
- `matplotlib` library for plotting

For more detailed information on the technologies and algorithms used, refer to the `drowning_detection_research.md` and `drowning_detection_algorithm.py` files.

## Integration with robot_car_v2 Model

This project integrates with the `robot_car_v2` model to enhance its capabilities. The integration allows project1 to utilize advanced features provided by the `robot_car_v2` model.

### Setup Instructions

1. **Clone the robot_car_v2 Repository**:
   ```bash
   git clone https://github.com/idanzada/robot_car_v2.git
   ```

2. **Install Dependencies**:
   Ensure that all dependencies required by the `robot_car_v2` model are installed. You can typically find these in the `requirements.txt` file of the `robot_car_v2` repository.
   ```bash
   pip install -r robot_car_v2/requirements.txt
   ```

3. **Configuration**:
   Configure the environment to recognize and utilize the `robot_car_v2` model. This may involve setting environment variables or modifying configuration files within project1.

### Synchronization Process

The synchronization process is handled by a script named `sync_with_robot_car_v2.py` located in the project1 repository. This script fetches the model, loads it into the project1 environment, and performs any necessary preprocessing or postprocessing steps.

For more detailed instructions on running the synchronization script, refer to the comments within the `sync_with_robot_car_v2.py` file.