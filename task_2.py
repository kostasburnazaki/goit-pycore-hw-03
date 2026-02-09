import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """
    Generates list or unique numbers for the lottery
        
    :param min: lower limit for the values 
    :param max: top limit for the values
    :param quantity: quantity of numbers in the list
    :return: Sorted list of unique numbers or empty list in case parameters are wrong
    """

    # Checking corectness of input data
    if (
        min < 1 or
        max > 1000 or
        min > max or 
        quantity < 1 or
        quantity > (max - min + 1)
    ):
        return []
    
    # Generation of random numbers
    numbers = random.sample(range(min, max + 1), quantity)

    # Sorting the result
    return sorted(numbers)


def main():
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)


if __name__ == "__main__":
    main()