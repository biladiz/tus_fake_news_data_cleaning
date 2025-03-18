# tus_fake_news_data_cleaning
 TUS Engineering Project - Sentiment Analysis to Detect Fake News - Fakeddit data celanup

COLAB --> Python 3.11.11


<table>
  <thead>
    <tr>
      <th>Item</th>
      <th>Description</th>
      <th>Link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Combined Dataset</td>
      <td>"All comments"</td>
      <td><a href="https://drive.google.com/drive/folders/150sL4SNi5zFK8nmllv5prWbn0LyvLzvo">Link</a></td>
    </tr>
    <tr>
      <td>V2.0 Dataset</td>
      <td>"Fakeddit dataset hosted online"</td>
      <td><a href="https://fakeddit.netlify.app/">Netlify</a>, <a href="https://github.com/entitize/Fakeddit">GitHub</a></td>
    </tr>
    <tr>
      <td>DataSet merged data - v1</td>
      <td>"Merging all_comments and train datasets"</td>
      <td>merged_data_v1.csv</td>
    </tr>
    <tr>
      <td>DataSet merged data - v2</td>
      <td>"Used NLTK stopwords and lemmatizer. Skipped/removed records without comments or submissions. Merged with 'commentsspecialdelim'."</td>
      <td>merged_data_v2.csv</td>
    </tr>
    <tr>
      <td>DataSet merged data - v14</td>
      <td>"Limited content and comments to 500 characters."</td>
      <td>merged_data_v14.csv</td>
    </tr>
    <tr>
      <td>Dataset cleaned features</td>
      <td>"Removed unnecessary columns. Updated delimiter to |__|."</td>
      <td>merged_data_v14_features.csv</td>
    </tr>
    <tr>
      <td>Dataset-Orig texts</td>
      <td>"Added original text columns."</td>
      <td>merged_cleaned_data_v20.csv</td>
    </tr>
    <tr>
      <td>Limited to 1000 rows</td>
      <td>"Restricted to 1000 rows for testing purposes."</td>
      <td><a href="https://tusmm-my.sharepoint.com/:x:/g/personal/a00326506_student_tus_ie/EcmvrDR2VQlNtYH955of5skBbbJEqcHkR--M-DwKAsR_8Q?e=jCjnZL">Link</a></td>
    </tr>
    <tr>
      <td>Data entries without images</td>
      <td>"Removed isImage=True entries, subreddits containing 'photo', and Reddit-generated comments. Used .tsv format to avoid issues with commas."</td>
      <td>merged_cleaned_data_v26_NoImage.tsv</td>
    </tr>
  </tbody>
</table>
