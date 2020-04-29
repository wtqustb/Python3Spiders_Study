import requests
import json

url = "http://118.184.217.73:7182/Login/UserLogin"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}

data = {
    "userId": "NDE4MjQwODk=",
    "userPass": "d2FuZ3RpYW5xaTg4NjY="
}

s = requests.Session()
resq = s.post(url=url,headers=headers,data=data)

posturl = "http://118.184.217.73:7182/ReportStudent/SLabStatisticPage/GetLabStatisticList"

postdata = {
    "LABTYPEID": -999,
    "LABNAME":"", 
    "ClassName":"", 
    "pageIndex": 1,
    "pageSize": 10,

}
base_url = "http://118.184.217.73:7182/"
response = s.post(url=posturl,headers=headers,data=postdata)
html = json.loads(response.text)
datalists = html["DataList"]
for datalist in datalists:
    print(base_url+datalist["LabDateUrl"])
