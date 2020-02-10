# BoseSoundTouchAPI
Created at Hack(h)er413 2020. Won "Best Use of the Bose API" by Bose and "Best Hack for Making your Home Accessible" by Wayfair

# SoundClutch

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

The project is built using Python 3.6+ and requires the following modules:
requests
pydub
urllib   
pathlib

### Running the project

Download and unzip the repository to your computer and Raspberry Pi.

Make sure the Bose SoundTouch, Raspberry Pi, and Computer are all on the same wifi networks. 

On your computer, start by running the udp_server.py, then runs the spotifyPlayback.py.  On the Rapberry Pi, run the ultrasonic_distance.py.

Then move towards the sensor, within a certain distance the audio will be paused, the notification sound will be play, then music will resume.

## Built With

* [
Bose SoundTouch API](https://developer.bose.com/guides/bose-soundtouch-api) - The API use to control the Bose SoundTouch
* [Raspberry Pi 3B and Ultrasonic Ping Sensor
](https://www.raspberrypi.org/documentation/) - The hardware use to enable envinment sensing
## Authors

* **Kunjal Panchal** - *Initial work* - [Astuary](https://github.com/Astuary)
* **Catherine Huang** - *Initial work* - [chuang1990](https://github.com/chuang1990)
* **Anita Yip** - *Initial work* - [aniyip](https://github.com/aniyip)
* **Emily Huang** - *Initial work* - [Ehuang1412](https://github.com/Ehuang1412)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Bose mentors Elizabeth Mezias and Daniel Roberts
