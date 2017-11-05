import org.sikuli.script.SikulixForJython
from java.util import *
from sikuli import *
import pdb
#import keyboard
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
                        sleep(1)
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

    def go_to_consumables_by_type(self, selected_type):
        self.go_to_consumables()
        Waiters.click_first_found_picture(self, (Tabs.Transfers.TransferMarket.consumables_type_text_selected, Tabs.Transfers.TransferMarket.consumables_type_text), 1)
        for item in range(1, 9):
            try:
                self.fifa_window_size.wait(selected_type, 1)
                type(Key.ENTER)
                break
            except FindFailed:
                os.system("left.exe")
        # for item in range(1, 20):
        #     try:
        #         self.fifa_window_size.wait(Tabs.Transfers.TransferMarket.consumables_type_contract_selected, 0)
        #         type(Key.ENTER)
        #         sleep(1)
        #         break
        #     except FindFailed:
        #         type(Key.LEFT)
        #         type(Key.LEFT)
        #         sleep(1)

    def select_qaulity(self, quality):
        Waiters.wait_and_click(self, Tabs.Transfers.Quality.quality, 1)
        for item in range(1, 8):
            try:
                self.fifa_window_size.wait(quality, 1)
                type(Key.ENTER)
                break
            except FindFailed:
                os.system("left.exe")


    # fifa_window_size.wait(Tabs.Transfers.Quality.quality_gold_entered, 1)

    def set_pricing(self, max_buy_now):
        Waiters.wait_and_click(self, Tabs.Transfers.Pricing.pricing_text, 2)
        for item in range(1, 8):
            try:
                self.fifa_window_size.wait(Tabs.Transfers.Pricing.max_buy_now_selected, 1)
                type(Key.ENTER)
                break
            except FindFailed:
                os.system("up.exe")
        self.fifa_window_size.wait(Tabs.Transfers.Pricing.set_price_form, 2)
        type(str(max_buy_now))
        type(Key.ENTER)
        self.fifa_window_size.wait(Buttons.s_manually_adjust_price, 2)
        type(Key.ESC)
        self.fifa_window_size.wait(Buttons.d_search, 2)

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
                #return
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
        fifa_window_size.wait(image_name, timeout)
        click(fifa_window_size.getLastMatch())
    def click_first_found_picture(list_to_search, timeout=0):
        for picture in list_to_search:
            try:
                fifa_window_size.wait(picture, timeout)
                click(fifa_window_size.getLastMatch())
                return
            except FindFailed:
                print str(picture) + " not found"

    # Relist = Actions()
    # Relist.relist_all()
    # Relist.clear_sold()
    #
    Start = Navigate()
    #Start.go_to_consumables_by_type(Tabs.Transfers.TransferMarket.consumables_type_contract_selected)
    # Start.select_qaulity(Tabs.Transfers.Quality.quality_gold_entered)
    # Start.set_pricing(500)
    type("d")
    for page in range(1, 100):
        try:
            fifa_window_size.wait(Buttons.actions, 5)
            print "Searching for ..."
            wait_and_click(Tabs.Transfers.TransferMarket.Contracts.contract_gold_half, 0)
            print "Something found, trying to buy"
            #pdb.set_trace()
            print '1'
            try:
                fifa_window_size.wait(Tabs.Transfers.TransferMarket.Contracts.contract_gold_full, 1)
            except FindFailed:
                type(Key.ESC)
            print '2'
            fifa_window_size.hover(Buttons.compare_price)
            print '3'
            wait_and_click(Buttons.buy_now, 0)
            print '4'
            wait_and_click(Buttons.yes, 1)
            print '5'
            fifa_window_size.wait(Messages.message_successful_purchase, 3)
            print "Bought!!!"
            click_first_found_picture((Buttons.continue_searching, Buttons.continue_searching_selected), 0)
            print "next page, as made purchase"
        except FindFailed:
            print "Nothing found, trying next page"
            fifa_window_size.wait(Buttons.actions, 1)
            type("c")
            sleep(0.5)

#    os.system("down.exe")
#    os.system("up.exe")
#    os.system("right.exe")
#    os.system("left.exe")


    #fifa_window_size.wait(Tabs.Transfers.Quality.quality_gold, 5)
    #fifa_window_size.wait(Tabs.Transfers.Pricing.max_buy_now_200, 5)
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







def rectungle():
    power = str(Fifa_window_size).split(']')
    new = power[0]
    new = new.replace(" ", ",")
    new = new.replace("x", ",")
    new = new.replace("R", "")
    new = new.replace("[", "")
    new_tuple = tuple(new.split(','))


# print full_contract_reg.click('contract.png')
# print full_contract_reg.findall('contract.png')
# for x in findAll(contract):  a = a + 1; print a
