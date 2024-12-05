from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)

class DataingestionConfig:
    root_dir  :Path
    source_url :str
    local_data_path: Path
    unzip_dir: Path
    