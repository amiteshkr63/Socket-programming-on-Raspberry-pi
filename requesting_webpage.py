import http.client
connection = http.client.HTTPSConnection("www.uci.edu",443)
connection.request("GET", "/")
response = connection.getresponse()
print("Status: {} and reason: {}".format(response.status, response.reason))
print(response.read(5000))
connection.close()



