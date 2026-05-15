import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    working_directory = os.path.abspath(working_directory)
    target_path = os.path.normpath(os.path.join(working_directory, file_path))
    try:
        valid_target_path = os.path.commonpath([working_directory, target_path]) == working_directory
    except ValueError as e:
        return f'Error: valid_target_path - {str(e)}'
    if not valid_target_path:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(target_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    os.makedirs(os.path.dirname(target_path), exist_ok=True)

    with open(target_path, 'w') as f:
        f.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'