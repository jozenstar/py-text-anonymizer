"""Email anonymizer module."""
import re
from .base_anonymizer import BaseAnonymizer


class EmailAnonymizer(BaseAnonymizer):
    """Email anonymizer.

    Sample usages (parametrized):
    >>> EmailAnonymizer('...').anonymize('aaa@aaa.com')
    '...@aaa.com'
    >>> EmailAnonymizer('***').anonymize('a-a@a.b.c')
    '***@a.b.c'
    >>> EmailAnonymizer('XXX').anonymize('a.d+a@a-a.com')
    'XXX@a-a.com'
    """

    def __init__(self, replacement):
        """
        :param str replacement:
        """
        if not isinstance(replacement, str):
            raise ValueError
        self._replacement = replacement

    def anonymize(self, text):
        """
        :param str text:
        :rtype: str
        """
        if not re.search(r'\w[^ ]*\w*@\w(.\w)*(\.\w.\w)+', text):
            print("data is not valid")
         #   raise ValueError
        email = text
        try:
            email = re.sub(r'\w+[^\s]*\w*?(@\w+[^\s]*(\.\w.\w)+)+',
                           self._replacement + r'\1', text)
        finally:
            return email

        #
        # @TODO: Implement it
        #
