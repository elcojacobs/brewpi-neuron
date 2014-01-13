brewpi-neuron
=============

Repository to get started with designing a new REST API for BrewPi.

This API will be served by the service layer. It will:
* expose various bots (Arduino's or other embedded device) to the GUI layers.
* provide access to logged time series data.
* provide access to all settings

We have chosen Python REST API Framework Eve to implement the API for now.
This will make it easy to mock an API to start designing a new web interface.
It will also help us to specify which objects we need on the embedded devices:
 in the API we will specify which kind of sensors, actuators and controllers we have and choose where certain settings reside.
For example Kp, Ki, and Kd should liven in a PID controller object and are returned by the API as nested variables.

To get started:

Install PyCharm:
^^^^^^^^^^^^^^^^
* Request the open source license code, by sending an e-mail to me (elco[at]brewpi), on IRC or via PM on the forum.
* Go to http://www.jetbrains.com/pycharm/download/ and download the professional edition of PyCharm.
* Install Pycharm
* Enter the license code
* Pick your settings (for the color scheme, I like monokai, a colorful dark theme)
* Open the directory of this repository
* Add python.exe to your list of interpreters and set is as the project interpreter

Install Eve:
^^^^^^^^^^^^
In PyCharm, go to File -> Settings -> Project Settings -> Project Interpreters -> Python Interpreters.
Install the package Eve (by Nicola Iarocci)

Install MongoDB
^^^^^^^^^^^^^^^
* Download MongoDB: http://www.mongodb.org/downloads
* Copy the content of the archive to for example C:\mongodb
* If you want to use a custom data directory, create the directory, for example C:\mongodb\data
    * Create a shortcut to start mongodb with the custom data dir: "C:\mongodb\bin\mongod.exe --dbpath c:\mongodb\data"


To test the REST interface:
---------------------------
* start mongodb with the shortcut from the previous step
* execute run.py







