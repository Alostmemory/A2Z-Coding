url = 'https://www.zohoapis.eu/crm/v2/functions/mass_update_recruit_records_contacts/actions/execute?auth_type=apikey&zapikey=1003.96a9752a3baf2798f1fc233bf270f413.68e027025f91915074e9042a6b4b71a8'
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
