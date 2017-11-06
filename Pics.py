from sikuli import *

round = 0
contracts_bought = 0
sell = "n"

items_to_sell = 100
sell_min = str(350)
sell_max = str(400)
sell_min_rare = str(700)
sell_max_rare = str(750)

fifa_window = Pattern("fifa_window.png").similar(0.90).targetOffset(0, 40)
club_logo = Pattern("club_logo").similar(0.80)


class Buttons(object):
    select_back = Pattern("button_select_back.png").similar(0.90)
    relist_all = Pattern("relist_all.png").similar(0.80)
    w_clear_sold_items = Pattern("w_clear_sold_items.png").similar(0.99)
    yes = Pattern("yes.png").similar(0.90)
    no = Pattern("no.png").similar(0.90)
    no_selected = Pattern("no_selected.png").similar(0.90)
    ok_selected = Pattern("ok_selected.png").similar(0.90)
    s_manually_adjust_price = Pattern("s_manually_adjust_price.png").similar(0.90)
    d_search = Pattern("d_search.png").similar(0.99)
    c_next_page = Pattern("c_next_page.png").similar(0.99)
    actions = Pattern("actions.png").similar(0.90)
    continue_searching = Pattern("continue_searching.png").similar(0.90)
    continue_searching_selected = Pattern("continue_searching_selected.png").similar(0.90)

    buy_now = Pattern("buy_now.png").similar(0.80)
    buy_now_selected = Pattern("buy_now_selected.png").similar(0.80)

    compare_price = Pattern("compare_price.png").similar(0.90)
    esc = Pattern("esc.png").similar(0.90)

    assign_now = Pattern("assign_now.png").similar(0.80)
    send_all_to_club = Pattern("send_all_to_club.png").similar(0.90)

    page = Pattern("page.png").similar(0.90).targetOffset(0, -200)


class Messages(object):
    message_exit_ut = Pattern("message_exit_from_UT.png").similar(0.95)
    problem_communicating_ea_server = Pattern("problem_communicating_ea_server.png").similar(0.95)
    message_successful_purchase = Pattern("message_successful_purchase.png").similar(0.98)
    message_sorry_expired = Pattern("message_sorry_expired.png").similar(0.80)





class Tabs(object):
    main_panel = Pattern("main_panel.png").similar(0.50)
    tab_transfers = Pattern("Tab_transfers.png").similar(0.40)

    class Transfers(object):
        transfer_market_selected = Pattern("transfer_market_selected.png").similar(0.90)
        transfer_market = Pattern("transfer_market.png").similar(0.90)
        transfer_market_panel = Pattern("transfer_market_panel.png").similar(0.60)
        transfer_list = Pattern("transfer_list.png").similar(0.90)
        transfer_list_selected = Pattern("transfer_list_selected.png").similar(0.90)
        transfer_list_logo = Pattern("transfer_list_logo.png").similar(0.90)
        transfer_list_link = Pattern("transfer_list_link.png").similar(0.90)
        search_results_link = Pattern("search_results_link.png").similar(0.90)
        bidding_options = Pattern("bidding_options.png").similar(0.90)

        class TransferMarket(object):
            consumables = Pattern("consumables.png").similar(0.90)
            consumables_selected = Pattern("consumables_selected.png").similar(0.90)
            consumables_type_text = Pattern("consumables_type_text.png").similar(0.99)
            consumables_type_text_selected = Pattern("consumables_type_text_selected.png").similar(0.99)
            consumables_type_contract_selected = Pattern("consumables_type_contract_selected.png").similar(0.99)

            class Contracts(object):
                contract_gold_full = Pattern("contract_gold_full.png").similar(0.96)
                contract_gold_half = Pattern("contract_gold_half.png").similar(0.96).targetOffset(-10, 0)


        class Quality(object):
            quality_selected = Pattern("quality_selected.png").similar(0.90)
            quality = Pattern("quality.png").similar(0.90)
            quality_gold = Pattern("quality_gold.png").similar(0.90)
            quality_gold_entered = Pattern("quality_gold_entered.png").similar(0.90)

        class Pricing(object):
            max_price = Pattern("max_price.png").similar(0.99)
            pricing_text = Pattern("pricing_text.png").similar(0.99)
            pricing_text_selected = Pattern("pricing_text_selected.png").similar(0.99)
            max_buy_now_selected = Pattern("max_buy_now_selected.png").similar(0.99)
            max_buy_now_200 = Pattern("max_buy_now_200.png").similar(0.99)
            set_price_form = Pattern("set_price_form.png").similar(0.99)


# full_contract=Pattern("full_player_manager.png").exact().targetOffset(-1,-38)
# player_rare=Pattern("player_rare.png").exact()

full_contract_reg = Region(8, 335, 590, 261)
bid_reg = Region(368, 381, 472, 185)
trans_target_reg = Region(559, 445, 267, 47)
con_reg = Region(32, 536, 975, 308)
