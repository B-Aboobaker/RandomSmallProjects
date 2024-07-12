mda = [
    [0, 5.00, 9.00, 16.00, 22.00, 30.00],

    [1, 10.00, 12.00, 18.00, 24.00, 36.00],

    [2, 20.00, 25.00, 32.00, 42.00, 53.00],

    [3, 32.00, 38.00, 45.00, 55.00, 68.00],

    [4, 46.00, 54.00, 65.00, 77.00, 90.00],

    [5, 60.00, 72.00, 84.00, 96.00, 120.00],

    [6, 85.00, 100.00, 120.00, 140.00, 175.00]
    ] 

count = 99

while count != 0:
    numOfWeeksWorked = int(input("Enter the number of weeks worked:\n"))
    if numOfWeeksWorked == 999:
        break

    numOfPositiveReviewsRecieved = int(input("Enter number of positive reviews recieved:\n"))
    if numOfPositiveReviewsRecieved == 999:
        break

    if numOfWeeksWorked > 7:
        numOfWeeksWorked = 6

    if numOfPositiveReviewsRecieved > 5:
        numOfPositiveReviewsRecieved = 4

    output = mda[numOfWeeksWorked][numOfPositiveReviewsRecieved]

    print("Bonus: $", output)
