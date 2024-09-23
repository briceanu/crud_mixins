import requests



url = "http://127.0.0.1:8000/book/update/"
# url = "http://127.0.0.1:8000/book/update/fc87f380-bbf7-414b-8c9a-afc23278356c"


params = {
    'book_id': 'fc87f380-bbf7-414b-8c9a-afc23278356c'
}
data = {
    # 'name':'la tiganci',
        'name':'la scaldat aidnwa',
        'year_of_publish':1972,
        # 'author':'ion bulai deleanu'
        }

# headers={'Content-Type': 'application/json'}
#  inside the body of the dictionary is the updated data

save = requests.patch(url=url,data=data,params=params)
# patch = requests.put(url=url,data=data,params=params)

 
print(save.status_code,save.text)
# print(patch.status_code,patch.text)