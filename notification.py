import requests
import xml.dom.minidom

# set the params:

ipaddr = "192.168.1.92" # enter your speaker IP address here
url = "https://freesound.org/data/previews/275/275571_4486188-hq.mp3" # enter the URL of the file you want to play here
#url = "file:///F:/MS%20-%20II/Bose%20Soundtouch/Hackher2020/resources/sample_soundtrack.mp3"
service = "That word..."
reason = "...it does not mean..."
message = "...what you think it means."
print(message)
key = "0k0RQaOC1nTLHX1DbHZRXNnBpjAlZOTH" # enter your API key here
volumeVal = "30" # enter volume here, a number between 10 and 70

send = requests.get('http://' + ipaddr + ':8090/now_playing')
responseXML = xml.dom.minidom.parseString(send.text)
responseXML_pretty = responseXML.toprettyxml()
print(responseXML_pretty)

send = requests.get('http://' + ipaddr + ':8090/volume')
print(send.text)
responseXML = xml.dom.minidom.parseString(send.text)
volume_tag = responseXML.getElementsByTagName('volume')
volumeVal = volume_tag[0].childNodes[0].firstChild.nodeValue
updated_volume = str(int(volumeVal)+20)

# form and send the /speaker POST request

sendXML = "<play_info><app_key>" + key + "</app_key><url>" + url + "</url><service>" + service + "</service><reason>" + reason + "</reason><message>" + message + "</message><volume>" + updated_volume + "</volume></play_info>"
send = requests.post('http://' + ipaddr + ':8090/speaker', data=sendXML)

# print a pretty version of the response - not required but can be helpful for reading errors if they occur

responseXML = xml.dom.minidom.parseString(send.text)
responseXML_pretty = responseXML.toprettyxml()
print (responseXML_pretty)
