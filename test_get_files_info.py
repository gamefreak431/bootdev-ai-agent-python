from functions.get_files_info import get_files_info

def main():
    tests = [
        ("calculator", "."),
        ("calculator", "/bin"),
        ("calculator", "../"),
        ("calculator", "main.py")
    ]

    for working_directory, directory in tests:
        result = get_files_info(working_directory, directory)
        print(result)


if __name__ == "__main__":
    main()