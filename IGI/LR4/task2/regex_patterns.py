"""
Contains all regex patterns for text analysis.
"""

PATTERNS = {
    # Phone numbers starting with 29 (9 digits)
    "phones": r"\b29\d{7}\b",

    # Words 
    "words": r"\b[a-zA-Zа-яА-ЯёЁ]+\b",
    
    # Smiles 
    "smiles": r"[:;]-*([([{)\]}])+", 

    # Sentence splitting
    "sentences": r"[^.!?]+[.!?]"
}