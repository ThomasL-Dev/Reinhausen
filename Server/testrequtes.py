import requests

r = requests.post("http://92.157.253.9:5002/api/connect/admin/admin")

print(r.text)