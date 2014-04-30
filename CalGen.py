#!/opt/local/bin/python
##### Need to import pip icalendar
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#	
#	Copyright 2014	<Dominique DERRIER>

from icalendar import Event,Calendar
from datetime import datetime
import pytz

cal=Calendar()
evt=Event()

cal['X-CALENDARSERVER-ACCESS']		="CONFIDENTIAL"
# CONFIDENTIAL | PUBLIC

#evt.add('dtstart',datetime(2014,04,29,20,0,0,tzinfo=pytz.timezone('America/Montreal')))
#evt.add('dtend',datetime(2014,04,29,21,0,0,tzinfo=pytz.timezone('America/Montreal')))
#evt.add('summary','Evenement secret')
#evt.add('description','Generated Evenement')
#
#cal.add_component(evt)


#evt2=Event()
#evt2.add('summary','Multiple Day')
#evt2.add('dtstart;VALUE=DATE','20140429')
#evt2.add('dtend;VALUE=DATE','20140501')
#cal.add_component(evt2)


from datetime import timedelta

f=open('dd.csv','r')
# read CVS file > DATE ; Event to produce calendar | full day
for a in f.read().splitlines():
	evt=Event()
	(t,v)= a.split(';')
	(d,m,y)=t.split('/')
	date = datetime(int(y),int(m),int(d))
	dstart= date.strftime('%Y%m%d')
	dtend= (date+timedelta(1)).strftime('%Y%m%d')
	evt.add('summary',v)
	evt.add('dtstart;VALUE=DATE',dstart)
	evt.add('dtend;VALUE=DATE',dtend)
	cal.add_component(evt)
f.close()

f=open('example.ics','wb')
f.write(cal.to_ical())
f.close()
