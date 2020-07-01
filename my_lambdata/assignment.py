# my_lambdata/assignment.py

from pandas import DataFrame

# TODO: helper function from assignment
# State abbreviation --> Full Name and vise versa.
# ex. FL --> FLorida, etc.


def state_names(df):
    '''
    Add a column of corresponding state names to a dataframe.

    Params (df) a DataFrame with a column containing state abbreviations.

    Return a copy of the original column with new column containing
    corresponding state names.

    '''
    df_state = df.copy()

    names = {'CA': 'California',
             'CO': 'Colorado',
             'CT': 'Connecticut',
             'DC': 'District of Columbia',
             'TX': 'Texas'}

    df_state['state'] = df_state['abbrev'].map(names)

    return df_state

if __name__ == "__main__":
    df = DataFrame({"abbrev": ['CA', 'CO', 'CT', 'DC', 'TX']})
    print(df.head())

    df_new = state_names(df)
    print(df_new.head())
