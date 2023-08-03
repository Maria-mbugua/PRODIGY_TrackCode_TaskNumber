# importing libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('C:\\Users\\NJERI\\Downloads\\Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_5607187.csv')

# Extract the necessary data for visualization
# For example, let's assume you want to visualize the distribution of country codes

# Select the column containing the country code data
country_data = data['Country Code']

# Create a bar chart
country_counts = country_data.value_counts()
plt.bar(country_counts.index, country_counts)

# Add labels and title
plt.xlabel('Country Code')
plt.ylabel('Count')
plt.title('Distribution of Country Codes')

# Rotate x-axis labels for better visibility if needed
plt.xticks(rotation='vertical')

# Display the bar chart
plt.show()
