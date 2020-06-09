"""Skype username anonymizer module."""

import re
from .base_anonymizer import BaseAnonymizer


class SkypeUsernameAnonymizer(BaseAnonymizer):
    """Skype username anonymizer.

    Sample usages (parametrized):
    >>> SkypeUsernameAnonymizer('#').anonymize('<a href="skype:loren?call"/>')
    '<a href="skype:#?call"/>'
    >>> SkypeUsernameAnonymizer('#').anonymize('<a href="skype:LOREN?chat"/>')
    '<a href="skype:#?chat"/>'
    """

    def __init__(self, replacement):
        """
        :param str replacement:
        """
        # Consider input validation
        self._repl = replacement

    def anonymize(self, text):
        """
        :param str text:
        :rtype: str
        """
        #if not re.match(r'\+\d+ \d+', text):
        #    print("data is not valid")
        #    raise ValueError
        skype = re.sub(r':\w+\?', ':' + self._repl + '?', text)
        return skype