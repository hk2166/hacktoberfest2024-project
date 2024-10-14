def calculate_bill(units):
    """
    Calculate the electricity bill based on the number of units consumed.

    Args:
        units (int): The number of units consumed.

    Returns:
        float: The total electricity bill.
    """
    if units < 0:
        raise ValueError("Units consumed cannot be negative")

    if units <= 100:
        return units * 10
    elif units <= 200:
        return (100 * 10) + ((units - 100) * 15)
    elif units <= 300:
        return (100 * 10) + (100 * 15) + ((units - 200) * 20)
    else:  # units > 300
        return (100 * 10) + (100 * 15) + (100 * 20) + ((units - 300) * 25)

# Driver Code
if __name__ == "__main__":
    try:
        units = int(input("Enter the number of units consumed: "))
        bill_amount = calculate_bill(units)
        print(f"The total electricity bill is: {bill_amount:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
