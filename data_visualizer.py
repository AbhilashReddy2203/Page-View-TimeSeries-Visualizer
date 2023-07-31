# Page-View-TimeSeries-Visualizer
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def draw_line_plot():
    # Load the data
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

    # Clean the data by filtering out days when the page views were in the top 2.5% or bottom 2.5%
    df_cleaned = df[
        (df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))
    ]

    # Create the line plot
    plt.figure(figsize=(14, 6))
    plt.plot(df_cleaned.index, df_cleaned['value'], color='r')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save and return the plot
    plt.savefig('line_plot.png')
    return plt.gcf()
def draw_bar_plot():
    # Load the data
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'])

    # Extract year and month from the date column
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()

    # Group the data by year and month, calculate average daily page views
    df_grouped = df.groupby(['year', 'month'])['value'].mean().unstack()

    # Define the month order for the bar plot
    month_order = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]

    # Create the bar plot
    plt.figure(figsize=(14, 6))
    ax = sns.barplot(data=df_grouped, x='year', y='value', hue_order=month_order, hue='month')
    plt.legend(title='Months', loc='upper left', labels=month_order)
    plt.title('Average Daily Page Views for Each Month (Year-wise)')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')

    # Save and return the plot
    plt.savefig('bar_plot.png')
    return plt.gcf()
def draw_box_plot():
    # Load the data
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'])

    # Extract year and month from the date column
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()

    # Define the month order for the box plot
    month_order = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]

    # Create the box plots
    plt.figure(figsize=(14, 6))

    # Year-wise box plot
    plt.subplot(1, 2, 1)
    sns.boxplot(data=df, x='year', y='value')
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')

    # Month-wise box plot
    plt.subplot(1, 2, 2)
    df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)
    sns.boxplot(data=df, x='month', y='value')
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')

    # Adjust layout and save the plot
    plt.tight_layout()
    plt.savefig('box_plot.png')
    return plt.gcf()
