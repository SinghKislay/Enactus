import requests
import time
headers = {'Authorization': 'Token eca427d26c5475d13ccc546d730c88da5acab494'}

'''
url = "http://vituc.pythonanywhere.com/api/data/"
data = {'query':'prak'}
r = requests.get(url,data=data, headers=headers)
print(r.json())
time.sleep(3)
'''

'''
url = "http://vituc.pythonanywhere.com/api/update_data/"
data={'username':'prak','name':'prateek Kumar','location':'ayodhya','starting_time':'267'}
p=requests.post(url,data=data,headers=headers)
print(p.json())
'''

'''
url = "http://vituc.pythonanywhere.com/api/service_request/"
data={'username':'prak','date':'11/3/2019','timeslot':'evening','worktime':123}
p=requests.post(url,data=data,headers=headers)
print(p.json())
'''

'''
url = "http://vituc.pythonanywhere.com/api/service_request/"
data={'date':'11/3/2019'}
r = requests.get(url,data=data, headers=headers)
print(r.json())
time.sleep(3)
'''

'''
url = "http://vituc.pythonanywhere.com/api/employee_request/"
data = {'username':'lawliet','working':1}
p=requests.post(url,data=data,headers=headers)
print(p.json())
'''

'''
url = "http://vituc.pythonanywhere.com/api/employee_request/"
p=requests.get(url,headers=headers)
print(p.json())
'''