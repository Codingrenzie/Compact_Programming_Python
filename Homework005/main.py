import pandas as pd
import matplotlib.pyplot as plt

def exchange_columns(df, column1, column2):
    column_list = list(df.columns)
    x, y = column_list.index(column1), column_list.index(column2)
    column_list[y], column_list[x] = column_list[x], column_list[y]
    return df[column_list]

if __name__ == '__main__':        
    # Question1
    df = pd.read_csv('data.csv')
    print(df.head(5))

    # Question2
    df['Index Column'] = df.index
    print(df.head(5))

    # Question3
    # Checks if sex is Male in, column sex
    # If so changes the letter to 'M'
    df.loc[(df.Sex == 'male'), 'Sex'] = 'M'
    print(df.head(5))

    # Question4
    column_names = df.columns
    # Retrieve column names
    print(column_names)
    # Get the sum of elements in the above result
    print(len(column_names))

    # Question5
    # Exchange following columns
    print(exchange_columns(df, 'Name', 'Ticket'))
    # Sorting by name
    print(df.sort_index(axis=1))

    # Question6
    no_objects = round(len(df.index) * 0.05)
    # Drops first 5%
    print(df.drop(df.index[:no_objects]))
    # Drops last 5%
    print(df.drop(df.index[-no_objects:]))

    # Question7
    # Fills the N/A values with average of Column 'Age'
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    print(df['Age'])

    # Question8
    # Defining two dictionaries
    dict_a = {"stationary": ["books", "pencils", "pens", "sharpners"], "Amount": [10, 5, 3, 1]}
    dict_b = {"stationary": ["books", "pencils", "pens", "sharpners"], "Price": [30, 5, 10, 2]}

    # Converting them to dataframes
    df_a = pd.DataFrame.from_dict(dict_a)
    df_b = pd.DataFrame.from_dict(dict_b)

    # Merging two dataframes
    print(pd.merge(df_a, df_b))

    # Apend two dataframes, as a new column to the first one
    print(pd.concat([df_a, df_b], axis=1))

    # Question9
    # Plot histogram for the column Age
    df.hist(column='Age')
    plt.show()

    # Question10
    print(df.corr())




