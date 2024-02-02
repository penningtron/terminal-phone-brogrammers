from googlesearch import search
from webbrowser import open

search_history = []

# Helper function to get user input and append to search history
def user_query():
    user_query_input = input("What would you like to search? ")
    search_history.append(user_query_input)
    return user_query_input

# Function to open a web browser
def open_browser():
    open(url = "https://www.google.com", new = 2)
    
    
# Search function
def google_search():
    query = user_query()
    resultList = list(search(query, num = 5, stop = 5))
    for elem in resultList:
        print(elem)
    choice = input("Would you like to make another query (Y/N)? ")
    if choice == "Y":
        google_search()
    elif choice == "N":
        history_choice = input("Would you like to see your search history (Y/N)? ")
        if history_choice == "Y":
            for elem2 in search_history:
                print(elem2)
        elif history_choice == "N":
            print("Thank you for searching.")
        else:
            raise ValueError("Not a valid choice.")
    else:
        raise ValueError("Not a valid choice.")
    

# def google_search2():
#     user_choice = input("Would you like to search something (Y/N)? ")
#     if user_choice != "Y" and user_choice != "N":
#         raise ValueError("Not a valid choice.")
#     elif user_choice == "Y":
#         while user_choice == "Y":
#             query = user_query
#             resultList = list(search(query, num = 5, stop = 5))
#             for elem in resultList:
#                 print(elem)

# google_search()
# open_browser()