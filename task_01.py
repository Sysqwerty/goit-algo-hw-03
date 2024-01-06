from pathlib import Path
import shutil
import os

source_path = Path('source_path')
destination_path = Path('destination_path')


def recursion_copy(source_path: Path, destination_path: Path = 'dist') -> None:
    try:
        if source_path.is_dir():
            for child in source_path.iterdir():
                recursion_copy(child, destination_path)
        else:
            file_extention = str(source_path).split('.').pop()
            newFilePath = Path(
                f'{destination_path}/{file_extention}')
            # create a folder if doesn't exist
            os.makedirs(str(newFilePath), exist_ok=True)
            # copy file to directory with file extention name, handle copy rights
            shutil.copy(source_path, newFilePath)
    except:
        print(f"No access rights to folder or file: '{source_path}'")


if __name__ == "__main__":
    recursion_copy(source_path, destination_path)
