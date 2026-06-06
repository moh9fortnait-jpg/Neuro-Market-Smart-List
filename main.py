# Project 13: Neuro-Market Smart List
# Real-time expense tracker for traditional markets

def main():
    print("--- Neuro-Market Smart List v1.0 ---")
    budget = float(input("Enter your market budget: "))
    total_spent = 0
    
    while True:
        item = input("\nItem name (or 'finish'): ")
        if item.lower() == 'finish': break
        price = float(input(f"Price for {item}: "))
        
        if total_spent + price > budget:
            print(f"Warning: This exceeds your budget by { (total_spent + price) - budget }!")
        else:
            total_spent += price
            print(f"Added. Remaining: {budget - total_spent}")

    print(f"\nFinal Summary: Spent {total_spent} out of {budget}.")