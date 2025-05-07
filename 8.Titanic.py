import pandas as pd

def map_reduce_with_pandas(input_file):
    df = pd.read_csv(input_file)

    deceased_male = df[(df['Survived']==0)&(df['Sex']=='male')]
    avg_age_deceased_male = deceased_male['Age'].mean()

    deceased_female = df[(df['Survived']==0)&(df['Sex']=='female')]

    count_deceased_female_by_class = deceased_female['Pclass'].value_counts()

    return avg_age_deceased_male,count_deceased_female_by_class

input_file = '8.titanic_dataset.csv'
avg_age,female_count_class = map_reduce_with_pandas(input_file)

print(f"Average age of deceased males: {avg_age:.2f}")
print("Count of deceased females by class:",female_count_class)
