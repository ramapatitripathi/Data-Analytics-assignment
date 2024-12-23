import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
file_path = "C:\\Users\\Ramapati\\OneDrive\\Desktop\\data analyst\\merge2.xlsx"  # Replace with your file path
data = pd.read_excel(file_path)

# Preview the data
print(data.head())

# Merge Cooking Sessions and Order Details
merged_data = data.merge(
    data,
    left_on=['CookingSessions csv.User ID', 'CookingSessions csv.Session ID'],
    right_on=['OrderDetails csv.User ID', 'OrderDetails csv.Session ID'],
    suffixes=('_session', '_order')
)

# Preview merged data
print(merged_data.head())
print(merged_data.columns.tolist())

# Analyze relationship between session duration, ratings, and order frequency
session_order_analysis = merged_data.groupby('CookingSessions csv.Session ID_session').agg({
    'CookingSessions csv.Duration (mins)_session': 'mean',
    'CookingSessions csv.Session Rating_session': 'mean',
    'OrderDetails csv.Order ID_session': 'count'
}).reset_index()

print(session_order_analysis.head())


# Identify popular dishes based on order count
popular_dishes = data['OrderDetails csv.Dish Name'].value_counts().reset_index()
popular_dishes.columns = ['Dish Name', 'Order Count']

print(popular_dishes.head())

# Analyze orders by age group
data['Age Group'] = pd.cut(data['Age'], bins=[0, 18, 35, 50, 100], labels=['Teen', 'Young Adult', 'Adult', 'Senior'])
demographics_analysis = data.groupby('Age Group').agg({
    'Total Orders': 'sum',
    'Favorite Meal': 'count'
}).reset_index()

print(demographics_analysis)

# Analyze orders by location
location_analysis = data.groupby('Location').agg({
    'Total Orders': 'sum',
    'OrderDetails csv.Amount (USD)': 'sum'
}).reset_index()

print(location_analysis.head())

# Plot popular dishes
sns.barplot(x='Order Count', y='Dish Name', data=popular_dishes.head(10))
plt.title('Top 10 Popular Dishes')
plt.show()

# Plot orders by age group
sns.barplot(x='Age Group', y='Total Orders', data=demographics_analysis)
plt.title('Orders by Age Group')
plt.show()
