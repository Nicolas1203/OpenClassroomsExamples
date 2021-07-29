# Flask example for creating a model API

## Dependencies

	pip install -r requirements.txt


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

3. The easiest way (not the cleanest though) is to copy the useful file to a new directory to create a new repository for the API
	
		mkdir api
		cp Procfile flask_heroku.py trained_model.pkl requirements.txt ./api/
		cd api

4. initialize a local git repo for heroku

		git init
		git add Procfile flask_heroku.py trained_model.pkl requirements.txt
		git commit -m "First commit for heroku"

5. initialize heroku environment

	heroku create --buildpack heroku/python

6. deploy heroku server

		git push heroku master

or 

		git push heroku main

depending of your branch name.

7. Testing your reployed server. You should get an output saying its all running, at a specific address, e.g. https://calm-mountain-09944.herokuapp.com/. Check it in your browser and see the welcome message.

8. Test a prediction by addind 'predict?index=10' to the url. For example: https://calm-mountain-09944.herokuapp.com/predict?index=10


## References

https://devcenter.heroku.com/articles/heroku-cli#download-and-install
https://www.heroku.com/python
