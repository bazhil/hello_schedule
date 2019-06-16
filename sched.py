import schedule
import time

def work():
    print('Work is done!')

def coffebreak():
    print('Let\'s drink some coffe')

def motion():
    print('I\'t monday, let\'s do some motion!')

def minute():
    print('You lost another one minute!')

schedule.every(1).minutes.do(work)
schedule.every().day.at('01:20').do(coffebreak)
schedule.every().monday.do(motion)
schedule.every().minute.at(':00').do(minute)

while True:
    schedule.run_pending()
    time.sleep(1)