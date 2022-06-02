import requests
from bs4 import BeautifulSoup

url = "https://www.trustpilot.com/review/crypto.com"
result = requests.get(url).content

doc = BeautifulSoup(result, "html.parser")


names = doc.find_all(class_ = "typography_typography__QgicV typography_bodysmall__irytL typography_weight-medium__UNMDK typography_fontstyle-normal__kHyN3 styles_consumerName__dP8Um")
titles = doc.find_all(class_ = "link_internal__7XN06 typography_typography__QgicV typography_weight-inherit__iX6Fc typography_fontstyle-inherit__ly_HV link_notUnderlined__szqki typography_color-inherit__TlgPO")
descriptions = doc.find_all(class_ = "typography_typography__QgicV typography_body__9UBeQ typography_color-black__5LYEn typography_weight-regular__TWEnf typography_fontstyle-normal__kHyN3")
repliesFrom = doc.find_all(class_ = "typography_typography__QgicV typography_bodysmall__irytL typography_weight-heavy__E1LTj typography_fontstyle-normal__kHyN3 styles_replyCompany__ro_yX")
replies = doc.find_all(class_ = "typography_typography__QgicV typography_bodysmall__irytL typography_color-gray-7__9Ut3K typography_weight-regular__TWEnf typography_fontstyle-normal__kHyN3 styles_message__shHhX")
frameList = []

for i in range(len(names)):
  dataDict = {"Username": "", "Title" : "" ,"Description" : "", "ReplyFrom" : "", "Reply": ""}
  
  replyFrom = repliesFrom[i].string
  replyFrom = replyFrom.replace("Reply from ", "")

  dataDict['Username'] = names[i].string
  dataDict['Title'] = titles[i].string
  dataDict['Description'] = descriptions[i].string
  dataDict['ReplyFrom'] = replyFrom
  dataDict['Reply'] = replies[i].string

  frameList.append(dataDict)


df = pd.DataFrame(frameList)
df.to_csv('Feedback.csv')

print(df)
