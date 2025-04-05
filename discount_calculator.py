
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if the discount is 20% or higher.
    Returns the discounted price or the original price otherwise.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

def main():
    try:
        # Prompt user for input
        price = float(input("Enter the original price: "))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Calculate final price
        final_price = calculate_discount(price, discount_percent)

        # Output result
        if discount_percent >= 20:
            print(f"Discount applied! Final price: ${final_price:.2f}")
        else:
            print(f"No discount applied. Final price: ${final_price:.2f}")

    except ValueError:
        print("Please enter valid numeric values for price and discount.")

# Run the main function
main()
