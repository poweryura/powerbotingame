import org.sikuli.script.SikulixForJython
from sikuli import *
import pdb
import os
from itertools import count
import inspect
from Pics import *
import smtplib
# import pyautogui
# zfrom pywinauto.application import Application
# import win32gui
import re
from random import randint
import smtplib
import datetime
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


class Main(object):
    def __init__(self):
        setAutoWaitTimeout(3)
        print "Activating Fifa Window"
        #click(fifa_window)
        self.fifa_window_size = Region(App.focusedWindow())
        print self.fifa_window_size
        self.fifa_window_size.click(club_logo)
        print "Window is activated, as club logo found"


class Waiters(Main):

    def click_first_found_picture(self, list_to_search, timeout=0):
        for picture in list_to_search:
            try:
                self.fifa_window_size.wait(picture, timeout)
                click(self.fifa_window_size.getLastMatch())
                return
            except FindFailed:
                print str(picture) + " not found"

    def wait_and_click(self, image_name, timeout=0):
        # mozilla_size.click(image_name)
        self.fifa_window_size.wait(image_name, timeout)
        click(self.fifa_window_size.getLastMatch())


class Navigate(Waiters):

    def go_to_home_sceen(self):
        try:
            print "Checking if home page"
            self.fifa_window_size.wait(Tabs.main_panel, 0)
            print "Home page by default"
        except FindFailed:
            print "not home page"
            for item in range(1, 5):
                    try:
                        type(Key.ESC)
                        self.fifa_window_size.wait(Tabs.main_panel, 1)
                        # self.fifa_window_size.wait(Messages.message_exit_ut, 1)
                        # Waiters.wait_and_click(self, Buttons.no_selected)
                        print "HOME PAGE"
                        break
                    except FindFailed:
                        print " Not HOME yet"

    def go_to_transfer_list(self):
        self.go_to_home_sceen()
        Waiters.wait_and_click(self, Tabs.tab_transfers)
        Waiters.click_first_found_picture(self, (Tabs.Transfers.transfer_list_selected, Tabs.Transfers.transfer_list_logo), 1)
        self.fifa_window_size.wait(Tabs.Transfers.transfer_list_link, 3)

    def go_to_transfer_market(self):
        self.go_to_home_sceen()
        Waiters.wait_and_click(self, Tabs.tab_transfers)
        Waiters.click_first_found_picture(self, (Tabs.Transfers.transfer_market, Tabs.Transfers.transfer_market_selected), 1)
        self.fifa_window_size.wait(Tabs.Transfers.transfer_market_panel, 3)

    def go_to_consumables(self):
        self.go_to_transfer_market()
        Waiters.click_first_found_picture(self, (Tabs.Transfers.TransferMarket.consumables_selected, Tabs.Transfers.TransferMarket.consumables), 1)

    def go_to_consumables_contract(self):
        self.go_to_consumables()
        Waiters.click_first_found_picture(self, (Tabs.Transfers.TransferMarket.consumables_type_text_selected, Tabs.Transfers.TransferMarket.consumables_type_text), 1)
        for item in range(1, 20):
            try:
                self.fifa_window_size.wait(Tabs.Transfers.TransferMarket.consumables_type_contract_selected, 0)
                type(Key.ESC)
                break
            except FindFailed:
                type(Key.LEFT)
                type(Key.LEFT)
                sleep(1)

class Actions(Navigate):

    def relist_all(self):
        self.go_to_transfer_list()
        try:
            self.wait_and_click(Buttons.relist_all, 2)
            self.wait_and_click(Buttons.yes, 2)
        except FindFailed:
            print "Looks nothing to re-list"

    def clear_sold(self):
        if self.fifa_window_size.exists(Tabs.Transfers.transfer_list_link, 0) is not None:
            print "alredy in trasfer list"
            #self.fifa_window_size.wait(Tabs.Transfers.transfer_list_link, 3)
            try:
                self.wait_and_click(Buttons.w_clear_sold_items, 2)
            except FindFailed:
                print "Looks nothing to clear"
        else:
            self.go_to_transfer_list()
        try:
            self.wait_and_click(Buttons.w_clear_sold_items, 2)
        except FindFailed:
            print "Looks nothing to clear"

if __name__ == '__main__':

    fifa_window_size = Region(App.focusedWindow())
    def wait_and_click(image_name, timeout=0):
        # mozilla_size.click(image_name)
        wait(image_name, timeout)
        click(getLastMatch())
    def click_first_found_picture(list_to_search, timeout=0):
        for picture in list_to_search:
            try:
                wait(picture, timeout)
                click(fifa_window_size.getLastMatch())
                return
            except FindFailed:
                print str(picture) + " not found"

    # Relist = Actions()
    # Relist.relist_all()
    # Relist.clear_sold()

    Start = Navigate()
    for item in range(1, 10):
        Start.go_to_consumables_contract()

    #     Start.go_to_transfer_list()
    #     Start.go_to_transfer_market()
    pdb.set_trace()

    #Start.go_to_transfer_list()


    #Start.go_to_home_sceen();


    # relist
    # sleep(1); type('q')  # relist_all
    # wait_and_click(Buttons.relist_all, 2)
    # wait_and_click(Buttons.yes, 2)




    #Clear sold
    # sleep(1); type('w')  # Clear sold
    #wait_and_click(Buttons.w_clear_sold_items, 2); sleep(2)








click_first_found_picture((Tabs.Transfers.transfer_list_logo, Tabs.Transfers.transfer_list_selected))
click_first_found_picture(
    (Tabs.Transfers.TransferMarket.consumables, Tabs.Transfers.TransferMarket.consumables_selected))

Fifa_window_size.click(Tabs.tab_transfers)
Fifa_window_size.click(Tabs.Transfers.transfer_list_selected)
Fifa_window_size.click(Buttons.relist_all);
Fifa_window_size.click(Buttons.yes)

Fifa_window_size.click(Tabs.Transfers.TransferMarket.consumables)
Fifa_window_size.click(Tabs.Transfers.TransferMarket.consumables_selected)



Fifa_window_size.hover(relist_all)
Fifa_window_size.hover(Tabs.Transfers.transfer_list_logo)
Fifa_window_size.hover(Tabs.Transfers.transfer_market)
Fifa_window_size.hover(Tabs.Transfers.transfer_market)

Fifa_window_size.click(Tabs.Transfers.TransferMarket.consumables_type_text)
Fifa_window_size.click(Tabs.Transfers.TransferMarket.consumables_type_text_selected)

Fifa_window_size.hover(Tabs.Transfers.Quality.quality_gold_entered)
sleep(3); type(Key.LEFT);  sleep(1); type(Key.LEFT);

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
sleep(3);
type('q')

wait(transfer_list)
pdb.set_trace()

sleep(2);
Fifa_window_size = Region(App.focusedWindow());
Fifa_window_size


# print full_contract_reg.click('contract.png')
# print full_contract_reg.findall('contract.png')
# for x in findAll(contract):  a = a + 1; print a
