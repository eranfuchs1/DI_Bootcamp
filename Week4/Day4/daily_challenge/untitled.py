def decode_matrix(string):
    return ''.join(filter(lambda x: x.isalpha(), [string.split('\n')[i][j]  for j in range(len(list(zip(*string.split('\n'))))) for i in range(len(string.split('\n')))]))

print(decode_matrix('''7i3
Tsi
h%x
i #
sM 
$a 
#t%
^r!'''))
