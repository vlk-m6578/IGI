"""
Handles ZIP archive creation.
"""

import zipfile
from pathlib import Path
from .file_handler import FileHandler

class ZipArchiver(FileHandler):
    """Extends FileHandler with archiving capabilities."""

    def archive_file(self, filename: str, zipname: str) -> Path:
        """Create ZIP archive with results."""
        zip_path = self.output_dir / zipname
        with zipfile.ZipFile(zip_path, "w") as zf:
            file_to_archive = self.output_dir / filename
            zf.write(file_to_archive, arcname=filename)
        return zip_path