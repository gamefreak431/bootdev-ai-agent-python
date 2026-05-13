from functions.get_files_info import get_files_info

def main():
    tests = [
        ("calculator", "."),
        ("calculator", "pkg"),
        ("calculator", "/bin"),
        ("calculator", "../"),
    ]

    for working_directory, directory in tests:
        result = get_files_info(working_directory, directory)
        print(f"Result for '{directory}' directory:\n{result}")


if __name__ == "__main__":
    main()