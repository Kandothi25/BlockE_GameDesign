print('Now give me an 8 bit binary number and I will convert it to decimal')
bin_dig1 = input('Enter the first digit: ')
bin_dig2 = input('Enter the second digit: ')
bin_dig3 = input('Enter the third digit: ')
bin_dig4 = input('Enter the fourth digit: ')
bin_dig5 = input('Enter the fifth digit: ')
bin_dig6 = input('Enter the sixth digit: ')
bin_dig7 = input('Enter the seventh digit: ')
bin_dig8 = input('Enter the eighth digit: ')
print('Your binary number is', bin_dig1+bin_dig2+bin_dig3+bin_dig4+bin_dig5+bin_dig6+bin_dig7+bin_dig8)
if int(bin_dig1) == 1:
    dec_dig1 = 128
else:
    dec_dig1 = 0
if int(bin_dig2) == 1:
    dec_dig2 = 64
else:
    dec_dig2 = 0
if int(bin_dig3) == 1:
    dec_dig3 = 32
else:
    dec_dig3 = 0
if int(bin_dig4) == 1:
    dec_dig4 = 16
else:
    dec_dig4 = 0
if int(bin_dig5) == 1:
    dec_dig5 = 8
else:
    dec_dig5 = 0
if int(bin_dig6) == 1:
    dec_dig6 = 4
else:
    dec_dig6 = 0
if int(bin_dig7) == 1:
    dec_dig7 = 2
else:
    dec_dig7 = 0
if int(bin_dig8) == 1:
    dec_dig8 = 1
else:
    dec_dig8 = 0
print('Your decimal number is', int(dec_dig1)+int(dec_dig2)+int(dec_dig3)+int(dec_dig4)+int(dec_dig5)+int(dec_dig6)+int(dec_dig7)+int(dec_dig8))