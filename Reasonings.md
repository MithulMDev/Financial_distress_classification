## Areas of focus

### Preprocessing

- <b>Null values (3) row wise<b> 
- The threshold was set to 3 or less null values per row, because more than three null values are resulting in more than 1/3rd of the data of the row as null values. 
- so 3 as a threshold is taken to keep the null values below or approximately 1/3rd of the row data. And we are focusing on row as each represent individual companies.
- so instead of focusing on the column or taking the metric as a whole, since each of the companies' metrics are interconnected, the null values per row is focused.


- <b>Isolation forests and Z score<b>

- Original data:
- Isolation Forest: 1402 outliers
- Z-score > 3: 2048 outliers

- ADASYN:
- with MICE: IF: 2741, Z-score: 2166
- with AE: IF: 2743, Z-score: 2184

- KMeans SMOTE:
- with MICE: IF: 2742, Z-score: 1957
- with AE: IF: 2739, Z-score: 1985

- SVM SMOTE:
- with MICE: IF: 2742, Z-score: 2026
- with AE: IF: 2740, Z-score: 2026

- Both MICE and AE perform similarly in capturing and reflecting the patterns of outliers, though AE seems to preserve more outliers compared.
- ADASYN significantly has increased the number of outliers detected as detected by isolations forests, which might introduce too many outliers
- Kmeans SMOTE and SVM SMOTE maintain a balanced approach in preserving the ratio of outliers as stated by isolation forests and Z score.
- SVMSMOTE results are consistent with AE and MICE indicating stability in the method.
  - The Z score shows that the outliers are in constant distance measure of standard deviation, thus well preserving the ratio of outliers and not artificially introducing too many new outliers.
  - Hence SVMSMOTE is found to be more suitable


- <b>Visualize TSNE graphs<b>
- Prior
  - This graph shows that there are overlapping clusters, class imbalance is observed as one color is dominating, the lack of clear boundaries suggest that the data needs to be preprocessed as straight forward classification is challenging.
- MICE vs AE
  - AE has preserved original data patterns, as it closely resembles the original data prior to preprocessing
  - MICE has seen to have a bit more dispersion in the clusters. while it has maintained a close resembling pattern, it has also introduced some variability through the process, impersonating the underlying patterns and relationships of variables among each other.
  - MICE also suggests that there are possible new outliers as it is spread out when compared to AE, indicating the imputation could have introduced some meaningful and structural variability
  - MICE are slightly more dispersed suggesting, while it has handled imputation well, it has not preserved data like AE. So in conclusion AE seems to preserve the underlying patterns of the data - originality of the data. while MICE is observed to have introduced structural changes as it focuses on preserving the relationship between the variables for each instance. As a company's financial metrics are interelated and is different for each of the company based on industry, scale and nature of operations etc...
  - The relationships between variables in finance are often complex and multifaceted. The changes and variability introduced by MICE could be capturing these patterns which may not be apparent in the large chunk of data, as there is a high possibility that these pattern differ for each instance
  - The balance between preserving the originality and allowing meaningful variations is crucial.
- Imputation with class handling - ADASYN, KMSMOTE, SVMSMOTE


- <b>Comrpehensive analysis<b>
- Analysis such as correlation matrix, statistics, outlier detection (isolation forests, Z score), skewness and kurtosis are done in prior to preprocessing dataset and after each of the imbalance handling methods.
  - The df.info shows that there are typical outliers in the data
  - The correlation matrix shows that there are noticeable variables with strong correlations.
  - The extreme skewness and kurtosis values suggest that many features have significant outliers. These outliers could be genuine extreme values or potential data quality issues. They indicate indicate the presence of rare but high-value events or measurements
  - The high kurtosis values suggest that many data points are concentrated around the mean, with occasional extreme values causing heavy tails.
  - Correlation heatmap of processed data also shows a few highly correlated ratios.
  - Especially SVMSMOTE + MICE combination has preserved most of the correlated variables or has shown more number of correlated variables
  - The correlated variables for MICE and Autoencoders are observed to be different
  - Similar patterns of non-normal distributions are observed on PCA processed datasets of various combinations through Skewness and kurtosis.
  - The Pearson and Spearman statistics post processing of all the combinations are observed to have strong non linear relationship, thus preserving the original data pattern.
-------------------------- should populate answers
- This is to know the preservation of patterns of data of each methods with the original dataset


- <b>Linear and non-linear comparison<b>
- Pearson and Spearman are calculated on the original dataset and also on the imbalance handled datasets to know the preservations of pattern of the data.
-------------------------- should populate answers
- The difference is printed, if the difference is high then it means non linear data


- <b>Null values imputation - MICE & Autoencoders<b>
- MICE - give the mathematical computation and the reasoning why this is choosen for imputation as it works well with interconnected variables/columns.
- Autoencoders - give the mathematical computation and the reasoning behind choosing this as an other alternative

  
- <b>Class imbalance handling - ADASYN, KmeansSMOTE, SVMSMOTE
- Give basic mathematical formulae for each and also a basic interpretation. 
- Give the reasoning why these (each of them) is choosen among other variety of types of methods
- The above given statistical, pattern visualization - TSNE, linear and non linear, outliers, skewness, kurtosis, and other analysis methods are computed and given after implementation of each of the methods


### Machine learning models - predictions

- <b>Train models<b>
- Capture and analyze the time taken of each of the models and on each of the dataset
- Evaluation metrics of each model of each combination
- LIME and SHAP graphs explanations
