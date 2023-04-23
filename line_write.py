# Write a method in python to write multiple line of text contents into a text file mylife.txt.

# create header
header = "\033[92mText Line Writer\033[0m"
print(header.center(55, " "))
print("Programmed by: \033[94mTed Paulo A. Feranil\033[0m")
print("=" * 50)
def line_write():
    # open myfile.txt(append)
    with open("myfile.txt", "a") as myfile:    
         # Let user enter line
        enter_line = input("\033[92mEnter line:\033[0m ")
        myfile.write(enter_line + "\n")

# start
line_write()


# Let user choose whether add more text per line or stop
while True:
    choice = input("Are there more lines y/n? ")
    # If y
    if choice == "y":
        # Repeat the process
        line_write()
    # If n
    elif choice == "n":
        print("Text written succcesfully.\U0001F973 \U0001F973")
        # Stop the program
        break
    # If invalid key
    else:
        print("Invalid Key")
        continue
