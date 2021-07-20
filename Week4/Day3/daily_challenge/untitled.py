import sys
if len(sys.argv) <= 2:
    print(f'usages: python {sys.argv[0]} [decrypt|encrypt] <shift value>')
    exit(1)

def escape(string):
    string = string.strip('"')
    string = string.strip("'")
    string = string.rstrip('\\d')
    string = string.rstrip('\\x')
    string = string.rstrip('\\w')
    stdin_pipe(string)
    for es, literal in zip(['\\\\t', '\\\\r', '\\\\\\','\\\\v','\\\\n'], '\t\r\\\v\n'):
        string = string.replace(es, literal)
    #string = string.rstrip('\n')
    return string
ending_nl = ''
def stdin_pipe(string):
    if string[-1] == '\n':
        ending_nl = '\n'
    return string
print(escape(''.join([chr(((( (ord(l) -(97 if l.islower() else 65)) + ((-1 if sys.argv[1] == 'decrypt' else 1) * (int(sys.argv[2]))))) % 26) + (97 if l.islower() else 65)) if l.isalpha() else l for l in stdin_pipe(ascii(sys.stdin.read().rstrip('\d')))])), end='')
print(ending_nl, end='')
