from sikuli import *

round = 0
contracts_bought = 0
sell = "n"

items_to_sell = 100
sell_min = str(350)
sell_max = str(400)
sell_min_rare = str(700)
sell_max_rare = str(750)

fifa_window = Pattern("fifa_window.png").similar(0.70).targetOffset(0, 40)
club_logo = Pattern("club_logo").similar(0.80)


class Buttons(object):
    select_back = Pattern("button_select_back.png").similar(0.90)
    relist_all = Pattern("relist_all.png").similar(0.80)
    w_clear_sold_items = Pattern("w_clear_sold_items.png").similar(0.90)
    yes = Pattern("yes.png").similar(0.80)
    no = Pattern("no.png").similar(0.90)
    no_selected = Pattern("no_selected.png").similar(0.80)
    yes_selected = Pattern("yes_selected.png").similar(0.95)

    ok_selected = Pattern("ok_selected.png").similar(0.90)
    arrow_selected = Pattern("arrow_selected.png").similar(0.95)
    s_manually_adjust_price = Pattern("s_manually_adjust_price.png").similar(0.90)
    d_search = Pattern("d_search.png").similar(0.95)
    c_next_page = Pattern("c_next_page.png").similar(0.90)
    actions = Pattern("actions.png").similar(0.90)
    continue_searching = Pattern("continue_searching.png").similar(0.90)
    continue_searching_selected = Pattern("continue_searching_selected.png").similar(0.90)

    button_list_on_transfer_market = Pattern("button_list_on_transfer_market.png").similar(0.90)
    sell_list_on_transfer_market = Pattern("sell_list_on_transfer_market.png").similar(0.90)

    buy_now = Pattern("buy_now.png").similar(0.80)
    buy_now_selected = Pattern("buy_now_selected.png").similar(0.80)

    compare_price = Pattern("compare_price.png").similar(0.90)
    esc = Pattern("esc.png").similar(0.90)

    assign_now = Pattern("assign_now.png").similar(0.80)
    assign_now_after_buy = Pattern("assign_now_after_buy.png").similar(0.90)
    assign_now_after_buy_selected = Pattern("assign_now_after_buy_selected.png").similar(0.90)
    place_on_transfer_list = Pattern("place_on_transfer_list.png").similar(0.90)

    send_all_to_club = Pattern("send_all_to_club.png").similar(0.90)

    page = Pattern("page.png").similar(0.90).targetOffset(0, -200)

    expired_cross = Pattern("expired_cross.png").similar(0.90)

    team_viewer_ok = Pattern("team_viewer_ok.png").similar(0.90)


class Messages(object):
    message_exit_ut = Pattern("message_exit_from_UT.png").similar(0.90)
    problem_communicating_ea_server = Pattern("problem_communicating_ea_server.png").similar(0.90)
    message_successful_purchase = Pattern("message_successful_purchase.png").similar(0.80)
    message_sorry_expired = Pattern("message_sorry_expired.png").similar(0.90)
    message_send_all_items_to_club = Pattern("message_send_all_items_to_club.png").similar(0.80)
    message_send_all_items_to_club_selected = Pattern("message_send_all_items_to_club_selected.png").similar(0.80)
    message_maximum_items_in_transfer_list = Pattern("message_maximum_items_in_transfer_list.png").similar(0.80)
    message_maximum_reached_to_buy = Pattern("message_maximum_reached_to_buy.png").similar(0.80)

    message_nothing_found = Pattern("message_nothing_found.png").similar(0.80)


class Tabs(object):
    # main_panel = Pattern("main_panel.png").similar(0.99)
    main_panel = Pattern("main_panel.png").similar(0.80)
    main_panel_buttons = Pattern("main_panel_buttons.png").similar(0.85)

    tab_transfers = Pattern("Tab_transfers.png").similar(0.80)
    tab_transfers_selected = Pattern("Tab_transfers_selected.png").similar(0.80)

    ultimate_team = Pattern("ultimate_team.png").similar(0.90)
    ultimate_team_selected = Pattern("ultimate_team_selected.png").similar(0.90)

    ultimate_team_2 = Pattern("ultimate_team_2.png").similar(0.90)
    ultimate_team_selected_2 = Pattern("ultimate_team_2_selected.png").similar(0.90)
    search_results_tab = Pattern("search_results_tab.png").similar(0.95)


    class Transfers(object):
        transfer_market_selected = Pattern("transfer_market_selected.png").similar(0.90)
        transfer_market = Pattern("transfer_market.png").similar(0.90)
        transfer_market_panel = Pattern("transfer_market_panel.png").similar(0.60)
        transfer_list = Pattern("transfer_list.png").similar(0.90)
        transfer_list_selected = Pattern("transfer_list_selected.png").similar(0.90)
        transfer_list_logo = Pattern("transfer_list_logo.png").similar(0.90)
        transfer_list_link = Pattern("transfer_list_link.png").similar(0.80)
        search_results_link = Pattern("search_results_link.png").similar(0.90)
        bidding_options = Pattern("bidding_options.png").similar(0.90)

        class TransferMarket(object):
            consumables = Pattern("consumables.png").similar(0.90)
            consumables_selected = Pattern("consumables_selected.png").similar(0.90)
            consumables_type_text = Pattern("consumables_type_text.png").similar(0.80)
            consumables_type_text_selected = Pattern("consumables_type_text_selected.png").similar(0.80)
            consumables_type_contract_selected = Pattern("consumables_type_contract_selected.png").similar(0.99)

            class Contracts(object):
                contract_gold_full = Pattern("contract_gold_full.png").similar(0.96)
                # contract_gold_half = Pattern("contract_gold_half.png").similar(0.96).targetOffset(10, 60)
                contract_gold_half = Pattern("contract_gold_half.png").similar(0.96).targetOffset(-20, 10)
                contract_gold_common = Pattern("contract_gold_common.png").exact()

        class Quality(object):
            quality_selected = Pattern("quality_selected.png").similar(0.90)
            quality = Pattern("quality.png").similar(0.90)
            quality_gold = Pattern("quality_gold.png").similar(0.90)
            quality_gold_entered = Pattern("quality_gold_entered.png").similar(0.90)

        class Pricing(object):
            max_price = Pattern("max_price.png").similar(0.90)
            pricing_text = Pattern("pricing_text.png").similar(0.90)
            pricing_text_selected = Pattern("pricing_text_selected.png").similar(0.90)
            max_buy_now_selected = Pattern("max_buy_now_selected.png").similar(0.99)
            max_buy_now = Pattern("max_buy_now.png").similar(0.95)

            max_buy_now_200 = Pattern("max_buy_now_200.png").similar(0.90)
            set_price_form = Pattern("set_price_form.png").similar(0.90)

        class TransferList(object):
            transfer_list_List_on_transfer_market = Pattern("transfer_list_List_on_transfer_market.png").similar(0.90)
            transfer_list_List_on_transfer_market_selected = Pattern(
                "transfer_list_List_on_transfer_market_selected.png").similar(0.90)

        class BoughtItems(object):
            keep_items = Pattern("keep_items.png").similar(0.90)
            send_to_transfer_list = Pattern("send_to_transfer_list.png").similar(0.90)
            send_to_transfer_list_selected = Pattern("send_to_transfer_list_selected.png").similar(0.90)

            confirm_items = Pattern("confirm_items.png").similar(0.90)

            duplicate_message = Pattern("duplicate_message.png").similar(0.80)



        class Players(object):
            Players = Pattern("Players.png").similar(0.80)
            Players_selected = Pattern("Players_selected.png").similar(0.90)
            Player_name = Pattern("Player_name.png").similar(0.85)
            Player_name_selected = Pattern("Player_name_selected.png").similar(0.85)
            Player_pricing = Pattern("Player_pricing.png").similar(0.90)
            league = Pattern("league.png").similar(0.95)
            league_selected = Pattern("league_selected.png").similar(0.95)
            icons_selected = Pattern("icons_selected.png").similar(0.95)
            icons = Pattern("icons.png").similar(0.95)

            class Names(object):
                class Rare(object):
                    Rate_75 = ['Jeremy Toljan', 'Abdoulay Diaby', 'Andre Gray', 'Kevin Akpoguma', 'Lekue',
                               'Moussa Dembele', 'Simon Falette', 'Soualiho Meite', 'Bebe', 'Ailton', 'Ryan Donk',
                               'Selcuk Inan', 'Bart Ramselaar', 'Ridgeciano Haps', 'Borja Baston', 'Achraf Hakimi',
                               'Chancel Mbemba', 'Antonio Barreca', 'Daniel Amartey', 'Mame Diouf', 'Dwight Gayle',
                               'Lukas Klostermann', 'Mathew Leckie', 'Patrick van Aanholt', 'Jurgen Damm',
                               'Papa Ndiaye', 'Christian Atsu', 'Sam Larsson', 'Abel Hernandez', 'Dmitriy Tarasov',
                               'Omar Colley', 'Nahitan Nandez', 'Darwin Machis', 'Andreas Cornelius', 'Vieirinha',
                               'Wesley', 'Andrea Petagna', 'Leigh Griffiths', 'Mejia', 'Hector Villalba',
                               'Orbelin Pineda', 'Joe Bryan', 'Laurent Depoitre', 'Vladimir Hernandez', 'Sander Berge',
                               'Matej Vydra', 'Andreas Cornelius', 'Francois Kamano', 'Konstantinos Stafylidis',
                               'Christopher Jullien', 'Adama', 'Moussa Dembele', 'Scott Sinclair',
                               'Leandro Gonzalez', 'Andres Ibarguen', 'Jonathan Kodjia', 'Zambo Anguissa',
                               'Edgar Mendez', 'Bebe', 'Matias Fernandez', 'Paolo Hurtado', 'Hanno Behrens',
                               'Christian Luyindama', 'Carlos Lopez', 'Gamarra', 'Ahmed Musa',
                               'Alfredo Donnarumma', 'Idrissa Mandiang', 'Juan Camilo', 'Francesco Caputo',
                               'Thievy Bifouma', 'Romulo Otero', "Stephane M", 'Sekou Sanogo', 'Aden Flint',
                               'Slobodan Rajkovic', 'Marc Schnatterer', 'Ike Opara', 'Luis Quinones', 'Raul Bobadilla',
                               'Alberth Elis', 'Darwin Quintero', 'Pablo Guinazu', 'Frank Acheampong', 'Lei Wu',
                               'Marcelo Saracchi']
                    Rate_76 = ['Moussa Sissoko', 'Hernani', 'Riza Durmisi', 'Arthur Masuaku', 'Dalbert',
                               'Borja Iglesias', 'Daniel Ginczek', 'Jetro Willems', 'Wilfried Bony', 'Dayot Upamecano',
                               'Lasse Schone', 'Enner Valencia', 'Henry Onyekuru', 'Milot Rashica',
                               'Solomon Kverkvelia', 'Stefan Ristovski', 'Rick Karsdorp', 'Theo Hernandez',
                               'Andreas Samaris', 'Caner Erkin', 'Jeffrey Bruma', 'Cyril Thereau', 'Francisco Geraldes',
                               'Jean-Kevin Augustin', 'Ivan Ordets', 'Cheikhou Kouyate','Serdar Aziz', 'DeAndre Yedlin',
                               'Ruben Sobrino', 'Gregoire Defrel', 'Marten de Roon', 'Florent Hanin', 'Eder Balanta',
                               'Ismaila Sarr', 'Emmanuel Boateng', 'Dorlan Pabon', 'Willy Boly', 'James Forrest',
                               'Renan Bardini Bressan', 'Martin Benitez', 'Pontus Jansson', 'Diego Gonzalez',
                               'Ruslan Malinovskyi', 'Alan Ruiz', 'Gil', 'Jose Sosa', 'Luca Zuffi', 'Ihlas Bebou',
                               'Moses Simon', 'Rodolfo Pizarro', 'Seydou Doumbia', 'Kieran Tierney', 'Raul Ruidiaz',
                               'Fabricio Bustos', 'Moussa Konate', 'Juan Manuel Iturbe','Alexander Djiku','Kevin Mbabu',
                               'Fredy Guarin','Yevhen Khacheridi','Alfa Semedo Esteves','Omar Abdulrahman']
                    Rate_77 = ['Alberto Moreno', 'Eric Maxim Choupo-Moting', 'Jordan Lukaku', 'Troy Deeney',
                               'Carlos Sanchez', 'Denis Zakaria', 'Eric Maxim Choupo-Moting', 'Ferland Mendy',
                               'Georgiy Dzhikiya', 'Yussuf Poulsen', 'Frenkie de Jong', "Alfred N'Diaye",
                               'Wilson Eduardo', 'Blerim Dzemaili', 'Kevin Lasagna', 'Thilo Kehrer', 'Joaquin Correa',
                               'Felipe Caicedo', 'Aleix Vidal', 'Hernan Perez', 'Wout Weghorst', 'Okay Yokuslu',
                               'Jefferson Montero', 'Nordi Mukiele', 'Lucas Ocampos', "M'Baye Niang", 'Papa Kouli Diop',
                               'Jermain Defoe', 'Frank Fabra', 'Jose Izquierdo', 'Caiuby', 'Giovanni Sio',
                               'Aviles Hurtado', 'Dakonam Djene', 'Yannick Bolasie', 'Djaniny', 'Shoya Nakajima',
                               'Benjamin Moukandjo', 'Vinicius Junior', 'Nicolas Pallois', "M'Baye Niang",
                               'Jozy Altidore', 'Lautaro Acosta', 'Giovani dos Santos', 'Carlos Villanueva',
                               'Diego Buonanotte', 'Sidcley']
                    Rate_83 = ['Shinji Kagawa', 'Juan Mata', 'Gabriel Jesus', 'Mateo Kovacic', 'David Luiz',
                               'Kingsley Coman', 'Corentin Tolisso', 'Nacho Fernandez', 'Jordan Pickford',
                               'Samu Castillejo', 'Bas Dost', 'Danilo Pereira', 'Daniele De Rossi', 'Julian Draxler',
                               'Adan', 'Anthony Martial', 'Aymeric Laporte', 'Malcom', 'Morata', 'Kepa Arrizabalaga',
                               'Leon Goretzka', 'Naby Keita', 'Lucas Vazquez', 'Reina', 'Bruno Fernandes',
                               'Emiliano Viviano', 'Felipe', 'Presnel Kimpembe', 'Adrien Rabiot', 'Thomas Lemar',
                               'Stefan Savic', 'Jonathan Tah', 'Quincy Promes', 'Manu Trigueros', 'Pizzi',
                               'Danijel Subasic', 'Aduriz', 'Quincy Promes', 'Kevin Strootman', 'Steve Mandanda',
                               'Timo Horn', 'Giuliano', 'Lucas Leiva', 'Willian Jose', 'Ever Banega', 'Gerard Moreno',
                               'Kamil Glik', 'Oliver Baumann', 'Memphis Depay', 'Timo Werner', 'Luiz Gustavo',
                               'Mario Balotelli', 'Rui Patricio', 'Yannick Carrasco']
                    Rate_84 = [ 'Ilkay Gundogan',
                               'Sergi Roberto', 'Cesc Fabregas', 'Niklas Sule', 'Moussa Dembele', 'Dele Alli',
                               'Henrikh Mkhitaryan', 'Sokratis', 'Carvajal', 'Raul Albiol', 'Alex Telles',
                               'Angel Di Maria', 'Andrea Barzagli', 'Juan Cuadrado', 'Bernardo Silva','Filho Jorge',
                               #'Kyle Walker', 'Willian',

                               # 'Javi Martinez', 'Heung Min Son', 'Davinson Sanchez',
                               'Alexandre Lacazette', 'Jose Callejon', 'Marquinhos', 'Jose Maria Gimenez',
                               'Stefan de Vrij', 'William Carvalho', 'Rodrigo', 'Florian Thauvin',
                               'Illarramendi', 'Quaresma', 'Dimitri Payet', 'Alejandro Gomez', 'Karim Benzema']

                    not_actual_84 = ['Mattia Perin', 'Mario Mandzukic', 'Wojciech Szczesny',
                                    'Bernd Leno', 'Lopes', 'Stephane Ruffier', 'Kasper Schmeichel','Sergio Asenjo',
                                    'Hradecky','Jonas','William Carvalho', 'Neto'
                                    ]

                    actual_85 = ['Miranda', 'Sami Khedira', 'Yacine Brahimi', 'Edin D', 'Kompany', 'Arturo Vidal',
                                 'Pepe', 'Franck Rib', 'Diego Costa']

                    Price_20K_30K = ['Ivan Rakitic', 'Sergej Milinkovic', 'Thomas Lemar', 'Gianluigi Buffon',
                                    'Geoffrey Kondogbia', 'Marcus Rashford', 'Nemanja Matic', 'Marco Asensio',
                                    'Dele Alli', 'Ederson', 'Medhi Benatia', 'Nabil Fekir', 'Sergio Busquets',
                                    'Joao Cancelo','Felipe Anderson']

                    Price_30K_50K = ['Kalidou Koulibaly', 'ter Stegen', 'Thiago Silva', 'Mats Hummels',
                                     'Samir Handanovic', 'Antonio Valencia', 'Marek Hamsik', 'Kostas Manolas',
                                     'Moussa Dembele', 'Raheem Sterling', 'Marco Asensio',
                                     'Diego Godin', 'Anthony Martial', 'Fred', 'Jan Vertonghen', 'Mauro Icardi',
                                     'Fernandinho', 'Alisson', 'David Silva', 'Willian', 'Ivan Rakitic']



                class Custom(object):
                    custom1 = ['Camacho', 'Bernat', 'Mere', 'Mascarell', 'Pablo Insua']
                    Bonucci = ['Bonucci']
                    Handanovi = ['Handanovi']
                    Thiago = ['Thiago Al']
                    Eriksen = ['Eriksen']
                    Marchisio = ['Marchisio']
                    Godin = ['Godin']
                    Oblak = ['Oblak']
                    Ozil = ['Ozil']
                    Higuain = ['Higuain']
                    Hamsik = ['Hamsik']
                    Robben = ['Robben']
                    Verratti = ['Verratti']
                    yarmolenko = ['yarmolenko']

                class Customr(object):
                    custom2000 = [  # 'Danny Rose',
                        'Keane', 'Delaney', 'Ivanovic', 'Piszc',
                        'Toprak', 'Howedes',
                        # 'Kevin Volland',
                        'Eric Dier', 'Franco Vazquez',  # 'Paulo Henrique'
                        'Leon Bail', 'Lars Bender', 'Vitolo',
                        # 'Gamberini',
                        'Dainelli', 'Ruiz',
                        # 'Guilavo',
                    ]

                    custom1500 = ['Danny Rose', 'Plea',
                                  # 'Lozano',
                                  'Weiser',
                                  'Bigas', 'Lenglet'
                                  ]

    class MyClub(object):
        my_club = Pattern("my_club.png").similar(0.90)
        my_club_selected = Pattern("my_club_selected.png").similar(0.90)
        my_club_inside = Pattern("my_club_inside.png").similar(0.90)
        my_club_inside_selected = Pattern("my_club_inside_selected.png").similar(0.90)
        club_search_logo = Pattern("club_search_logo.png").similar(0.90)
        starter_objectives = Pattern("starter_objectives.png").similar(0.90)
        club_player_stats = Pattern("club_player_stats.png").similar(0.90)

        class ClubSearch(object):
            club_reset = Pattern("club_reset.png").similar(0.90)
            club_reset_selected = Pattern("club_reset_selected.png").similar(0.90)

            club_search_type = Pattern("club_search_type.png").similar(0.90)
            club_search_type_selected = Pattern("club_search_type_selected.png").similar(0.90)

            club_search_type_consumables_selected = Pattern("club_search_type_consumables_selected.png").similar(0.90)
            club_search_Item_Type = Pattern("club_search_Item_Type.png").similar(0.90)
            club_search_Item_Type_contracts_selected = Pattern("club_search_Item_Type_contracts_selected.png").similar(
                0.90)

            list_on_transfer_market = Pattern("list_on_transfer_market.png").similar(0.90)
            list_on_transfer_market_selected = Pattern("list_on_transfer_market_selected.png").similar(0.90)
            list_on_transfer_market_big = Pattern("list_on_transfer_market_big.png").similar(0.90)
            list_on_transfer_market_big_selected = Pattern("list_on_transfer_market_big_selected.png").similar(0.90)

            starting_price = Pattern("starting_price.png").similar(0.80)
            starting_price_selected = Pattern("starting_price_selected.png").similar(0.80)
            club_set_price_form = Pattern("club_set_price_form.png").similar(0.80)

            club_buy_now_price = Pattern("club_buy_now_price.png").similar(0.80)
            club_buy_now_price_selected = Pattern("club_buy_now_price_selected.png").similar(0.80)

            club_sent_to_transfer_message = Pattern("club_sent_to_transfer_message.png").similar(0.90)
            club_sent_to_transfer_message_maximum_reached = Pattern(
                "club_sent_to_transfer_message_maximum_reached.png").similar(0.90)

            class Contarcts(object):
                club_contract_gold_full = Pattern("club_contract_gold_full.png").similar(0.93)
                club_contract_gold_full_1 = Pattern("club_contract_gold_full_1.png").similar(0.93)

                club_contract_gold_half = Pattern("club_contract_gold_half.png").similar(0.93)
                club_contract_gold_half_1 = Pattern("club_contract_gold_half_1.png").similar(0.93)

                club_contract_gold_mega = Pattern("club_contract_gold_mega.png").similar(0.93)


# full_contract=Pattern("full_player_manager.png").exact().targetOffset(-1,-38)
# player_rare=Pattern("player_rare.png").exact()

full_contract_reg = Region(8, 335, 590, 261)
bid_reg = Region(368, 381, 472, 185)
trans_target_reg = Region(559, 445, 267, 47)
con_reg = Region(32, 536, 975, 308)
