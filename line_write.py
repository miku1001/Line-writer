# Write a method in python to write multiple line of text contents into a text file mylife.txt.

def line_write():
# open myfile.txt(append)
    with open("myfile.txt", "a") as myfile:
        while True:    
            # Let user enter line
            enter_line = input("Enter line: ")
            myfile.write(enter_line + "/n")
            # Let user choose whether add more text per line or stop
            choice = input("Are there more lines y/n? ")
            # If y
# Repeat the process
# If n
# Stop the program
# start
line_write()