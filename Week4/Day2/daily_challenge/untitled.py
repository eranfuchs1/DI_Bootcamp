birthdate = input('enter your birthdate:(format: <DD/MM/YYYY>) ')
year = int(birthdate.split('/')[-1])
candles = 'i' * int(str(2021 - year)[-1])
if len(candles) < 5:
    underscores = '_' * ((5 - len(candles)) // 2)
    candles = underscores + candles + underscores
if len(candles) < 5:
    candles += '_'
underscores2 = '_' * 2
happy = ':'.join('Happy')
birthday = ':'.join('Birthday')
line3 = f"{'_' * 2}|{'_'* (len(happy) + 1 + len(candles) * 2 - 9)}|{'_' * 2}"
underscores1 = '_' * ((len(line3) - len(candles) - 6) // 2)
top_inject = ''
if len(candles) % 2 == 0:
    top_inject = '_'

cake = f"""
  {' ' * 2}{underscores1}{candles}{underscores1}{top_inject} {' ' * 2} 
 {' ' * 2}|{':' * (len(candles) - 4)}{happy}{':' * (len(candles) - 4)}|{' ' * 2} 
 {line3} 
|{'^' * len(line3)}|
|{':' * ((len(line3) - (len(birthday)) )// 2)}{birthday}{':' * ((len(line3) - (len(birthday))) // 2)}|
|{' ' * len(line3)}|
_{'_' * len(line3)}_
"""
if year % 4 == 0:
    print('leap year means 2 cakes!')
    for piece in cake.split('\n'):
        print(f"{piece}   {piece}")
else:
    print(cake)
