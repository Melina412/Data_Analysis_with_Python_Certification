import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('./medical_examination.csv')

# Add 'overweight' column
df['overweight'] = df.apply(lambda x: 1 if x['weight'] / (x['height']/100) ** 2 > 25 else 0, axis=1)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x <= 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x <= 1 else 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_melt = df.melt(id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_melt.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    # Draw the catplot with 'sns.catplot()'
    plot = sns.catplot(data=df_cat, x='variable', y='total', col='cardio', kind='bar', hue='value', palette='husl')



    # Get the figure for the output
    fig = plot


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_clean = df[df['ap_lo'] <= df['ap_hi']]

    height_less = df['height'].quantile(0.025)
    height_more = df['height'].quantile(0.975)
    weight_less = df['weight'].quantile(0.025)
    weight_more = df['weight'].quantile(0.975)

    df_clean = df_clean[df_clean['height'] >= height_less]
    df_clean = df_clean[df_clean['height'] <= height_more]
    df_clean = df_clean[df_clean['weight'] >= weight_less]
    df_clean = df_clean[df_clean['weight'] <= weight_more]

    df_heat = df_clean

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, mask=mask, fmt=".1f", cbar_kws={"shrink": 0.5}, square=True, center=0, vmax=0.3, linewidth=0.5)



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig