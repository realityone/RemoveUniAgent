#!/usr/bin/env python3
# encoding=utf-8
import hashlib

SLAT = '7964E099ED14FAB59A4497C14F16A526'

def make_pass(dyn_code):
    dyn_code = '{}{}'.format(dyn_code, SLAT)
    buf = bytearray(len(dyn_code) * 2)
    for i, c in enumerate(dyn_code):
        buf[i * 2] = ord(c)
        buf[i * 2 + 1] = 0

    h = hashlib.md5(buf).hexdigest()
    first = h[:6].upper()

    code = bytearray(len(first))
    for i, c in enumerate(first):
        code[i] = ord(c)
        if code[i] >= 65 and code[i] <= 90:
            code[i] = ((code[i] - 65) % 10) + 48
        if code[i] == 52:
            code[i] = 56
        elif code[i] == 55:
            code[i] = 57
    return code.decode('utf-8')

def main():
    print(make_pass('320696'))

if __name__ == '__main__':
    main()

