import re

class VTools:

    @staticmethod
    def is_command(string):
        return bool(re.fullmatch(r"@[A-Z]{2}", string))