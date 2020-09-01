
import requests,re

def gettoken():

    #url
    url = 'http://api.app.33reading.cn/app/1/user/sign/loginp'

    data = {
        'mobile': '15210881156',
        'password': '111111'
    }
    r = requests.post(url,json=data) #请求url，获得返回的数据信息
    print("响应的json串",r.text)
    #print("响应的状态码",r.status_code)
    token = re.findall("(?:\"token\":\")([^\"]+)", r.text)
    #print ( "通过正则截取出来的结果",token )  # 这里是list  re.compile("(?:\"device_id\":\")([^\"]+)")
    return token

if __name__ == "__main__":
    gettoken()