import re
from typing import List
from task2.regex_patterns import PATTERNS

class PhoneAnalyzer:
    """Finds phone numbers matching criteria: all phones are 9 characters long and start with 29"""

    def __init__(self, text: str):
        self.text = text

    def find_phones(self) -> List[str]:
        """Extract valid phone numbers."""
        return re.findall(PATTERNS["phones"], self.text)