FROM python:3.7
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
# EXPOSE 5000
# CMD ["python", "run.py"]
CMD ["gunicorn", "-b", "0.0.0.0:5000", "games:create_app('games.config.DevConfig')"]
