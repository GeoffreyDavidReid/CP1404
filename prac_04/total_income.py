"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def print_report(month, months_int, incomes):
    total = 0
    print()
    print("Income Report")
    print("-------------")
    for month in range(1, months_int + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months_int = int(input("How many months? "))

    for month in range(1, months_int + 1):
        income = float(input('{} {} {}'.format("Enter income for month ", str(month), ": ")))
        incomes.append(income)
    print_report(month, months_int, incomes)

main()
