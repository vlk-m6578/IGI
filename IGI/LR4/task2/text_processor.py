import re
from typing import List, Dict
from pathlib import Path
from task2.regex_patterns import PATTERNS

class TextProcessor:
    """Base class for text processing operations."""

    def __init__(self, text: str):
        self._text = text
        self._sentences = self._split_sentences()
        self._words = self._extract_words()

    @property
    def text(self) -> str:
        """Возвращает исходный текст."""
        return self._text

    def _split_sentences(self) -> List[str]:
        """Split text into sentences using regex."""
        return re.findall(PATTERNS["sentences"], self._text)
    
    def _extract_words(self) -> List[str]:
        """Extract all words from text."""
        return re.findall(PATTERNS["words"], self._text, flags=re.IGNORECASE)
    
    def get_sentence_stats(self) -> Dict[str, int]:
        """Calculate sentence type statistics."""
        stats = {
            "total": len(self._sentences),
            "declarative": 0,
            "interrogative": 0,
            "exclamatory": 0
        }
        for sent in self._sentences:
            if sent.strip().endswith('.'):
                stats["declarative"] += 1
            elif sent.strip().endswith('?'):
                stats["interrogative"] += 1
            elif sent.strip().endswith('!'):
                stats["exclamatory"] += 1
        return stats
    
    def calculate_word_stats(self) -> Dict[str, float]:
        """Calculate average word and sentence length."""
        total_chars = sum(len(word) for word in self._words)
        avg_word_len = round(total_chars / len(self._words)) if self._words else 0

        sent_chars = sum(len(re.sub(r'[^a-zA-Zа-яА-ЯёЁ]', '', sent)) for sent in self._sentences)
        avg_sent_len = round(sent_chars / len(self._sentences)) if self._sentences else 0

        return {
            "avg_word_length": avg_word_len,
            "avg_sentence_length": avg_sent_len
        }
    
    def find_smiles(self) -> int:
        """Count valid smileys in text."""
        matches = re.findall(PATTERNS["smiles"], self._text)
        return len(matches)