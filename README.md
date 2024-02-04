# Drinks Application

## Introduction
#### This application exposes a recipe of drinks and cocktails.
#### It includes different search options and allows you to filter the drinks by the ingredients you have at home. 
#### You are invited to try one of these drinks to dinner!
## Usage

1. To get a list of all the drinks names and id numbers - use the url: http://127.0.0.1:8000/all_drinks/ .
2. To get specific drink by its id number - use the url: http://127.0.0.1:8000/drink/ and provide the id number after the "/".
    #### for example: http://127.0.0.1:8000/drink/14029
3. To get list of drinks by their id numbers - use the url: http://127.0.0.1:8000/drinks_by_ids/?id=<id_num_1>&id=<id_num_2> (replace <id_num_i> with the id number you want). the list can be in any length you choose.
    #### for example: http://127.0.0.1:8000/drinks_by_ids/?id=14029&id=15395&id=15423
4. To get list of drinks that contain at least one of an ingredients list - use the url: http://127.0.0.1:8000/drinks_by_ingredients/any/?ingredients=<ingredient_1>&ingredients=<ingredient_2> (replace <ingredient_i> with the i'th ingredient from the ingredients list)
    #### for example: http://127.0.0.1:8000/drinks_by_ingredients/any/?ingredients=vodka&ingredients=orange
5. To get list of drinks that contain all of an ingredients list - use the url: http://127.0.0.1:8000/drinks_by_ingredients/all/?ingredients=<ingredient_1>&ingredients=<ingredient_2> (replace <ingredient_i> with the i'th ingredient from the ingredients list)
    #### for example: http://127.0.0.1:8000/drinks_by_ingredients/all/?ingredients=vodka&ingredients=orange

### Logs:
Logs of the app can be found under: logs/ ProjectLogs_{Date}.log .

Logs of the unit test can be found under: logs/ testsLogs_{Date}.log .
## Data Source

The Data of this application was taken from Kaggle site:
https://www.kaggle.com/datasets/ai-first/cocktail-ingredients/