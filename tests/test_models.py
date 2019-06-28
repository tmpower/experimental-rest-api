# call: pytest -v test_models.py::TestUsers or just py.test

import pytest
from games import create_app, db
from games.models import User
from flask import json


class TestUsers():

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


    def test_new_user(self, test_client):
        user1 = User()
        user1.username = "ezizdurdy1"
        user1.hash_password("password1")
        user2 = User()
        user2.username = "ezizdurdy2"
        user2.hash_password("password1")

        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

        assert user1.username == 'ezizdurdy1'
        assert not user1.verify_password('password')
