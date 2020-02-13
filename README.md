# SoundClutch
BoseSoundTouchAPI Created at Hack(h)er413 2020. Won "Best Use of the Bose API" by Bose and "Best Hack for Making your Home Accessible" by Wayfair
https://dashboard.hackher413.com/projects/10

## Description as a Tweet:
Ever missed an important event because your music or gaming was too loud? Now you can get notified on every event you think is important with Bose speakers in your home.

## Inspiration:
We were inspired in three ways:

Purpose - Collectively, we wanted to work on projects that matter and can benefit other people. Missing out on important events because we were so immersed in our environment and technologies is a concern we thought could be addressed, using the SoundTouch as our vehicle.

Adventure - Because we typically don't have access to products like the Bose SoundTouch, we wanted to experiment with how far we can go with various hardware products we haven't had any experience with and we wanted to have fun while putting all the pieces together.

Challenge - With little to no experience with hardware, we wanted to see how we fared learning to set up and use different components, facilitate data communication, and integrate an API. Hackathons are such a great time to work on passion projects that we otherwise wouldn't have been able to make on our own and without the hardware, mentoring resources, and support from one another.

What it does:
SoundClutch is constantly sensing its environment to determine when a significant event is happening and whether it needs to lower or raise its volume in response to the event.

Some use cases include:

- when you're listening to music and someone rings the doorbell; SoundTouch will lower the volume so that you can hear that someone rang your doorbell ring

- when you're out of the house and someone unexpectedly opens the door; SoundTouch will raise its volume and start playing a song or a recorded conversation to simulate someone being at home in order to deter unwelcome intruders

- when people are out clubbing and the fire alarm goes off; SoundTouch can silence the music the DJ is playing so that all clubbers can hear the fire alarm and listen to directions to exit safetly via Bose's ability to customize notification

## How we built it:
We programmed distance sensor HC-SR04 mounted on a Raspberry Pi 3 Model B to detect whether someone is performing a certain activity and send activity data to a server using Python. In turn, the server notifies the Bose SoundTouch 10 speaker, which we programmed to broadcast a notification via the Bose SoundTouch API. All communication is routed via the Verizon Jetpack 4G LTE Mobile Hotspot.

## Technologies we used:
Python
Raspberry Pi
Other Hardware
Challenges we ran into:
- working on items not natively supported by the API, so we created our own methods to perform what we wanted to do
- pushing the boundardy with how to develop hardware in ways that they weren't designed to develop with

## Accomplishments we're proud of:
We have a working product!!!

## What we've learned:
- the importance of asking for help - we spent time figuring out where the point of failure in the code was when it was in fact the hardware that did not work
- using oscillosopes to debug
- prioritizing tasks to create a minimum viable product
- completing a project in a team with varied knowledge and diverse backgrounds

## What's next:
- creating more system notifcations as reminders
- integrating with more Bose partner APIs
- improving use case with different sensory data
- explore implementing in other speakers and headphones like Bose Frames

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

The project is built using Python 3.6+ and requires the following modules:
requests
pydub
urllib   
pathlib

## Built with:
* [
Bose SoundTouch API](https://developer.bose.com/guides/bose-soundtouch-api) - The API use to control the Bose SoundTouch
* [Raspberry Pi 3B and Ultrasonic Ping Sensor
](https://www.raspberrypi.org/documentation/) - The hardware use to enable envinment sensing

We programmed distance sensor HC-SR04 mounted on a Raspberry Pi 3 Model B to detect whether someone is performing a certain activity and send activity data to a server using Python. In turn, the server notifies the Bose SoundTouch 10 speaker, which we programmed to broadcast a notification via the Bose SoundTouch API. We integrated it with the Spotify API. All communication is routed via the Verizon Jetpack 4G LTE Mobile Hotspot.

### Running the project

Download and unzip the repository to your computer and Raspberry Pi.

Make sure the Bose SoundTouch, Raspberry Pi, and Computer are all on the same wifi networks. 

On your computer, start by running the udp_server.py, then runs the spotifyPlayback.py.  On the Rapberry Pi, run the ultrasonic_distance.py.

Then move towards the sensor, within a certain distance the audio will be paused, the notification sound will be play, then music will resume.

## Authors

* **Kunjal Panchal** - *Initial work* - [Astuary](https://github.com/Astuary)
* **Catherine Huang** - *Initial work* - [chuang1990](https://github.com/chuang1990)
* **Anita Yip** - *Initial work* - [aniyip](https://github.com/aniyip)
* **Emily Huang** - *Initial work* - [Ehuang1412](https://github.com/Ehuang1412)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Bose mentors Elizabeth Mezias and Daniel Roberts
