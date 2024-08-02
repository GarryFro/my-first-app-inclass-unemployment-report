
# this is the "app/alpha.py" file..

import os
from dotenv import load_dotenv

load_dotenv() # look in the .evn file for env vars 

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo") #you dont need the demo
#if you forget to set your api key, it will default back to demo
