def main():
    cost_per_item = 19.99
    quantity = 5 
    subtotal_cost = cost_per_item*quantity
    tax = subtotal_cost * 0.13
    total_cost = tac=x + subtotal_cost

    # YOUR CODE TO CALCULATE THE TOTALS GOES HERE    
    cost_per_item = 19.99
    quantity = 5 
    subtotal_cost = (cost_per_item*quantity).__round__(2)
    tax = (subtotal_cost * 0.13).__round__(2)
    total_cost = (tax + subtotal_cost).__round__(2)

    
   # YOUR CODE TO PRINT THE TOTALS GOES HERE 
    print(f"cost_per_item = ${cost_per_item:0.2f}")
    print(f"quantity = {quantity}")
    print(f"subtotal_cost = ${subtotal_cost:0.2f}")
    print(f"tax = ${tax:0.2f}")
    print(f"total_cost = ${total_cost:0.2f}")
    print(f'cost_per_item = ${cost_per_item:0.2f}') # a sample for you to use for the other prices

if __name__ == "__main__":
    main()
