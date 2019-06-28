# call: pytest -v test_api.py::TestApi or just py.test

import pytest
from games import create_app, db
from flask import json


class TestApi():

    @pytest.fixture(scope='module')
    def test_client(self):
        self.flask_app = create_app('games.config.TestConfig')
    
        testing_client = self.flask_app.test_client()

        ctx = self.flask_app.app_context()
        ctx.push()
        db.create_all()
    
        yield testing_client
    
        db.session.remove()
        db.drop_all()
        ctx.pop()


    def test_get_games(self, test_client):
        response = test_client.get('/api/v1.0/games')
        # data = json.loads(response.data)

        assert response.status_code == 200
        # assert data['games'] != 0


    def test_post_games(self, test_client):
        info = {"title": "CounterStrike", "token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU2MTQyMjAzOSwiZXhwIjoxNTYxNDIyNjM5fQ.eyJpZCI6MX0.xmB23WJsxxIVDscb1lACiVdUQwfGwXuciqpkdLqWILUWPYAL_zf7imw4l7Vr73x338wwLK_JBWUu2aIh6xBeYw"}
        response = test_client.post('/api/v1.0/games', data = json.dumps(info), content_type='application/json')
        # data = json.loads(response.data)

        assert response.status_code == 401


    def test_delete_game(self, test_client):
        info = {}
        info["token"] = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU2MTQyMjAzOSwiZXhwIjoxNTYxNDIyNjM5fQ.eyJpZCI6MX0.xmB23WJsxxIVDscb1lACiVdUQwfGwXuciqpkdLqWILUWPYAL_zf7imw4l7Vr73x338wwLK_JBWUu2aIh6xBeYw"
        response = test_client.delete('/api/v1.0/games/1', data = json.dumps(info), content_type='application/json')
        data = json.loads(response.data)

        assert response.status_code == 401
        assert "wrong credentials" in data['message']
