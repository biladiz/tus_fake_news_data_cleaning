# tus_fake_news_data_cleaning
 TUS Engineering Project - Sentiment Analysis to Detect Fake News - Fakeddit data celanup

COLAB --> Python 3.11.11

Item                        Description         	                      Link
Combined Dataset            "All comments"                              https://drive.google.com/drive/folders/150sL4SNi5zFK8nmllv5prWbn0LyvLzvo
V2.0 Dataset                "Fakeddit dataset hosted online"            https://fakeddit.netlify.app/, https://github.com/entitize/Fakeddit
DataSet merged data - v1    "Merging all_comments and train datasets"   merged_data_v1.csv
DataSet merged data - v2    "Used NLTK stopwords and lemmatizer. Skipped/removed records without comments or submissions. Merged with "commentsspecialdelim"."                                                merged_data_v2.csv
DataSet merged data - v14   "Limited content and comments to 500 characters." merged_data_v14.csv
Dataset cleaned features    "Removed unnecessary columns. Updated delimiter to |__|." merged_data_v14_features.csv
Dataset-Orig texts          "Added original text columns."              merged_cleaned_data_v20.csv
Limited to 1000 rows        "Restricted to 1000 rows for testing purposes.   https://tusmm-my.sharepoint.com/:x:/g/personal/a00326506_student_tus_ie/EcmvrDR2VQlNtYH955of5skBbbJEqcHkR--M-DwKAsR_8Q?e=jCjnZL
Data entries without images Removed isImage=True entries, subreddits containing "photo", and Reddit-generated comments. Used .tsv format to avoid issues with commas. "                                                   merged_cleaned_data_v26_NoImage.tsv

