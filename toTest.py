import requests
import json
def get_news(date):
    response=requests.post("http://127.0.0.1:8000/api/fetch-news/",data=json.dumps({"date":date}))
    print(response.json())
    print(response.status_code)
def get_records():
    response=requests.get("http://127.0.0.1:8000/api/list-news/",data=json.dumps({"date":["2020-06-26","2020-06-29"],"category":["business","science"]}))
    print(response.json())
    print(response.status_code)
#get_news("2020-06-28")
get_records()