import requests
import json

URL="http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    print("Hello here")
    data={}
    if id is not None:
        data={'id':id}

    json_data=json.dumps(data)
    
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)

#get_data()
def post_data():
    data={
        'name':'Samriddha',
        'roll':104,
        'city':'Kanchanpur'

    }
    json_data=json.dumps(data)
    print(URL)
    print(json_data)
    r=requests.post(url=URL,data=json_data)
    print(r)
    msg=r.json()
    print(msg)

post_data()