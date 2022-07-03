import requests
# define the api url
url = 'https://jsonplaceholder.typicode.com/users'
# api call
response = requests.get(url)
# get the data from the response
data = response.json()
# giving the user wanted to find
options = '\n*** id - name - username - website - email - address - phone - company *** \n'
input = input(f"{options}\n--- What do you want to know about the user? : ")
# giving the all json data 
for i in data:
    # loop in the data
    for j in i:
        # check data in the json file
        if j == input:
            if j == 'address':
                print(f"{i['address']['street']} {i['address']['suite']} {i['address']['city']} {i['address']['zipcode']}")
                break
            if j == 'company':
                print(f"{i['company']['name']} {i['company']['catchPhrase']} {i['company']['bs']}")
                break
            # print data
            print(' -- ',i[j])