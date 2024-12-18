from functions import (
    register_user,
    authenticate_user,
    get_closing_prices,
    analyze_closing_prices,
    save_to_csv,
    read_from_csv
)

def main():
    print("Welcome to the Stock Selection Tool!")
    while True:
        choice = input("1. Register\n2. Login\nChoose an option: ")
        if choice == '1':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            print(register_user(email, password))
        elif choice == '2':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if authenticate_user(email, password):
                print("Login successful!\n")
                break
            else:
                print("Invalid credentials. Try again.")
    

    while True:
        ticker = input("Enter stock ticker (e.g., 1155.KL): ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        data = get_closing_prices(ticker, start_date, end_date)
        if isinstance(data, str):
            print(data)
        else:
            print(data)
            results = analyze_closing_prices(data)
            print("Analysis Results:")
            for key, value in results.items():
                print(f"{key}: {value}")
            
            save_choice = input("Save results? (yes/no): ").lower()
            if save_choice == 'yes':
                email = input("Enter your email for tracking: ")
                save_to_csv(
                    [{"Email": email, "Ticker": ticker, **results}],
                    "user_data.csv"
                )
            
            another = input("Analyze another stock? (yes/no): ").lower()
            if another != 'yes':
                break
    
    read_choice = input("Do you want to view saved data? (yes/no): ").lower()
    if read_choice == 'yes':
        data = read_from_csv("user_data.csv")
        print(data)

if __name__ == "__main__":
    main()

