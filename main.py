from directory.people import get_employees
from directory.salary import calculate_salary
from datetime import datetime

if __name__ == '__main__':
    print(datetime.today())
    get_employees()
    calculate_salary()