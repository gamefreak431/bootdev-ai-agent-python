from functions.get_file_content import get_file_content

def main():
    tests = [
        ("calculator", "lorem.txt"),
        ("calculator", "main.py"),
        ("calculator", "pkg/calculator.py"),
        ("calculator", "/bin/cat"),
        ("calculator", "pkg/does_not_exist.py")
    ]

    for working_directory, file_path in tests:
        result = get_file_content(working_directory, file_path)
        if file_path == "lorem.txt":
            is_truncated = "truncated" in result.split('...')[1]
            print(f"{file_path} truncated: {is_truncated}")
        else:
            print(f"Result for '{file_path}' file:\n{result}")


if __name__ == "__main__":
    main()