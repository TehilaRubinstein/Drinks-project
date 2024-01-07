import pandas as pd
import numpy as np

class Data:
    num_of_ingredients = 0
    data_frame = None

    """
    Constractor that loads the data into dataframe and initializes the class 
    variables.
    @:param filename: the name of the data file to load

    """
    def __init__(self, filename):
        df = pd.read_csv(filepath_or_buffer=filename)
        if df.empty:
            raise Exception("The given file is empty")
        df = df.replace(to_replace=np.nan, value="", regex=True)
        self.num_of_ingredients = len(
            [col for col in df.columns if 'Ingredient' in col])
        self.data_frame = df


data = Data(filename='C:/Users/tehil/OneDrive/Documents/DrinksAppProject/resources/all_drinks.csv')
