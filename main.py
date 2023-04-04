import random
MAX_VALUE = 100
MIN_VALUE = 1
ROWS = 3
COLUMNS = 3

symbols_count = {
    "A":2,
    "B":4,
    "C":5,
    "E":3,
    "F":2
}

symbols_values = {
    "A":2,
    "B":4,
    "C":5,
    "E":3,
    "F":2
}
def check_winnings(columns,bet_lines,bet,balance):
    first_column = []
    second_column = []
    third_columns = []
    for element in columns:
        if len(first_column) < 3:
            first_column.append(element)
        elif len(second_column) < 3:
            second_column.append(element)
        elif len(third_columns) < 3:
            third_columns.append(element)
    check_duplicates_first = set(first_column) # we make sets because if there's three characters same it will return only one but remove the two duplicates
    check_duplicates_second = set(second_column)
    check_duplicates_third = set(third_columns)

    if len(check_duplicates_first) == 1:
        print("Winning line is --> line one --<")
        balance += bet_lines * bet
        print(f"You got it this time ,now you have {balance}$")
        playagain(balance)
    elif len(check_duplicates_second) == 1:
        print("Winning line is --> line two <--")
        balance += bet_lines * bet
        print(f"You got it this time ,now you have {balance}$")
        playagain(balance)
    elif len(check_duplicates_third) == 1:
        print("Winning line is --> line three --<")
        balance += bet_lines * bet
        print(f"You got it this time ,now you have {balance}$")
        playagain(balance)
    elif len(check_duplicates_first) > 1 or len(check_duplicates_second) > 1 or len(check_duplicates_third):
        get_sum = bet_lines * bet
        balance = balance - get_sum
        print(f"You didn't get it try again ,now you have {balance}$")
        playagain(balance)




def spin_slot_machine(symbols):
    all_symbols = []
    columns = []
    length_of_spin = 9
    for symbol,symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)
    for i in range(length_of_spin):
        get_random = random.choice(all_symbols)
        columns.append(get_random)
    return columns
def print_slot_machine(columns):
    first_row = ' | '.join(columns[0:3])
    second_row = ' | '.join(columns[3:6])
    third_row = ' | '.join(columns[6:9])
    print(first_row)
    print(second_row)
    print(third_row)






def deposit():
    while True:
        deposit_money = input("How much money would you like to deposit?: $")
        if deposit_money.isdigit():
            deposit_money = int(deposit_money)
            if deposit_money > 0:
                break
            else:
                print("You should deposit more than 0$")
        print("Enter a digit")
    return deposit_money
def bet_on_lines():
    while True:
        lines = input("On how many lines would you like to bet(1-3)?: ")
        if lines.isdigit():
            lines = int(lines)
            if lines >= 1 and lines <= 3:
                break
            else:
                print("Number of lines should be between 1-3")
        print("Enter a number of lines")
    return lines


def get_bet():
    while True:
        bet = input("How much money would you like to bet on one line(1$-100$): ")
        if bet.isdigit():
            bet = int(bet)
            if bet <= MAX_VALUE and bet >= MIN_VALUE:
                break
            else:
                print("Money should be between 1-100$")
        else:
            print("Enter a digit")
    return bet


def spin():
    balance = deposit()
    lines_number = bet_on_lines()
    while True:
        bet_money = get_bet()
        total_bet = bet_money * lines_number
        if total_bet > balance:
            print(f"Your balance is {balance}$.Balance shoudn't be less than betting money , bet less!")
        else:
            break
    print(f"You are betting {total_bet}$ on {lines_number} lines.")
    slot_machine = spin_slot_machine(symbols_count)
    print_slot_machine(slot_machine)
    check_winnings(slot_machine,lines_number,bet_money,balance)
def playagain(balance):
    while True:
        answer = input("Do you want to play again(Press Enter or q to quit): ")
        if answer != "" or balance == 0:
            print(f"You left with {balance}$, Good Bye!")
            break
        else:
            if int(balance) > 0:
                lines_number = bet_on_lines()
                bet_money = get_bet()
                slot_machine = spin_slot_machine(symbols_count)
                print_slot_machine(slot_machine)
                check_winnings(slot_machine,lines_number,bet_money,balance)
                break





spin()