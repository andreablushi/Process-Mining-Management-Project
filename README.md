# Recommendation System for Process Monitoring

Implementation of **predictive process monitoring** and **prescriptive recommendations** using Decision Trees with boolean encoding.

The project was developed as part of the course "Process Mining and Management", held by Prof. Chiara Di Francescomarino at the University of Trento, within the Master's Degree in Computer Science.

[View Full Report (PDF)](docs/report.pdf)

## Table of Contents

* [1. Repository Contents](#1-repository-contents)
* [2. Installation and Setup](#2-installation-and-setup)

## 1. Repository Contents

- **src/**: Source code modules
   - **utils.py**: Core utilities (log processing, encoding, hyperparameter optimization)
   - **plotting.py**: Visualization functions (decision trees, confusion matrices, metrics)
- **logs/**: Compressed event log files (XES format)
- **docs/**: Documentation and outputs
- **app.log**: Application log file
- **notebook.ipynb**: Main Jupyter Notebook for experiments
- **requirements.txt**: Python dependencies

## 2. Installation and Setup

To install and set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/andreablushi/Recommendation-System
   cd Recommendation-System
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Extract the event logs in the `logs/` directory:
   ```bash
      unzip 'logs/*.zip' -d logs/
   ```

5. Run the Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

6. Open `notebook.ipynb` in your browser to start working with the project.