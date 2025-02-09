from src import data_processing
from typing import Annotated
from fastapi import APIRouter, Query, Request, HTTPException
import logging
from src import constants, utilities
from src.models import Drink


router = APIRouter()
df = data_processing.data.data_frame

"""
This function returns the recipe of a drink by its ID number.
@:param id_drink: the ID number of the wanted drink
@:return json format of the drink's details and recipe
"""
@router.get(path="/drink/{drink_id}")
async def get_drink_by_id(request: Request, drink_id: int):
    logging.info(constants.START_MSG % str(request.url))
    result = await utilities.get_drink(drink_id)
    logging.info(constants.FINISH_MSG % str(request.url))
    return result


"""
This function returns all the drinks recipes that their id number appears in 
the given list.
@:param id: array of the id numbers of the wanted drinks
@:return json of the drinks details and recipes
"""
@router.get(path="/drinks_by_ids/", response_model=list[Drink.Drink])
async def get_drink_by_ids(request: Request,
                           id: Annotated[list[int] | None, Query()] = None):
    logging.info(constants.START_MSG % str(request.url))
    drinks = []
    num_of_ids = len(id)

    for cur_drink_id in range(num_of_ids):
        drinks.append(await utilities.get_drink(id[cur_drink_id]))

    logging.info(constants.FINISH_MSG % str(request.url))
    return drinks


"""
This function returns all the drink names that contain:
-> at least one ingredient from the given ingredients list *if any_or_all 
parameter is 'any'*.
-> all the ingredients in the list *if any_or_all parameter is 'all'*.
@:param ingredients: array of ingredients
@:param any_or_all: to choose which filter to apply
@:return json with array of all the names of the drinks that contain at least 
one ingredient from the given list
"""

@router.get(path="/drinks_by_ingredients/{any_or_all}/")
async def get_by_ingredients(request: Request, any_or_all: str, ingredients: Annotated[
        list[str] | None, Query()] = None):
    logging.info(constants.START_MSG % str(request.url))
    if any_or_all == "any":
        results = utilities.get_df_contains_any_ingredient_in_list(ingredients)
    elif any_or_all == "all":
        results = utilities.get_df_contains_all_ingredient_in_list(ingredients)
    else:
        logging.error(constants.WRONG_URL_PARAMETER)
        raise HTTPException(
            status_code=400,
            detail=constants.WRONG_URL_PARAMETER)

    if results.shape[0] > 0:  # creates name list of all the drinks in results
        names = (results[constants.NAME_COLUMN].to_string(index=False).
                 replace("\n", ","))
        logging.info(constants.FINISH_MSG % str(request.url))
        return {"drinks": " ".join(names.split())}

    logging.error(constants.EMPTY_FINISH_MSG)
    raise HTTPException(
        status_code=404,
        detail=constants.EMPTY_FINISH_MSG)


"""
This function returns the names and id numbers of all the drinks in the 
dataframe.
@:return json with list of all names and id numbers
"""
@router.get(path="/all_drinks/")
async def all_drinks_names_ids(request: Request):
    logging.info(constants.START_MSG % str(request.url))
    cur_data = df[[constants.NAME_COLUMN, constants.ID_COLUMN]]
    cur_data = cur_data.rename(columns={constants.NAME_COLUMN: "Name",
                                        constants.ID_COLUMN: "ID"})
    logging.info(constants.FINISH_MSG % str(request.url))
    return {"Drinks": cur_data.to_dict(orient="records")}
