# Computer Infrastructure Module

![FAANG finance chart](https://www.trueup.io/img/tag/faang_plus.svg)


**Author**: David Scally  
**University**: Atlantic Technological University  
**Module**: Computer Infrastructure  
**Class**: September 2025 

## Overview

This project is an analysis of the famous five 'FAANG' companies hourly stock data across the most recent 5 day period. 

| Company        | Ticker |
|---------------|--------|
| Meta Platforms | META   |
| Apple Inc.     | AAPL   |
| Amazon.com     | AMZN   |
| Netflix Inc.   | NFLX   |
| Alphabet Inc.  | GOOG   |


The goal, across four pre-set problems,  is to read in the finanace data, use functions to save a csv and plots in our desired naming convention, then script & automate the running of our csv & plots.
See below Stated Aim & Problems listed 1-4 for more detail.


## Module Learning Outcomes

Learn how to:

1. Use, configure, and script in a command line interface environment.

2. Manipulate and move data and code using the command line.

3. Compare commonly available software infrastructures and architectures.

4. Select appropriate infrastructure for a given computational task.

My assessment for this module.

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

 - README - This file, used to explain the project
 - problems.ipynb - Jupyter notebook with solutions to above problems
 - data - Folder that contains csv files of FAANG stock data over the last 5 days
 - plots - Opens latest file in data folder & generates plot of closing prices of FAANG stocks over the last 5 days
 - faang.py - Python script that runs, downloading the data and creating the plots of FAANG data
 - .github/workflows - Conatains script 'faang.yml' that runs the code every Saturday morning.
 - requirements.txt - List of packages used in the analysis
 
 - 

  ## Installation

1. Clone the repository

```python
git clone https://github.com/Mr-Scarf/computer-infrastructure
```
2. Install dependencies/required packages


```python
pip install -r requirements.txt
```
3. Run the Jupyter notebook or the python scipt:
```python
Jupyter notebook  `problems.ipynb` 
```
or

```python
python  `faang.py' 
```


## Problems
Create a notebook called problems.ipynb in the root of the repository. Complete all problems detailed in problems.md in this notebook.

Keep your notebook reproducible, clean and concise. Use a level 1 heading for the notebook title. Use level 2 Markdown headings to clearly identify each problem within the notebook. Use Markdown cells to give explanations and insights into your code. Follow Python coding standards and guidelines such as PEP8. Write clean, readable, and efficient code using meaningful variable names and consistent formatting.

Break code into smaller, manageable cells whenever possible. Each code cell should focus on a single step in your overall solution. Comment your code to explain what each line does. You can use modules in the standard library. You may also use any of the packages in the requirements.txt file in this repository and their dependencies. Ask before using anything else.

## Target Audience
Create your submission with the following target audience in mind: an informed computing professional, such as a prospective employer. Assume they have a strong background in computing but may not be familiar with the specific language, packages, or tools you use.

A reviewer should be able to clone your repository and run any code within it with minimal setup. Include setup instructions in your README.md, and all necessary data files and images, clearly organized. If any files are too large to include in your repository, explain this in your README. Where possible, provide code to automatically download them.

## Feedback and Consistency
Work on your repository throughout the assessment timeline. Your commit history should show how your work evolved: improvements, refinements, and added clarity. Where feedback is given, it can only be based on what you have pushed to GitHub by that point in time. Make sure you have submitted the repository URL and pushed your commits.

If you have issues with Git, ask for help early. Do not delete files or commits without consulting your lecturer. Large, last-minute commits will not be accepted.

## Marking Scheme
Your submission will be assessed across the following five equally-weighted categories. Your mark will be based only on the contents of your repository. Make sure it provides clear evidence of the criteria listed.

Remember to keep the target audience in mind. A good submission will meet most of the criteria in each category. An excellent submission will demonstrably meet all the criteria. Note that the overall impression your submission creates may influence marks in each category.

## Presentation
Your repository should be well-organized, with a clear, and logical structure.
Your README should clearly explain the purpose of your repository and how to run any code it contains.
Your notebook should present a clear narrative, making it easy to follow your thought process.
A knowledgeable expert reviewing your repository should be able to understand its contents without your help.
## Research
Your submission should demonstrate research on relevant topics, showing an understanding of the material.
You should build upon existing literature and documentation rather than just presenting basic solutions.
References and comparisons to similar work should be included.
References should be put into context - how and why they are relevant to your submission.
## Documentation
Your repository should contain standard files, such as a README, to provide context for your work.
All concepts should be clearly and concisely explained within your notebooks.
Code should include informative comments that clarify its purpose and functionality.
Your notebook should include an introduction providing context and a conclusion to summarize any results.
## Development
Your code should be efficient and well-structured, effectively addressing the problem at hand.
Standard programming structures, algorithms, and testing methods should be applied where appropriate.
The overall architecture of your code should be clean, demonstrating good coding practices.
Your code should demonstrate your knowledge of established style conventions and norms.
## Consistency
Your commit history should show detailed, incremental changes over time.
There should be evidence of steady progress throughout the semester, rather than last-minute submissions.
Your repository should reflect a process of review and refinement, demonstrating continuous improvement.
Your commit history should demonstrate your refinement of both code and explanations over time.
End