import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r'C:\Users\shrih\OneDrive\Desktop\intel\StudentsPerformance.csv')


# Set seaborn style
sns.set(style="whitegrid")

# Show the first few rows
print(df.head())

# 1. Gender distribution
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='gender', palette='pastel')
plt.title('Gender Distribution')
plt.show()

# 2. Parental level of education
plt.figure(figsize=(10,5))
sns.countplot(data=df, x='parental level of education', palette='muted', order=df['parental level of education'].value_counts().index)
plt.xticks(rotation=45)
plt.title('Parental Level of Education')
plt.show()

# 3. Test preparation course vs. average scores
df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

plt.figure(figsize=(6,4))
sns.boxplot(data=df, x='test preparation course', y='average_score', palette='Set2')
plt.title('Effect of Test Preparation on Average Score')
plt.show()

# 4. Score distributions by gender
plt.figure(figsize=(14,4))
for i, subject in enumerate(['math score', 'reading score', 'writing score']):
    plt.subplot(1, 3, i+1)
    sns.histplot(data=df, x=subject, hue='gender', kde=True, palette='coolwarm')
    plt.title(f'{subject.title()} by Gender')
plt.tight_layout()
plt.show()

# 5. Relationship between math and reading scores
plt.figure(figsize=(6,6))
sns.scatterplot(data=df, x='math score', y='reading score', hue='gender', palette='cool')
plt.title('Math vs Reading Score')
plt.show()

# 6. Correlation heatmap
plt.figure(figsize=(6,5))
sns.heatmap(df[['math score', 'reading score', 'writing score']].corr(), annot=True, cmap='YlGnBu')
plt.title('Correlation Between Scores')
plt.show()
