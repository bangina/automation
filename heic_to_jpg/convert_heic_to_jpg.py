import subprocess

def convert_heic_to_jpg(source_dir):
    
    # heic-to-jpg CLI 명령어 실행
    command = f'heic-to-jpg -s {source_dir}'
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Converted HEIC files in {source_dir} to JPG")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    source_directory = input("Enter the source directory path containing HEIC files: ")
    convert_heic_to_jpg(source_directory)
