import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def select_categorical_columns(df):
    # select only categorical columns and drop those with too many categories
    categorical_cols = df.select_dtypes(include=['object']).columns
    categorical_cols = df[categorical_cols].drop(['Name', 'Doctor',
        'Date of Admission', 'Discharge Date', 'Hospital'], axis=1).columns
    return categorical_cols

def get_column_number(columns):
    print("The following columns are available to be analysed:")
    # enumerated for loop to go through each element of columns
    for i, col in enumerate(columns):
        print(f"{i}. {col}")
    # get input from user and convert it to integer type
    column_no = int(input("Enter the column number you like to analyse:\n"))
    return column_no

def plot_selected_column(df, column):
    fig, ax = plt.subplots(1, 2)
    fig.suptitle(f"{column}", fontsize=20)
    sns.set_theme()
    ax[0].set_title("Bar Chart")
    df[column].value_counts().plot(kind="bar", color=sns.color_palette("tab10"),
        ax=ax[0])
    ax[1].set_title("Pie Chart")
    df[column].value_counts().plot(kind="pie", ylabel="",
        color=sns.color_palette("tab10"), ax=ax[1])
    plt.tight_layout()
    plt.show()

filename = "healthcare_dataset.csv" # str variable to set the csv file name
df = pd.read_csv(filename) # read and convert the csv file into a dataframe

categorical_cols = select_categorical_columns(df)
col = get_column_number(categorical_cols)
while ((col >= len(categorical_cols)) or col < 0):
    print("You have entered an invalid column number, please try again.\n")
    col = get_column_number(categorical_cols)
print(f"You have selected {categorical_cols[col]}")
plot_selected_column(df, categorical_cols[col])
