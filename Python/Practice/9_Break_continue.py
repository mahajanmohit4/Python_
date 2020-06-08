while(1):
    i = int(input("Please enter a number\n"))
    if (i < 100):
        print("TRY AGAIN!!!")
        continue
    else:
        print("Congratulations! you have entered a number greater than 100")
        break