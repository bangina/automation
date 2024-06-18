# HEIC to JPG Converter

This script converts HEIC files in a specified directory to JPG format using the `heic-to-jpg` CLI tool.

## Requirements

- Python 3.x
- `heic-to-jpg` Python package
- ImageMagick

## Setup

1. **Create and activate a virtual environment**:

    ```bash
    python3 -m venv myenv
    source myenv/bin/activate
    ```

2. **Install dependencies**:

    ```bash
    pip install heic-to-jpg
    brew install imagemagick
    ```

## Usage

1. **Save the script to a file**, e.g., `convert_heic_to_jpg.py`:

    ```python
    import subprocess

    def convert_heic_to_jpg(source_dir):
        # heic-to-jpg CLI command execution
        command = f'heic-to-jpg -s {source_dir}'
        try:
            subprocess.run(command, shell=True, check=True)
            print(f"Converted HEIC files in {source_dir} to JPG")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred: {e}")

    if __name__ == "__main__":
        source_directory = input("Enter the source directory path containing HEIC files: ")
        convert_heic_to_jpg(source_directory)
    ```

2. **Run the script**:

    ```bash
    python convert_heic_to_jpg.py
    ```

3. **Enter the source directory path** when prompted:

    ```
    Enter the source directory path containing HEIC files: path/to/heic_files
    ```

    The script will convert all HEIC files in the specified directory to JPG format.

## Notes

- Make sure `heic-to-jpg` and ImageMagick are properly installed and available in your system's PATH.
- The script uses the `subprocess` module to run the `heic-to-jpg` command. If you encounter any issues, ensure that the `heic-to-jpg` command works correctly in your terminal.

## License

This project is licensed under the MIT License.
