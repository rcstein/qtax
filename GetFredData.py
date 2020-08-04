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
        
class Releases(FredAPI):
    def __init__(self):
        super.__init__(self, api_key)
        self.root_url = self.root_url + "releases"
        
class Tags(FredAPI):
    def __init__(self):
        super.__init__(self, api_key)
        self.root_url = self.root_url + "tags"
        
class Sources(FredAPI):
    def __init__(self):
        super.__init__(api_key)
        self.root_url = self.root_url + "sources"
        
class Series(FredAPI):
    def __init__(self, api_key, series_id = 3):
        super().__init__(api_key)
        self.series_id = series_id
        self.root_url = self.root_url + "series"

        
    def get_data(self, file_type = 'json', **kwargs):
        url = self.root_url + '/observations?series_id={}&api_key={}'.format(self.series_id,self.api_key)
        for key, val in kwargs.items():
            url += '&{}={}'.format(key,val)
        if file_type == 'json':
            return JSONResponse(url,'observations')
        elif file_type == 'txt':
            return self._get_as_text(url)

class JSONResponse():
    def __init__(self, url, nested_data_name):
        self.response = json.loads(requests.get(url + '&file_type=json').text)
        self.data = json_normalize(self.response[nested_data_name])
        
    def to_pandas(self):
        return pd.read_json(self.data,orient = 'records')
    
    def save(self, path = './'):
        """Save retrieved data as csv. Default location is current directory."""
        pass

