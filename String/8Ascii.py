#  Find the output of:
# -- problem for ascii concept

def shift_string(s):
    return ''.join(chr((ord(char) - 97 + 1) % 26 + 97) for char in s)

print(shift_string('hello world'))