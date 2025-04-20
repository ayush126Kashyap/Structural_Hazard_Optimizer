# Structural Hazard Detection and ALU Simulation

This repository contains a Python-based simulation for detecting and avoiding structural hazards in a pipelined CPU architecture. The project implements a predictive logic approach to dynamically manage hardware resources, reduce pipeline stalls, and improve CPU throughput. It also provides visualization of hazard detection and ALU update patterns over time.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Architecture and Algorithm](#architecture-and-algorithm)  
4. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Create and Activate Virtual Environment (optional but recommended)](#create-and-activate-virtual-environment-optional-but-recommended)  
   - [Install Dependencies](#install-dependencies)  
5. [Usage](#usage)  
   - [Running the Simulation](#running-the-simulation)  
   - [Interactive Input Format](#interactive-input-format)  
   - [Sample Run](#sample-run)  
6. [Code Structure](#code-structure)  
7. [Results and Analysis](#results-and-analysis)  
8. [Contributing](#contributing)  
9. [License](#license)  
10. [Authors]

---

## Project Overview

In modern pipelined processors, structural hazards occur when multiple instructions compete for the same hardware resource, causing stalls and degrading performance. This simulation demonstrates a real-time, predictive logic-based mechanism to:

- Detect structural hazards by analyzing time differences between instruction issue events.  
- Dynamically manage ALU resource allocation to prevent conflicts.  
- Visualize ALU engagement, idling, and hazard occurrences over time.  

The approach achieves a reduction in pipeline stalls (~27.7%) and throughput improvement (~24.5%) over traditional static scheduling methods, as validated in the accompanying report.

---

## Features

- **Predictive Hazard Detection**: Computes time differences (`dtspex`) between instruction timestamps to identify imminent resource conflicts.  
- **Dynamic ALU Updates**: Adjusts two ALU channels (`alu_update` and `alu_update1`) to stall or engage operations based on hazard conditions.  
- **Interactive CLI**: Users enter instructions (`ADD`, `SUB`, `MUL`, `DIV`) with two operands; the system processes until the `done` command.  
- **Real-Time Plots**: Generates time-series plots of ALU updates and hazard flags using Matplotlib.  
- **Extensible Design**: Easily configurable thresholds and resource-mapping logic for further experimentation.

---

## Architecture and Algorithm

1. **Instruction Fetch & Timestamping**  
   Each instruction input is timestamped relative to the simulation start.

2. **Operation Execution**  
   Supports `ADD`, `SUB`, `MUL`, `DIV`, updating an accumulator and storing results in `lis_value`.

3. **Hazard Detection**  
   - Compute `dtspex[i] = tspex[i+1] - tspex[i]` for all consecutive timestamps.  
   - Flag a structural hazard if `dtspex[i+1] <= THRESHOLD` (default `3` time units).

4. **Preventive Actions**  
   - Insert idle cycles (stalls) into `alu_update` lists when hazards are predicted.  
   - Propagate adjustments to the secondary ALU channel as needed.

5. **Visualization**  
   Pad all series to the same length and plot:  
   - ALU engagement (`1`), idling (`0`), and unused (`-1`).  
   - Hazard flags (`1` for hazard, `0` for safe).

---

## Getting Started

### Prerequisites

- Python 3.7 or higher  
- pip (Python package manager)

### Create and Activate Virtual Environment (optional but recommended)

bash
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
### Install Dependencies
pip install -r requirements.txt
matplotlib

## Usage
#### Running the Simulation
     python structural_hazard_sim.py
Interactive Input Format
Instruction format: OPERATION RS RT

OPERATION: ADD, SUB, MUL, or DIV

RS, RT: Integer operands

Exit simulation: Enter done as the instruction

## Sample Run
Instruction: ADD 5 3
The values of accumulator:
8
Time Specification (tspex):
0.00
...
Structural Hazards Detected (shaz):
0
ALU Update:
1
Other ALU Update:
-1

Instruction: MUL 2 10
...
Instruction: done

## Code Structure
├── structural_hazard_sim.py    # Main simulation and plotting logic
├── requirements.txt            # Python dependencies
├── README.md                   # This document
└── final_report.pdf            # Detailed project report and results (CAO)
structural_hazard_sim.py defines functions:

instruction_value(op, rs, rt): Executes ALU ops and records results.

struct_hazard(): Computes dtspex, detects hazards, updates ALU lists.

printing(): Prints current values and hazard info.

plot_graphs(): Pads sequences and plots time-series data.

main(): Orchestrates user input loop and final plotting.

## Results and Analysis
Refer to the final_report.pdf for detailed evaluation:

Pipeline Stall Reduction: 27.67% fewer stalls compared to static scheduling.

Throughput Improvement: 24.5% increase in overall CPU throughput.

Simulation Efficiency: Achieved 80% active processing time vs. 60% baseline.

Graphs generated by the simulation illustrate ALU engagement patterns and hazard occurrences over time.

## Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create a new branch: git checkout -b feature/my-feature

Make your changes and add tests where applicable

Commit and push: git push origin feature/my-feature

Open a pull request describing your changes

Please adhere to the existing code style and document new functionality.

## License
This project is licensed under the MIT License.

## Authors
Vedant Singh — vedant.singh2023a@vitstudent.ac.in

Rajwant — rajwant.sarma2023@vitstudent.ac.in

Ayush Kashyap — ayush.kashyap2023@vitstudent.ac.in





