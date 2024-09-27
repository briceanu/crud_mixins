import requests


# 
url = 'http://127.0.0.1:8000/book'


data = {"name":'fapowfma',
        "author":'a;wodmadwo ',
        'year_of_publish':1960
        }

# 
params={'year_of_publish':1970}
# save = requests.post(url=url,data=data)
list_books = requests.get(url='http://127.0.0.1:8000/listbooks',params=params)



# print(save.status_code,save.text)
print(list_books.status_code,list_books.text)