import twint, time, datetime, pyAesCrypt

def FirePayload(filePath, encryptPass):
    print("Activate Payload!")
    bufferSize = 64 * 1024
    print("Switch Activated - Initiate Lockdown Mode")
    exit()

def CheckKey(c, delayTime, filePath, encryptPass, targetTime):
    try:
        twint.run.Search(c)
    except ValueError:
        print("Opps")
    tweets = twint.output.twint_list
    if not tweets:
        if (time.time() >= targetTime): FirePayload(filePath, encryptPass)
        else:
            print("No results")
            time.sleep(delayTime)
            CheckKey(c, delayTime, filePath, encryptPass, targetTime)
    else:
        print("Switch Deactivated")
        exit()

def GetTargets():
    c = twint.Config()
    startTime = input("Date to start searching (format: %Y-%m-%d)\n>")
    try: datetime.datetime.strptime(startTime, '%Y-%m-%d')
    except ValueError:
        print("That's not a date, try again (format: %Y-%m-%d)")
        GetTargets()
    c.Since = startTime
    c.Search = input("Keyphrase to disarm switch?\n>")
    c.Username = input("Twitter account to watch?\n>")
    delayTime = int(input("Time to wait between checking the account\n>"))
    filePath = input("File to encrypt if switch clocks 0?\n>")
    encryptPass = input("Password to encrypt file?\n>")
    targetTime =(time.time() + (int(input("How many minutes to rum before firinig?\n>"))*60))
    c.Hide_output = True
    c.Store_object = True
    CheckKey(c, delayTime, filePath, encryptPass, targetTime)

GetTargets()