
import requests




url = 'http://127.0.0.1:8000/deletebook'
params = {'book_id': 'f45330a7-a747-4e35-bb1c-dd1e1035a852'}

# Authorization headers
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3NDY5NTY5LCJpYXQiOjE3Mjc0NjkyNjksImp0aSI6IjBlYWRiNmFiZDdjNDQ1MzRhZWIyMDUzMDQ5ODkzMDJhIiwidXNlcm5hbWUiOiJjb3N0aWNhIn0.Vpb2iKTxoHRribKOxZGt44OtZRoYP2UjLWvtpjAo7O8'
}

# Sending the DELETE request with headers
remove = requests.delete(url=url, params=params, headers=headers)

print(remove.url)
print(remove.status_code,remove.text)