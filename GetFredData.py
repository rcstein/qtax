#!/usr/bin/env python
# coding: utf-8

# In[51]:


key = 'a250df75af2accf2846eacbb9ceaa4fd'
import os
import json
import requests
import pandas as pd
from pandas.io.json import json_normalize 

class FredAPI():
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.root_url = 'https://api.stlouisfed.org/fred/'
    
class Category(FredAPI):
    def __init__(self,category_id):
        super.__init__(self, api_key)
        self.root_url = self.root_url + "category"
        self.category_id = category_id
        
    def get(self):
        url = self.root_url + '?category_id={}&api_key={}'.format(self.category_id,self.api_key)
        return JSONResponse(url,'categories').data
    
    def get_children(self):
        url = self.root_url + '/children?category_id={}&api_key={}'.format(self.category_id,self.api_key)
        return JSONResponse(url,'categories').data
    
    def get_related(self):
        url = self.root_url + '/related?category_id={}&api_key={}'.format(self.category_id,self.api_key)
        return JSONResponse(url,'categories').data
    
    def get_series(self,**kwargs):
        url = self.root_url + '/series?category_id={}&api_key={}'.format(self.category_id,self.api_key)
        for key, val in kwargs.items():
            url += '&{}={}'.format(key,val)
        return JSONResponse(url,'seriess').data
    
    def get_tags(self,**kwargs):
        url = self.root_url + '/tags?category_id={}&api_key={}'.format(self.category_id,self.api_key)
        for key, val in kwargs.items():
            url += '&{}={}'.format(key,val)
        return JSONResponse(url,'tags').data
    
    def get_related_tags(self,**kwargs):
        url = self.root_url + '/tags?category_id={}&api_key={}'.format(self.category_id,self.api_key)
        for key, val in kwargs.items():
            url += '&{}={}'.format(key,val)
        return JSONResponse(url,'tags').data
    
class Releases(FredAPI):
    def __init__(self):
        super.__init__(self, api_key)
        self.root_url = self.root_url + "releases"
        
class Tags(FredAPI):
    def __init__(self):
        super.__init__(self, api_key)
        self.root_url = self.root_url + "tags"
        
    def get_tags(self,**kwargs):
        url = self.root_url + '/tags?&api_key={}'.format(self.api_key)
        for key, val in kwargs.items():
            url += '&{}={}'.format(key,val)
        return JSONResponse(url,'tags').data
    
    #def get_series(self, tags, **kwargs):
        #url = self.root_url + '/series?tag_names='
        #'#&api_key={}'.format(self.api_key)
        
class Sources(FredAPI):
    def __init__(self):
        super.__init__(api_key)
        self.root_url = self.root_url + "sources"
        
class Series(FredAPI):
    def __init__(self, api_key, series_id):
        super().__init__(api_key)
        self.series_id = series_id
        self.root_url = self.root_url + "series"
        
    def get_data(self, file_type = 'json', **kwargs):
        url = self.root_url + '/observations?series_id={}&api_key={}'.format(self.series_id,self.api_key)
        for key, val in kwargs.items():
            url += '&{}={}'.format(key,val)
        return JSONResponse(url,'observations').data

class JSONResponse():
    def __init__(self, url, nested_data_name):
        self.response = json.loads(requests.get(url + '&file_type=json').text)
        self.data = json_normalize(self.response[nested_data_name])

    def save(self, path = './', **kwargs):
        """Save retrieved data as csv. Default location is current directory. Kwargs passed
        to pandas data frame .to_csv() method."""
        self.data.to_csv(path, **kwargs)

