import pandas as pd
import matplotlib.pyplot as plt

def select_categorical_columns(df):
    # select only categorical columns and drop those with too many categories
    print("all cols:", df.columns)
    print("dtypes:", df.dtypes)
    categorical_cols = df.select_dtypes(include=['object']).columns
    print("first categorical cols:", categorical_cols)
    categorical_cols = df[categorical_cols].drop(['Name', 'Doctor',
        'Date of Admission', 'Discharge Date', 'Hospital'], axis=1).columns
    return categorical_cols

filename = "healthcare_dataset.csv" # str variable to set the csv file name
df = pd.read_csv(filename) # read and convert the csv file into a dataframe
categorical_cols = select_categorical_columns(df)
print("categorical cols:", categorical_cols)
