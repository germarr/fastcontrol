from typing import Optional
from fastapi import FastAPI
from youtube_dash import main
from youtube_trending import data_to_dict, flags
from fastapi.middleware.cors import CORSMiddleware
from twitch import top_hundred, top_streamers,get_all_user_videos, topStreamsII

import urllib.parse


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
    query = f'SELECT * FROM df_8_26_2021 WHERE {country} >= 1 ORDER BY likecount desc LIMIT {values}'
    db = data_to_dict(q=query)
    flag_list = flags(q=query, valor=values)
    
    return {
        "items":db,
        "flags":flag_list
    }

@app.get("/tophundred")
def topvideos():
    """
    Bring the top 100 games that are streaming on Twitch right now.
    """
    vid = top_hundred()

    return vid

@app.get("/streamers/{language}")
def topTwitchStreamers(language:str="es"):
    """
    List of all the top Streamers onn Twitch right now.
    """
    streamers = top_streamers(lang=language)
    return streamers

@app.get("/streamervideos/{URL}")
def streamervideos(URL:str):
    """
    This function returns the last 100 videos from a streamer.
    """
    top100 = get_all_user_videos(channelURL=URL)
    
    return top100

@app.get("/topstreams/{language}/{q}")
def topstreams(language:str, q: Optional[int] = 1):
    """
    This function returns the last 100 videos from a streamer.
    """
    topstreamers = topStreamsII(loops=q,language=language)
    
    return topstreamers