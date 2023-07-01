import requests

url = 'https://api.stackexchange.com/2.3/questions?fromdate=1688083200&todate=1688256000&order=desc&sort=activity&tagged=Python&site=stackoverflow'

response = requests.get(url)
#print(response.json())

for i in range(len(response.json()['items'][0])):
    print(response.json()['items'][i]['title'])
