import sys
import os

read_path = sys.argv[1]
write_path = sys.argv[1] + ".temp"
with open(read_path, "r", encoding="utf-8") as read_file:
    with open(write_path, "w", encoding="utf-8") as write_file:
        for line in read_file:
            if line[0] == "#" and line[1] != " ":
                line = line[0] + " sent-id = " + line[1:]
            write_file.write(line)

os.rename(write_path, read_path)
