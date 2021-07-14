import requests
from pygame import mixer 
from datetime import datetime, timedelta
import time


age = 23 #you age
district_id = 307 #district which you want to check for
pincodes = ["686671","686661","686692","686691"] #the pincodes in the district which you want to check against

actual = datetime.today().strftime("%d-%m-%Y")

URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={did}&date={date}".format(did=district_id,date=actual)
header = {'accept':'application/json','Accept-Language':'en_US'}

while True:
    
    result = requests.get(URL, headers=header)
    
    if result.ok and result.json()['centers']:
        for i in result.json()['centers']:
            if str(i['pincode']) in pincodes:
                if i['sessions'][0]['available_capacity_dose1']>0 and i['sessions'][0]['min_age_limit']<age:
                    print("Center Name: ",i['name'])
                    print('Center Address : ',i['address'])
                    print('Block Name:',i['block_name'])
                    print('Date : ',i['sessions'][0]['date'])
                    print("Vaccine : ",i['sessions'][0]['vaccine'])
                    print("Fee :",i['fee_type'])
                    print("----------------------------------------")
                    mixer.init()
                    mixer.music.load('sound/dingdong.wav')
                    mixer.music.play()
                else:
                    print("Search Completed , No Vaccine Available")
                    
    time.sleep(40)
