import requests
import time
url = "http://127.0.0.1:8000/api/update_data/"
headers = {'Authorization': 'Token fb79f081eb09fb2a0e542972a698b8d67a555ba3'}
'''
while True:
    r = requests.get(url, headers=headers)
    print(r.json())
    time.sleep(3)
'''
data={'name':'ram','location':'ayodhya','starting_time':'123'}
p=requests.post(url,data=data,headers=headers)
print(p.json())