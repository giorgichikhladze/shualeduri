# 1.
import random
books = [
    {"სათაური": "Pride and Prejudice", "ავტორი": "Jane Austen", "წელი": 1813},
    {"სათაური": "The Great Gatsby", "ავტორი": "F. Scott Fitzgerald", "წელი": 1925},
    {"სათაური": "The Picture of Dorian Gray", "ავტორი": "Oscar Wilde","წელი": 1890},
    {"სათაური": "The Lord of the Rings ", "ავტორი": "J.R.R. Tolkien","წელი": 1954},
    {"სათაური": "Crime and Punishment ","ავტორი": "Fyodor Dostoevsky","წელი": 1866},
    {"სათაური": "The Old Man and the Sea", "ავტორი": "Ernest Hemingway","წელი": 1952},
    {"სათაური": "1984", "ავტორი": "George Orwell","წელი": 1949},
    {"სათაური": "The book of five rings","ავტორი": "Miyamoto Musashi","წელი": 1645 },
    {"სათაური": "The Stranger","ავტორი": "Albert Camus","წელი": 1942},
    {"სათაური": "Metamorphosis","ავტორი": "Franz Kafka","წელი": 1915},
]

while True:
    print("მოგესალმებით ბიბლიოთეკაში, გთხოვთ აირჩიოთ ქმედება.")
    print(f"ამ ეტაპზე ბიბლიოთეკაში არის {len(books)} წიგნი.")
    print("1. ყველა წიგნის ნახვა")
    print("2. წიგნის დამატება")
    print("3. წიგნის გატანა")
    print("4. გასვლა")

    inp = input("ჩაწერეთ ციფრი და აირჩიეთ სასურველი ქმედება: ")

    if inp == "1":
        for i, book in enumerate(books, 1):
            print(f"{i}. {book['სათაური']} - {book['ავტორი']} ({book['წელი']})")
        print("-" * 30)

    elif inp == "2":
        print("-" * 30)
        title = input("შეიყვანეთ წიგნის სახელი: ")
        author = input("შეიყვანეთ ავტორის სახელი: ")

        while True:
            year = input("შეიყვანეთ წელი: ")

            if year.isdigit():
                break
            else:
                print("გთხოვთ შეიყვანეთ მხოლოდ რიცხვები!")

        book_added = {
            "სათაური": title,
            "ავტორი": author,
            "წელი": int(year),
        }
        books.append(book_added)
        print("-" * 30)
        print(f"წიგნი {title} დაემატა ბიბლიოთეკაში.")
        print(f"ბიბლიოთეკაში ახლა {len(books)} წიგნია")
        print("-" * 30)

    elif inp == "3":
        remove = input("რომელი წიგნის გატანა გსურთ? ჩაწერეთ მხოლოდ სათაური: ").strip().lower()
        for book in books:
            if book["სათაური"].strip().lower() == remove:
                books.remove(book)
                print(f"წიგნი {remove} გატანილია")
                print(f"ბიბლიოთეკაში ახლა {len(books)} წიგნია")

    elif inp == "4":
        print("თქვენ გახვედით ბიბლიოთეკიდან.")
        break
    else:
        print("შეიყვანეთ ციფრი 1-4მდე!")

# 2.

icons = ["ჯვარი", "ყვავი", "აგური", "გული"]
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

deck = []

for icon in icons:
    for number in numbers:
        deck.append([number, icon])

random.shuffle(deck)


card_value = {
    2: 2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J": 10, "Q": 10, "K": 10, "A": 11
}

def calculate(hand):
    total = 0
    for card in hand:
        value = card[0]
        total += card_value[value]
    return total

player_hand = []
computer_hand = []

for i in range(2):
    player_hand.append(deck.pop())
    computer_hand.append(deck.pop())

def remove(hand):
    text = ""
    for card in hand:
        text += str(card[0]) + "-" + card[1] + "  "
    return text

print(f"თქვენი კარტი: {remove(player_hand)}")
print(f"კომპიუტერის კარტი: {remove(computer_hand)}")


current_score = calculate(player_hand)
computer_score = calculate(computer_hand)

player_lose = False

