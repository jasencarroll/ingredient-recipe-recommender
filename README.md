# Ingredient Recipe Recommender

```text
ingredient-recipe-recommender/
├── model/
│   ├── recipe-recommender.joblib   # Recommendation Model
├── src/
│   ├── data/                       # Datasets (not in Git)
│   ├── __init__.py                 # Python entry point for src module
│   ├── app.py                      # Streamlit application
│   ├── features.py                 # Features engineering and selection file
│   ├── main.py                     # Main model pipeline
│   ├── modeling.py                 # File for modeling
│   ├── preprocessing.py            # Data cleaning
│   ├── recommender.py              # Recommendation engine
│   ├── validation.py               # Developed validation checks
├── LICENSE                         # How the app can be used
├── README.md                       # Instructions for use
├── requirements.txt                # Dependencies
├── selected_features.csv           # CSV output from the model
```

# Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
3. [Usage](#usage)
   - [Basic Commands](#basic-commands)
   - [Advanced Features](#advanced-features)
4. [Contributing](#contributing)
5. [License](#license)

# Introduction
Your introduction content here.

# Getting Started
Getting started content here.

## Prerequisites
Prerequisites content here.

## Installation
The following are for Unix operating systems. For Windows you'll need to use Python's version of venv instead of a global package. 

### Get the Repo

```bash
git clone https://github.com/jasencarroll/ingredient-recipe-recommender.git
cd ingredient-recipe-recommender
```

### Make the venv
```bash
virtualenv .venv
source .venv/bin/activate
```

### Get the requirements
```bash
pip install -r requirements.txt
```

### Build the Model (Optional)
```bash
python main.py
```

### Run the App
```bash
streamlit run app.py
```

# Usage
Usage content here.

## Basic Commands
Basic commands content here.

## Advanced Features
Advanced features content here.

# Contributing
Contributing content here.

# License
License content here.

## Author

Jasen Carroll \
13 Feb 2025