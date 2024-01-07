import logging

from fastapi.testclient import TestClient
from src.main import app
import tests.expected_jsons


client = TestClient(app)

def test_get_by_id():

    response = client.get(url="http://127.0.0.1:8000/drink/14029",
                          headers={'Accept': 'application/json'})
    assert response.status_code == 200
    assert response.json() == tests.expected_jsons.get_by_id_1
    logging.info("pass test")

    response = client.get(url="http://127.0.0.1:8000/drink/14555",
                          headers={'Accept': 'application/json'})
    assert response.status_code == 200
    assert response.json() == tests.expected_jsons.get_by_id_2
    logging.info("pass test")

def test_get_by_ids():

    response = client.get(
        url="http://127.0.0.1:8000/drinks_by_ids/?id=14029&id=15395&id=15423",
        headers={'Accept': 'application/json'})
    assert response.status_code == 200
    assert response.json() == tests.expected_jsons.get_by_ids_1
    logging.info("pass test")

    response = client.get(url="http://127.0.0.1:8000/drinks_by_ids/?id=11",
                          headers={'Accept': 'application/json'})
    assert response.status_code == 404
    assert response.json() == tests.expected_jsons.get_by_ids_2
    logging.info("pass test")

def test_get_by_exact_ingredients():

    response = client.get(url="http://127.0.0.1:8000/drinks_by_ingredients/?ingredients=vodka&ingredients=orange",
                          headers={'Accept': 'application/json'})
    assert response.status_code == 200
    assert response.json() == tests.expected_jsons.get_by_exact_ingredients_1
    logging.info("pass test")

    response = client.get(
        url="http://127.0.0.1:8000/drinks_by_ingredients/?ingredients=shir",
        headers={'Accept': 'application/json'})
    assert response.status_code == 404
    assert response.json() == tests.expected_jsons.get_by_exact_ingredients_2
    logging.info("pass test")

def test_all_drinks_names_ids():

    response = client.get(
        url="http://127.0.0.1:8000/all_drinks/",
        headers={'Accept': 'application/json'})
    assert response.status_code == 200
    assert response.json() == tests.expected_jsons.all_drinks_names_ids_1
    logging.info("pass test")



