from typing import Optional
from fastapi import FastAPI
from youtube_dash import main
from youtube_trending import data_to_dict

app = FastAPI()


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
    db = data_to_dict()
    country = country
    values= values
    country_videos = db.loc[db[country] >= 1].reset_index().head(values).transpose().to_dict()
    single_country = [country_videos[i] for i,x in enumerate(country_videos)]
    flag_list = []

    for i in range(values):
        valueOne = i
        valueTwo = i+1
        flags = db.loc[db[f"{country}"] == 1].iloc[valueOne:valueTwo,15:-2].reset_index().iloc[:,1:].transpose().reset_index().rename(columns={0:"counts"}).query('counts >0').set_index("index").transpose().columns
        flag_list.append([])
            
        for si in range(len(flags)):
            flag_list[i].append(flags[si])
    
    return {
        "items":single_country,
        "flags":flag_list
    }