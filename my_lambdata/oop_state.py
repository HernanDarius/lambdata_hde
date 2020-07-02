# my_lambdata/assignment.py

from pandas import DataFrame

class DataFrameProcessor():
    '''
            Params (df) a DataFrame with a column containing state abbreviations.
    '''
    def __init__(self, df):
        self.df=df

    def state_names(self):
        '''
        Add a column of corresponding state names to a dataframe.

        Return a copy of the original column with new column containing
        corresponding state names.

        '''

        names = {'CA': 'California',
                'CO': 'Colorado',
                'CT': 'Connecticut',
                'DC': 'District of Columbia',
                'TX': 'Texas'}

        self.df['state'] = self.df['abbrev'].map(names)


if __name__ == "__main__":
    df = DataFrame({"abbrev": ['CA', 'CO', 'CT', 'DC', 'TX']})
    #print(df.head())

    #df_new = state_names(df)
    #print(df_new.head())

    processor = DataFrameProcessor(df=df)
    print(processor.df.head())
    processor.state_names()
    print(processor.df.head())
