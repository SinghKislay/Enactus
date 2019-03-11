import requests
import time
url = "http://127.0.0.1:8000/api/employee_request/"
headers = {'Authorization': 'Token eca427d26c5475d13ccc546d730c88da5acab494'}

'''
data = {'query':'ram'}
r = requests.get(url,data=data, headers=headers)
print(r.json())
time.sleep(3)
'''

'''
data={'username':'enactus','name':'kislay Kunal Singh','location':'ayodhya','starting_time':'267'}
p=requests.post(url,data=data,headers=headers)
print(p.json())
'''
'''
data={'username':'prak','date':'11/3/2019','timeslot':'evening','worktime':123}
p=requests.post(url,data=data,headers=headers)
print(p.json())
'''
'''
r = requests.get(url, headers=headers)
print(r.json())
time.sleep(3)
'''
data = {'username':'lawliet','working':0}
p=requests.post(url,data=data,headers=headers)
print(p.json())