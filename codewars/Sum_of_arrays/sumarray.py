def sum_array(numbers):
    if not numbers:
        return 0

    total=0
    for num in numbers:
        total=total+num
    return total