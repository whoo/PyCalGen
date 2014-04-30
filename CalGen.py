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
evt.add('dtstart',datetime(2014,04,29,20,0,0,tzinfo=pytz.timezone('America/Montreal')))
evt.add('dtend',datetime(2014,04,29,21,0,0,tzinfo=pytz.timezone('America/Montreal')))
evt.add('summary','Evenement secret')
evt.add('description','Generated Evenement')

cal.add_component(evt)


#evt2=Event()
#evt2.add('dtstart',datetime(2014,04,30,20,0,0,tzinfo=pytz.timezone('America/Montreal')))
#evt2.add('dtend',datetime(2014,04,30,21,0,0,tzinfo=pytz.timezone('America/Montreal')))
#cal.add_component(evt2)


f=open('example.ics','wb')
f.write(cal.to_ical())
f.close()
