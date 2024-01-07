from pathlib import Path
import shutil
import os
import argparse


def recursion_copy(source_path: Path, destination_path: Path = 'dist') -> None:
    try:
        if source_path.is_dir():
            for child in source_path.iterdir():
                print(f'Handling file: {str(child)}')
                recursion_copy(child, destination_path)
        else:
            file_extension = source_path.suffix
            # remove a dot from the extension
            new_file_path = destination_path / file_extension[1:]
            # create the folder if it doesn't exist
            new_file_path.mkdir(parents=True, exist_ok=True)
            shutil.copy(source_path, new_file_path)
    except Exception as e:
        print(
            f"Error: {e} - No access rights to folder or file: '{source_path}'")


def main():
    parser = argparse.ArgumentParser(
        description='Recursively copy files from source_path to destination_path.')
    parser.add_argument('source_path', type=Path,
                        help='Source path for recursive copy')
    parser.add_argument('--destination_path', type=Path, default=Path('dist'),
                        help='Destination path for copied files (default: dist)')

    args = parser.parse_args()
    print(f"Hi. I'm going to copy files from '{args.source_path}' folder to '{
          args.destination_path}' folder sorting them by folders with the files extention name")
    recursion_copy(args.source_path, args.destination_path)


if __name__ == "__main__":
    main()
