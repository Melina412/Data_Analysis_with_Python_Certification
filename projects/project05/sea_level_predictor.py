import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('./epa-sea-level.csv')

    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    x2 = df['Year'].iloc[-14:]
    y2 = df['CSIRO Adjusted Sea Level'].iloc[-14:]

    future_x = np.arange(2014, 2051)

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 7))
    plt.scatter(x, y, color='c', label='data')

    # Create first line of best fit
    res =  linregress(x, y)
    x_extrapolated = x.copy()
    x_extrapolated = pd.concat([x_extrapolated, pd.Series(future_x)], ignore_index=True)

    plt.plot(x_extrapolated, res.intercept + res.slope*x_extrapolated, color='b', label=f'linear regression 1880 - most recent')

    # Create second line of best fit
    res2 =  linregress(x2, y2)
    x2_extrapolated = x2.copy()
    x2_extrapolated = pd.concat([x2_extrapolated, pd.Series(future_x)], ignore_index=True)

    plt.plot(x2_extrapolated, res2.intercept + res2.slope*x2_extrapolated, color='r', label=f'linear regression 2000 - most recent')
   
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()