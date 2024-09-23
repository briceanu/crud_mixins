
import requests




url = 'http://127.0.0.1:8000/deletebook'
# url = 'http://127.0.0.1:8000/removebook/'

params = {'book_id':'f45330a7-a747-4e35-bb1c-dd1e1035a852'}
# remove = requests.delete(url=url,params=params)
remove = requests.delete(url=url,params=params)



print(remove.url)
print(remove.status_code,remove.text)