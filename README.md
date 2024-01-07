# Drinks Application

## Introduction
#### This application contains database of recipes of drinks. It includes different search options and allows you to filter the drinks by the ingredients you have at home. You are invited to try one of this drinks to dinner!
## Usage

1. To get a list of all the drinks names and id numbers - use the url: http://127.0.0.1:8000/all_drinks/ .
2. To get specific drink by its id number - use the url: http://127.0.0.1:8000/drink/ and provide the id number after the "/". 
3. To get list of drinks by their id numbers - use the url: http://127.0.0.1:8000/drinks_by_ids/?id=<id_num_1>&id=<id_num_2> (replace <id_num_i> with the id number you want). the list can be in any length you choose.
4. To get list of drinks that contain at least one of an ingredients list - use the url: http://127.0.0.1:8000/drinks_by_ingredients/?ingredients=<ingredient_1>&ingredients=<ingredient_2> (replace <ingredient_i> with the i'th ingredient from the ingredients list)

## Data Source

The Data of this application was taken from Kaggle site:
https://www.kaggle.com/datasets/ai-first/cocktail-ingredients/