from math import e


def main() -> None:
    print('This program calculates the monthly payments of a fixed-term mortgage using a certain interest rate!')
    while True:
        user_input = input('Enter a fixed-term mortgage: ')

        while user_input[0] != '$':
            user_input = input('Enter a fixed-term mortgage: ')

        fixed_term_mortgage = float(user_input[1:])

        user_input = input('Enter an interest rate: ')

        while user_input[-1] != '%':
            user_input = input('Enter an interest rate: ')

        interest_rate = float(user_input[:-1])/100

        user_input = input('Enter the number of terms: ')

        while not user_input.isnumeric():
            user_input = input('Enter the number of terms: ')

        n = int(user_input)

        compounding_intervals = ['Monthly', 'Weekly', 'Daily', 'Continuously']

        output = f"""
        Select one of these compounding intervals:
        {compounding_intervals[0]}
        {compounding_intervals[1]}
        {compounding_intervals[2]}
        {compounding_intervals[3]}
        """

        print(output)

        compounding_interval = input('Enter a compounding interval: ')

        effective_interest_rate = interest_rate
        while compounding_interval.capitalize() not in compounding_intervals:
            compounding_interval = input('Enter a compounding interval: ')

        if compounding_interval == compounding_intervals[1]:
            effective_interest_rate = ((1 + interest_rate / 4) ** 4) - 1

        elif compounding_interval == compounding_intervals[2]:
            effective_interest_rate = ((1 + interest_rate / 30) ** 30) - 1

        elif compounding_interval == compounding_intervals[3]:
            effective_interest_rate = (e ** interest_rate) - 1

        # print(effective_interest_rate)

        monthly_payment = ((effective_interest_rate * (1 + effective_interest_rate)
                           ** n)/((1 + effective_interest_rate)**n - 1)) * fixed_term_mortgage

        output = f"""
        The monthly payment for a fixed-term mortgage of ${fixed_term_mortgage:.2f} with an interest rate of {interest_rate*100:.2f}%
        and a {compounding_interval.lower()} compounding period is approximately ${monthly_payment:.2f}.
        """

        print(output)


if __name__ == '__main__':
    main()
