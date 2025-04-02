# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If the discount is 20% or higher,3 apply the discount.
    Otherwise, return the original price.

    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to apply.

    Returns:
    float: The final price after applying the discount or the original price.
    """
    # Check if the discount percentage is 20% or higher
    if discount_percent >= 20:
        # Calculate the discounted price
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        # Return the original price if discount is less than 20%
        return price

# Prompt the user to enter the original price
try:
    original_price = float(input("Enter the original price of the item: "))
    # Prompt the user to enter the discount percentage
    discount_percentage = float(input("Enter the discount percentage: "))

    # Call the calculate_discount function to get the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the final price or the original price based on the discount
    if discount_percentage >= 20:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")