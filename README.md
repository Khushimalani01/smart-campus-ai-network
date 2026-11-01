# AI-Driven Intelligent Network for Smart Campus Applications

## Presented By:
1. Khushi Malani - KU2407U464
2. Krishna Shah - KU2407U703
3. Nirali Kodavala - KU2407U150
4. Mansoor Anas - KU2407U696

## Project Overview

This project explores how Artificial Intelligence and Machine Learning can help improve network monitoring and bandwidth planning in a smart campus environment.

The project consists of two separate prototypes:

1. **Cisco Packet Tracer Simulation:** A basic campus network designed using routers, switches, PCs, laptops, wireless access points, and servers.
2. **Python-Based AI/ML Prototype:** Uses simulated hourly campus network traffic to predict bandwidth usage and detect unusual traffic patterns.

**Note:** The Packet Tracer simulation and Python ML prototype are separate demonstrations. The ML model is not connected to a live campus network or the Packet Tracer topology.

## Objectives

- Design and simulate a basic smart campus network.
- Generate sample campus network traffic data.
- Predict bandwidth usage using Machine Learning.
- Compare different bandwidth prediction models.
- Detect unusual traffic patterns using anomaly detection.
- Explore how AI-based predictions can support network administrators.

## Technologies Used

**Network Simulation**
- Cisco Packet Tracer
- Routers and switches
- PCs, laptops, wireless access points and servers
- IPv4 addressing

**AI/ML Implementation**
- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

## Machine Learning Algorithms

| Algorithm | Purpose |
|---|---|
| Naive Previous-Day Baseline | Provides a basic reference for bandwidth prediction |
| Linear Regression | Predicts bandwidth usage using traffic-related features |
| Random Forest Regressor | Predicts bandwidth using multiple decision trees |
| Isolation Forest | Detects unusual network traffic patterns |

## Project Structure

```text
AI-Driven-Intelligent-Network/
│
├── smart_campus_ai.py
├── README.md
└── results/
    ├── model_comparison.csv
    ├── anomaly_metrics.csv
    ├── test_predictions.csv
    ├── actual_vs_predicted.png
    ├── feature_importance.png
    └── anomaly_detection.png
```

The `results` folder is generated automatically after successfully executing the Python code.

## How to Run the Project

### Using Google Colab

1. Open [Google Colab](https://colab.research.google.com/).
2. Create a new notebook.
3. Install the required libraries:

```python
!pip install numpy pandas matplotlib scikit-learn
```

4. Copy the complete Python code from `smart_campus_ai.py` into a code cell.
5. Execute the cell and wait for the program to finish.
6. The program generates a `results` folder containing evaluation files and graphs.

### Running Locally

Install Python and execute the following command in the terminal:

```bash
pip install numpy pandas matplotlib scikit-learn
```

Run the Python script:

```bash
python smart_campus_ai.py
```

The generated output files will be available in the `results` folder.

## Generated Outputs

| Output File | Description |
|---|---|
| model_comparison.csv | Comparison of bandwidth prediction models |
| anomaly_metrics.csv | Anomaly detection evaluation metrics |
| test_predictions.csv | Actual and predicted bandwidth values |
| actual_vs_predicted.png | Graph comparing actual and predicted bandwidth |
| feature_importance.png | Random Forest feature importance graph |
| anomaly_detection.png | Visualization of detected traffic anomalies |

The actual evaluation metrics and graphs are generated when the Python script is executed.

## Cisco Packet Tracer Simulation

The network simulation represents a basic smart campus environment containing routers, switches, end devices, wireless connectivity and servers.

Static IP addresses, subnet masks, default gateways and DNS settings are configured for network communication.

Connectivity can be tested using the Command Prompt on a PC:

```bash
ping 192.168.50.10
```

A successful ping response indicates connectivity between the tested devices.

## Limitations

- The network traffic dataset is simulated and not collected from a real campus network.
- The Packet Tracer simulation and Python ML implementation are separate prototypes.
- The project does not perform live network monitoring.
- The ML model does not automatically configure QoS policies.
- The system is an academic prototype and is not intended for production deployment.

## Future Scope

- Integrating real-time network traffic monitoring.
- Collecting real-world campus network traffic data.
- Developing a web-based monitoring dashboard.
- Implementing automated QoS recommendations.
- Exploring SDN-based network management.
- Improving prediction accuracy using larger datasets and advanced ML models.

## Conclusion

The project demonstrates how Machine Learning techniques can be applied to simulated campus network traffic for bandwidth prediction and anomaly detection. The Cisco Packet Tracer simulation provides a basic campus network design, while the Python prototype demonstrates the potential of AI-driven network analysis.

Together, these implementations provide an educational foundation for exploring intelligent network management in smart campus environments.

## Contributors

1. Khushi Malani - KU2407U464
2. Krishna Shah - KU2407U703
3. Nirali Kodavala - KU2407U150
4. Mansoor Anas - KU2407U696

## Academic Note

This project is developed for educational purposes as a Computer Networks mini project.
