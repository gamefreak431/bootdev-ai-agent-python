from functions.run_python_file import run_python_file

def main():
    tests = [
        ("calculator", "main.py", None),
        ("calculator", "main.py", ["3 + 5"]),
        ("calculator", "tests.py", None),
        ("calculator", "../main.py", None),
        ("calculator", "nonexistent.py", None),
        ("calculator", "lorem.txt", None),
    ]

    for working_directory, file_path, args in tests:
        result = run_python_file(working_directory, file_path, args)
        print(result)


if __name__ == "__main__":
    main()