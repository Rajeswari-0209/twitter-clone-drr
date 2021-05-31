from django.shortcuts import render
from rest_framework import viewsets
from twittercloneapp.serializers import TweetSerializer
from .models import Tweet

class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all().order_by()
    serializer_class = TweetSerializer
   
