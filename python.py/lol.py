#!/usr/bin/env python
import sys

commit_msg_filepath = sys.argv[1]

with open(commit_msg_filepath, "r+") as f:
    message = f.read()

    # Check if the commit message starts with the desired prefix
    if message[:2].isalpha():
        if message[3] == "-":
            if message[4:7].isdigit():
                print("Le format du message de commit est correct.")

        # Go to the beginning of the file and rewrite it
        f.seek(0)
        f.write(message)
        f.truncate()
        sys.exit(0)
    else:
        print("Error: Commit message does not start with 'Welcome to Python'.")
        sys.exit(1)
