import re
from typing import List
from task2.regex_patterns import PATTERNS

class WordAnalyzer:
    """Handles word-level analysis tasks."""

    VOWELS = 'aeiouаеёиоуыэюя'
    CONSONANTS = 'bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ'

    def __init__(self, text: str):
        self.words = re.findall(PATTERNS["words"], text.lower())

    def filter_words(self) -> List[str]:
        """Filter words with 2nd consonant and 3rd vowel."""
        filtered = []
        for word in self.words:
            if len(word) >= 3:
                second_char = word[1]
                third_char = word[2]
                if second_char in self.CONSONANTS and third_char in self.VOWELS:
                    filtered.append(word)
        return filtered
    
    def count_consonant_endings(self) -> int:
        """Count words ending with consonants."""
        return len([word for word in self.words if word[-1] in self.CONSONANTS])
    
    def get_seventh_words(self) -> List[str]:
        """Extract every 7th word."""
        return self.words[::7]
    
    def get_words_by_length(self, length: int) -> List[str]:
        """Find words with specified length."""
        return [word for word in self.words if len(word) == length]
