import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('./fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
top_views = df['value'].quantile(0.975)
bottom_views = df['value'].quantile(0.025)

df = df[(df['value'] <= top_views) & (df['value'] >= bottom_views)]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(24, 8))
    ax.plot(df, color="purple")
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')  

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_bar['month_name'] = df_bar['month'].apply(lambda x: month_names[x - 1])

    df_pivot = df_bar.pivot_table(index='year', columns='month_name', values='value', aggfunc='mean')
    df_pivot = df_pivot.reindex(columns=month_names)

    # Draw bar plot
    fig = df_pivot.plot(kind='bar', stacked=False, figsize=(10, 8))
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    plt.ticklabel_format(style='plain', axis='y')
    fig = plt.gcf()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    marker_style = {'marker': 'd', 'markerfacecolor': 'k'}

    fig, ax = plt.subplots(1, 2, figsize=(20, 6))
    plt.subplot(1,2,1)
    sns.boxplot(data=df_box, x='year', y='value', ax=ax[0], hue='year', palette='deep', legend=False, flierprops=marker_style, fliersize=2)
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.title('Year-wise Box Plot (Trend)')

    plt.subplot(1,2,2)
    sns.boxplot(data=df_box, x='month', y='value', ax=ax[1], order=month_order, hue='month', legend=False, flierprops=marker_style, fliersize=2)
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

# it's necessary to upgrade seaborn or else the draw_box_plot() function will throw a numpy attribute error!