import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    
    working_directory = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_directory, directory))
    try:
        valid_target_dir = os.path.commonpath([working_directory, target_dir]) == working_directory
    except ValueError as e:
        return f'Error: {str(e)}'


    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    return f'Success: "{directory}" is within the working directory'