while current_score < 21:
    inp1 = input(f"თქვენ გაქვთ {current_score} ქულა, გსურთ კარტის დამატება? ")
    if inp1.lower() == "yes":
        print("-" * 30)
        player_hand.append(deck.pop())
        current_score = calculate(player_hand)
        print(f"თქვენი კარტი ახლა არის {remove(player_hand)}")
        print(f"ქულების ჯამი არის: {current_score}")

        if current_score > 21:
            print("თქვენ წააგეთ :(")
            player_lose = True
            break
        elif inp1.lower() == "no":
            break

    if not player_lose:
        print("-" * 30)
        print("კომპიუტერის ჯერია.")
        computer_hand.append(deck.pop())
        while computer_score < 17:
            print("კომპიუტერი იღებს კარტს.")
            computer_hand.append(deck.pop())
            computer_score = calculate(computer_hand)
        print(f"კომპიუტერის კარტები: {remove(computer_hand)}")
        print(f"კომპიუტერის საბოლოო ქულა: {computer_score}")

        if computer_score > 21:
            print("კომპიუტერმა წააგო თამაში.")
            break
        elif current_score > computer_score:
            print("თქვენ მოიგეთ.")
            break
        elif computer_score > current_score:
            print("თქვენ წააგეთ.")
            break
        else:
            print("თამაში ფრედ დასრულდა")
            break


# 3.
import datetime
balance = 5000

while True:
    inp1 = input("აირჩიეთ ქმედება: გასვლა, ბალანსის ნახვა, გატანა, შემოტანა: ")

    if inp1 == "გასვლა":
        break

    elif inp1 == "ბალანსის ნახვა":
        print(f"თქვენი ბალანსი შეადგენს {balance} ლარს.")

    elif inp1 == "გატანა":
        money = int(input("ჩაწერეთ თანხის ოდენობა: "))
        if money > balance:
            print("თქვენს ანგარიშზე არასაკმარისი თანხაა!")
        else:
            balance -= money
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(f"{datetime.datetime.now()}: გატანა - {money} ლარი, ბალანსი - {balance}\n")
                print(f"თქვენ გაიტანეთ {money} ლარი.")

    elif inp1 == "შემოტანა":
        money = int(input("ჩაწერეთ თანხის ოდენობა: "))
        if money > 1000:
            print("1000 ლარზე მეტს ვერ შეიტანთ.")
        else:
            balance += money
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(f"{datetime.datetime.now()}: შემოტანა - {money} ლარი\n, ბალანსი - {balance}")

                print(f"თქვენ შეიტანეთ {money} ლარი.")




# 4.

def lottery():
    jackpot = 1500000
    wnumbers = set(random.sample(range(1, 50), 6))

    print(f"ჯეკპოტი შეადგენს {jackpot} ლარს.")

    inp1 = input("შეიყვანეთ სასურველი რიცხვები. მაგ: 3 19 21 30 34 48: ")
    user_input = set(map(int, inp1.split()))
    result = len(wnumbers.intersection(user_input))
    won_amount = 0
    if result == 6:
        won_amount = jackpot
    elif result == 5:
        won_amount = jackpot * 0.6
    elif result == 4:
        won_amount = jackpot * 0.4
    else:
        won_amount = 0

    match = len(wnumbers.intersection(inp1))

    print(f"თქვენს მიერ არჩეული რიცხვები არის: {inp1}")
    print(f"მომგებიანი რიცხვები არის: {sorted(list(wnumbers))}")
    print(f"დაემთხვა: {match}")
    print(f"თქვენი მოგება: {won_amount:,.2f} GEL")

lottery()


# 5.

mail = "user@mail.com"
password = "password123"
nickname = "george777"

print("გაითვალისწინეთ რომ უნდა შეიყვანოთ მხოლოდ Lowercase ლათინური ასოები, რიცხვების და სიმბოლოების გარეშე.")

while True:
    inp1 = input("გთხოვთ შეიყვანეთ თქვენი სახელი: ")

    if inp1.isdigit():
        print("თქვენ შეიყვანეთ რიცხვები! შეიყვანეთ მხოლოდ ასოები")

    elif not inp1:
        print("ველი ცარიელია")

    elif not inp1.isascii():
        print("შემოიყვანეთ მხოლოდ ლათინური ასოები!")

    elif not inp1.isalnum():
        print("შემოიყვანეთ მხოლოდ ასოები და არა სიმბოლოები!!!")

    elif not inp1.islower():
        print("შემოიყვანეთ მხოლოდ პატარა ასოები!")

    else:
        print(f"თქვენი სახელი არის {inp1}")
        print(f"თქვენი მეილი არის {mail}")
        print(f"თქვენი პაროლი არის {password}")
        print(f"თქვენი ზედმეტსახელი არის {nickname}")
        break
