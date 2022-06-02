import json

import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup

from datetime import datetime

import time as tim


forumLink=['https://www.cryptocompare.com/api/forum/get/posts/?tId=1182&tPosts=20','https://www.cryptocompare.com/api/forum/get/posts/?tId=310829&tPosts=20','https://www.cryptocompare.com/api/forum/get/posts/?tId=7605&tPosts=20','https://www.cryptocompare.com/api/forum/get/posts/?tId=5031&tPosts=20']





frameList=[]

def forum_crawler(cryptoName):
    print(cryptoName)

    if cryptoName is "BTC":
        # Setting up the soup object

        postedItem = json.loads(requests.get(forumLink[0]).content)["PostArray"]

        print(postedItem)


        for p in range (len(postedItem)):
            dataDict = {"Username": "", "Time": "", "Message": "", "Reply": "", "Like": 0, "Dislike": 0}

            username= postedItem[p]["Cryptopian"]["Name"]
            print(username)
            print(dataDict["Username"])
            dataDict["Username"]=username
            print(dataDict["Username"])

            time= postedItem[p]["Timestamp"]
            print(type(time))
            # time=datetime.fromtimestamp(time)
            # print(time)
            dataDict["Time"]=time

            msg=postedItem[p]["Body"]
            print(msg)
            dataDict["Message"]=msg

            reply=postedItem[p]["Actions"]["Comment"]["Total"]
            dataDict["Reply"]


            like=postedItem[p]["Actions"]["Agree"]["Total"]
            dataDict["Like"]=like


            dislike=postedItem[p]["Actions"]["Disagree"]["Total"]
            dataDict["Dislike"]=dislike



            frameList.append(dataDict)



    elif cryptoName == "ETH":
        # Setting up the soup object

        postedItem = json.loads(requests.get(forumLink[2]).content)["data"]

        for p in range(len(postedItem)):
            dataDict = {"Username": "", "Time": "", "Message": "", "Reply": "", "Like": 0, "Dislike": 0}
            username = postedItem[p]["Cryptopian"]["Name"]
            print(username)
            dataDict["Username"] = username

            time = postedItem[p]["Timestamp"]
            print(type(time))
            # time=datetime.fromtimestamp(time)
            # print(time)
            dataDict["Time"] = time

            msg = postedItem[p]["Body"]
            print(msg)
            dataDict["Message"] = msg

            reply = postedItem[p]["Actions"]["Comment"]["Total"]
            dataDict["Reply"]

            like = postedItem[p]["Actions"]["Agree"]["Total"]
            dataDict["Like"] = like

            dislike = postedItem[p]["Actions"]["Disagree"]["Total"]
            dataDict["Dislike"] = dislike

            frameList.append(dataDict)


    elif cryptoName == "XRP":
        # Setting up the soup object

        postedItem = json.loads(requests.get(forumLink[3]).content)["data"]

        for p in range(len(postedItem)):
            dataDict = {"Username": "", "Time": "", "Message": "", "Reply": "", "Like": 0, "Dislike": 0}
            username = postedItem[p]["Cryptopian"]["Name"]
            print(username)
            dataDict["Username"] = username

            time = postedItem[p]["Timestamp"]
            print(type(time))
            # time=datetime.fromtimestamp(time)
            # print(time)
            dataDict["Time"] = time

            msg = postedItem[p]["Body"]
            print(msg)
            dataDict["Message"] = msg

            reply = postedItem[p]["Actions"]["Comment"]["Total"]
            dataDict["Reply"]

            like = postedItem[p]["Actions"]["Agree"]["Total"]
            dataDict["Like"] = like

            dislike = postedItem[p]["Actions"]["Disagree"]["Total"]
            dataDict["Dislike"] = dislike

            frameList.append(dataDict)


    else:
        # Setting up the soup object

        postedItem = json.loads(requests.get(forumLink[1]).content)["data"]


        for p in range(len(postedItem)):
            dataDict = {"Username": "", "Time": "", "Message": "", "Reply": "", "Like": 0, "Dislike": 0}
            username = postedItem[p]["Cryptopian"]["Name"]
            print(username)
            dataDict["Username"] = username

            time = postedItem[p]["Timestamp"]
            print(type(time))
            # time=datetime.fromtimestamp(time)
            # print(time)
            dataDict["Time"] = time

            msg = postedItem[p]["Body"]
            print(msg)
            dataDict["Message"] = msg

            reply = postedItem[p]["Actions"]["Comment"]["Total"]
            dataDict["Reply"]

            like = postedItem[p]["Actions"]["Agree"]["Total"]
            dataDict["Like"] = like

            dislike = postedItem[p]["Actions"]["Disagree"]["Total"]
            dataDict["Dislike"] = dislike

            frameList.append(dataDict)


forum_crawler("BTC")

print(frameList)

df=pd.DataFrame(frameList)
df.to_csv('CryptocompareForum.csv')

print(df)