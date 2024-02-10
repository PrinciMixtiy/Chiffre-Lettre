class Chiffre:
    under_twenty_0 = ('zero', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept',
                      'huit', 'neuf', 'dix', 'onze', 'douze', 'treize', 'quatorze',
                      'quinze', 'seize', 'dix sept', 'dix huit', 'dix neuf')

    under_twenty_1 = ('', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept',
                      'huit', 'neuf', 'dix', 'onze', 'douze', 'treize', 'quatorze',
                      'quinze', 'seize', 'dix-sept', 'dix-huit', 'dix-neuf')

    under_twenty_2 = ('', '', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept',
                      'huit', 'neuf', 'dix', 'onze', 'douze', 'treize', 'quatorze',
                      'quinze', 'seize', 'dix sept', 'dix huit', 'dix neuf')

    tens = ('', 'dix', 'vingt', 'trente', 'quarante', 'cinquante', 'soixante',
            '', 'quatre vingt', '')

    units = ('cent', 'mille', 'million', 'milliarrd')

    def __init__(self, x):
        if not isinstance(x, str):
            x = str(x)
        self.lettre = self._convertir_en_lettre(x)

    def _nb(self, x: int) -> str:
        """methode pour traduire les nombres de 0 à 19

        Args:
            x (int): un nombre à traduire en lettre

        Returns:
            _type_: str
        """
        return f'{self.under_twenty_0[x].capitalize()}'

    def _dix(self, x: int) -> str:
        """methode pour traduire les nombres de 0 à 99

        Args:
            x (int): un nombre à traduire en lettre

        Returns:
            _type_: str
        """
        if x < 20:
            return self._nb(x)
        else:
            if (str(x)[0] == '7') or (str(x)[0] == '9'):  # pour 70 et 90
                return (f'{self.tens[int(str(x)[0]) - 1].capitalize()} '
                        f'{self.under_twenty_1[int(str(x)[1]) + 10].capitalize()}')
            else:
                return f'{self.tens[int(str(x)[0])].capitalize()} {self.under_twenty_1[int(str(x)[1])].capitalize()}'

    def _cent(self, x: int) -> str:
        """methode pour traduire les nombres de 0 à 999

        Args:
            x (int): un nombre à traduire en lettre

        Returns:
            _type_: str
        """
        if x < 100:
            return self._dix(x)
        else:
            dg = self.units[0]
            centaine = int(str(x)[0])
            reste = int(str(x)[-2:])
            if reste != 0:
                return f"{self.under_twenty_2[centaine].capitalize()} {dg.capitalize()} {self._dix(reste)}"
            else:
                return f"{self.under_twenty_2[centaine].capitalize()} {dg.capitalize()}"

    def _mille(self, x: int) -> str:
        """fonction pour traduire les nombres de 0 à 999 999

        Args:
            x (int): un nombre à traduire en lettre

        Returns:
            _type_: str
        """
        if x < 1000:
            return self._cent(x)
        else:
            dg = self.units[1]
            unite = int(str(x)[:-3])
            reste = int(str(x)[-3:])
            if unite == 1:
                millier = self.under_twenty_2[unite]
            else:
                millier = self._cent(unite)
            if reste != 0:
                return f"{millier} {dg.capitalize()} {self._cent(reste)}"
            else:
                return f"{millier} {dg.capitalize()}"

    def _million(self, x: int) -> str:
        """fonction pour traduire les nombres de 0 à 999 999 999

        Args:
            x (int): un nombre à traduire en lettre

        Returns:
            _type_: str
        """
        if x < 1000000:
            return self._mille(x)
        else:
            dg = self.units[2]
            unite = int(str(x)[:-6])
            reste = int(str(x)[-6:])
            millions = self._cent(unite)
            if reste != 0:
                return f"{millions} {dg.capitalize()} {self._mille(reste)}"
            else:
                return f"{millions} {dg.capitalize()}"

    def _milliard(self, x: int) -> str:
        """fonction pour traduire tous les nombres

        Args:
            x (int): un nombre à traduire en lettre

        Returns:
            _type_: str
        """
        if x < 1000000000:
            return self._million(x)
        else:
            dg = self.units[3]
            unite = int(str(x)[:-9])
            reste = int(str(x)[-9:])
            milliards = self._milliard(unite)
            if reste != 0:
                return f"{milliards} {dg.capitalize()} {self._million(reste)}"
            else:
                return f"{milliards} {dg.capitalize()}"

    @staticmethod
    def _negatif(x: int) -> bool:
        """fonction pour verifier si un nombre est negatif

        Args:
            x (int): le nombre à vérifier

        Returns:
            _type_: bool
        """
        return x < 0

    def _entier(self, x: int) -> str:
        """fonction pour traduire les nombres entiers

        Args:
            x (int): un nombre à traduire en lettre

        Returns:
            _type_: str
        """
        if not self._negatif(x):
            return self._milliard(x)
        else:
            y = int(str(x)[1:])
            return f"Moin {self._milliard(y)}"

    def _virgule(self, x: str) -> str:
        """fonction pour traduire la partie après la virgule

        Args:
            x (str): ce qu'il y a après la virgule
                     x est de type (str) pour eviter d'éliminer les premiers 0
                     exemple : 9898.0098  |   x = "0098"

        Returns:
            _type_: str
        """
        compteur_zero = 0
        after_zeros = x
        for i in range(len(x)):
            if x[i] == "0":
                compteur_zero += 1
            else:
                after_zeros = x[i:]
                break
        zeros = "Zero " * compteur_zero
        return f"{zeros}{self._milliard(int(after_zeros))} "

    def _reel(self, x: float) -> str:
        """fonction pour traduire les nombres reels

        Args:
            x (float): un nombre reel à traduire en lettre

        Returns:
            _type_: str
        """
        x = str(x)
        i = x.index(".")
        pred = x[:i]
        succ = x[i + 1:]
        if int(succ) == 0:
            if int(pred) != 0:
                return self._entier(int(pred))
            else:
                return self.under_twenty_0[0]
        else:
            if int(pred) != 0:
                return f"{self._entier(int(pred))} virgule {self._virgule(succ)}"
            else:
                if '-' in pred:
                    return f"Moins Zero virgule {self._virgule(succ)}"
                else:
                    return f"Zero virgule {self._virgule(succ)}"

    def _convertir_en_lettre(self, x: str) -> str:
        """fonction qui détermine le fonction à utiliser pour trauire un chiffre en lettre
           entier(x) si x est un nombre entier
           reel(x) si x est un nombre réel

        Args:
            x (str): un chiffre à traduire en lettre

        Returns:
            _types_: int or float
        """
        x = x.replace(" ", "")

        if not (("." in x) or ("," in x)):
            x = int(x)
            return self._entier(x)
        else:
            x = x.replace(",", ".")
            x = float(x)
            return self._reel(x)


if __name__ == '__main__':
    while True:
        x = input('Entrez un chiffre ou "exit" pour sortir : ')
        if x.lower() == "exit":
            break
        elif x == "":
            continue
        else:
            if " " in x:
                x = x.replace(" ", "")
            try:
                c = Chiffre(x)
                print(f'Chiffre : {x}')
                print(f'Lettre : {c.lettre}')
            except ValueError:
                print('Entrez un chiffre ou "exit" pour sortir : ')
            finally:
                print("")

        print("#=====+++++=====" * 5 + "#")
        print("")
