# my_lambdata/assignment.py

from pandas import DataFrame

class CustomDataFrame(DataFrame):
    ''''
    Params (df) a DataFrame with a column containing state abbreviations.
    '''

    def state_names(self):
        '''
        Add a column of corresponding state names to a dataframe.
        '''

        names = {'CA': 'California',
                'CO': 'Colorado',
                'CT': 'Connecticut',
                'DC': 'District of Columbia',
                'TX': 'Texas'}

        self['state'] = self['abbrev'].map(names)

if __name__ == "__main__":

    custom = CustomDataFrame({"abbrev": ['CA', 'CO', 'CT', 'DC', 'TX']})
    print(custom.head())

    custom.state_names()
    print(custom.head())