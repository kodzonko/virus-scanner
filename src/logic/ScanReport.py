from dataclasses import dataclass
from typing import Dict


@dataclass
class ScanReport:
    file_name: str
    file_size: str
    engines_results: Dict[str, bool]

    @property
    def virus_score(self):
        """ratio of positive scan results (file infected) to all results"""
        tested_positive_counter = 0
        all_results_counter = len(self.engines_results.items())
        for outcome in self.engines_results.values():
            if outcome:
                tested_positive_counter += 1
        return tested_positive_counter / all_results_counter

    def __str__(self):
        # TODO: Build string from all engines and test results
        output = '\n'.join(f'{engine}: {result}' for engine, result in self.engines_results.items())

        return f'File: {self.file_name}\n' + \
               f'Size: {self.file_size}' + \
               f'Results:\n{output}'
