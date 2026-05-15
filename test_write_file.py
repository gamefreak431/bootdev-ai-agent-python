from functions.write_file import write_file

def main():
    tests = [
        ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
        ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
        ("calculator", "/tmp/temp.txt", "this should not be allowed"),
    ]

    for working_directory, file_path, content in tests:
        result = write_file(working_directory, file_path, content)
        print(result)


if __name__ == "__main__":
    main()