from django.conf.urls import url
from APIs.views import callNewsAPI,news_details
urlpatterns=[
    url(r"^fetch-news/$",callNewsAPI.as_view()),
    url(r"^list-news/$",news_details.as_view())
]