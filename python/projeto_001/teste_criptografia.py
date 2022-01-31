def cryptograp(valor):
    value_comp = ''
    for letra in valor:
        if letra in 'Aa':
            value_comp += '@'
        elif letra in 'Bb':
            value_comp += 'D'
        elif letra in 'Cc':
            value_comp += '2'
        elif letra in 'Dd':
            value_comp += 'b'
        elif letra in 'Ee':
            value_comp += '&'
        elif letra in 'Ff':
            value_comp += '%'
        elif letra in 'Gg':
            value_comp += '6'
        elif letra in 'Hh':
            value_comp += '?'
        elif letra in 'Ii':
            value_comp += 'l'
        elif letra in 'Jj':
            value_comp += '+'
        elif letra in 'Kk':
            value_comp += 'Q'
        elif letra in 'Ll':
            value_comp += '1'
        elif letra in 'Mm':
            value_comp += 'N'
        elif letra in 'Nn':
            value_comp += 'M'
        elif letra in 'Oo':
            value_comp += '9'
        elif letra in 'Pp':
            value_comp += '7'
        elif letra in 'Qq':
            value_comp += '8'
        elif letra in 'Rr':
            value_comp += 'f'
        elif letra in 'Ss':
            value_comp += '#'
        elif letra in 'Tt':
            value_comp += '*'
        elif letra in 'Uu':
            value_comp += 'H'
        elif letra in 'Vv':
            value_comp += '!'
        elif letra in 'Ww':
            value_comp += '/'
        elif letra in 'Xx':
            value_comp += 'K'
        elif letra in 'Yy':
            value_comp += 'x'
        elif letra in 'Zz':
            value_comp += '5'
        elif letra in ' ':
            value_comp += '0'
        else:
            value_comp += letra
    return value_comp

ff = cryptograp(str(input('\n\nDigite algo: ')))

