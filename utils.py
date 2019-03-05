from subprocess import Popen, PIPE, STDOUT

def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)

def syscmd(cmd, encoding=''):
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT,close_fds=True)
    p.wait()
    output = p.stdout.read()
    if len(output) > 1:
        if encoding: return output.decode(encoding)
        else:
            return output
    return p.returncode