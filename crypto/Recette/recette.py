import string
import base64

data_input = '32 69 31 73 34 69 31 73 31 35 64 31 6f 34 39 69 31 6f 34 64 31 6f 33 69 31 6f 31 35 64 31 6f 32 32 64 31 6f 32 30 64 31 6f 31 39 69 31 6f 37 64 31 6f 35 64 31 6f 32 69 31 6f 35 35 69 31 6f 31 64 31 6f 31 39 64 31 6f 31 37 64 31 6f 31 38 64 31 6f 32 39 69 31 6f 31 32 69 31 6f 32 36 69 31 6f 38 64 31 6f 35 39 64 31 6f 32 37 69 31 6f 36 64 31 6f 31 37 69 31 6f 31 32 64 31 6f 37 64 31 6f 35 69 31 6f 31 64 31 6f 32 64 31 6f 31 32 69 31 6f 39 64 31 6f 32 36 64 31 6f'

# ----------------
# convert from hex
# ----------------
data_from_hex = [chr(int(x,16)) for x in data_input.split()]
print(f'{data_from_hex=}')


# --------------
# develop digits
# --------------
data_developped = ''
factor_accumulator = ''
for c in data_from_hex:
    if c in string.digits:
        factor_accumulator += c
    else:
        factor = int(factor_accumulator)
        data_developped += factor * c
        factor_accumulator = ''

print(f'{data_developped=}')


# ---------------------------------------------------------
# decode DeadFish : ref. https://esolangs.org/wiki/Deadfish
# ---------------------------------------------------------
data_from_deadfish = ''
accumulator = 0
for c in data_developped:
    if c == 'i':
        # increment
        accumulator += 1
    elif c == 'd':
        # decrement
        accumulator -= 1
    elif c == 's':
        # square
        accumulator *= accumulator
    elif c == 'o':
        # output
        data_from_deadfish += chr(accumulator)

print(f'{data_from_deadfish=}')


# -------------------
# decode from base 85
# -------------------
data_from_base85 = base64.a85decode(data_from_deadfish)
print(f'{data_from_base85=}')
