from typing import List, Dict
from pydantic import BaseModel
from src import constants, data_processing
from fastapi import HTTPException
import logging
import pandas as pd

df = data_processing.data.data_frame
num_of_ingredients = data_processing.data.num_of_ingredients

class Drink(BaseModel):
    name: str
    alcoholic: str
    category: str
    glass: str
    ingredients: List[Dict]
    instructions: str


"""
This function creates a json that contains the drink detail and recipe from the 
drink record. 
@:param drink_record: the record from the dataframe that contains the data of 
                      the drink to make json from
@:param num_of_ingredients: the maximum number of ingredients that can appears 
                            in drink record
@:return json that contains the drink's details and recipe
"""
def to_json(drink_record):
    ingredients = []
    for ingredient_index in range(num_of_ingredients):
        index = str(ingredient_index + 1)
        ingredient = {"ingredient": drink_record["strIngredient"
                                                 + index].values[0],
                      "measure": drink_record["strMeasure" + index].values[0]}
        if ingredient["ingredient"] != "":
            ingredients.append(ingredient)
    return {"name": drink_record[constants.NAME_COLUMN].values[0],
            "alcoholic": drink_record["strAlcoholic"].values[0],
            "category": drink_record["strCategory"].values[0],
            "glass": drink_record["strGlass"].values[0],
            "ingredients": ingredients,
            "instructions": drink_record["strInstructions"].values[0]}


"""
This function checks the validation of the id number and return json that 
contains the recipe of the drink.
@:param drink_id - the id number of the wanted drink
@return result - json that contains the recipe of the drink 
"""
async def get_drink(drink_id):
    if drink_id not in df[constants.ID_COLUMN].unique():
        logging.error(constants.ID_NOT_EXIST_ERR % str(drink_id))
        raise HTTPException(
            status_code=404,
            detail=constants.ID_NOT_EXIST_ERR % str(drink_id))
    drink_id_cond = df[constants.ID_COLUMN] == drink_id
    result = to_json(drink_record=df[drink_id_cond])
    return result


"""
This function gets list of ingredients and return dataframe that contains all 
the drinks that at least one of the ingredients appear in their recipe.
@:param ingredients - the list of ingredients
@return results - the filtered dataframe 
"""
def get_df_contains_ingredient(ingredients):
    results = None
    for ingredient in ingredients:
        ingredient = " " + ingredient + " "
        contain_ingredient_cond = df.apply(
            lambda row: (" " + row.astype(str) + " ").str.
            contains(ingredient, case=False).any(), axis=1)

        temp_results = df[contain_ingredient_cond]  # drinks that contain
        # the current ingredient

        if results is None:  # update of the first iteration
            results = temp_results

        elif temp_results.shape[0] > 0:  # other iterations
            results = (pd.concat(objs=[results, temp_results]).
                       drop_duplicates().reset_index(drop=True))
    return results
