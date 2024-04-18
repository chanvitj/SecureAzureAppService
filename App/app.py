from flask import Flask, request
import pymongo 
import os

app = Flask(__name__)

@app.route('/')
def hello():
  r = {"id": 1, "title": "This is JSON data from App-Tier. Test#12"}
  return r 

@app.route('/getinfo')
def getinfo():
  print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
  connectionString = os.environ.get('CONNECTION_STRING')
  databaseName = "jewdatabase"
  collectionName = "jewdemocollection"
  myclient = pymongo.MongoClient(connectionString)
  mydb = myclient[databaseName]
  mycol = mydb[collectionName]
  r=[]
  for d in mycol.find():
    del d['_id']
    r.append(d)
  print(r)

  ip = ""
  x_forwarded_for = False
  if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
    print("HTTP_X_FORWARDED_FOR is None.")
    print(request.environ['REMOTE_ADDR'])
    ip = request.environ['REMOTE_ADDR']
    x_forwarded_for = False
  else:
    print("HTTP_X_FORWARDED_FOR is not None.")
    print(request.environ['HTTP_X_FORWARDED_FOR'])
    ip = request.environ['HTTP_X_FORWARDED_FOR']
    x_forwarded_for = True

  # d={
  #   "IsXForwardedFor": x_forwarded_for,
  #   "REMOTE_ADDR": request.environ['REMOTE_ADDR'],
  #   "HTTP_X_FORWARDED_FOR": request.environ['HTTP_X_FORWARDED_FOR']
  # }
  # r.append(d)
  # print(r)
  # print(request)
  print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
  return r

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)


### Sample python using RestAPI connecting to MongoDB.
# import requests

# # Replace with actual API endpoint URL
# url = "https://api.example.com/data/users"

# # Replace with your API authentication credentials (if required)
# headers = {"Authorization": "Bearer YOUR_API_KEY"}  # Example with an API key

# # Send a GET request to retrieve data
# response = requests.get(url, headers=headers)

# # Check for successful response
# if response.status_code == 200:
#   # Parse the JSON response (assuming JSON format)
#   data = response.json()
#   print(data)  # This will print the retrieved data (potentially user information)
# else:
#   print(f"Error: {response.status_code}")
