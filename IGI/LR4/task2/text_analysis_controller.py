"""
Orchestrates text analysis workflow.
"""

from pathlib import Path
from .text_processor import TextProcessor
from .analyzers import PhoneAnalyzer, WordAnalyzer
from .file_operations import FileHandler, ZipArchiver

class TextAnalysisController:
    """Manages complete analysis pipeline."""
    
    def __init__(self):
        self.results = {}
        self.file_handler = FileHandler()
        self.archiver = ZipArchiver()
        
    def run_analysis(self, text: str):
        """Execute all analysis steps."""
        # General stats
        processor = TextProcessor(text)
        sentence_stats = processor.get_sentence_stats()
        word_stats = processor.calculate_word_stats()
        self.results.update({
            "total_sentences": sentence_stats["total"],
            "declarative_sentences": sentence_stats["declarative"],
            "interrogative_sentences": sentence_stats["interrogative"],
            "exclamatory_sentences": sentence_stats["exclamatory"],
            "avg_sentence_length": word_stats["avg_sentence_length"],
            "avg_word_length": word_stats["avg_word_length"],
            "smiles_count": processor.find_smiles()
        })
    
        # Phone analysis
        phones = PhoneAnalyzer(text).find_phones()
        self.results["phones"] = phones
    
        # Word analysis
        word_analyzer = WordAnalyzer(text)
        self.results.update({
            "filtered_words": word_analyzer.filter_words(),
            "consonant_endings_count": word_analyzer.count_consonant_endings(),
            "seventh_words": word_analyzer.get_seventh_words(),
        })
    
        # Words by average length
        avg_len = self.results["avg_word_length"]
        words_by_len = word_analyzer.get_words_by_length(avg_len)
        self.results["words_with_avg_length"] = words_by_len if words_by_len else f"Слов длиной {avg_len} символов нет"
        
    def save_results(self):
        """Save and archive results."""
        try:
            # Save to text file
            txt_path = self.file_handler.save_to_file(self.results, "analysis.txt")
            
            # Create ZIP archive
            zip_path = self.archiver.archive_file("analysis.txt", "results.zip")
            print(f"Results saved to: {zip_path}")
            
        except PermissionError:
            print("Error: No write permissions for the output directory.")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")