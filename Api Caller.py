url = 'https://www.zohoapis.eu/crm/v2/functions/mass_update_recruit_records_contacts/actions/execute?auth_type=apikey&zapikey=<api-key>'
runs = 130
import time
import requests
it = 0
while it < runs:
    it = it+1
    reply = requests.request("GET",url)
    print (reply.text.encode("utf-8"))
    print (str(runs - it) + " Runs remaining")
    time.sleep(4)
