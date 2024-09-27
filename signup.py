import requests
import sys




def signup():


        url ='http://127.0.0.1:8000/signup'

        data = {'username':'costica',
                'password':'12Giiaw',
                'confirm_password':'12Giiaw',
                'email':'gigi@gmail.com',
                'date_joined': '2020-12-07' 
                }





        res = requests.post(url=url,data=data)
        print(res.status_code,res.url)
        print(res.text)
    



def show_users():
        url ='http://127.0.0.1:8000/signup'


        res = requests.get(url=url)
        print(res.status_code,res.url)
        print(res.text)



def signin():
        url ='http://127.0.0.1:8000/signin'

        data = {'username':'costica','password':'12Giiaw'}

        res = requests.post(url=url,data=data)
        print(f'{res.status_code}\n{res.url}')
        print(res.text)




if __name__ == '__main__':
        
        if sys.argv[1] == 'signup':
                show_users()
        elif sys.argv[1]=='show users':
                signup()        
        elif sys.argv[1]== 'signin':
                signin()

        else:
                exit()



