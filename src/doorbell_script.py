import requests         # for making http calls
import xml.dom.minidom  # for parsing the XML data
import math             # to adjust volume correctly
import calendar         # to get pause timestamp of tracks
import time             # to get pause timestamp of tracks
from pydub import AudioSegment # to split the audio file due to lack of seeker for tracks
import urllib.request   # to convert url to uri and download the content locally
import pathlib          # to convert uri to url
import os               # to manipulate retalive and absolute local paths

# set the params:
ipaddr = "192.168.1.92" # enter your speaker IP address here
macaddr = "7C-01-0A-5C-D4-E1" # enter your speaker MAC address here
notification_sound_url = "https://freesound.org/data/previews/275/275571_4486188-hq.mp3" # enter the URL of the file you want to play here
service = "That word..." # Track name
reason = "...it does not mean..." # Artist name
message = "...what you think it means." # Album name
key = "0k0RQaOC1nTLHX1DbHZRXNnBpjAlZOTH" # enter your API key here
volumeVal = "40" # enter volume here, a number between 10 and 70

# form and send the /volume get request to get the current speakers volume
send = requests.get('http://' + ipaddr + ':8090/volume')
print(send.text)
responseXML = xml.dom.minidom.parseString(send.text)
volume_tag = responseXML.getElementsByTagName('volume')
responseXML_pretty = responseXML.toprettyxml()

# print (responseXML_pretty)
# print(volume_tag[0].childNodes[0].firstChild.nodeValue)
volumeVal = volume_tag[0].childNodes[0].firstChild.nodeValue


print(responseXML_pretty)
print(volume_tag[0].childNodes[0].firstChild.nodeValue)
volumeVal = volume_tag[0].childNodes[0].firstChild.nodeValue

# Updating the volume
updated_volume = str(math.floor(int(volumeVal)/2))
print(updated_volume)

send = requests.get('http://' + ipaddr + ':8090/now_playing')
print(send.text)

# Getting the current track info
send = requests.get('http://' + ipaddr + ':8090/now_playing')
responseXML = xml.dom.minidom.parseString(send.text)
responseXML_pretty = responseXML.toprettyxml()
print(responseXML_pretty)

now_playing_tag = responseXML.getElementsByTagName('nowPlaying')
album_tag = now_playing_tag[0].childNodes[2].firstChild.nodeValue
list_album_tag = album_tag.split(';')
print(list_album_tag)
url_from_album_tag = list_album_tag[0]  # get current track url
timestamp_from_album_tag = list_album_tag[1]    # get track start timestamp
print (responseXML_pretty)

""""send = requests.get('http://' + ipaddr + ':8090/select')
responseXML = xml.dom.minidom.parseString(send.text)
responseXML_pretty = responseXML.toprettyxml()
print (responseXML_pretty)"""

"""keystate = "press"
responseXML = bs(send.text, 'html.parser')
responseXML = xml.dom.minidom.parseString(send.text)
responseXML_pretty = responseXML.toprettyxml()

send = requests.get('http://' + ipaddr + ':8090/select')
responseXML = xml.dom.minidom.parseString(send.text)
responseXML_pretty = responseXML.toprettyxml()
print (responseXML_pretty)

keystate = "press"
keyvalue = "PAUSE"
sendXML = "<key state=\""+ keystate + "\" sender=\"Gabbo\">"+keyvalue+"</key>"
"""

current_timestamp = calendar.timegm(time.gmtime())

"""
send = requests.post('http://' + ipaddr + ':8090/key', data=sendXML)
keystate = "release"
keyvalue = "PAUSE"
sendXML = "<key state=\""+ keystate + "\" sender=\"Gabbo\">"+keyvalue+"</key>"
send = requests.post('http://' + ipaddr + ':8090/key', data=sendXML)

responseXML = xml.dom.minidom.parseString(send.text)
responseXML_pretty = responseXML.toprettyxml()
print (responseXML_pretty)"""

delta_time = current_timestamp - int(timestamp_from_album_tag)
print(delta_time)

file_name = "./whole_mp3.mp3"
shortened_file_name = "./split_mp3.mp3"
urllib.request.urlretrieve(url_from_album_tag, file_name)

AudioSegment.converter = "../resources/ffmpeg/ffmpeg/bin/ffmpeg.exe"
AudioSegment.ffmpeg = "../resources/ffmpeg/ffmpeg/bin/ffmpeg.exe"
AudioSegment.ffprobe ="../resources/ffmpeg/ffmpeg/bin/ffmpeg.exe"
sound = AudioSegment.from_mp3(file_name)

# len() and slicing are in milliseconds
second_half = sound[delta_time*1000:]

# writing mp3 files is a one liner
second_half.export(shortened_file_name, format="mp3")

#sendXML = "<volume>"+updated_volume+"</volume>"
#send = requests.post('http://' + ipaddr + ':8090/volume', data=sendXML)

#responseXML = xml.dom.minidom.parseString(send.text)
#responseXML_pretty = responseXML.toprettyxml()
#print (responseXML_pretty)

time.sleep(2)
sendXML = "<play_info><app_key>" + key + "</app_key><url>" + notification_sound_url + "</url><service>" + service + "</service><reason>" + reason + "</reason><message>" + message + "</message><volume>" + volumeVal + "</volume></play_info>"
send = requests.post('http://' + ipaddr + ':8090/speaker', data=sendXML)

responseXML = xml.dom.minidom.parseString(send.text)
responseXML_pretty = responseXML.toprettyxml()
print (responseXML_pretty)

"""keystate = "press"
keyvalue = "PAUSE"
sendXML = "<key state=\""+ keystate + "\" sender=\"Gabbo\">"+keyvalue+"</key>"
send = requests.post('http://' + ipaddr + ':8090/key', data=sendXML)

keystate = "release"
keyvalue = "PAUSE"
sendXML = "<key state=\""+ keystate + "\" sender=\"Gabbo\">"+keyvalue+"</key>"
send = requests.post('http://' + ipaddr + ':8090/key', data=sendXML)

responseXML = xml.dom.minidom.parseString(send.text)
responseXML_pretty = responseXML.toprettyxml()
print (responseXML_pretty)"""

shortened_file = pathlib.Path(os.path.abspath(shortened_file_name)).as_uri()

time.sleep(2)
sendXML = "<play_info><app_key>" + key + "</app_key><url>" + shortened_file + "</url><service>" + service + "</service><reason>" + reason + "</reason><message>" + message + "</message><volume>" + volumeVal + "</volume></play_info>"
send = requests.post('http://' + ipaddr + ':8090/speaker', data=sendXML)

responseXML = xml.dom.minidom.parseString(send.text)
responseXML_pretty = responseXML.toprettyxml()
print (responseXML_pretty)
