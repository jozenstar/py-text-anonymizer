"""Phone number anonymizer module."""

import re
from .base_anonymizer import BaseAnonymizer


class PhoneNumberAnonymizer(BaseAnonymizer):
    """Phone number anonymizer.

    Sample usages (parametrized):
    >>> PhoneNumberAnonymizer('X').anonymize('+48 666777888')
    '+48 666777XXX'
    >>> PhoneNumberAnonymizer('X', 5).anonymize('+48 666777888')
    '+48 6667XXXXX'
    >>> PhoneNumberAnonymizer('*', 1).anonymize('+48 666777888')
    '+48 66677788*'
    >>> PhoneNumberAnonymizer('x', 9).anonymize('+55 666777000')
    '+55 xxxxxxxxx'
    """

    def __init__(self, replacement, last_digits=3):
        """
        :param str replacement:
        :param int last_digits:
        """
        if not isinstance(replacement, str) or not isinstance(last_digits, int):
            raise ValueError
        self._repl = replacement
        self._digits = last_digits

    def anonymize(self, text):
        """
        :param str text:
        :rtype: str
        """
       # if not re.match(r'\+\d+ \d+', text):
        #    print("data is not valid")
       #     raise ValueError
        phone = re.sub(r'(\+\d+ \d*)\d{' + str(self._digits) + '}[\t]?',
                       r'\1' + self._repl*self._digits, text)
        return phone
