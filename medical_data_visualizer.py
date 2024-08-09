import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 Import the data from medical_examination.csv and assign it to the df variable
df = pd.read_csv("https://github.com/freeCodeCamp/boilerplate-medical-data-visualizer/raw/main/medical_examination.csv")

# 2 Create the overweight column in the df variable
# To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. 
# Use the value 0 for NOT overweight and the value 1 for overweight.
df['overweight'] = ((df['weight'] / (df['height'] / 100) ** 2) > 25).astype(int)

# 3 Normalize data by making 0 always good and 1 always bad. 
#If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, np.where(df['cholesterol'] == 1, 0, df['cholesterol']))
df['gluc'] = np.where(df['gluc'] == 1, 0, np.where(df['gluc'] > 1, 1, df['gluc']))

# 4 Draw the Categorical Plot in the draw_cat_plot function
# Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's catplot(). 
# The dataset should be split by Cardio so there is one chart for each cardio value. 
# The chart should look like examples/Figure_1.png. (https://github.com/freeCodeCamp/boilerplate-medical-data-visualizer/blob/main/examples/Figure_1.png)
def draw_cat_plot():
    # 5 Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight in the df_cat variable.
    # &
    # 6 Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat =  pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], 
                    var_name='variable', value_name='value')
    

    # 7 Convert the data into long format and create a chart that shows the value counts of the categorical features using the following method provided by the seaborn library import : sns.catplot()
    g = sns.catplot(x='variable', hue='value', col='cardio', data=df_cat, kind='count', col_order=[0, 1], col_wrap=2, height=5, aspect=1.5)

    # 8 Get the figure for the output and store it in the fig variable
    fig = g.fig


    # 9 Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# 10 Draw the Heat Map in the draw_heat_map function
# Create a correlation matrix using the dataset. 
# Plot the correlation matrix using seaborn's heatmap(). 
# Mask the upper triangle. The chart should look like examples/Figure_2.png. (https://github.com/freeCodeCamp/boilerplate-medical-data-visualizer/blob/main/examples/Figure_2.png)
def draw_heat_map():

# 11 Clean the data in the df_heat variable by filtering out the following patient segments that represent incorrect data:
    # A. height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
    # B. height is more than the 97.5th percentile
    # C. weight is less than the 2.5th percentile
    # D. weight is more than the 97.5th percentile
    df_heat = df[(df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975)) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))]

    # 12 Calculate the correlation matrix and store it in the corr variable
    corr = df_heat.corr()

    # 13 Generate a mask for the upper triangle and store it in the mask variable
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14 Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(8, 6))  

    # 15 Plot the correlation matrix using the method provided by the seaborn library import: sns.heatmap()
    sns.heatmap(corr, annot=True, cmap='coolwarm', mask=mask, fmt='.2f', ax=ax, vmin=-1, vmax=1)

    # 16 Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig