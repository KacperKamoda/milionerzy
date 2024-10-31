import random

questions = [
    {
        "question": "Ile kontynentów ma świat?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "Który z poniższych to największa planeta w Układzie Słonecznym?",
        "options": ["Ziemia", "Mars", "Jowisz", "Saturn"],
        "answer": "Jowisz"
    },
    {
        "question": "Jakie jest najdłuższe pasmo górskie na świecie?",
        "options": ["Andes", "Himalaje", "Alpy", "Rocky Mountains"],
        "answer": "Andes"
    },
    {
        "question": "Stolicą którego kraju jest Oslo?",
        "options": ["Szwecja", "Dania", "Norwegia", "Finlandia"],
        "answer": "Norwegia"
    },
    {
        "question": "Jaki pierwiastek chemiczny ma symbol O?",
        "options": ["Wodór", "Hel", "Tlen", "Azot"],
        "answer": "Tlen"
    },
    {
        "question": "Ile nóg ma pająk?",
        "options": ["6", "8", "10", "12"],
        "answer": "8"
    },
    {
        "question": "Który kraj ma najwięcej ludności na świecie?",
        "options": ["Indie", "Chiny", "Stany Zjednoczone", "Brazylia"],
        "answer": "Chiny"
    },
    {
        "question": "Kto jest autorem powieści 'Krzyżacy'?",
        "options": ["Adam Mickiewicz", "Bolesław Prus", "Henryk Sienkiewicz", "Juliusz Słowacki"],
        "answer": "Henryk Sienkiewicz"
    },
    {
        "question": "Ile dni ma luty w roku przestępnym?",
        "options": ["28", "29", "30", "31"],
        "answer": "29"
    },
    {
        "question": "Która rzeka jest najdłuższa na świecie?",
        "options": ["Nil", "Amazonka", "Jangcy", "Missisipi"],
        "answer": "Amazonka"
    },
    {
        "question": "Który sport jest nazywany 'królową sportów'?",
        "options": ["Piłka nożna", "Lekkoatletyka", "Tenis", "Koszykówka"],
        "answer": "Lekkoatletyka"
    },
    {
        "question": "Który pierwiastek ma symbol Au?",
        "options": ["Srebro", "Miedź", "Złoto", "Platyna"],
        "answer": "Złoto"
    },
    {
        "question": "W którym roku Polska wstąpiła do Unii Europejskiej?",
        "options": ["2000", "2004", "1998", "2010"],
        "answer": "2004"
    },
    {
        "question": "Który kontynent jest największy pod względem powierzchni?",
        "options": ["Afryka", "Azja", "Europa", "Ameryka Północna"],
        "answer": "Azja"
    },
    {
        "question": "Jakie jest najgłębsze jezioro na świecie?",
        "options": ["Jezioro Wiktorii", "Jezioro Bajkał", "Jezioro Tanganika", "Jezioro Michigan"],
        "answer": "Jezioro Bajkał"
    },
    {
        "question": "Który prezydent USA podpisał Deklarację Niepodległości?",
        "options": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"],
        "answer": "Thomas Jefferson"
    },
    {
        "question": "Jaką walutę używa Japonia?",
        "options": ["Won", "Jen", "Peso", "Dinar"],
        "answer": "Jen"
    },
    {
        "question": "W którym roku wybuchła II wojna światowa?",
        "options": ["1914", "1939", "1941", "1945"],
        "answer": "1939"
    },
    {
        "question": "Który kraj wynalazł makaron?",
        "options": ["Chiny", "Włochy", "Grecja", "Turcja"],
        "answer": "Chiny"
    },
    {
        "question": "Jakie jest największe zwierzę na świecie?",
        "options": ["Słoń afrykański", "Płetwal błękitny", "Rekin wielorybi", "Nosorożec biały"],
        "answer": "Płetwal błękitny"
    },
    {
        "question": "Które miasto jest stolicą Australii?",
        "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
        "answer": "Canberra"
    },
    {
        "question": "Który metal jest najlżejszy?",
        "options": ["Żelazo", "Miedź", "Lit", "Aluminium"],
        "answer": "Lit"
    },
    {
        "question": "W którym kraju znajduje się Machu Picchu?",
        "options": ["Chile", "Brazylia", "Peru", "Argentyna"],
        "answer": "Peru"
    },
    {
        "question": "Która planeta jest najbliżej Słońca?",
        "options": ["Wenus", "Ziemia", "Merkury", "Mars"],
        "answer": "Merkury"
    },
    {
        "question": "Który kraj wygrał najwięcej mistrzostw świata w piłce nożnej?",
        "options": ["Brazylia", "Niemcy", "Argentyna", "Francja"],
        "answer": "Brazylia"
    },
    {
        "question": "Kto jest autorem 'Władcy Pierścieni'?",
        "options": ["George Orwell", "J.K. Rowling", "J.R.R. Tolkien", "C.S. Lewis"],
        "answer": "J.R.R. Tolkien"
    },
    {
        "question": "Jak nazywa się stolica Japonii?",
        "options": ["Kioto", "Osaka", "Tokio", "Nagoya"],
        "answer": "Tokio"
    },
    {
        "question": "Które zwierzę jest symbolem narodowym Australii?",
        "options": ["Koala", "Emu", "Kangur", "Wombat"],
        "answer": "Kangur"
    },
    {
        "question": "Który organ w ludzkim ciele jest odpowiedzialny za produkcję insuliny?",
        "options": ["Wątroba", "Żołądek", "Trzustka", "Jelito cienkie"],
        "answer": "Trzustka"
    },
    {
        "question": "Kto był pierwszym człowiekiem w kosmosie?",
        "options": ["Neil Armstrong", "John Glenn", "Yuri Gagarin", "Buzz Aldrin"],
        "answer": "Yuri Gagarin"
    },
    {
        "question": "Jakie jest oficjalne język Brazylii?",
        "options": ["Hiszpański", "Angielski", "Portugalski", "Francuski"],
        "answer": "Portugalski"
    },
    {
        "question": "Kto napisał powieść '1984'?",
        "options": ["George Orwell", "Aldous Huxley", "Ray Bradbury", "H.G. Wells"],
        "answer": "George Orwell"
    },
    {
        "question": "Który kontynent jest najmniejszy pod względem powierzchni?",
        "options": ["Antarktyda", "Europa", "Australia", "Ameryka Południowa"],
        "answer": "Australia"
    },
    {
        "question": "Który gaz dominuje w ziemskiej atmosferze?",
        "options": ["Tlen", "Wodór", "Dwutlenek węgla", "Azot"],
        "answer": "Azot"
    },
    {
        "question": "Kto jest autorem 'Zbrodni i kary'?",
        "options": ["Fiodor Dostojewski", "Lew Tołstoj", "Aleksander Puszkin", "Anton Czechow"],
        "answer": "Fiodor Dostojewski"
    },
    {
        "question": "Która planeta w Układzie Słonecznym jest najgorętsza?",
        "options": ["Merkury", "Wenus", "Ziemia", "Mars"],
        "answer": "Wenus"
    },
    {
        "question": "Które miasto było gospodarzem Letnich Igrzysk Olimpijskich w 2016 roku?",
        "options": ["Rio de Janeiro", "Londyn", "Pekin", "Ateny"],
        "answer": "Rio de Janeiro"
    },
    {
        "question": "Jaka jest najdłuższa rzeka w Europie?",
        "options": ["Dunaj", "Wołga", "Loara", "Ren"],
        "answer": "Wołga"
    },
    {
        "question": "Które państwo graniczy z największą liczbą innych państw?",
        "options": ["Rosja", "Chiny", "Indie", "Niemcy"],
        "answer": "Chiny"
    },
    {
        "question": "Który instrument jest największym przedstawicielem rodziny dętych drewnianych?",
        "options": ["Flet", "Klarnet", "Obój", "Fagot"],
        "answer": "Fagot"
    },
    {
        "question": "Jak nazywa się najmniejsze państwo na świecie?",
        "options": ["Liechtenstein", "Monako", "San Marino", "Watykan"],
        "answer": "Watykan"
    },
    {
        "question": "Kto namalował 'Mona Lisę'?",
        "options": ["Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", "Salvador Dali"],
        "answer": "Leonardo da Vinci"
    },
    {
        "question": "Który kontynent ma najmniejszą populację?",
        "options": ["Australia", "Antarktyda", "Ameryka Południowa", "Europa"],
        "answer": "Antarktyda"
    },
    {
        "question": "Jak nazywa się największy ocean na świecie?",
        "options": ["Ocean Atlantycki", "Ocean Indyjski", "Ocean Spokojny", "Ocean Arktyczny"],
        "answer": "Ocean Spokojny"
    },
    {
        "question": "Który kontynent jest nazywany 'Czarnym Lądem'?",
        "options": ["Ameryka Północna", "Afryka", "Azja", "Australia"],
        "answer": "Afryka"
    },
    {
        "question": "Jakie zwierzę jest najszybsze na lądzie?",
        "options": ["Tygrys", "Słoń", "Cheetah (Gepard)", "Zebra"],
        "answer": "Cheetah (Gepard)"
    },
    {
        "question": "Która część ciała człowieka jest odpowiedzialna za trawienie?",
        "options": ["Wątroba", "Nerki", "Żołądek", "Serce"],
        "answer": "Żołądek"
    },
    {
        "question": "Jak nazywa się proces, w którym rośliny wytwarzają energię?",
        "options": ["Fotosynteza", "Oddychanie", "Fermentacja", "Sublimacja"],
        "answer": "Fotosynteza"
    },
    {
        "question": "Jakie jest najwyższe wodospad na świecie?",
        "options": ["Wodospad Niagara", "Wodospad Angel", "Wodospad Iguaçu", "Wodospad Yosemite"],
        "answer": "Wodospad Angel"
    },
    {
        "question": "Które z poniższych zwierząt jest ssakiem?",
        "options": ["Krokodyl", "Słoń", "Zebra", "Żaba"],
        "answer": "Słoń"
    },
    {
        "question": "Jakie jest największe miasto w USA pod względem liczby ludności?",
        "options": ["Los Angeles", "Chicago", "Nowy Jork", "Houston"],
        "answer": "Nowy Jork"
    },
    {
        "question": "Które z poniższych państw ma najwyższe góry?",
        "options": ["Indie", "Nepal", "Brazylia", "Kanada"],
        "answer": "Nepal"
    },
    {
        "question": "Jakie jest najstarsze znane pismo na świecie?",
        "options": ["Hieroglify", "Pismo klinowe", "Runy", "Pismo obrazkowe"],
        "answer": "Pismo klinowe"
    },
    {
        "question": "Który z tych naukowców jest znany z teorii względności?",
        "options": ["Isaac Newton", "Albert Einstein", "Niels Bohr", "Stephen Hawking"],
        "answer": "Albert Einstein"
    },
    {
        "question": "Jakie jest stężenie tlenu w atmosferze w procentach?",
        "options": ["20,9%", "21,5%", "18,3%", "22,0%"],
        "answer": "20,9%"
    },
    {
        "question": "Kto był królem Anglii przed Elżbietą II?",
        "options": ["Henryk VIII", "Jerzy VI", "Edward VII", "Karol I"],
        "answer": "Jerzy VI"
    },
    {
        "question": "Jak nazywa się najdłuższa rzeka w Afryce?",
        "options": ["Zambezi", "Nil", "Kongo", "Niger"],
        "answer": "Nil"
    },
    {
        "question": "Jakie jest główne miasto Kanady?",
        "options": ["Toronto", "Montreal", "Ottawa", "Vancouver"],
        "answer": "Ottawa"
    },
    {
        "question": "Który kraj znany jest z produkcji czekolady?",
        "options": ["Szwajcaria", "Francja", "Belgia", "Ghana"],
        "answer": "Szwajcaria"
    },
    {
        "question": "Jak nazywa się największa pustynia na świecie?",
        "options": ["Sahara", "Gobi", "Antarktyda", "Kalahari"],
        "answer": "Antarktyda"
    },
    {
        "question": "Które z poniższych zwierząt jest najstarszym znanym gatunkiem?",
        "options": ["Tyranozaur", "Wieloryb", "Wielbłąd", "Niedźwiedź"],
        "answer": "Wieloryb"
    },
    {
        "question": "Jakie jest główne miasto Hiszpanii?",
        "options": ["Barcelona", "Madryt", "Walencja", "Sewilla"],
        "answer": "Madryt"
    },
    {
        "question": "Jakie zwierzę jest znane jako król dżungli?",
        "options": ["Tygrys", "Lew", "Pantera", "Jaguar"],
        "answer": "Lew"
    },
    {
        "question": "Która z poniższych gier planszowych jest najstarsza?",
        "options": ["Szachy", "Go", "Monopoly", "Scrabble"],
        "answer": "Go"
    },
    {
        "question": "Jakie jest największe jezioro w Afryce?",
        "options": ["Jezioro Wiktorii", "Jezioro Tanganika", "Jezioro Bajkał", "Jezioro Kaspijskie"],
        "answer": "Jezioro Wiktorii"
    },
    {
        "question": "Jak nazywa się najbardziej złożona struktura w ciele człowieka?",
        "options": ["Serce", "Mózg", "Płuca", "Wątroba"],
        "answer": "Mózg"
    },
    {
        "question": "Kto jest autorem teorii ewolucji?",
        "options": ["Isaac Newton", "Charles Darwin", "Galileo Galilei", "Nikola Tesla"],
        "answer": "Charles Darwin"
    },
    {
        "question": "Jakie państwo ma najwięcej wysp?",
        "options": ["Indonezja", "Japonia", "Szwecja", "Filipiny"],
        "answer": "Szwecja"
    },
    {
        "question": "Który pierwiastek jest najcięższy na Ziemi?",
        "options": ["Złoto", "Ołów", "Osm", "Uran"],
        "answer": "Osm"
    },
    {
        "question": "Jaką jednostką mierzy się prąd elektryczny?",
        "options": ["Wat", "Volt", "Amper", "Ohm"],
        "answer": "Amper"
    },
    {
        "question": "Kto namalował 'Gwiaździstą noc'?",
        "options": ["Claude Monet", "Vincent van Gogh", "Paul Cézanne", "Edgar Degas"],
        "answer": "Vincent van Gogh"
    },
    {
        "question": "Który wynalazek przypisuje się Alexanderowi Grahamowi Bellowi?",
        "options": ["Telefon", "Samolot", "Samochód", "Radio"],
        "answer": "Telefon"
    },
    {
        "question": "W którym kraju wynaleziono papier?",
        "options": ["Chiny", "Egipt", "Grecja", "Rzym"],
        "answer": "Chiny"
    },
    {
        "question": "Który z tych oceanów jest najmniejszy?",
        "options": ["Ocean Atlantycki", "Ocean Indyjski", "Ocean Spokojny", "Ocean Arktyczny"],
        "answer": "Ocean Arktyczny"
    },
    {
        "question": "Który gaz jest najbardziej palny?",
        "options": ["Tlen", "Azot", "Wodór", "Dwutlenek węgla"],
        "answer": "Wodór"
    },
    {
        "question": "Która planeta ma największą liczbę księżyców?",
        "options": ["Jowisz", "Saturn", "Ziemia", "Mars"],
        "answer": "Saturn"
    },
    {
        "question": "Który z poniższych instrumentów muzycznych należy do grupy strunowych?",
        "options": ["Fortepian", "Gitara", "Flet", "Trąbka"],
        "answer": "Gitara"
    },
    {
        "question": "Jakie państwo jest największym producentem kawy na świecie?",
        "options": ["Kolumbia", "Brazylia", "Wietnam", "Etiopia"],
        "answer": "Brazylia"
    },
    {
        "question": "Jaki jest najdłuższy tunel na świecie?",
        "options": ["Tunel Laerdal", "Tunel Gotthard", "Tunel Seikan", "Tunel Euro"],
        "answer": "Tunel Gotthard"
    },
    {
        "question": "Która z tych rzek płynie przez Paryż?",
        "options": ["Loara", "Sekwana", "Ren", "Rodan"],
        "answer": "Sekwana"
    },
    {
        "question": "Które z poniższych zwierząt jest ssakiem morskim?",
        "options": ["Delfin", "Rekin", "Meduza", "Krab"],
        "answer": "Delfin"
    },
    {
        "question": "Który kraj jest znany jako ojczyzna olimpijskich igrzysk?",
        "options": ["Stany Zjednoczone", "Wielka Brytania", "Grecja", "Francja"],
        "answer": "Grecja"
    },
    {
        "question": "Jakie państwo ma największą liczbę sąsiadujących krajów?",
        "options": ["Rosja", "Chiny", "Indie", "Brazylia"],
        "answer": "Chiny"
    },
    {
        "question": "Który wynalazek zrewolucjonizował komunikację w XIX wieku?",
        "options": ["Telegraf", "Telefon", "Radio", "Telewizja"],
        "answer": "Telegraf"
    },
    {
        "question": "Jakie państwo ma największą powierzchnię na świecie?",
        "options": ["Kanada", "Rosja", "Stany Zjednoczone", "Chiny"],
        "answer": "Rosja"
    },
    {
        "question": "Które z poniższych miast jest znane jako 'Wielkie Jabłko'?",
        "options": ["Los Angeles", "Londyn", "Nowy Jork", "Chicago"],
        "answer": "Nowy Jork"
    },
    {
        "question": "Które z tych państw ma kształt buta?",
        "options": ["Hiszpania", "Włochy", "Francja", "Grecja"],
        "answer": "Włochy"
    },
    {
        "question": "Jakie miasto jest stolicą Indii?",
        "options": ["Bombaj", "Nowe Delhi", "Kalkuta", "Bangalore"],
        "answer": "Nowe Delhi"
    },
    {
        "question": "Które zwierzę słynie z tego, że zmienia kolor skóry?",
        "options": ["Kameleon", "Żaba", "Wąż", "Iguana"],
        "answer": "Kameleon"
    },
    {
        "question": "Który kraj leży na dwóch kontynentach?",
        "options": ["Rosja", "Kanada", "Chiny", "Australia"],
        "answer": "Rosja"
    },
    {
        "question": "Który pierwiastek chemiczny jest podstawowym składnikiem diamentu?",
        "options": ["Węgiel", "Wodór", "Srebro", "Złoto"],
        "answer": "Węgiel"
    },
    {
        "question": "Jakie państwo jest ojczyzną pizzy?",
        "options": ["Francja", "Hiszpania", "Włochy", "Grecja"],
        "answer": "Włochy"
    },
    {
        "question": "Który stan USA jest największy pod względem powierzchni?",
        "options": ["Kalifornia", "Teksas", "Alaska", "Floryda"],
        "answer": "Alaska"
    },
    {
        "question": "Jakie jest największe państwo w Afryce pod względem powierzchni?",
        "options": ["Nigeria", "Sudan", "Algieria", "Kongo"],
        "answer": "Algieria"
    },
    {
        "question": "Jak nazywa się największa wyspa na świecie?",
        "options": ["Nowa Zelandia", "Grenlandia", "Madagaskar", "Islandia"],
        "answer": "Grenlandia"
    },
    {
        "question": "Które z poniższych miast było stolicą Związku Radzieckiego?",
        "options": ["Leningrad", "Kijów", "Moskwa", "Stalingrad"],
        "answer": "Moskwa"
    },
    {
        "question": "Który ocean leży między Ameryką a Europą?",
        "options": ["Ocean Indyjski", "Ocean Spokojny", "Ocean Arktyczny", "Ocean Atlantycki"],
        "answer": "Ocean Atlantycki"
    },
    {
        "question": "Który kraj jest znany z wynalezienia papieru?",
        "options": ["Egipt", "Grecja", "Chiny", "Indie"],
        "answer": "Chiny"
    },
    {
        "question": "Który kontynent ma najwięcej państw?",
        "options": ["Azja", "Afryka", "Europa", "Ameryka Północna"],
        "answer": "Afryka"
    },
    {
        "question": "Które z tych miast słynie z Wieży Eiffla?",
        "options": ["Rzym", "Berlin", "Londyn", "Paryż"],
        "answer": "Paryż"
    },
    {
        "question": "Jakie jest najmniejsze morze na świecie?",
        "options": ["Morze Karaibskie", "Morze Czarne", "Morze Bałtyckie", "Morze Azowskie"],
        "answer": "Morze Azowskie"
    },
    {
        "question": "Jak nazywa się najstarsze miasto na świecie?",
        "options": ["Jerycho", "Rzym", "Ateny", "Kair"],
        "answer": "Jerycho"
    },
    {
        "question": "Które zwierzę słynie z umiejętności budowy tam?",
        "options": ["Bóbr", "Wydra", "Kuna", "Krab"],
        "answer": "Bóbr"
    },
    {
        "question": "Jakie miasto jest znane jako 'Miasto Świateł'?",
        "options": ["Tokio", "Paryż", "Nowy Jork", "Berlin"],
        "answer": "Paryż"
    },
    {
        "question": "Który z tych krajów ma największą liczbę wysp?",
        "options": ["Norwegia", "Japonia", "Indonezja", "Szwecja"],
        "answer": "Indonezja"
    },
    {
        "question": "Który ptak nie lata, ale potrafi biegać z dużą prędkością?",
        "options": ["Flaming", "Pingwin", "Struś", "Pelikan"],
        "answer": "Struś"
    }
]

prize_values = [1000, 5000, 10000, 50000, 125000, 500000, 1000000]

lifelines = {
    "50/50": True,
    "telefon": True,
    "publiczność": True
}



def ask_question(question_data):
    print(question_data["question"])
    for idx, option in enumerate(question_data["options"], 1):
        print(f"{idx}. {option}")
    return question_data


def get_user_answer():
    try:
        user_input = int(input("Wybierz numer odpowiedzi (1-4): "))
        if 1 <= user_input <= 4:
            return user_input
        else:
            print("Niepoprawny wybór, spróbuj ponownie.")
            return get_user_answer()
    except ValueError:
        print("Musisz wybrać liczbę!")
        return get_user_answer()


def use_lifeline(question, correct_option):
    available_lifelines = [lifeline for lifeline, available in lifelines.items() if available]

    if not available_lifelines:
        print("Brak dostępnych kół ratunkowych.")
        return

    print("\nDostępne koła ratunkowe:")
    for idx, lifeline in enumerate(available_lifelines, 1):
        print(f"{idx}. {lifeline.capitalize()}")

    lifeline_choice = input(
        f"Wybierz koło ratunkowe (1-{len(available_lifelines)}) lub wpisz Enter, aby kontynuować bez koła: ").lower()
    if not lifeline_choice:
        return

    if lifeline_choice.isdigit():
        lifeline_idx = int(lifeline_choice) - 1
        if 0 <= lifeline_idx < len(available_lifelines):
            lifeline = available_lifelines[lifeline_idx].lower()
        else:
            print("Niepoprawny wybór.")
            return use_lifeline(question, correct_option)
    elif lifeline_choice == "nie":
        return
    else:
        print("Niepoprawny wybór.")
        return use_lifeline(question, correct_option)

    if lifeline == "50/50" and lifelines["50/50"]:
        wrong_options = [i for i, option in enumerate(question["options"], 1) if i != correct_option]
        to_remove = random.sample(wrong_options, 2)
        print("Opcje po użyciu 50/50:")
        for i in range(1, 5):
            if i == correct_option or i not in to_remove:
                print(f"{i}. {question['options'][i - 1]}")
        lifelines["50/50"] = False

    elif lifeline == "telefon" and lifelines["telefon"]:

        hint_chance = random.randint(1, 100)
        if hint_chance <= 70:
            print("Telefon do przyjaciela: 'Myślę, że poprawna odpowiedź to',", question["options"][correct_option - 1])
        else:
            print("Telefon do przyjaciela: 'Nie jestem pewien, ale może',", random.choice(question["options"]))
        lifelines["telefon"] = False

    elif lifeline == "publiczność" and lifelines["publiczność"]:
        public_vote = [0, 0, 0, 0]
        public_vote[correct_option - 1] = random.randint(40, 60)
        remaining_percentage = 100 - public_vote[correct_option - 1]
        for i in range(4):
            if i != correct_option - 1:
                public_vote[i] = random.randint(0, remaining_percentage)
                remaining_percentage -= public_vote[i]
        print("Publiczność głosuje:")
        for idx, vote in enumerate(public_vote, 1):
            print(f"{idx}. {question['options'][idx - 1]} - {vote}% głosów")
        lifelines["publiczność"] = False

    else:
        print("Wybrane koło ratunkowe nie jest dostępne.")


def game():
    random.shuffle(questions)
    prize = 0
    total_questions = len(prize_values)

    for i, question in enumerate(questions[:total_questions], 1):
        print(f"\nPytanie {i} za {prize_values[i - 1]} zł:")
        print(f"Pozostało pytań: {total_questions - i}")
        current_question = ask_question(question)
        correct_answer = current_question["answer"]
        correct_option = current_question["options"].index(correct_answer) + 1

        # Użycie koła ratunkowego przed odpowiedzią
        use_lifeline(current_question, correct_option)

        # Odpowiedź użytkownika
        user_choice = get_user_answer()

        if user_choice == correct_option:
            prize = prize_values[i - 1]
            print("Poprawna odpowiedź!\n")
        else:
            print(f"Niestety, błędna odpowiedź. Prawidłowa odpowiedź to: {correct_answer}.")
            break

    print(f"\nKoniec gry! Wygrałeś: {prize} zł.")
    return prize


def main():
    print(
        '''
            ███╗   ███╗██╗██╗     ██╗ ██████╗ ███╗   ██╗███████╗██████╗ ███████╗██╗   ██╗
            ████╗ ████║██║██║     ██║██╔═══██╗████╗  ██║██╔════╝██╔══██╗╚══███╔╝╚██╗ ██╔╝
            ██╔████╔██║██║██║     ██║██║   ██║██╔██╗ ██║█████╗  ██████╔╝  ███╔╝  ╚████╔╝ 
            ██║╚██╔╝██║██║██║     ██║██║   ██║██║╚██╗██║██╔══╝  ██╔══██╗ ███╔╝    ╚██╔╝  
            ██║ ╚═╝ ██║██║███████╗██║╚██████╔╝██║ ╚████║███████╗██║  ██║███████╗   ██║   
            ╚═╝     ╚═╝╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝    
                                                                             
        '''
    )
    print("Witaj w grze 'Milionerzy'! Czy jesteś gotowy, aby wygrać milion?")
    print("Masz do dyspozycji 3 koła ratunkowe: 50/50, telefon do przyjaciela oraz pytanie do publiczności.")
    print("Zaczynamy!\n")

    while True:
        global lifelines
        lifelines = {
            "50/50": True,
            "telefon": True,
            "publiczność": True
        }
        game()
        restart = int(input("Czy chcesz zagrać jeszcze raz? (Tak(1)/Nie(2)): "))
        if restart != 1:
            print("Dziękujemy za grę!")
            break


if __name__ == "__main__":
    main()