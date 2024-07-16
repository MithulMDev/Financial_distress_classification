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
  - The visualization shows that the ADASYN has generated interwoven data with varied scales as resembled by the gradual transition of colors, but is preserving more of the original data pattern.
    - It is also suggesting the ADASYN is generating samples that bridge gaps between existing data points, potentially creating a more countinuous representation of data. Still this could be beneficial in cases of detecting subtle patterns that could be lost due to aggressive sampling
  - The KmeansSMOTE plot shows that there are distinct clusters with sharp boundaries.
    - The spread of light green and yellow points across different areas, also overlaying colors, suggest KMeansSMOTE is creating new instances of data based on cluster centroids and the minority, which may not always follow the original data distributions and its patterns
    - It emphasizes well defined boundaries of data, which could be advantageous in classification tasks
  - The SVMSMOTE shows that the this method is in the middle of the ADASYN and Kmeans in the cluster definition
    - Color transition appears smoother than Kmeans while also having distinct boundaries with minimal overlapping data of different scales
    - this happens as SVMSMOTE generates instances based on the support vectors of the minority class, and since support vectors lie close to the decision boundaries of the classes, there is distinct clusters and is also suggesting that this method preserves the range of scales of data.
    - Thought the boundaries are not as sharply seen as in the case of KMeansSMOTE, there is very minimal over lapping of data.
    - This suggests that SVMSMOTE is creating more instances along the class boundaries, thus enhancing seperation while attempting to maintain the original structure 
    - There are different rows of data present in each of the dataset processed using each combinations, this is due to different class imbalance handling mechanisms. But nonetheless they are varied in a range of 100 rows approximately.
  

- <b>Comrpehensive analysis<b>
- Analysis such as correlation matrix, statistics, outlier detection (isolation forests, Z score), skewness and kurtosis are done in prior to preprocessing dataset and after each of the imbalance handling methods.
  - The df.info shows that there are typical outliers in the data
  - The correlation matrix shows that there are noticeable variables with strong correlations.
  - The extreme skewness and kurtosis values suggest that many features have significant outliers. These outliers could be genuine extreme values or potential data quality issues. They indicate indicate the presence of rare but high-value events or measurements
  - The high kurtosis values suggest that many data points are concentrated around the mean, with occasional extreme values causing heavy tails.
  - Correlation heatmap of processed data also shows a few highly correlated ratios.
  - The patterns of correlated variables are similar for eahc method - MICE and autoencoder. MICE with class handling combinations has seen to have high number of correlated variables
  - Especially combinations with MICE has preserved most of the correlated variables or has shown more number of correlated variables
  - The correlated variables for MICE and Autoencoders are observed to be different
  - Similar patterns of non-normal distributions are observed on PCA processed datasets of various combinations through Skewness and kurtosis.
  - The Pearson and Spearman statistics post processing of all the combinations are observed to have strong non linear relationship, thus preserving the original data pattern.

  - Isolation forest and Z score:
    - Since the underlying data is seen to have non-normal ditributions through high number of skewness and kurtosis, we are implementing isolation forest (which doesn't follow any assumptions on the pattern of the data), and z-score (which assumes that the data follows a normal distribution) to have a comprehensive understanding of the pattern and the outliers
    - Kmeans SMOTE has resulted in fewest of outliers compared to other methods as seen through Z score analysis, while ADASYN seems to have generated high number of potential outliers
    - SVMSMOTE has seen to closely replicate the original data with similar no of potential outliers
    - SVMSMOTE + AE has been observed to maintain a reasonable balance in terms of data distribution and outlier generation
    - Isolations forests show the consistency of proportion of outlier values generated through preprocessing methods. Thus indicating the oversampling methods have preserved the outlier data's proportion to the normal data.
    - Since the z scores have stated more proportion of outliers in the original dataset, and the preprocessing methods have shown to thicken the tails of the distribution, resulting in lesser no of outliers detected by Z score.
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
- Since in the real life there are very less proportion of financially distressed companies compared to the healthy companies, Class imbalance issues persist in most of the financial predictions.
- Give basic mathematical formulae for each and also a basic interpretation. 
- Give the reasoning why these (each of them) is choosen among other variety of types of methods
- The above given statistical, pattern visualization - TSNE, linear and non linear, outliers, skewness, kurtosis, and other analysis methods are computed and given after implementation of each of the methods


### Machine learning models - predictions

- <b>Train models<b>
- Capture and analyze the time taken of each of the models and on each of the dataset
- Evaluation metrics of each model of each combination
- LIME and SHAP graphs explanations
