from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Initialize Spark session
spark = SparkSession.builder \
    .appName("StudentPerformanceFactors") \
    .getOrCreate()

# Load dataset
df = spark.read.csv("/home/sat3812/Downloads/archive/StudentPerformanceFactors.csv", header=True, inferSchema=True)

# Check for missing values
missing_values = df.select([F.count(F.when(F.col(c).isNull(), c)).alias(c) for c in df.columns]).toPandas()
print("Missing Values:\n", missing_values[missing_values > 0])

# Imputation: Mean for numerical and Mode for categorical variables
num_cols = [field.name for field in df.schema.fields if field.dataType.typeName() in ['integer', 'double']]
cat_cols = [field.name for field in df.schema.fields if field.dataType.typeName() == 'string']

# Mean imputation for numerical columns
for col in num_cols:
    mean_value = df.select(F.mean(col)).first()[0]
    df = df.fillna({col: mean_value})

# Mode imputation for categorical columns
for col in cat_cols:
    mode = df.groupBy(col).count().orderBy(F.desc("count")).first()[0]
    df = df.fillna({col: mode})

# Check for duplicates
duplicates = df.dropDuplicates()  # Drop duplicates directly
print("Duplicate Rows:\n", duplicates.count())

# Remove duplicates
df = df.dropDuplicates()

# Convert to Pandas DataFrame for visualization
pdf = df.toPandas()

# Outlier detection using box plots for numerical predictors
plt.figure(figsize=(15, 10))
for i, col in enumerate(num_cols):
    plt.subplot(5, 4, i + 1)
    sns.boxplot(data=pdf, x=col)
    plt.title(f'Box Plot of {col}')
plt.tight_layout()
plt.show()

# Distribution check for numerical predictors
pdf[num_cols].hist(bins=30, figsize=(15, 10))
plt.suptitle('Histograms of Numerical Features')
plt.show()

# Bar graph for categorical variables
for col in cat_cols:
    plt.figure(figsize=(10, 6))
    pdf[col].value_counts().plot(kind='bar')
    plt.title(f'Bar Graph of {col}')
    plt.xlabel(col)
    plt.ylabel('Counts')
    plt.show()

# Encode categorical variables if necessary
pdf = pd.get_dummies(pdf, columns=cat_cols)

# Check for NaN values and fill or drop them
numeric_pdf = pdf.select_dtypes(include=[np.number]).fillna(0)

# Correlation matrix
correlation_matrix = numeric_pdf.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Define the target variable for correlation analysis
target_variable = 'Exam_Score'

# Top correlated predictors with the target variable
top_corr = correlation_matrix[target_variable].abs().nlargest(4).index[1:]  # Get the top 3 predictors (excluding the target)
print("Top 3 Correlated Predictors with", target_variable, ":\n", top_corr)

# Print correlations for each predictor
for col in top_corr:
    print(f"Correlation between {col} and {target_variable}: {correlation_matrix.loc[col, target_variable]:.2f}")

# Create separate scatter plots for each predictor
for col in top_corr:
    plt.figure(figsize=(10, 6))
    plt.scatter(pdf[col], pdf[target_variable], color='blue', alpha=0.5)
    plt.title(f'Scatter Plot of {col} vs {target_variable}')
    plt.xlabel(col)
    plt.ylabel(target_variable)
    plt.grid(True)
    plt.show()

# Stop the Spark session
spark.stop()
