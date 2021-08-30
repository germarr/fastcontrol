from typing import Optional
from fastapi import FastAPI
from youtube_dash import main
from youtube_trending import data_to_dict, flags
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins=['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/youtube_dash/{URL}")
def get_data(URL:str=None):
    """
    Grab the main stats from a sinngle Youtube Channel. To test this API call copy a youtube line and split it on the "?" sign. 
    You should en up with "v=<some random symbols>"
    """
    data = main(mainURL=URL)
    
    return{
        "items":data
    }


@app.get("/trending/{country}")
def get_country(country:str="MX", values:int=5):
#db = get_videolist(countries = ['AR', 'AU', 'BO', 'BR', 'CA', 'CL', 'CO', 'CR', 'DE', 'EC', 'ES', 'FR', 'GB', 'IN', 'IT', 'JP', 'KR', 'MX', 'PE', 'PT', 'US', 'UY'] , date = date_new)
    db = data_to_dict(q=f'SELECT * FROM df_8_26_2021 WHERE {country.lower()} >= 1 ORDER BY dislikecount desc LIMIT {values}')
    flag_list = flags(pais=country, valor=values)
    
    return {
        "items":db,
        "flags":flag_list
    }