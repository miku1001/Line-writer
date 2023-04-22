# Write a method in python to write multiple line of text contents into a text file mylife.txt.

def line_write():
# open myfile.txt(append)
    with open("myfile.txt", "a") as myfile:
        while True:    
            # Let user enter line
            enter_line = input("Enter line: ")
            myfile.write(enter_line + "\n")
            # Let user choose whether add more text per line or stop
            choice = input("Are there more lines y/n? ")
            # If y
            if choice == "y":
                # Repeat the process
                enter_line = input("Enter line: ")
                myfile.write(enter_line + "\n")
                choice = input("Are there more lines y/n? ")
            # If n
            if choice == "n":
                # Stop the program
                break
            else:
                print("Invalid Key")
                choice = input("Are there more lines y/n? ")

# start
line_write()