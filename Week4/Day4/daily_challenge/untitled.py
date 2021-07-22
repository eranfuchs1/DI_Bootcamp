decode_matrix = lambda string: ' '.join(filter(lambda x: x,''.join(map(lambda x: x if x.isalpha() else ' ', [string.split('\n')[i][j]  for j in range(len(list(zip(*string.split('\n'))))) for i in range(len(string.split('\n')))])).split(' ')))

print(decode_matrix('''7i3
Tsi
h%x
i #
sM 
$a 
#t%
^r!'''))
