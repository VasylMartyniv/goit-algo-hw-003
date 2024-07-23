import argparse
import os
import shutil


def copy_files(src_dir, dst_dir):
    try:
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)
            if os.path.isdir(src_path):
                copy_files(src_path, dst_dir)
            else:
                file_extension = os.path.splitext(item)[1].lstrip('.').lower() or 'no_extension'
                extension_dir = os.path.join(dst_dir, file_extension)

                if not os.path.exists(extension_dir):
                    os.makedirs(extension_dir)

                shutil.copy2(src_path, extension_dir)
                print(f"Copied {src_path} to {extension_dir}")

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    parser = argparse.ArgumentParser(description='Recursively copy and sort files by extension.')
    parser.add_argument('src_dir', help='Source directory path')
    parser.add_argument('dst_dir', nargs='?', default='dist', help='Destination directory path (default: dist)')

    args = parser.parse_args()

    src_dir = args.src_dir
    dst_dir = args.dst_dir

    if not os.path.exists(src_dir):
        print(f"The source directory {src_dir} does not exist.")
        return

    copy_files(src_dir, dst_dir)
    print("File copying and sorting complete.")


if __name__ == "__main__":
    main()
