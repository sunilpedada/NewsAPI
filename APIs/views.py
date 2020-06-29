from django.shortcuts import render
from django.views.generic import View
import json
from newsapi import NewsApiClient
from rest_framework.views import APIView
from APIs.serializing import category_serializing,news_serializing
from rest_framework.response import Response
from APIs.models import Category
from django.http import HttpResponse
import re
import datetime
import pandas as pd
import operator
from django.db.models import Q
from functools import reduce
# Create your views here.
class callNewsAPI(View):
    def post(self,request):
        body=json.loads(request.body)
        date_format=datetime.datetime.strptime(body["date"], '%Y-%m-%d')
        date=date_format.date()
        newsapi = NewsApiClient(api_key='f4690d7c570f4a42931ea222274b37df')
        categorys=["business","entertainment","general","health","science"]
        total_data_format=[]
        result={}
        for category in categorys:
            top_headlines = newsapi.get_top_headlines(q='bitcoin',category=category)
            articles=top_headlines["articles"]
            count=0
            for element in articles:
                data_format={}
                date_splite=re.split("[a-zA-Z]",element["publishedAt"])
                date_format_str=date_splite[0]+date_splite[1]
                date_format=datetime.datetime.strptime(date_format_str, '%Y-%m-%d%H:%M:%S')
                if date_format.date()==date:
                    print("date is ok")
                    data_format.update({"category":category,"name":element["source"]["name"],"author":str(element["author"]),"title":element["title"],"description":element["description"],"published":date_format,"urlToImage":element["urlToImage"]})
                    total_data_format.append(data_format)
                    count+=1
                # print(data_format)
            result.update({category:{"count":count}})
        serialized=category_serializing(data=total_data_format,many=True)
        if serialized.is_valid():
            serialized.save()
            result.update({"category_status":201})
            print("ok")
        else:
            result.update({"category_status":400})
        return HttpResponse(json.dumps(result),status=result["category_status"],content_type="application/json")
class news_details(View):
    def get(self,request,**kwarg):
        raw_body=request.body
        body=json.loads(raw_body)
        date_field=body["date"]
        date_list=pd.date_range(start=date_field[0],end=date_field[1])
        #data=Category.objects.filter(published__in=date_list)
        #data=Category.objects.filter(category__in=["science","business"])
        data=Category.objects.filter(category__in=body["category"])|Category.objects.filter(published__in=date_list)
        result=[]
        status=400
        for q in data:
            result.append({"category":q.category,"author":q.author,"title":q.title,"description":q.description,"published":q.published,"urlToImage":q.urlToImage})
        if result:
            status=200
            result_dump=json.dumps(result,indent=4, sort_keys=True, default=str)
            return HttpResponse(result_dump,status=status,content_type="application/json")
        msg=json.dumps({"error":"data is not avaliable"})
        return HttpResponse(msg,status=status,content_type="application/json")