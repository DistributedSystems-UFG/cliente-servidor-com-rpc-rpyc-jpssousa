import rpyc

def remote_add(a,b):
    return a+b

def remote_sub(a,b):
    return a-b

def remote_mult(a,b):
    return a*b

def remote_div(a,b):
    if (b == 0):
        return 'Undefined'
    return a/b

ip = '44.203.156.19'

conn = rpyc.classic.connect(ip)
add = conn.teleport(remote_add)
sub = conn.teleport(remote_sub)
mult = conn.teleport(remote_mult)
div = conn.teleport(remote_div)

conn.execute('print("eval(2+3)")')
print('eval (2+3): ', conn.eval('2+3'))
conn.execute('print("add(1,2)")')
print('add(1,2) = ', add(1,2))
conn.execute('print("sub(3,5)")')
print('sub(3,5) = ', sub(3,5))
conn.execute('print("mult(-1,7)")')
print('mult(-1,7) = ', mult(-1,7))
conn.execute('print("div(2,0)")')
print('div(2,0) = ', div(2,0))
conn.execute('print("div(5,2)")')
print('div(5,2) = ', div(5,2))
