import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

def get_files_info(working_directory: str, directory: str = ".") -> str:  
    working_directory = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_directory, directory))
    try:
        valid_target_dir = os.path.commonpath([working_directory, target_dir]) == working_directory
    except ValueError as e:
        return f'Error: valid_target_dir - {str(e)}'
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{target_dir}" is not a directory'
    
    dir_info = []
    for dir in os.listdir(target_dir):
        dir_path = os.path.join(target_dir, dir)
        try:
            size = os.path.getsize(dir_path)
        except OSError as e:
            return f'Error: size - "{dir_path}": {str(e)}'
        is_dir = os.path.isdir(dir_path)
        dir_info.append(f'- {dir}: file_size={size} bytes, is_dir={is_dir}')
    
    return '\n'.join(dir_info)