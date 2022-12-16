
def sort_arr(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def my_func(a, b):
    count = 1
    result = 1 / a
    while count < abs(b):
        result *= 1 / a
        count += 1
    return result


def calc_time(a):
    hours = a // 3600
    minutes = a // 60 % 60
    seconds = a % 60

    if hours < 10:
        hours = "0" + str(hours)
    if minutes < 10:
        minutes = "0" + str(minutes)
    if seconds < 10:
        seconds = "0" + str(seconds)
    return f"Время на часах: {hours}:{minutes}:{seconds}"


