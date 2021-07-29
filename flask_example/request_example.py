import requests

url = 'http://localhost:5000/predict?index=10'

if __name__ == '__main__':
	print(requests.get(url).content)