import org.sikuli.script.SikulixForJython
# from java.util import *
# from sikuli import *
import pdb
from Pics import *
import players

import time
import smtplib
import datetime

import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
#
# from pydub import AudioSegment
# from pydub.playback import play
# song = AudioSegment.from_wav("sound.wav")
# play(song)

import random
import os
import inspect
from Pics import *


class Main(object):
    def __init__(self):
        setAutoWaitTimeout(3)
        print "Activating Fifa Window"
        click(fifa_window, 3)
        self.fifa_window_size = Region(App.focusedWindow())
        # self.fifa_window_size = Region(0, 0, 1280, 750)
        self.fifa_window_size_left_up = Region(0, 0, 600, 600)
        # self.fifa_window_size.highlight(1)
        print self.fifa_window_size
        # self.fifa_window_size.click(club_logo)
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

    def click_any_first_found_picture(self, list_to_search, timeout=1):
        for times in range(0, timeout):
            print "searching " + str(times)
            for picture in list_to_search:
                try:
                    self.fifa_window_size.wait(picture, 1)
                    click(self.fifa_window_size.getLastMatch())
                    return
                except FindFailed:
                    print str(picture) + " not found"

    def wait_and_click(self, image_name, timeout=0):
        # mozilla_size.click(image_name)
        self.fifa_window_size.wait(image_name, timeout)
        click(self.fifa_window_size.getLastMatch())


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
    def initiate_market_wipe(first_hour, run='no', contracts='no'):
        # print(first_hour)
        current_hour = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H')
        # print(current_hour)
        if first_hour != current_hour or run == 'yes':
            print "Current time is: %s" % current_hour
            print("doing market WIPE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            first_hour = current_hour
            go_home = Navigate()
            go_home.go_to_home_screen()
            # Re-list contract
            try:
                relist = Actions()
                relist.relist_all()
                relist.clear_sold()
            except FindFailed:
                print "Failed with sell re-list or clear"
            # Sell contract
            # try:
            #     Navigation = Navigate()
            #     Sell = Actions()
            #     Navigation.go_to_my_club()
            #     Navigation.select_contracts_to_sell()
            #     Sell.sell_contracts(200, 250)
            # except FindFailed:
            #     print "Failed with sell contract"

        # if contracts == 'yes':
        #     buy_contract()
        # else:
        #     pass
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
    def hover_mouse(x, y):
        mouseLoc = Env.getMouseLocation()
        x_position = mouseLoc.getX()
        y_position = mouseLoc.getY()
        hover(Location(x_position + x, y_position + y))


class Navigate(Waiters):
    def check_if_home_page(self):
        try:
            print "Checking if home page"
            try:
                self.fifa_window_size.wait(Tabs.main_panel_buttons_1, 0)
                print "Home page by default"
                return True
            except FindFailed:
                try:
                    self.fifa_window_size.wait(Tabs.main_panel_buttons_2, 0)
                    print "Home page by default"
                    return True
                except FindFailed:
                    print "Not HOME PAGE"
                    return False
        except FindFailed:
            return False

    def check_if_exit_message(self):
        if self.fifa_window_size.exists(Messages.message_exit_ut, 1) is not None:
            try:
                Waiters.wait_and_click(self, Buttons.no_selected)
            except FindFailed:
                Waiters.wait_and_click(self, Buttons.no)
            print "HOME PAGE"
            return True

    def go_to_home_screen(self):
        print(inspect.stack()[0][3])
        if self.check_if_exit_message():
            print "HOME PAGE"
            return

        if self.check_if_home_page():
            print "HOME PAGE"
            return

        # try:
        #     wait(Buttons.team_viewer_ok, 1)
        #     click(getLastMatch())
        # except FindFailed:
        #     pass

        for item in range(1, 5):
            try:
                type(Key.ESC)
                sleep(1)
                if self.check_if_home_page():
                    print "HOME PAGE"
                    return
                # break
            except FindFailed:
                print " Not HOME PAGE yet"

        if self.check_if_exit_message():
            return

        self.check_if_main_menu()

    def check_if_main_menu(self):
        try:
            self.fifa_window_size.exists(Messages.message_exit_game, 1)
            Waiters.wait_and_click(self, Buttons.no_selected)
            Waiters.click_any_first_found_picture(self, (Tabs.ultimate_team, Tabs.ultimate_team_selected))
            sleep(90)
        except FindFailed:
            print "Unknown location!!!!"

    def go_to_transfer_list(self):
        self.go_to_home_screen()
        Waiters.click_first_found_picture(self, (Tabs.tab_transfers, Tabs.tab_transfers_selected))
        Waiters.click_first_found_picture(self,
                                          (Tabs.Transfers.transfer_list_selected, Tabs.Transfers.transfer_list), 1)
        self.fifa_window_size.wait(Tabs.Transfers.transfer_list_link, 3)

    def go_to_transfer_market(self):
        self.go_to_home_screen()
        print "Going to transfer market"
        Waiters.click_first_found_picture(self, (Tabs.tab_transfers, Tabs.tab_transfers_selected), 2)
        Waiters.click_first_found_picture(self,
                                          (Tabs.Transfers.transfer_market, Tabs.Transfers.transfer_market_selected), 2)
        self.fifa_window_size.wait(Tabs.Transfers.transfer_market_panel, 3)

    def go_to_consumables(self):
        self.go_to_transfer_market()
        Waiters.click_first_found_picture(self, (
            Tabs.Transfers.TransferMarket.consumables_selected, Tabs.Transfers.TransferMarket.consumables), 2)

    def go_to_players(self):
        try:
            Waiters.wait_and_click(self, Buttons.ok_selected)
        except FindFailed:
            pass

        if self.fifa_window_size.exists(Tabs.Transfers.Players.Players_selected, 1) is not None:
            sleep(1)
            type('q')
            sleep(1)
            print "Reset all"
            return

        self.go_to_transfer_market()
        Waiters.click_first_found_picture(self,
                                          (Tabs.Transfers.Players.Players_selected, Tabs.Transfers.Players.Players), 3)
        self.fifa_window_size.wait(Tabs.Transfers.Players.Players_selected, 1)
        sleep(1)
        print "Reset all"
        type('q')
        sleep(1)

    def go_to_icons(self):

        if self.fifa_window_size.exists(Tabs.Transfers.Players.icons, 1) is not None:
            return
        self.go_to_transfer_market()

        Waiters.click_first_found_picture(self,
                                          (Tabs.Transfers.Players.Players_selected, Tabs.Transfers.Players.Players), 2)

        self.fifa_window_size.wait(Tabs.Transfers.Players.Players_selected, 1)

        sleep(1)
        print "Reset all"
        type('q')
        sleep(1)

        Waiters.wait_and_click(self, Tabs.Transfers.Players.league)
        self.fifa_window_size.wait(Tabs.Transfers.Players.league_selected, 1)

        for item in range(1, 40):
            try:
                self.fifa_window_size.wait(Tabs.Transfers.Players.icons_selected, 1)
                type(Key.ESC)
                break
            except FindFailed:
                os.system("left.exe")

    def set_player_name(self, name):
        Waiters.click_first_found_picture(self, (Tabs.Transfers.Players.Player_name_selected, Tabs.Transfers.Players.
                                                 Player_name), 2)
        self.fifa_window_size.wait(Tabs.Transfers.Players.Player_pricing, 2)

        # Settings.TypeDelay = 0.1
        type(name)
        Settings.TypeDelay = 0.1
        sleep(0.3)

        self.fifa_window_size.wait(Buttons.arrow_selected, 1)
        type(Key.ENTER)

    def go_to_my_club(self):
        self.go_to_home_screen()
        Waiters.click_first_found_picture(self, (Tabs.MyClub.my_club, Tabs.MyClub.my_club_selected), 2)
        self.fifa_window_size.hover(Tabs.main_panel_buttons_1)
        Waiters.click_first_found_picture(self,
                                          (Tabs.MyClub.my_club_inside_selected, Tabs.MyClub.my_club_inside), 2)
        self.fifa_window_size.wait(Tabs.MyClub.club_search_logo, 3)

    def select_contracts_to_sell(self):
        print(inspect.stack()[0][3])
        Waiters.click_first_found_picture(self, (
            Tabs.MyClub.ClubSearch.club_reset, Tabs.MyClub.ClubSearch.club_reset_selected), 2)
        Waiters.click_first_found_picture(self, (
            Tabs.MyClub.ClubSearch.club_search_type, Tabs.MyClub.ClubSearch.club_search_type_selected), 2)

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

        # self.fifa_window_size.wait(Buttons.d_search)
        type("d")

    def select_consumables_by_type(self, selected_type):
        print(inspect.stack()[0][3])
        Waiters.click_first_found_picture(self, (Tabs.Transfers.TransferMarket.consumables_type_text_selected,
                                                 Tabs.Transfers.TransferMarket.consumables_type_text), 3)
        for item in range(1, 9):
            try:
                self.fifa_window_size.wait(selected_type, 1)
                type(Key.ENTER)
                break
            except FindFailed:
                os.system("left.exe")

    def select_quality(self, quality):
        print(inspect.stack()[0][3])
        Waiters.wait_and_click(self, Tabs.Transfers.Quality.quality, 1)
        for item in range(1, 8):
            try:
                self.fifa_window_size.wait(quality, 1)
                type(Key.ENTER)
                break
            except FindFailed:
                os.system("left.exe")

    def set_pricing(self, max_buy_now):
        print(inspect.stack()[0][3])
        try:
            Waiters.wait_and_click(self, Tabs.Transfers.Pricing.pricing_text, 2)
        except FindFailed:
            Waiters.wait_and_click(self, Tabs.Transfers.Pricing.pricing_text_selected, 2)
        for item in range(1, 8):
            try:
                self.fifa_window_size.wait(Tabs.Transfers.Pricing.max_buy_now_selected, 1)
                type(Key.ENTER)
                break
            except FindFailed:
                os.system("up.exe")
        # try:
        #     Waiters.wait_and_click(self, Tabs.Transfers.Pricing.max_buy_now_selected, 2)
        # except FindFailed:
        #     Waiters.wait_and_click(self, Tabs.Transfers.Pricing.max_buy_now, 2)

        self.fifa_window_size.wait(Tabs.Transfers.Pricing.set_price_form, 2)
        type(str(max_buy_now))
        type(Key.ENTER)
        self.fifa_window_size.wait(Buttons.s_manually_adjust_price, 2)
        # type(Key.ESC)
        self.fifa_window_size.wait(Buttons.d_search, 2)


class Actions(Navigate):
    page = 0
    bought_items = 0
    expired_items = 0

    def relist_all(self):
        print(inspect.stack()[0][3])
        self.go_to_transfer_list()
        try:
            self.fifa_window_size.wait(Buttons.relist_all, 2)
            type("e")
            self.wait_and_click(Buttons.yes, 2)
        except FindFailed:
            print "Looks nothing to re-list"
        sleep(4)

    # try:
    #     if self.fifa_window_size.exists(Buttons.relist_all, 5) is not None:
    #         print "Need to relist manually "
    #         for page in range(1, 11):
    #             print page
    #             type("c")
    #             sleep(1)
    #             try:
    #                 self.fifa_window_size.wait(Buttons.c_next_page, 3)
    #             except FindFailed:
    #                 print "looks that last page"
    #                 break
    #         try:
    #             for items_to_re_list in range(1, 100):
    #                 self.fifa_window_size.wait(Buttons.expired_cross, 1)
    #                 self.fifa_window_size.wait(Buttons.button_list_on_transfer_market, 1)
    #                 type(Key.ENTER)
    #                 Waiters.click_first_found_picture(self, (
    #                     Tabs.Transfers.TransferList.transfer_list_List_on_transfer_market,
    #                     Tabs.Transfers.TransferList.transfer_list_List_on_transfer_market), 1)
    #                 self.fifa_window_size.wait(Tabs.MyClub.ClubSearch.club_sent_to_transfer_message, 5)
    #                 Waiters.wait_and_click(self, Buttons.arrow_selected)
    #                 sleep(2)
    #         except FindFailed:
    #             print "Done with manual re-listing"
    #     else:
    #         print "Done with re-listing"
    # except FindFailed:
    #     print "Done with re-listing"

    def clear_sold(self):
        print(inspect.stack()[0][3])
        self.go_to_transfer_list()
        try:
            sleep(2)
            if self.fifa_window_size.exists(Buttons.w_clear_sold_items, 1) is not None:
                print "Clearing..."
                type("w")
                sleep(3)
            else:
                print "Looks nothing to clear"
        except FindFailed:
            pass

    def sell_contracts(self, start_price, buy_now_price):
        print(inspect.stack()[0][3])
        sell_item = 0
        try:
            for selling in range(1, 100):
                sell_item = sell_item + 1
                print "Selling item: %s " % str(sell_item)
                Waiters.click_first_found_picture(self, (Tabs.MyClub.ClubSearch.Contarcts.club_contract_gold_full,
                                                         Tabs.MyClub.ClubSearch.Contarcts.club_contract_gold_full_1,
                                                         Tabs.MyClub.ClubSearch.Contarcts.club_contract_gold_half,
                                                         Tabs.MyClub.ClubSearch.Contarcts.club_contract_gold_half_1), 2)
                print "contract to sell found"

                self.fifa_window_size.wait(Tabs.MyClub.ClubSearch.Contarcts.club_contract_gold_mega, 3)
                Waiters.wait_and_click(self, Tabs.MyClub.ClubSearch.list_on_transfer_market_big, 2)

                Waiters.click_first_found_picture(self, (
                    Tabs.MyClub.ClubSearch.starting_price, Tabs.MyClub.ClubSearch.starting_price_selected), 3)
                self.fifa_window_size.wait(Tabs.MyClub.ClubSearch.club_set_price_form, 3)
                type(str(start_price))
                type(Key.ENTER)

                # Waiters.click_first_found_picture(self, (Tabs.MyClub.ClubSearch.club_buy_now_price,
                # Tabs.MyClub.ClubSearch.club_buy_now_selected), 1)
                Waiters.wait_and_click(self, Tabs.MyClub.ClubSearch.club_buy_now_price)
                self.fifa_window_size.wait(Tabs.MyClub.ClubSearch.club_set_price_form, 3)
                type(str(buy_now_price))
                type(Key.ENTER)

                sleep(random.uniform(0.1, 1.0))
                Waiters.wait_and_click(self, Tabs.MyClub.ClubSearch.list_on_transfer_market, 2)
                # Waiters.click_first_found_picture(self, (Tabs.MyClub.ClubSearch.list_on_transfer_market,
                # Tabs.MyClub.ClubSearch.list_on_transfer_market_selected), 1)

                self.fifa_window_size.wait(Tabs.MyClub.ClubSearch.club_sent_to_transfer_message, 5)
                Waiters.wait_and_click(self, Buttons.arrow_selected)
        except FindFailed:
            if self.fifa_window_size.exists(Messages.message_maximum_items_in_transfer_list, 1) is not None:
                print "Maximum items are listed"
                Waiters.wait_and_click(self, Buttons.ok_selected)
            else:
                print "Somewhere failed to sell"

    def save_bought_items(self):
        print(inspect.stack()[0][3])
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

    def buy_contracts(self, pages):
        print(inspect.stack()[0][3])
        print "Going to search for %s pages" % pages
        bought_items = 0
        expired_items = 0
        type("d")
        # pdb.set_trace()
        if self.fifa_window_size.exists(Buttons.page, 5) is not None:
            for page in range(1, pages):
                count_bad_click = 0
                if bought_items == 29:
                    self.save_bought_items()
                    return
                # Move mouse to top
                try:
                    # self.fifa_window_size.hover(Buttons.page)
                    self.fifa_window_size.hover(Location(0, 750))

                except FindFailed:
                    pass

                print "Page: " + str(page + 1)

                try:
                    # Wait for actions button
                    self.fifa_window_size.wait(Buttons.actions, 3)
                    print "Searching..."

                    # Search for item
                    # pdb.set_trace()
                    Waiters.wait_and_click(self, Tabs.Transfers.TransferMarket.Contracts.contract_gold_half)
                    # location = fifa_window_size.wait(Tabs.Transfers.TransferMarket.Contracts.contract_gold_half).getCenter()
                    print "Something found, trying to selected and buy"
                    # hover(location); Service.hover_mouse(0, 100); Service.hover_mouse(0, -100); click(getLastMatch())
                    # fifa_window_size.wait(Tabs.Transfers.TransferMarket.Contracts.contract_gold_half, 0); hover(getLastMatch()); Service.hover_mouse(0, 100); Service.hover_mouse(0, -100); click()

                    try:
                        print "Checking if right item was clicked (FULL size)"
                        self.fifa_window_size_left_up.wait(Tabs.Transfers.TransferMarket.Contracts.contract_gold_full,
                                                           2)
                    except FindFailed:

                        try:
                            # pdb.set_trace()
                            type("c")

                            print "bad click"
                            type("c")
                            print "Next page"

                            if self.fifa_window_size.exists(Tabs.Transfers.bidding_options, 0) is not None:
                                print "clicked on wrong item"
                                type(Key.ESC)
                                continue
                            else:
                                continue
                        except FindFailed:
                            pass

                    # as item was selected, clicking on buy now
                    Waiters.click_first_found_picture(self, (Buttons.buy_now, Buttons.buy_now_selected), 2)
                    Waiters.wait_and_click(self, Buttons.yes, 3)

                    # fifa_window_size.exists(Messages.message_sorry_expired, 1)
                    for attempts in range(1, 3):
                        try:
                            self.fifa_window_size.wait(Messages.message_successful_purchase, 4)
                            Waiters.click_first_found_picture(self, (
                                Buttons.continue_searching, Buttons.continue_searching_selected), 2)
                            bought_items = bought_items + 1
                            print "Bought: %s items !!" % str(bought_items)
                            print "Going to the next page, as purchase done here"
                            break
                        except FindFailed:
                            if self.fifa_window_size.exists(Messages.message_sorry_expired, 1) is not None:
                                expired_items = expired_items + 1
                                print "Expired item: %s" % str(expired_items)
                                if expired_items == 10:
                                    print "Too many expired items, does not make sense to continue," \
                                          "goig to start search again "
                                    self.fifa_window_size.click(Buttons.ok_selected)
                                    # self.fifa_window_size.wait(Tabs.Transfers.search_results_link, 3)
                                    # type(Key.ESC)
                                    # self.fifa_window_size.wait(Buttons.d_search, 3)
                                    # type('d')
                                    return
                                self.fifa_window_size.click(Buttons.ok_selected)
                                self.fifa_window_size.wait(Tabs.Transfers.TransferMarket.Contracts.contract_gold_full,
                                                           2)
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
        elif self.fifa_window_size.exists(Messages.message_nothing_found, 3) is not None:
            Waiters.wait_and_click(self, Buttons.ok_selected)
            print "Nothing found in search results"
        elif self.fifa_window_size.exists(Messages.problem_communicating_ea_server, 2) is not None:
            Waiters.wait_and_click(self, Buttons.ok_selected)
            print "Looks that EA blocked access, waiting for 10 mins"
            sleep(600)
            return
        else:
            print "Dont know current stage, going home screen"
            self.go_to_home_screen()

    def buy_players(self, value_to_sell_if_duplicate):
        print(inspect.stack()[0][3])
        self.fifa_window_size.wait(Buttons.d_search, 1)
        type('d')

        if self.fifa_window_size.exists(Buttons.actions, 2) is not None:
            type(Key.ENTER)
            Waiters.click_first_found_picture(self, (Buttons.buy_now, Buttons.buy_now_selected), 1)
            print("Player Found!!!!!!!!!!!!!!!!!!!")
            Waiters.wait_and_click(self, Buttons.yes, 3)
            try:
                self.fifa_window_size.wait(Messages.message_successful_purchase, 3)
                Waiters.click_first_found_picture(self,
                                                  (Buttons.assign_now_after_buy_selected, Buttons.assign_now_after_buy),
                                                  2)
                print("Player BOUGHT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                import pdb; pdb.set_trace()

                if self.fifa_window_size.exists(Tabs.Transfers.BoughtItems.duplicate_message, 3) is not None:
                    print('Duplicated item!!')
                    sleep(5)
                    # self.fifa_window_size.click(Tabs.MyClub.ClubSearch.list_on_transfer_market, 2)
                    type('s')
                    Waiters.click_first_found_picture(self, (
                        Tabs.MyClub.ClubSearch.starting_price_selected, Tabs.MyClub.ClubSearch.starting_price), 2)
                    self.fifa_window_size.wait(Tabs.Transfers.Pricing.set_price_form, 2)
                    listing_price = int(value_to_sell_if_duplicate) * 10
                    print("listing for: " + str(listing_price))
                    type(str(int(int(value_to_sell_if_duplicate) * 10)))
                    type(Key.ENTER)
                    os.system("down.exe")
                    self.fifa_window_size.wait(Tabs.MyClub.ClubSearch.club_buy_now_price_selected, 2)
                    type(Key.ENTER)
                    sleep(0.5)
                    type(str(int(int(value_to_sell_if_duplicate) * 10)))
                    sleep(0.5)
                    type(Key.ENTER)
                    self.fifa_window_size.click(Buttons.sell_list_on_transfer_market, 2)
                    Waiters.wait_and_click(self, Buttons.ok_selected, 3)
                    try:
                        Waiters.click_any_first_found_picture(self, (Buttons.ok_selected, Buttons.yes_selected), 3)
                    except FindFailed:
                        pass
                    self.back_to_search()

                else:
                    print('Non duplicated item')
                    self.fifa_window_size.wait(Tabs.Transfers.BoughtItems.confirm_items, 2)
                    type('e')
                    print('Sent to club!!!')
                    self.back_to_search()

            except FindFailed:
                if self.fifa_window_size.exists(Messages.message_sorry_expired, 1) is not None:
                    print("Expired")
                    self.back_to_search()

                else:
                    print("debbug")
                    self.back_to_search()

        elif self.fifa_window_size.exists(Messages.problem_communicating_ea_server, 1) is not None:
            Waiters.wait_and_click(self, Buttons.ok_selected)
            print "Looks that EA blocked access, waiting for 10 mins"
            sleep(600)
            return
        else:
            print "Player not found"
            Waiters.click_any_first_found_picture(self, (Buttons.arrow_selected, Buttons.yes_selected), 1)
            sleep(random.uniform(3.0, 7.0))
            type(Key.ESC)

    def back_to_search(self):
        for i in range(1, 5):
            type(Key.ESC)
            try:
                if self.fifa_window_size.exists(Tabs.search_results_tab, 2) is not None:
                    break
                else:
                    Waiters.click_any_first_found_picture(self, (Buttons.arrow_ok_selected, Buttons.yes_selected), 1)
            except FindFailed:
                print "Unknown state"


class Page(object):

    def __init__(self):
        try:
            # os.system("taskkill /im chrome.exe")
            os.system("taskkill /f /im  chrome.exe")
            sleep(5)
        except:
            pass
        self.sent = []

        options = webdriver.ChromeOptions()
        options.add_argument(r"user-data-dir=c:\Users\power\AppData\Local\Google\Chrome\User Data")

        # self.driver = webdriver.Chrome(executable_path="geckodriver.exe")
        try:
            self.driver = webdriver.Chrome(chrome_options=options)
            # sleep(2)
            self.driver.implicitly_wait(5)
        except:
            pass

    def open_link(self, player_link):
        self.driver.get(player_link)

    def get_lowest_player_price(self, time=10, ):
        # price = self.driver.find_element_by_id("pc-lowest-5")
        try:
            element = WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.ID, "pc-lowest-1"))
            )
            return element.text
        except:
            print "Web price not found, returning none"
            return None


