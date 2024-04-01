# Project Overview

With little more than a few requirements and a messy data set to reference, it’s time to take a swing at this project. While Quantium has a few core tech stacks they work with on a regular basis, a small interactive visualisation like this one is perfectly suited to the Dash framework. Dash is a Python framework for developing visual tools to interrogate data. It’s easy to use, quick to develop with, and results in a pretty finished product. Before you can get to work on the application itself, set up your local development environment for working with Dash. Your local development environment can be thought of as a workbench with all the tools necessary to progress on a project. Invest an adequate amount of time setting up a good workbench and development on any project will be made far easier.

One of the best ways to manage dependencies in Python is with virtual environments. Each virtual environment contains a Python interpreter and a collection of project dependencies. They are entirely encapsulated in a single folder, and easy to work with once you get the hang of them. For this project, you will set up a Python 3.9 virtual environment. Review the resources linked below for more information.

Next, add the dash and pandas packages as dependencies to your virtual environment.

## How to Run This App

*(The following instructions apply to Posix/bash. Windows users should check [here](link_to_windows_instructions).)*

1. First, clone this repository and open a terminal inside the root folder.

2. Create and activate a new virtual environment (recommended) by running the following:
    ```bash
    python3 -m venv myvenv
    source myvenv/bin/activate
    ```

3. Install the requirements:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the app:
    ```bash
    python app.py
    ```

5. Open a browser at [http://127.0.0.1:8050](http://127.0.0.1:8050).
