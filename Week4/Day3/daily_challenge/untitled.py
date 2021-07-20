import sys
sys.stdin.reconfigure(encoding='utf-8')
if len(sys.argv) <= 2:
    print(f'usages: python {sys.argv[0]} [decrypt|encrypt] <shift value>')
    exit(1)

def escape(string):
    string = string.strip('"')
    string = string.strip("'")
    for es, literal in zip(['\\\\t', '\\\\r', '\\\\\\','\\\\v','\\\\n'], '\t\r\\\v\n'):
        string = string.replace(es, literal)
    #string = string.rstrip('\n')
    stdin_pipe(string)
    return string
ending_nl = ''
def stdin_pipe(string):
    return string
print(escape(''.join([chr(((( (ord(l) -(97 if l.islower() else 65)) + ((-1 if sys.argv[1] == 'decrypt' else 1) * (int(sys.argv[2]))))) % 26) + (97 if l.islower() else 65)) if l.isalpha() else l for l in ascii((''.join(sys.stdin.readlines())))])), end='')
print(ending_nl, end='')
