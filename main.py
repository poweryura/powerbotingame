import org.sikuli.script.SikulixForJython
from sikuli import *
import pdb
import os
from itertools import count
import inspect
from Pics import *

#import Pics
import smtplib
#import pyautogui
#zfrom pywinauto.application import Application
#import win32gui
import re
from random import randint
import smtplib
import random


class Service(object):

    @staticmethod
    def send_mail():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("yyura2014@gmail.com", "Power123456")
        msg = "Check BOT Captcha"
        server.sendmail("yyura2014@gmail.com", "poweryura@gmail.com", msg)
        server.quit()

    @staticmethod
    def initiate_market_wipe(first_hour):
        print(inspect.stack()[0][3])
        print(first_hour)
        current_hour = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H')
        print(current_hour)
        if first_hour != current_hour:
            print("doing market WIPE")
            first_hour = current_hour
        else:
            pass
        return first_hour

    @staticmethod
    def take_screenshot(prefix, global_browser_size):
        current_time = str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + '_' + prefix + '_' ".jpg"
        ImageGrab.grab(bbox=global_browser_size).save(current_time, "JPEG")
        print("Saved screenshot: %s" % current_time)

    @staticmethod
    def timing(f):
        def wrap(*args):
            time1 = time.time()
            ret = f(*args)
            time2 = time.time()
            print('%s function took %0.3f ms' % (f.__name__, (time2 - time1) * 1000.0))
            return ret

        return wrap

    @staticmethod
    def load_config_file(file):
        f = open(file)
        Picsy = yaml.safe_load(f)
        print('config file %s loaded' % file)
        f.close()
        return Picsy

setAutoWaitTimeout(3)


def activate_fifa():
#Fifa = App("FIFA 18")
#Fifa.focus('FIFA 18')
    print "Activating Fifa Window"
    #click(fifa_window)
    Fifa_window_size = Region(App.focusedWindow())
    print Fifa_window_size
    Fifa_window_size.wait(club_logo)
    print "Window is activated, as club logo found"
    return Fifa_window_size


Fifa_window_size = activate_fifa()

pdb.set_trace()

Fifa_window_size.click(Tabs.tab_transfers)
Fifa_window_size.click(Tabs.Transfers.transfer_list_selected)
Fifa_window_size.click(Buttons.relist_all)
Fifa_window_size.click(Buttons.yes)

Fifa_window_size.click(Tabs.Transfers.TransferMarket.consumables)
Fifa_window_size.click(Tabs.Transfers.TransferMarket.consumables_selected)
type('q')



pdb.set_trace()


Fifa_window_size.hover(relist_all)
Fifa_window_size.hover(Tabs.Transfers.transfer_list_logo)
Fifa_window_size.hover(Tabs.Transfers.transfer_market)
Fifa_window_size.hover(Tabs.Transfers.transfer_market)


Fifa_window_size.click(Tabs.Transfers.TransferMarket.consumables_type_text)
Fifa_window_size.click(Tabs.Transfers.TransferMarket.consumables_type_text_selected)

Fifa_window_size.hover(Tabs.Transfers.Quality.quality_gold_entered)
sleep(5); type(Key.LEFT); type(Key.LEFT); sleep(1); type(Key.LEFT); type(Key.LEFT)
Fifa_window_size.hover(Tabs.Transfers.Quality.quality_gold)



def rectungle():
    power = str(Fifa_window_size).split(']')
    new = power[0]
    new = new.replace(" ", ",")
    new = new.replace("x", ",")
    new = new.replace("R", "")
    new = new.replace("[", "")
    new_tuple = tuple(new.split(','))

type(Key.BACKSPACE)
sleep(3); type('q')


wait(transfer_list)
pdb.set_trace()

sleep(2); Fifa_window_size = Region(App.focusedWindow()); Fifa_window_size


#print full_contract_reg.click('contract.png')
#print full_contract_reg.findall('contract.png')
#for x in findAll(contract):  a = a + 1; print a
