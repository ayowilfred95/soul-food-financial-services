# Project Overview

The objective of this project is to develop an interactive visualization tool using the Dash framework for analyzing transaction data provided by Soul Foods. The main focus is to explore sales trends, particularly before and after a price increase on January 15, 2021, for Pink Morsels.

## Introduction

Effective data processing is essential for converting raw data into actionable insights. Soul Foods has supplied three CSV files containing transaction data for their morsel line. The task involves processing this data to extract pertinent information and presenting it visually.

## Data Processing

- Eliminate rows containing products other than Pink Morsels.
- Merge "quantity" and "price" columns into a unified "sales" field.
- Preserve the "date" and "region" fields.

## Setup

To initialize the development environment:

1. Clone this repository and navigate to the root directory.
2. Create and activate a new Python 3.9 virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

*(These instructions are for Posix/bash. Windows users should refer to [Windows instructions](link_to_windows_instructions).)*

1. Clone this repository and open a terminal within the root directory.
2. Optionally, create and activate a new virtual environment for isolation:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Launch the application:
    ```bash
    python app.py
    ```
5. Open a web browser and visit [http://127.0.0.1:8050](http://127.0.0.1:8050).
6. To deactivate the virtual environment when finished:
    ```bash
    deactivate
    ```

## Resources

- [Dash Documentation](https://dash.plotly.com/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

## Visual display
![Screenshot](screenshots/screenshot.png)