def buy_player_func(name, price=None, percentage=0.5, futbin='yes', random_name=True, random_price=None):
    try:
        try:
            if random_name:
                name = random.choice(name)
        except KeyError:
            name_for_exc = name
            name = random.choice(list(name))

            if futbin == 'yes':
                print "Opening WEB of FUTBIN for latest price...  "

                Futbin.open_link(name_for_exc[name][1])
                price = Futbin.get_lowest_player_price()
                # Futbin.driver.quit()
                print 'FUTBIN price: ' + name + ': ' + price

                if price == '0' or price is None:
                    price = name_for_exc[name][0]
                    print "Taking default price from script " + str(price)
                    price = str(price)
                elif "," in price:
                    price = int(price.replace(",", ""))
                else:
                    pass

                price = price - (price * percentage)
                price = int(float(price))
                # round to 500
                price = (price + 250) // 500 * 500

            # price_range = random.randrange(0, int(name_for_exc[name][0])/20, 100)
            # print price_range

        if price is None:
            price = name_for_exc[name][0]

        if random_price is True:
            price = int(price) * random.uniform(0.8, 1)
            price = format(int(price), 'd')

        print "!!!!! Going to search for: " + name + " for: " + str(price)

        navigation.go_to_players()
        navigation.set_player_name(name)
        navigation.set_pricing(price)
        navigation.buy_players(price)

    except FindFailed:
        print "Failed with buy player"
        type(Key.ESC)


