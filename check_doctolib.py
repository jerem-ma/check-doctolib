#!/bin/python3
import datetime
import time
import json

from gi.repository import Notify

import requests as rq

try:
    Notify.init('Check Doctolib')
    while True:
        today = datetime.date.today()
        day = str(today.day)
        month = str(today.month)
        year = str(today.year)
        #begin_date = year + "-" + month + "-" + day
        limit = 60 
        for i in range(0, limit//14 + 1):

            now = datetime.datetime.utcnow()
            raw_hour = now.hour + 2
            hour = "0" + str(raw_hour) if raw_hour < 10 else str(raw_hour)
            minute = "0" + str(now.minute) if now.minute < 10 else str(now.minute)
            second = "0" + str(now.second) if now.second < 10 else str(now.second)
            clock = '[' + hour + ':' + minute + ':' + second + '] '

            delta = datetime.timedelta(days=i*14)
            tmp_begin_date = today + delta

            availabilities_link = 'https://www.doctolib.fr/availabilities.json?start_date=' + str(tmp_begin_date) + '&visit_motive_ids=689642&agenda_ids=117589&insurance_sector=public&practice_ids=43475&limit=14'

            print(clock + str(tmp_begin_date))
            try:
                r = rq.get(availabilities_link, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1'})
            except rq.exceptions.ConnectionError:
                print(clock + " An error occured during connection")
                time.sleep(30)
                continue

            print(r.text)
            data = json.loads(r.text)
            availabilities = data['availabilities']
            if data['total'] == 0:
                print(clock + 'No one found !')

                for day_data in availabilities:
                    if len(day_data['slots']) == 0:
                        continue

                    next_date = day_data['date']
                    next_slots = day_data['slots']
                    hours = []
                    for slot in next_slots:
                        splited_time = slot.split('T')[1].split(':')
                        time_slot = splited_time[0] + ':' + splited_time[1]
                        hours.append(time_slot)

                    print(clock + next_date + "  " + str(hours))
                    notif = Notify.Notification.new('New appointment', 'Date : ' + next_date + '\n' + str(hours))
                    notif.set_timeout(35*1000)
                    notif.show()
            time.sleep(5)
        
        time.sleep(30)

except KeyboardInterrupt:
    Notify.uninit()
