from math import e
from sys import exit
from unicodedata import category


def main() -> None:
    print('💸 Welcome to The Mortgage Calculator! 💸')
    exit_message: str = 'Exiting program...'
    while True:
        try:
            user_input: str = input('Enter a fixed-term mortgage: ')
            if user_input == 'exit':
                print(exit_message)
                exit()

            currency_symbols: list[str] = [
                ch for ch in user_input if category(ch) == 'Sc']

            if user_input[0] not in currency_symbols:
                print('Please enter a valid mortgage...')
                continue

            fixed_term_mortgage: float = float(user_input[1:])

            user_input = input('Enter an interest rate: ')

            if user_input[-1] == '%':
                interest_rate: float = float(user_input[:-1])/100
            else:
                interest_rate: float = float(user_input)

            user_input = input('Enter the number of terms: ')

            n: int = int(user_input)

            compounding_intervals: list[str] = [
                'Monthly', 'Weekly', 'Daily', 'Continuously']

            prompt: str = f"""
Select one of these compounding intervals:
{compounding_intervals[0]}
{compounding_intervals[1]}
{compounding_intervals[2]}
{compounding_intervals[3]}"""

            print(prompt)

            compounding_interval: str = input(
                'Enter a compounding interval: ').capitalize()

            if compounding_interval not in compounding_intervals:
                print('Please enter a valid compounding interval...')
                continue

        except ValueError:
            print('Please enter valid input...')
            continue

        except KeyboardInterrupt:
            print(exit_message)
            exit()

        if compounding_interval == compounding_intervals[1]:
            effective_interest_rate: float = ((1 + interest_rate / 4) ** 4) - 1
        elif compounding_interval == compounding_intervals[2]:
            effective_interest_rate: float = (
                (1 + interest_rate / 30) ** 30) - 1
        elif compounding_interval == compounding_intervals[3]:
            effective_interest_rate: float = (e ** interest_rate) - 1
        else:
            effective_interest_rate: float = interest_rate

        monthly_payment: float = ((effective_interest_rate * (1 + effective_interest_rate) ** n)/(
            (1 + effective_interest_rate)**n - 1)) * fixed_term_mortgage

        output: str = f"""
The monthly payment for a fixed-term mortgage of ${fixed_term_mortgage:,.2f} with an interest rate of {interest_rate:.2%}
and a {compounding_interval.lower()} compounding period is approximately ${monthly_payment:,.2f}."""

        print(output)


if __name__ == '__main__':
    main()
