 # Computer Infrastructure Assignment: Automate a Python Workflow (FAANG stock data)

![FAANG finance chart](https://www.trueup.io/img/tag/faang_plus.svg)


**Author**: David Scally  
**University**: Atlantic Technological University  
**Module**: Computer Infrastructure  
**Class**: September 2025 

## Overview

The goal of the assignment is to demonstrate tools learned in the module, such as using Python tools to collect, analyse, visualise and automation of a workflow.
We will demonstrate this by looking at the well known five 'FAANG' companies hourly stock data across the most recent five-day period.


| Company        | Ticker |
|---------------|--------|
| Meta Platforms | META   |
| Apple Inc.     | AAPL   |
| Amazon.com     | AMZN   |
| Netflix Inc.   | NFLX   |
| Alphabet Inc.  | GOOG   |


Across four pre-set problems, the assignment is to read in the finance data, use functions to save csv files and plots in our desired naming convention, then script & automate the workflow using Github Actions. 
See below, **Stated Aim** & **Problems** listed 1-4 for more detail.

## Stated Aim  

Complete problems outlined in course module - See problems 1-4 below:

 
## Problem 1: Data from yfinance

Using the [yfinance](https://github.com/ranaroussi/yfinance) Python package, write a function called `get_data()` that downloads all hourly data for the previous five days for the five FAANG stocks:

- Facebook (META)
- Apple (AAPL)
- Amazon (AMZN)
- Netflix (NFLX)
- Google (GOOG)

The function should save the data into a folder called `data` in the root of your repository using a filename with the format `YYYYMMDD-HHmmss.csv` where `YYYYMMDD` is the four-digit year (e.g. 2025), followed by the two-digit month (e.g. `09` for September), followed by the two digit day, and `HHmmss` is hour, minutes, seconds.
Create the `data` folder if you don't already have one.

## Problem 2: Plotting Data

Write a function called `plot_data()` that opens the latest data file in the `data` folder and, on one plot, plots the `Close` prices for each of the five stocks.
The plot should include axis labels, a legend, and the date as a title.
The function should save the plot into a `plots` folder in the root of your repository using a filename in the format `YYYYMMDD-HHmmss.png`.
Create the `plots` folder if you don't already have one.

## Problem 3: Script

Create a Python script called `faang.py` in the root of your repository.
Copy the above functions into it and it so that whenever someone at the terminal types `./faang.py`, the script runs, downloading the data and creating the plot.
Note that this will require a shebang line and the script to be marked executable.
Explain the steps you took in your notebook.

## Problem 4: Automation

Create a [GitHub Actions workflow](https://docs.github.com/en/actions) to run your script every Saturday morning.
The script should be called `faang.yml` in a `.github/workflows/` folder in the root of your repository.
In your notebook, explain each of the individual lines in your workflow.


## Repository Contents

 - **.github/workflows** - Contains script 'faang.yml' that runs the code every Saturday morning.
 - **data** - Folder that contains csv files of 'FAANG' stock data over the last five days.
 - **plots** - Contains generated plots of 'FAANG' stock closing prices over the last five days, based on latest data file.
 - **.gitignore** - Tells Git which files to ignore in repository.
 - **README** - This file, used to explain the project.
 - **faang.py** - Python script with function to download, save and create plots of 'FAANG' data.
 - **problems.ipynb** - Jupyter notebook with solutions to above problems.
 - **requirements.txt** - List of packages used in the analysis.
 
 
  ## Installation

1. **Clone the repository.**

```bash
git clone https://github.com/Mr-Scarf/computer-infrastructure
```
2. **Install dependencies/required packages.**


```bash
pip install -r requirements.txt
```
3. **Run the jupyter notebook or the python script:**
```bash
Jupyter notebook  `problems.ipynb` 
```
**or**

```bash
python  `faang.py' 
```


