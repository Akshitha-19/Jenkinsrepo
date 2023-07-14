start = 10  # Change this value to set the starting point of the range
end = 100  # Change this value to set the ending point of the range

for num in range(start, end+1):
    # Convert the number to a string and check if it is equal to its reverse
    if str(num) == str(num)[::-1]:
        print(num)

