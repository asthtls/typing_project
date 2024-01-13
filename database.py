# db 연동 MongoDB 7.0 Windows

from pymongo import MongoClient
import datetime
# DB 생성 및 Auto Commit
# DB 경로
client = MongoClient("mongodb://localhost:27017")
db = client['typing_game']
records = db['records']


def insert_record(cor_cnt, et):
    record = {
        "cor_cnt":cor_cnt,
        "record" : et,
        "regdate": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    records.insert_one(record)
