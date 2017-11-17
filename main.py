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



#Settings.MinSimilarity = 0.7
#Settings.MoveMouseDelay = 0.3
#Settings.Highlight = True
#setAutoWaitTimeout(1)
getAutoWaitTimeout()


class Service(object):
    @staticmethod
    def send_mail():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("yyura2014@gmail.com", "Power")
        msg = "Check BOT "
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

    @staticmethod
    def rectangle():
        power = str(fifa_window_size).split(']')
        new = power[0]
        new = new.replace(" ", ",")
        new = new.replace("x", ",")
        new = new.replace("R", "")
        new = new.replace("[", "")
        new_tuple = tuple(new.split(','))

    @staticmethod
    def hover_mouse(x, y):
        mouseLoc = Env.getMouseLocation()
        x_position = mouseLoc.getX()
        y_position = mouseLoc.getY()
        hover(Location(x_position+x, y_position+y))

class Main(object):
    def __init__(self):
        setAutoWaitTimeout(3)
        print "Activating Fifa Window"
        #click(fifa_window, 3)
        #self.fifa_window_size = Region(App.focusedWindow())
        self.fifa_window_size = Region(0, 0, 1280, 750)
        self.fifa_window_size_left_up = Region(0, 0, 600, 600)
        #self.fifa_window_size.highlight(1)
        print self.fifa_window_size
        #self.fifa_window_size.click(club_logo)
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
            #self.fifa_window_size.wait(Tabs.main_panel, 0)
            self.fifa_window_size.wait(Tabs.main_panel_buttons, 0)
            print "Home page by default"
            return
        except FindFailed:
            print "Not HOME PAGE"
            for item in range(1, 5):
                    try:
                        type(Key.ESC)
                        sleep(1)
                        self.fifa_window_size.wait(Tabs.main_panel_buttons, 2)
                        print "HOME PAGE"
                        return
                        #break
                    except FindFailed:
                        print " Not HOME PAGE yet"
            if self.fifa_window_size.exists(Messages.message_exit_ut, 1) is not None:
                try:
                    Waiters.wait_and_click(self, Buttons.no_selected)
                except FindFailed:
                    Waiters.wait_and_click(self, Buttons.no)
            else:
                pass

        try:
            Waiters.wait_and_click(self, Buttons.no_selected)
        except FindFailed:
            print "Unknown location!!!!"

        try:
            self.fifa_window_size.click(Messages.message_send_all_items_to_club)
        except FindFailed:
            pass

        try:
            self.fifa_window_size.click(Buttons.ok_selected)
        except FindFailed:
            pass

        try:
            self.fifa_window_size.click(Buttons.continue_searching_selected)
        except FindFailed:
            pass

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


    def go_to_my_club(self):
        self.go_to_home_sceen()
        Waiters.click_first_found_picture(self, (Tabs.MyClub.my_club, Tabs.MyClub.my_club_selected), 2)
        self.fifa_window_size.hover(Tabs.MyClub.club_player_stats)
        Waiters.click_first_found_picture(self,
                                          (Tabs.MyClub.my_club_inside_selected, Tabs.MyClub.my_club_inside), 2)
        self.fifa_window_size.wait(Tabs.MyClub.club_search_logo, 3)

    def select_contracts_to_sell(self):
        Waiters.click_first_found_picture(self, (Tabs.MyClub.ClubSearch.club_reset_selected, Tabs.MyClub.ClubSearch.club_reset), 2)
        Waiters.click_first_found_picture(self, (Tabs.MyClub.ClubSearch.club_search_type_selected, Tabs.MyClub.ClubSearch.club_search_type), 2)

        for item in range(1, 8):
            try:
                self.fifa_window_size.wait(Tabs.MyClub.ClubSearch.club_search_type_consumables_selected, 1)
                break
            except FindFailed:
                os.system("left.exe")

        Waiters.wait_and_click(self, Tabs.MyClub.ClubSearch.club_search_Item_Type)

        for item in range(1, 10):
            try:
                self.fifa_window_size.wait(Tabs.MyClub.ClubSearch.club_search_Item_Type_contracts_selected, 1)
                break
            except FindFailed:
                os.system("left.exe")

        #self.fifa_window_size.wait(Buttons.d_search)
        type("d")


    def select_consumables_by_type(self, selected_type):
        Waiters.click_first_found_picture(self, (Tabs.Transfers.TransferMarket.consumables_type_text_selected, Tabs.Transfers.TransferMarket.consumables_type_text), 3)
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

    def select_quality(self, quality):
        Waiters.wait_and_click(self, Tabs.Transfers.Quality.quality, 1)
        for item in range(1, 8):
            try:
                self.fifa_window_size.wait(quality, 1)
                type(Key.ENTER)
                break
            except FindFailed:
                os.system("left.exe")

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
    page = 0
    bought_items = 0
    expired_items = 0

    def relist_all(self):
        self.go_to_transfer_list()
        try:
            self.wait_and_click(Buttons.relist_all, 2)
            self.wait_and_click(Buttons.yes, 2)
        except FindFailed:
            print "Looks nothing to re-list"
        sleep(4)

    def clear_sold(self):
        if self.fifa_window_size.exists(Tabs.Transfers.transfer_list_link, 3) is not None:
            print "already in transfer list"
            #self.fifa_window_size.wait(Tabs.Transfers.transfer_list_link, 3)
            try:
                sleep(4)
                self.wait_and_click(Buttons.w_clear_sold_items, 5)
                sleep(3)
            except FindFailed:
                print "Looks nothing to clear"
        else:
            print "Looks nothing to clear"
            pass
        #
        # try:
        #     self.wait_and_click(Buttons.w_clear_sold_items, 2)
        # except FindFailed:
        #     print "Looks nothing to clear"
        # sleep(2)

    def buy_contracts(self, pages):
        bought_items = 0
        expired_items = 0
        type("d")
        if self.fifa_window_size.wait(Buttons.page, 5) is not None:
            for page in range(1, pages):
                if bought_items == 29:
                    self.save_bought_items()
                    return
                # Move mouse to top
                try:
                    #self.fifa_window_size.hover(Buttons.page)
                    self.fifa_window_size.hover(Location(0, 766))

                except FindFailed:
                    pass

                print "Page: " + str(page + 1)

                try:
                    # Wait for actions button
                    self.fifa_window_size.wait(Buttons.actions, 3)
                    print "Searching..."

                    # Search for item
                    #pdb.set_trace()
                    Waiters.wait_and_click(self, Tabs.Transfers.TransferMarket.Contracts.contract_gold_half)
                    #location = fifa_window_size.wait(Tabs.Transfers.TransferMarket.Contracts.contract_gold_half).getCenter()
                    print "Something found, trying to selected and buy"
                    #hover(location); Service.hover_mouse(0, 100); Service.hover_mouse(0, -100); click(getLastMatch())
                    #fifa_window_size.wait(Tabs.Transfers.TransferMarket.Contracts.contract_gold_half, 0); hover(getLastMatch()); Service.hover_mouse(0, 100); Service.hover_mouse(0, -100); click()

                    try:
                        print "Checking if right item was clicked (FULL size)"
                        self.fifa_window_size_left_up.wait(Tabs.Transfers.TransferMarket.Contracts.contract_gold_full, 2)
                    except FindFailed:
                        try:
                            #pdb.set_trace()
                            print "bad click"
                            if self.fifa_window_size.exists(Tabs.Transfers.bidding_options, 0) is not None:
                                print "clicked on wrong item"
                                type(Key.ESC)
                                continue
                            else:
                                continue
                        except FindFailed:
                            pass

                    # as item was selected, clicking on buy now
                    Waiters.click_first_found_picture(self, (Buttons.buy_now, Buttons.buy_now_selected), 1)
                    Waiters.wait_and_click(self, Buttons.yes, 3)

                    # fifa_window_size.exists(Messages.message_sorry_expired, 1)
                    for attempts in range(1, 3):
                        try:
                            self.fifa_window_size.wait(Messages.message_successful_purchase, 4)
                            Waiters.click_first_found_picture(self, (Buttons.continue_searching, Buttons.continue_searching_selected), 2)
                            bought_items = bought_items + 1
                            print "Bought: %s items !!" % str(bought_items)
                            print "Going to the next page, as purchase done here"
                            break
                        except FindFailed:
                            if self.fifa_window_size.exists(Messages.message_sorry_expired, 1) is not None:
                                expired_items = expired_items + 1
                                print "Expired item: %s" % str(expired_items)
                                if expired_items == 10:
                                    print "Too many expired items, does not make sense to continue, goig to start search again"
                                    # self.fifa_window_size.click(Buttons.ok_selected)
                                    # self.fifa_window_size.wait(Tabs.Transfers.search_results_link, 3)
                                    # type(Key.ESC)
                                    # self.fifa_window_size.wait(Buttons.d_search, 3)
                                    # type('d')
                                    return
                                self.fifa_window_size.click(Buttons.ok_selected)
                                self.fifa_window_size.wait(Tabs.Transfers.TransferMarket.Contracts.contract_gold_full, 2)
                                type(Key.ESC)
                                break
                            else:
                                print "Unknown state, and starting again to parse message"

                                if self.fifa_window_size.exists(Tabs.Transfers.search_results_link) is not None:
                                    print "Doing ESC"
                                    type(Key.ESC)
                                    break

                                try:
                                    self.fifa_window_size.click(Messages.message_maximum_reached_to_buy)
                                    print "You have reached the maximum purchases"
                                    self.save_bought_items()
                                except FindFailed:
                                    pass

                                try:
                                    self.fifa_window_size.click(Buttons.arrow_selected)
                                except FindFailed:
                                    pass


                    print "Clicking next page"
                    type("c")
                    sleep(random.uniform(0.3, 0.6))
                    continue
                except FindFailed:
                    print "Nothing found, trying next page..."
                    self.fifa_window_size.wait(Buttons.s_manually_adjust_price, 2)
                    type("c")
                    sleep(random.uniform(0.3, 0.6))
        elif self.fifa_window_size.wait(Messages.message_nothing_found, 5) is not None:
            Waiters.wait_and_click(self, Buttons.ok_selected)
            print "Nothing found in search results"
        else:
            print "Dont know current stage, going home screen"
            self.go_to_home_sceen()

    def sell_contracts(self, start_price, buy_now_price):
        sell_item = 0
        try:
            for selling in range(1, 100):
                sell_item = sell_item + 1
                print "Selling item: %s " % str(sell_item)
                Waiters.click_first_found_picture(self, (Tabs.MyClub.ClubSearch.Contarcts.club_contract_gold_full, Tabs.MyClub.ClubSearch.Contarcts.club_contract_gold_half), 2)
                print "contract to sell found"

                self.fifa_window_size.wait(Tabs.MyClub.ClubSearch.Contarcts.club_contract_gold_mega, 2)
                Waiters.wait_and_click(self, Tabs.MyClub.ClubSearch.list_on_transfer_market_big, 2)

                Waiters.click_first_found_picture(self, (Tabs.MyClub.ClubSearch.starting_price, Tabs.MyClub.ClubSearch.starting_price_selected), 3)
                self.fifa_window_size.wait(Tabs.MyClub.ClubSearch.club_set_price_form, 3)
                type(str(start_price))
                type(Key.ENTER)

                #Waiters.click_first_found_picture(self, (Tabs.MyClub.ClubSearch.club_buy_now_price, Tabs.MyClub.ClubSearch.club_buy_now_selected), 1)
                Waiters.wait_and_click(self, Tabs.MyClub.ClubSearch.club_buy_now_price)
                self.fifa_window_size.wait(Tabs.MyClub.ClubSearch.club_set_price_form, 3)
                type(str(buy_now_price))
                type(Key.ENTER)

                sleep(random.uniform(0.1, 1.0))
                Waiters.wait_and_click(self, Tabs.MyClub.ClubSearch.list_on_transfer_market, 2)
                #Waiters.click_first_found_picture(self, (Tabs.MyClub.ClubSearch.list_on_transfer_market, Tabs.MyClub.ClubSearch.list_on_transfer_market_selected), 1)

                self.fifa_window_size.wait(Tabs.MyClub.ClubSearch.club_sent_to_transfer_message, 5)
                Waiters.wait_and_click(self, Buttons.arrow_selected)
        except FindFailed:
            if self.fifa_window_size.exists(Messages.message_maximum_items_in_transfer_list, 1) is not None:
                print "Maximum items are listed"
                Waiters.wait_and_click(self, Buttons.ok_selected)
            else:
                print "Somewhere failed to sell"

    def save_bought_items(self):
        for i in range(1, 5):
            type(Key.ESC)
            try:
                if self.fifa_window_size.exists(Messages.message_send_all_items_to_club, 2) is not None:
                    self.fifa_window_size.click(Messages.message_send_all_items_to_club)
                    break
                elif self.fifa_window_size.exists(Tabs.main_panel, 1) is not None:
                    print "Nothing to save"
                    break
                else:
                    print "Still nothing"
                sleep(1)
                # wait_and_click(Buttons.send_all_to_club, 5)
                # type('w')
            except FindFailed:
                print "Unknown state after purchases"


if __name__ == '__main__':

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

        #return x_position, y_position

    while True:
        try:
            Relist = Actions()
            Relist.relist_all()
            Relist.clear_sold()

            Navigation = Navigate()
            Sell = Actions()

            #Sell
            Navigation.go_to_my_club()
            Navigation.select_contracts_to_sell()
            Sell.sell_contracts(200, 250)

            #Buy
            # Navigation.go_to_consumables()
            # Navigation.select_consumables_by_type(Tabs.Transfers.TransferMarket.consumables_type_contract_selected)
            # Navigation.select_quality(Tabs.Transfers.Quality.quality_gold_entered)
            # Navigation.set_pricing(200)
            # Sell.buy_contracts(300)
            # Sell.save_bought_items()

        except FindFailed:
            print "Starting again"
