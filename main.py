#import statements
import time
import urllib2
import json
import os
#Date-Time functionality
#--------------------------------------------------------------------------
_date = time.strftime("%d/%m/%Y")
_time = time.strftime("%I:%M%p")
print _date
print _time

'''
#Weather functionality - courtesy of the weather underground API
#--------------------------------------------------------------------------
f = urllib2.urlopen('http://api.wunderground.com/api/YOUR_API_KEY/geolookup/conditions/q/IA/Rochester.json')
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
print "Current temperature in %s is: %s" % (location, temp_f)
f.close()
'''
#Add webcam functionality
#--------------------------------------------------------------------------


#Add Alarm functionality
#-------------------------------------------------------------------------
alarm_HH = input("What hour do you want to wake up? : ")
alarm_MM = input("What minute do you want to wake up? : ")
print("We're set for " + str(alarm_HH) + ":" + str(alarm_MM))

while True:
    now = time.localtime()
    if now.tm_hour >= int(alarm_HH) and now.tm_min  >= int(alarm_MM):
        print("Yup this works!")
        #os.popen("YOUR SONG / SOUND HERE")
        break
    else:
        time.sleep(10)
        print("not yet!")
        if now.tm_hour <= int(alarm_HH) and now.tm_min <= int(alarm_MM):
            break
