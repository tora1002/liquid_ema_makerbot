# -*- coding: utf-8 -*-
import sys
import os
import random
import ccxt

#### api keys #####
api_keys = [
    {"api_key": "1056960", "api_secret": "SR/ctMSNUoIiFC/5OxApAPCLCJguQMNemTHLUZTSSDno3RG16KxSART8cSS8LO8Cb2WAPQxE+Twh2mm7JWR+IQ=="},
    {"api_key": "1056960", "api_secret": "SR/ctMSNUoIiFC/5OxApAPCLCJguQMNemTHLUZTSSDno3RG16KxSART8cSS8LO8Cb2WAPQxE+Twh2mm7JWR+IQ=="},
    {"api_key": "1056960", "api_secret": "SR/ctMSNUoIiFC/5OxApAPCLCJguQMNemTHLUZTSSDno3RG16KxSART8cSS8LO8Cb2WAPQxE+Twh2mm7JWR+IQ=="},
    {"api_key": "1056960", "api_secret": "SR/ctMSNUoIiFC/5OxApAPCLCJguQMNemTHLUZTSSDno3RG16KxSART8cSS8LO8Cb2WAPQxE+Twh2mm7JWR+IQ=="},
    {"api_key": "1056960", "api_secret": "SR/ctMSNUoIiFC/5OxApAPCLCJguQMNemTHLUZTSSDno3RG16KxSART8cSS8LO8Cb2WAPQxE+Twh2mm7JWR+IQ=="}
]

num = random.randint(0,4)
using_key = api_keys[num]

API_KEY = using_key["api_key"]
API_SECRET = using_key["api_secret"]

##### set ccxt #####
liquid = ccxt.liquid({
    "apiKey" : API_KEY,
    "secret" : API_SECRET
})


