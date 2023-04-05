# Creata a program to read and write into a txt file.
# The program should prompt the user to enter the name of a file.
# If the file exists, it should let the user know and allow the user make changes into the file by adding content or changing words in the file.


# If the file doesn't exist, it should create the file and allow the user be able to write into the file. And also be able to make changes to the file.

# Before a user is able to make any changes to a file they should see the content of the file.


filename = input('Enter file name: ')
try:
    file = open(filename)
    if file:
        print('file exists')
        cmd = input('enter (y) to add to file and (n) to change words: ')
        if cmd == 'y':
            file = open(filename, 'a')
            while True:
                enter = input('add content: ')
                if enter == 'done':
                    file.close()
                    break
                else:
                    file.write(enter + '\n')
        elif cmd == 'n':
            with open(filename, 'r+') as file:
                lines = file.readlines()
                for words in lines:
                    words.split()
                    print(words.rstrip())
                file.seek(0)
                enter = input('\n Enter the word to change: ')
                read = file.read()
                if enter in read:
                    file.seek(0)
                    print(f'Do you want to change {enter}? y/n: ')
                    a = input('>>> ')
                    if a == 'y':
                        new_word = input(
                            f'Enter the word you want to change {enter} with: ')
                        for line in lines:
                            modified_line = line.replace(
                                enter, new_word)
                            file.write(modified_line)
                        print(f'{enter} changed to {new_word} successfully')
                        file.close()

                    elif a == 'n':
                        print('successfully aborted')
                else:
                    print(f'no such word as {enter}')


except FileNotFoundError as e:
    print('File not found')
    cmd = input('create file y/n: ')
    if cmd == 'y':
        file = open(filename, 'w')
        choice = input('write to file y/n: ')
        if choice == "y":
            while True:
                line = input('Type here: ')
                if line == 'done':
                    file.close()
                    break
                else:
                    file.write(line + '\n')
    else:
        print('closed.')
