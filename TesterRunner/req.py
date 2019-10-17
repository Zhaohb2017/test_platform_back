import requests,json
paramsCardPlayBack = {"id": 67631,
                      "sesskey":'100005-1569217353-101-65243e22cc2e489804763bc081340203-101-0-0' ,
                      "method": "Amember.getShareGameRecord",
                               }

url = "https://changdeqp.qqsgame.com/majiangcd/api/mobile/api.php?api="
data = url + json.dumps(paramsCardPlayBack)
req = requests.get(data)
print(req.text)
# print(PlayBack_data.text)