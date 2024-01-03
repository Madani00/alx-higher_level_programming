#!/usr/bin/python3
for le in range(97, 123):
    if chr(le) != 'e' and chr(le) != 'q':
        print('{:c}'.format(le), end='')
