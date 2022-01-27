"""6 question 5 sprint"""
import calendar


def day_of_week(day):
    try:
        int_day = int(day)
        if int_day in range(1, 8):
            return calendar.day_name[int_day-1]
        else:
            return "There is no such day of the week! Please try again."
    except ValueError:
        return "You did not enter a number! Please try again."


if __name__ == '__main__':
    print(day_of_week(2))  # output:   "Tuesday"
    print(day_of_week(11))  # output:  "There is no such day of the week! Please try again."
    print(day_of_week("Monday"))  # output:   "You did not enter a number! Please try again."

