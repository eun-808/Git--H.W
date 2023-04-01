def rep_char(a,b):
    return a*b
def welcome_msg(n):
    msg1 = f'Hello {name},'
    msg2 = 'Welcome to Seoul.'
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    print(rep_char('-',nstr))
    print(f'{msg1}\n{msg2}')
    print(rep_char('-',nstr))
name = input('input his/her name: ')
welcome_msg(name)