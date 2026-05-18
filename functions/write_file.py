import os
from google.genai import types


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write to, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file. Omit or leave empty to create a blank file.",
            )
        },
    ),
)

def write_file(working_directory: str, file_path: str, content: str="") -> str:
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