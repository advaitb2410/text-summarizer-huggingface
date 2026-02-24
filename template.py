import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

project_name = "text-summarizer-huggingface"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "pyproject.toml",
    "README.md"
]

for file in list_of_files:
    file_path = Path(file)
    file_dir = file_path.parent

    if not file_dir.exists():
        os.makedirs(file_dir)
        logging.info(f"Created directory: {file_dir}")

    if (not file_path.exists() or file_path.stat().st_size == 0) and file_path.suffix != ".ipynb":
        file_path.touch()
        logging.info(f"Created file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}")
