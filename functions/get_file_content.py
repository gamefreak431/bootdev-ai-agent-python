import os
from constants import MAX_CHARS
from google.genai import types


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves the content of a specified file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to retrieve content from, relative to the working directory",
            ),
        },
    ),
)

def get_file_content(working_directory: str, file_path: str) -> str:
    working_directory = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_directory, file_path))
    try:
        valid_target_file = os.path.commonpath([working_directory, target_file]) == working_directory
    except ValueError as e:
        return f'Error: valid_target_file - {str(e)}'
    if not valid_target_file:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    with open(target_file, 'r') as f:
        content = f.read(MAX_CHARS)
        if f.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    return content