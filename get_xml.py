import requests
import json

url = "http://118.184.217.73:7182/ReportStudent/SLabStatisticPage/GetLabStatisticList"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
    "Referer":"http://118.184.217.73:7182/ReportStudent/SLabStatisticPage/GetLabStatisticList",
    "Cookie":"COOKIES_KEY_USERNAME=41824000; ASP.NET_SessionId=fx1nlikdt4kun2f0affzlckr"
              
}

data = {
    "LABTYPEID": -999,
    "LABNAME":"", 
    "ClassName":"", 
    "pageIndex": 1,
    "pageSize": 10,

}

base_url = "http://118.184.217.73:7182/"

def get_response():
    response = requests.post(url=url, headers=headers,data=data)

    try:
        if response.status_code == 200:
            return response.text
        else:
            print(response.status_code)
    except BaseException as e:
        print(e.args)


def get_xml(response):
    html = json.loads(response)
    datalists = html["DataList"]
    for datalist in datalists:
        print(base_url+datalist["LabDateUrl"])
        



if __name__ == "__main__":
    get_xml(get_response())