if __name__ == '__main__':
    navigation = Actions()
    first_hour = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H')
    Futbin = Page()

    while True:
        try:
            # buy_player_func(Tabs.Transfers.Players.Names.Rare.price_85, price='6000', random_price=True)
            # for each in Tabs.Transfers.Players.Names.Rare.all_85:
            #     buy_player_func([each], price='6000', random_price=True)

            # buy_player_func(Tabs.Transfers.Players.Names.Rare.all_85, price='9000', random_price=True)
            # sleep(random.uniform(1, 3))
            # buy_player_func(Tabs.Transfers.Players.Names.Rare.price_86, price='14000', random_price=True)
            # sleep(random.uniform(1, 3))
            # buy_player_func(Tabs.Transfers.Players.Names.Rare.all_87, price='18000', random_price=True)
            # # buy_player_func(['Hummels'], price='3000')
            buy_player_func(players.Exceptional.From30to50, None, 0.30)
            buy_player_func(players.Exceptional.From30to50, None, 0.30)
            buy_player_func(players.Exceptional.From30to50, None, 0.30)
            buy_player_func(players.Exceptional.From30to50, None, 0.30)
            buy_player_func(players.Exceptional.From30to50, None, 0.30)
            buy_player_func(players.Exceptional.From50to100, None, 0.25)
            buy_player_func(players.Exceptional.From100to200, None, 0.25)
            buy_player_func(players.Exceptional.From200to1M, None, 0.20)
            #
            #
            first_hour = Service.initiate_market_wipe(first_hour, run='no', contracts="no")
            #sleep(random.uniform(1, 3))
        except Exception as error:
            print error
