# Copyright (C) 2012
# Tejas Bubane (tejasbubane@gmail.com)
# Date: 5 Apr 2012 # Time: 03:16

import gammu

sm = gammu.StateMachine()
sm.ReadConfig()
number = raw_input('Number: ')
msg = raw_input('Message: ')
sm.Init()
message = {
    'Text': str(msg),
    'SMSC': {'Location': 1},
    'Number': str(number),
}
sm.SendSMS(message)
