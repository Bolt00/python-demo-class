'''
'a' -> append mode. This would open up the file and append changes(read, write). It creates a file if it dosn't exist.

'w' -> Write mode. This allows to write to a file. If the file already contains content, it'll overwrite. It creates a file if it doesn't exist.

'r' -> Read mode. This is just used to read the file. This is the default mode.
'''


fhand = open('demo.txt')
num_lines = 0
for line in fhand:
    num_lines += 1

print(f'The file contains {num_lines} lines of text')

