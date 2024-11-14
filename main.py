from datetime import datetime

def calculate_fine(book_id, due_date, return_date):
    """Calculates the fine for an overdue library book.

    Args:
        book_id (str): The ID of the book.
        due_date (str): The due date of the book in the format "YYYY-MM-DD".
        return_date (str): The return date of the book in the format "YYYY-MM-DD".

    Returns:
        None
    """

    due_date = datetime.strptime(due_date, "%Y-%m-%d")
    return_date = datetime.strptime(return_date, "%Y-%m-%d")

    days_overdue = (return_date - due_date).days

    if days_overdue <= 7:
        fine_rate = 20
    elif days_overdue <= 14:
        fine_rate = 50
    else:
        fine_rate = 100

    fine_amount = days_overdue * fine_rate

    print("Book ID:", book_id)
    print("Due Date:", due_date.strftime("%Y-%m-%d"))
    print("Return Date:", return_date.strftime("%Y-%m-%d"))
    print("Days Overdue:", days_overdue)
    print("Fine Rate (Ksh/day):", fine_rate)
    print("Fine Amount (Ksh):", fine_amount)

book_id = input("Enter Book ID: ")
due_date = input("Enter Due Date (YYYY-MM-DD): ")
return_date = input("Enter Return Date (YYYY-MM-DD): ")

calculate_fine(book_id, due_date, return_date)
