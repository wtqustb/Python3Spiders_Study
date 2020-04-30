import requests
import re
import json
import base64
import sys


base_url = "http://118.184.217.73:7182/"
posturl = "http://118.184.217.73:7182/ReportStudent/SLabStatisticPage/GetLabStatisticList"
headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    }

def get_base64(msg):
    msg = msg.encode('ascii')
    bs64 = base64.b64encode(msg)
    pattern = re.compile("b'(.*?)'")
    result = re.match(pattern,str(bs64))
    return result[1]


def login(user,password):
    url = "http://118.184.217.73:7182/Login/UserLogin"
    userId = get_base64(user)
    userPass = get_base64(password)
    data = {
        "userId": userId,
        "userPass": userPass
    }
    # 维持对话
    s = requests.Session()
    resp = s.post(url=url,headers=headers,data=data)

    # 获取xml文件的页面
    postdata = {
        "LABTYPEID": -999,
        "LABNAME":"", 
        "ClassName":"", 
        "pageIndex": 1,
        "pageSize": 10,

    }
    
    response = s.post(url=posturl,headers=headers,data=postdata)
    try:
        html = json.loads(response.text)
        datalists = html["DataList"]
        result = []
        for datalist in datalists:
            print(base_url+datalist["LabDateUrl"])
            result.append(datalist["LabDateUrl"])
        return result
    except BaseException as e:
        print("="*100)
        print("请确认输入的账号密码是否正确.....")
        sys.exit()



def get_xml(url):
    response = requests.get(url,headers)
    try:
        if response.status_code == 200:
            return response.content
        else:
            print(response.status_code)
    except BaseException as e:
        print(e.args)

def save_file(xml_urls):
    for xml_url in xml_urls:
        html = get_xml(base_url+xml_url)
        file_name = re.findall("[\u4e00-\u9fa5]+",xml_url)[0]
        with open(file_name+".xml","wb") as f:
            f.write(bytes(html))


if __name__ == "__main__":
    user = input("请输入你的学号：")
    password = input("请输入你的密码：")
    xml_urls = []
    xml_urls = login(user,password)
    save_file(xml_urls)
    


