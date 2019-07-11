from games import create_app, db

app = create_app('games.config.DevConfig')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
