"""Offer anonymizer module."""
from .base_anonymizer import BaseAnonymizer


class OfferAnonymizer(BaseAnonymizer):
    """Offer anonymizer."""

    def __init__(self):
        self._anonymizers = []

    def add_anonymizer(self, anonymizer):
        """
        :param Anonymizer anonymizer:
        """
        self._anonymizers.append(anonymizer)

    def anonymize(self, text):
        """
        :param str text:
        :rtype: str
        """
        for anonymizer in self._anonymizers:
            text = anonymizer.anonymize(text)
        return text
