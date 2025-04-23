"""
Manages file operations and directory creation.
"""

from pathlib import Path

class FileHandler:
    """Handles file saving operations."""
    def __init__(self, output_dir: str = "results"):
        self.output_dir = Path(output_dir)
        self._create_directory()

    def _create_directory(self):
        """Create output directory if not exists."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def save_to_file(self, data: dict, filename: str) -> Path:
        """Save data to text file."""
        output_path = self.output_dir / filename
        with open(output_path, "w", encoding="utf-8") as f:
            for key, value in data.items():
                f.write(f"{key}: {value}\n")
        return output_path
