# entrance fee = 2
# first full or partial hour = 3
# successive full or partial hours = 4
# enter at time E, leave at time L (HH:MM)
# assume E is before L and on the same day

import sys
E, L = sys.argv[1], sys.argv[2]

print(E, L)


def get_parking_fee(E, L):
    # my solution
    from math import ceil
    entrance_fee = 2
    first_hour_rate = 3
    successive_rate = 4
    successive_hours = 0
    total_fee = entrance_fee

    entry_hour, entry_minute = E.split(":")
    exit_hour, exit_minute = L.split(":")
    time_in = int(entry_hour)*60 + int(entry_minute)
    time_out = int(exit_hour)*60 + int(exit_minute)
    total_fee = entrance_fee
    if (time_out - time_in > 0):
        total_fee += first_hour_rate  # instructions are vague re. in & out fee?
    if (time_out - time_in >= 60):
        successive_hours = ceil((time_out - time_in)/60 - 1)
        total_fee += successive_hours * successive_rate
    return total_fee


print(get_parking_fee(E, L))


def get_faster_fee(E, L):
    # accepted solution
    entry_hour, entry_minute = E.split(":")
    exit_hour, exit_minute = L.split(":")
    hours = ((int(exit_hour)*60 + int(exit_minute))
             - (int(entry_hour)*60 + int(entry_minute))) / 60
    if int(hours) != hours:
        hours += 1
    return 5 + (max(int(hours-1), 0)) * 4


print(get_faster_fee(E, L))

# Questions:
# What if we need to change the rates structure so that they vary
# throughout the day, e.g. higher during rush hour, or lower on weekends?
# What if we need to change it so that we can bill for multi-days?
# What if we need to change the fee structure?
# What if we start billing on the quarter hour?
# Isn't this a Point of Sale program, placing maintenance and customization
# above performance?
