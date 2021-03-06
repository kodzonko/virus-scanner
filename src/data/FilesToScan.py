import os
from pathlib import Path
from typing import List


class FilesToScan:
    files_to_scan = []

    @classmethod
    def add_files_to_scan_queue(cls, paths: List[Path, str]) -> None:
        """
        Opens a dialogue to select file(s) to scan

        :return:
        None
        """
        for path in paths:
            if os.path.isfile(path) and path not in cls.files_to_scan:
                cls.files_to_scan.append(path)

    @classmethod
    def clear_queue(cls) -> None:
        """Clears scan queue"""
        cls.files_to_scan.clear()
