import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from Google Drive
file_path = '/content/drive/MyDrive/TUS/Engineering_Project/data/cleaned_chunks/merged_cleaned_data_v36_no_photo.csv'
data = pd.read_csv(file_path)

# Group data by 'subreddit' and calculate percentages of FAKE and TRUE labels
label_counts = data.groupby('subreddit')['2_way_label'].value_counts().unstack(fill_value=0)
label_percentages = label_counts.div(label_counts.sum(axis=1), axis=0) * 100
label_percentages.rename(columns={0: 'FAKE', 1: 'TRUE'}, inplace=True)

# Plot percentage of FAKE and TRUE labels
label_percentages.plot(kind='bar', stacked=True, figsize=(10, 6), color=['red', 'green'])

# Customize the plot
plt.title('Percentage of FAKE vs TRUE Labels by Subreddit', fontsize=16)
plt.xlabel('Subreddit', fontsize=14)
plt.ylabel('Percentage (%)', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.legend(['FAKE', 'TRUE'], fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()