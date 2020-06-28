#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 11:56:54 2020

@author: abdo
"""

# Opt hello world (https://en.wikipedia.org/wiki/%22Hello,_World!%22_program)
print('Hello, World!')

# Import the pandas library
import pandas as pd
 
# Read the data from a csv file and save it as a pandas dataframe named 'xg_data'
# Replace the file path with the location on your computer where the csv file is saved (in my case it's in D:/Tom/Downloads/)
xg_data = pd.read_csv('/Users/abdo/Documents/Github/python-for-fantasy-football/1 - introduction/epl_xg.csv')
 
# Take a look at the data
xg_data

# Show the first 3 rows of the data
xg_data.head(3)

#Show the last 7 rows of the data
xg_data.tail(7)

# Show the data for Leicester (note that 'is equal to' is written as '==' instead of '=')
# The code below essentially reads as 'show the xg_data dataframe where the 'Team' column is equal to 'Leicester'
# Because Leicester is a string, you need to write it using either single or double quotes
xg_data[xg_data['Team'] == 'Arsenal']


# Filter the rows where goals scored is greater than or equal to 15, and save the result in a new dataframe
# Note that in this case because 15 is an integer, we don't need to use quotes
# For more information about data types, see https://realpython.com/python-data-types/
high_scorers = xg_data[xg_data['G'] >= 15]
high_scorers

# Print a list of the teams that have scored at least 15 goals
print(list(high_scorers['Team']))

# Show some summary statistics for each column in the original dataframe
xg_data.describe()

# Add new columns for goal difference, expected goal difference and non-penalty expected goal difference
xg_data['GD'] = xg_data['G'] - xg_data['GA']
xg_data['xGD'] = xg_data['xG'] - xg_data['xGA']
xg_data['NPxGD'] = xg_data['NPxG'] - xg_data['NPxGA']
 
# Order the teams by NPxGD to help give an idea of who the good and bad teams are currently
xg_data = xg_data.sort_values(by=['NPxGD'], ascending=False)
xg_data


