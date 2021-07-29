# Flask example for creating a model API

## Dependencies

	pip install scikit-learn
	pip install flask
	pip install unicorn
	pip install resquests


## Steps to run locally
1. Run
	
	python train_save.py

to train and save a model using pickle

2. Run

	python flask_example.py

to run a flask server on your local machine

3.

	python request_example.py

to call your model on the server and get some response


## Steps to deploy it on a public server using Heroku

1. Install Heroku CLI. [Official documentation](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

2. Create an account on [Heroku](https://id.heroku.com/login)

2. Open a terminal and fo to the folder containing our files (here flask_example).

3. run

	heroku create


## References

https://devcenter.heroku.com/articles/heroku-cli#download-and-install
https://www.heroku.com/python
