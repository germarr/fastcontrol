import psycopg2
import psycopg2.extras
import csv
import pandas as pd
from datetime import datetime, timedelta
import json

datefile = "df_8_26_2021"

def data_to_dict(datefile=datefile):
    conn = psycopg2.connect("host=34.66.221.94 port=5432 dbname=book_db user=postgres password=password")
    cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cur.execute(f'SELECT * FROM {datefile} ORDER BY dislikecount desc')
    fulldf = cur.fetchall()
    df = [{
    "channel_id":str(i['channel_id']),
    "channel_title":str(i["channel_title"]),
    "video_id":str(i["title"]),
    "publishedAt":str(i["publishedat"]),
    "title":str(i["title"]),
    "viewCount":int(i["viewcount"]),
    "likecount":int(i["likecount"]),
    "dislikeCount":int(i["dislikecount"]),
    "commentCount":int(i["commentcount"]),
    "thumbnail":str(i["thumbnail"]),
    "link":str(i["link"]),
    "video_lang":str(i["video_lang"]),
    "categoryId":str(i["categoryid"]),
    "CountriesTreding":int(i["sum_of_countries"]),
    "AR":int(i["ar"]),
    "AU":int(i["au"]),
    "BO":int(i["bo"]),
    "BR":int(i["br"]),
    "CA":int(i["ca"]),
    "CL":int(i["cl"]),
    "CO":int(i["co"]),
    "CR":int(i["cr"]),
    "DE":int(i["de"]),
    "EC":int(i["ec"]),
    "ES":int(i["es"]),
    "FR":int(i["fr"]),
    "GB":int(i["gb"]),
    "IN":int(i["india"]),
    "IT":int(i["it"]),
    "JP":int(i["jp"]),
    "KR":int(i["kr"]),
    "MX":int(i["mx"]),
    "PE":int(i["pe"]),
    "PT":int(i["pt"]),
    "US":int(i["us"]),
    "UY":int(i["uy"])
    } for i in fulldf]
    
    return df

if __name__ == "__main__":
    # execute only if run as a script
    data_to_dict()

