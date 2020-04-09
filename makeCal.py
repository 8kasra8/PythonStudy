from datetime import date, datetime , timedelta
from icalendar import Calendar, Event

def add_to_cal (name_dob):
    now = date.today()
    cal = Calendar()
    for dicEntry in name_dob.items():

        event = Event()
        event.add('summary', dicEntry[0].title()+'\'s Birthday')
        event.add('description', dicEntry[1])

        dobString =  dicEntry[1].split(',')[0] + ' ' + str(now.year)
        dobObj= datetime.strptime(dobString, '%B %d %Y').date()
        dobTomorrow = dobObj + timedelta(days=1)

        event.add('dtstart', dobObj)
        event.add('dtend', dobTomorrow)
        cal.add_component(event)

        print (event)

    f = open('generatedByApp.ics', 'wb')
    f.write(cal.to_ical())
    f.close()

#testDic = {'kasra zanganeh':'December 16, 1982','mona zanganeh':'October 10, 1985'}
#add_to_cal(testDic)

#for item in testDic.items():
#    print(item[1])
#    dateob = datetime.strptime(item[1], '%B %d, %Y')
#    print(dateob)
