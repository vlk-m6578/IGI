"""
Module containing serialization classes.
"""

from abc import ABC, abstractmethod
import csv
import pickle
from typing import Dict
from task1.models import RationalNumber

class Serializer(ABC):
    """Abstract base class for serializers."""

    @abstractmethod
    def serialize(self, data: Dict[str, RationalNumber], filename: str):
        pass

    @abstractmethod
    def deserialize(self, filename: str) -> Dict[str, RationalNumber]:
        pass

class CSVSerializer(Serializer):
    """CSV format serializer."""

    def serialize(self, data: Dict[str, RationalNumber], filename: str):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for key, value in data.items():
                writer.writerow([key, value.numerator, value.denominator])

    def deserialize(self, filename: str) -> Dict[str, RationalNumber]:
        data = {}
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                data[row[0]] = RationalNumber(int(row[1]), int(row[2]))
        return data
    
class PickleSerializer(Serializer):
    """Pickle format serializer."""
    
    def serialize(self, data: Dict[str, RationalNumber], filename: str):
        with open(filename, 'wb') as f:
            pickle.dump(data, f)

    def deserialize(self, filename: str) -> Dict[str, RationalNumber]:
        with open(filename, 'rb') as f:
            return pickle.load(f)
        