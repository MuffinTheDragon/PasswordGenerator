import random
from typing import List

"""
This module contains a password generator application which allows the generation of random passwords based on length and character type.
"""



class PasswordGenerator:
    """ Class for generating passwords

    === Attributes ===
    character_bank:
        dictionary that stores alpha characters, special symbols and ambiguous
        characters where the keys are 1, 2, 3
    length:
        specific length of password
    frequency:
        1 - letters, n - numbers + prev,
        2 - special symbols + prev's,
        3 - ambiguous characters.
        If no frequency is entered, password is comprised of letters only
    r_len:
        If True, generate the length of the list randomly
    password:
        stores the generated password

    === Representation Invariants ===
    length >= 6
    frequency inputs must be of the characters described
    """
    length: int
    frequency: str
    r_len: bool
    password: str

    character_bank = {1: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                      2: "!@#$%^&*", 3: "~`()<>,.?/:=\";'[]}{\\|_+-"}

    # letter_bank = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # symbol_bank = "!@#$%^&*"
    # amb_bank = "~`()<>,.?/:=\";'[]}{\\|_+-"

    def __init__(self, r_len: bool = False, length: int = 6,
                 frequency: str = "1") -> None:
        """ Initialize new password generator specifications
        """
        self.frequency = frequency
        if r_len:
            self._generate_length()
        else:
            self.length = length

        self.password = ""
        self.add_to_password()

    def _generate_length(self) -> None:
        """ Generate a random number between [6, 2048]
        """

        self.length = random.randint(6, 2048)

    def add_to_password(self) -> None:
        """ Generate random characters and add them to the final password
        """
        key_picker = 1

        if self.frequency == "2":
            key_picker = 2
        elif self.frequency == "3":
            key_picker = 3

        if self.length < 6:
            print("Password length must be between 6 and 2048 characters.")

        else:
            count = 0
            while count != self.length:
                char_pick = random.randint(1, key_picker)
                index_pick = random.randint(0, len(
                    self.character_bank[char_pick]) - 1)

                self.password += self.character_bank[char_pick][index_pick]

                count += 1

    def get_password(self) -> str:
        """ Return the generated password
        """

        return self.password

    def get_password_statistics(self) -> str:
        """ Return some statistics for the password generated
        """

        return "\n===Statistics===\nPassword length: {} \nPassword frequency:" \
               " {} \n".format(self.length, self.frequency)

    def r_generate_passwords(self, count: int) -> List[str]:
        """ Generate specific number of passwords at the same time
        """

        c = 0
        ans = []
        while c != count:
            self.add_to_password()
            ans.append(self.get_password())
            self.password = ""
            c += 1

        return ans


p = PasswordGenerator(False, 6, "3")
print(p.get_password())
print(p.get_password_statistics())
# print(p.r_generate_passwords(5))
