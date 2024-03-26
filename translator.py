# -*- coding: utf-8 -*-

"""
@author: Princi Mixtiy
Script: Chiffre -> Lettre
"""

zero_to_nine = ('zero', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept',
                'huit', 'neuf')

zero_to_nineteen = zero_to_nine + ('dix', 'onze', 'douze', 'treize', 'quatorze',
                                   'quinze', 'seize', 'dix sept', 'dix huit', 'dix neuf')

ten_levels = ('', 'dix', 'vingt', 'trente', 'quarante', 'cinquante', 'soixante',
              '', 'quatre vingt', '')

levels = ('cent', 'mille', 'million', 'milliarrd')


def dix(x: int, /) -> str:
    """fonction pour traduire les nombres de 0 à 99

        Args:
            x (int): un nombre à traduire en lettre

        Returns:
            _type_: str
        """
    if x < 20:
        return zero_to_nineteen[x].capitalize()

    else:
        part2 = ''

        if (str(x)[0] == '7') or (str(x)[0] == '9'):
            # pour 70 et 90
            part1 = f'{ten_levels[int(str(x)[0]) - 1].capitalize()}'
            if int(str(x)[1]) != 0:
                part2 = f' {zero_to_nineteen[int(str(x)[1]) + 10].capitalize()}'
        else:
            part1 = f'{ten_levels[int(str(x)[0])].capitalize()}'
            if int(str(x)[1]) != 0:
                part2 = f' {zero_to_nineteen[int(str(x)[1])].capitalize()}'

        return part1 + part2


def cent(x: int, /) -> str:
    """fonction pour traduire les nombres de 0 à 999

        Args:
            x (int): un nombre à traduire en lettre

        Returns:
            _type_: str
        """
    if x < 100:
        return dix(x)

    else:
        lvl = levels[0]

        unite = int(str(x)[0])
        reste = int(str(x)[-2:])

        part1 = ''
        part2 = lvl.capitalize()
        part3 = ''

        if unite != 1:
            part1 = f'{zero_to_nine[unite].capitalize()} '

        if reste != 0:
            part3 = f' {dix(reste)}'

        return part1 + part2 + part3


def mille(x: int, /) -> str:
    """fonction pour traduire les nombres de 0 à 999 999

        Args:
            x (int): un nombre à traduire en lettre

        Returns:
            _type_: str
        """
    if x < 1000:
        return cent(x)

    else:
        lvl = levels[1]

        unite = int(str(x)[:-3])
        reste = int(str(x)[-3:])

        part1 = ''
        part2 = lvl.capitalize()
        part3 = ''

        if unite != 1:
            part1 = cent(unite) + ' '

        if reste != 0:
            part3 = f' {cent(reste)}'

        return part1 + part2 + part3


def million(x: int, /) -> str:
    """fonction pour traduire les nombres de 0 à 999 999 999

    Args:
        x (int): un nombre à traduire en lettre

    Returns:
        _type_: str
    """
    if x < 1000000:
        return mille(x)

    else:
        lvl = levels[2]

        unite = int(str(x)[:-6])
        reste = int(str(x)[-6:])

        part1 = cent(unite) + ' '
        part2 = lvl.capitalize()
        part3 = ''

        if reste != 0:
            part3 = f" {mille(reste)}"

        return part1 + part2 + part3


def milliard(x: int, /) -> str:
    """fonction pour traduire tous les nombres positifs

    Args:
        x (int): un nombre à traduire en lettre

    Returns:
        _type_: str
    """
    if x < 1000000000:
        return million(x)

    else:
        lvl = levels[3]

        unite = int(str(x)[:-9])
        reste = int(str(x)[-9:])

        part1 = milliard(unite) + ' '
        part2 = lvl.capitalize()
        part3 = ''

        if reste != 0:
            part3 = f" {million(reste)}"

        return part1 + part2 + part3


def entier(x: int, /) -> str:
    """fonction pour traduire les nombres entiers

    Args:
        x (int): un nombre à traduire en lettre

    Returns:
        _type_: str
    """
    if x >= 0:
        return milliard(x)
    else:
        y = abs(x)
        return f"Moin {milliard(y)}"


def virgule(x: str, /) -> str:
    """fonction pour traduire la partie après la virgule

    Args:
        x (str): ce qu'il y a après la virgule
                 x est de type (str) pour eviter d'éliminer les premiers 0
                 exemple : 9898.0098  |   x = "0098"

    Returns:
        _type_: str
    """
    zero_len = 0
    after_zeros = ''

    for i in range(len(x)):
        if x[i] == "0":
            zero_len += 1
        else:
            after_zeros = int(x[i:])
            break

    zeros = "Zero " * zero_len
    return f"{zeros}{milliard(after_zeros)}"


def reel(x: float, /) -> str:
    """fonction pour traduire les nombres reels

    Args:
        x (float): un nombre reel à traduire en lettre

    Returns:
        _type_: str
    """
    
    if isinstance(x, int):
        return entier(x)
        
    else:
        x = str(x)
        i = x.index(".")
        pred = x[:i]
        succ = x[i+1:]

        part1 = 'Zero'
        part2 = ''
        part3 = ''

        if int(pred) != 0:
            part1 = entier(int(pred))

        if int(succ) != 0:
            part2 = ' virgule '
            part3 = virgule(succ)

        return part1 + part2 + part3


translate = reel

if __name__ == '__main__':
    import sys
    number = sys.argv[1]
    number = number.replace(',', '.').replace(' ', '')
    print(f'{float(number)}: {translate(float(number))}')
