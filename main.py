#import statements
import time
import urllib2
import json


#Print the current date and time for reference
print time.strftime("%d/%m/%Y")
print time.strftime("%I:%M%p")


f = urllib2.urlopen('http://api.wunderground.com/api/ea509b7f81eea8a3/geolookup/conditions/q/IA/Rochester.json')
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
print "Current temperature in %s is: %s" % (location, temp_f)
f.close()
