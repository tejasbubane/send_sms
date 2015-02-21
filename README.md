* Author: Tejas Bubane (tejasbubane@gmail.com)
* Date: 5 Apr 2012
* Time: 03:16

For phones which are not S-40 or if you want to connect the phone via USB-cable, the gammurc file needs to be changed accordingly.
Refer [the gammu config docs](http://wammu.eu/docs/manual/faq/config.html) for more info.

If you have an S-40 phone having bluetooth, set it in automatic pairing mode with your PC.

This is a simple python program that can send sms through a connected phone.
It uses [gammu python APIs (python-gammu)](http://wammu.eu/docs/manual/python/).

### Usage:

* Place the gammurc file (prepared as per above config link) in the /etc/ folder

* Then run the python script, enter the recepient number, enter the message and its delivered..!!

### Note:

Tested on my Nokia 2730c connected via bluetooth and should work on all phones supported by gammu.
