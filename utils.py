# utils.py
from datetime import date, timedelta

def convert_mins(time_in_mins):
    """
    Converts time in minutes to H:MM
    
    time_in_mins: int
    return: str
    """
    hours = time_in_mins // 60
    mins_int = time_in_mins % 60
    if mins_int < 10:
        mins_str = "0" + str(mins_int)
    else:
        mins_str = str(mins_int)
        
    return(f"{hours}:{mins_str}")

def cal_due_date():
    """
    Calculates due date as 7 days from today
    
    return: str
    """
    
    today = date.today()    # get today's date
    due_date = today + timedelta(days=7)    # add 7 days
    return due_date.strftime("%Y-%m-%d")
    