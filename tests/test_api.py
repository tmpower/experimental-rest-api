# call: pytest -v test_api.py::TestApi

import pytest
import requests

url = 'http://127.0.0.1:5000' # The root url of the flask app

class TestApi():
    def test_get_games(self):
        response = requests.get(url+'/games')
        data = response.json()

        assert response.status_code == 200
        assert data['games'] == 0

    def test_delete_game(self):
        response = requests.delete(url+'/games/1')
        data = response.json()

        assert response.status_code == 204
        assert len(data) == 0

# def test_get_games(client):
#     response = client.get("/api/games")
#     assert response.status_code == 200
#     assert response.data["games"] ==  
