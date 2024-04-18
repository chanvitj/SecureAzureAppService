from flask import Flask, render_template
import requests
import json 
import socket
import platform
import os

# app = Flask(__name__)
app = Flask(__name__, template_folder='./')

@app.route('/')
def hello():
  print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
  fqdn = os.environ.get('APP_FQDN')
  # fqdn = "jewlab136-app.azurewebsites.net"
  # fqdn = "10.20.4.4"
  ip_json = json.loads(resolve_fqdn(fqdn))
  print("FQDN=" + fqdn)
  print("IP of FQDN=", ip_json)
  
  url = "https://" + fqdn + "/getinfo"
  headers = {'content_type': 'application/json'}
  method = 'GET'
  try:
    response = requests.request(method, url, headers=headers, verify=False)

    if response.status_code == 200:
      data = response.json()
      print("Data from App Tier is here.")
      print(type(data))
      # print(data)
      # data.append(ip_json)
      print(data)
      print("^^^^^^^^^^^^^^^^^^^^^^^^^^")
      # return data 
      return render_template("index.html", data=data)  # Pass data directly
    else:
      print("cannot access to app tier")
      print("^^^^^^^^^^^^^^^^^^^^^^^^^^")
      return f"Error[{response.status_code}]: cannot access to app tier"

  except requests.exceptions.RequestException as e:
    print(f"Error making request: {e}")
    print("cannot access to app tier")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^")
    return f"Error making request: {e}"
    
  # r = {"id": 1, "title": "This is Web-Tier. Test #11"}
  # return r 
  # data = [
  #     {"name": "Alice", "age": 30, "city": "New York"},
  #     {"name": "Bob", "age": 25, "city": "London"},
  # ]
  # return render_template("index.html", data=data)  # Pass data directly

def resolve_fqdn(fqdn):
  """
  Resolves a given FQDN to a list of IP addresses using DNS lookup.

  Args:
      fqdn: The FQDN to resolve (string).

  Returns:
      A JSON string containing the resolved IP addresses (string), 
      or an empty string if the resolution fails.
  """
  try:
    ips=socket.gethostbyname_ex(fqdn)
    print(ips)
    if platform.system() == "Windows":
      # Use nslookup on Windows
      ip_list = socket.gethostbyname_ex(fqdn)[2]
    else:
      # Use socket directly on Linux/macOS (prioritizes dnsquery)
      ip_list = socket.gethostbyname_ex(fqdn)[2]
  except socket.gaierror:
    # Resolution failed
    ip_list = []
  
  if ip_list:
    # Convert IP list to comma-separated string
    ip_string = ",".join(ip_list)
    return f'{{"IP": "{ip_string}"}}'
  else:
    return "{}"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)
