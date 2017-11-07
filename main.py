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
                        self.fifa_window_size.wait(Tabs.main_panel, 2)
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
        Waiters.click_first_found_picture(self, (Tabs.Transfers.transfer_market, Tabs.Transfers.transfer_market_selected), 2)
        self.fifa_window_size.wait(Tabs.Transfers.transfer_market_panel, 3)

    def go_to_consumables(self):
        self.go_to_transfer_market()
        Waiters.click_first_found_picture(self, (Tabs.Transfers.TransferMarket.consumables_selected, Tabs.Transfers.TransferMarket.consumables), 2)

    def select_consumables_by_type(self, selected_type):
        Waiters.click_first_found_picture(self, (Tabs.Transfers.TransferMarket.consumables_type_text_selected, Tabs.Transfers.TransferMarket.consumables_type_text), 2)
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

    page = 0
    bought_items = 0

    fifa_window_size = Region(App.focusedWindow())

    @Service.timing
    def wait_and_click(image_name, timeout=0):
        # mozilla_size.click(image_name)
        fifa_window_size.wait(image_name, timeout)
        click(fifa_window_size.getLastMatch())

    @Service.timing
    def click_first_found_picture(list_to_search, timeout=0):
        for picture in list_to_search:
            try:
                fifa_window_size.wait(picture, timeout)
                click(fifa_window_size.getLastMatch())
                return
            except FindFailed:
                print str(picture) + " not found"

    def hover_mouse():
        mouseLoc = Env.getMouseLocation()
        x_position = mouseLoc.getX()
        y_position = mouseLoc.getY()

        hover(Location(x_position, y_position-40))

        #return x_position, y_position


    # Relist = Actions()
    # Relist.relist_all()
    # Relist.clear_sold()
    #
    Start = Navigate()
    Start.go_to_consumables()
    Start.select_consumables_by_type(Tabs.Transfers.TransferMarket.consumables_type_contract_selected)
    Start.select_qaulity(Tabs.Transfers.Quality.quality_gold_entered)
    Start.set_pricing(200)
    #pdb.set_trace()
    type("d")

    def save_bought_items():
        if fifa_window_size.exists(Buttons.send_all_to_club) is not None:
            type(Key.ESC)
            wait_and_click(Buttons.send_all_to_club, 5)
            type('w')
            sleep(1)
        else:
            print "Nothing to assign, exiting"
            type(Key.ESC)



    for page in range(1, 300):

        # Move mouse to top
        try:
            fifa_window_size.hover(Buttons.page)
        except FindFailed:
            pass

        print "Page: " + str(page + 1)

        try:
            # Wait for actions button
            fifa_window_size.wait(Buttons.actions, 3)
            print "Searching..."

            # Search for item
            wait_and_click(Tabs.Transfers.TransferMarket.Contracts.contract_gold_half)
            print "Something found, trying to buy"
            #hover(Location(fifa_window_size.find(Tabs.Transfers.TransferMarket.Contracts.contract_gold_half).getTarget()))

            try:
                print "Checking if item was clicked (FULL size)"
                fifa_window_size.wait(Tabs.Transfers.TransferMarket.Contracts.contract_gold_full, 2)
            except FindFailed:
                try:
                    print "bad click"
                    if exists(Tabs.Transfers.bidding_options, 0) is not None:
                        print "clicked on wrong item"
                        type(Key.ESC)
                        continue
                    else:
                        continue
                except FindFailed:
                    pass

            # as item was selected, clicking on buy now
            click_first_found_picture((Buttons.buy_now_selected, Buttons.buy_now), 2)
            wait_and_click(Buttons.yes, 2)

            #fifa_window_size.exists(Messages.message_sorry_expired, 1)
            for attempts in range(1, 3):
                try:
                    fifa_window_size.wait(Messages.message_successful_purchase, 3)
                    break
                except FindFailed:
                    if fifa_window_size.exists(Messages.message_sorry_expired, 1)is not None:
                        print "Expired item"
                        fifa_window_size.click(Buttons.ok_selected)
                        fifa_window_size.wait(Tabs.Transfers.TransferMarket.Contracts.contract_gold_full, 2)
                        type(Key.ESC)
                        break
                    else:
                        print "Unknown state, doing ESC, and starting again to parse message"
                        type(Key.ESC)
                        try:
                            fifa_window_size.click(Buttons.arrow_selected)
                        except FindFailed:
                            pass

                    # Looks that item bought


                print "Bought: %s items !!" % str(bought_items + 1)
                click_first_found_picture((Buttons.continue_searching, Buttons.continue_searching_selected), 0)
            print "Going to the next page, as made purchase done here"
            type("c")
            sleep(random.uniform(0.3, 0.6))
            continue

        except FindFailed:
            print "Nothing found, trying next page..."
            fifa_window_size.wait(Buttons.s_manually_adjust_price, 1)
            type("c")
            sleep(random.uniform(0.3, 0.6))
    save_bought_items()
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
