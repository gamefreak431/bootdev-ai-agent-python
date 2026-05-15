import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args=None):
    working_directory = os.path.abspath(working_directory)
    target_path = os.path.normpath(os.path.join(working_directory, file_path))
    try:
        valid_target_path = os.path.commonpath([working_directory, target_path]) == working_directory
    except ValueError as e:
        return f'Error: valid_target_path - {str(e)}'
    if not valid_target_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_path):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file'
    
    command = ["python", target_path]
    if args:
        command.extend(args)

    try:
        result = subprocess.run(command, cwd=working_directory, capture_output=True, text=True, timeout=30)
    except subprocess.TimeoutExpired:
        return f'Error: "{file_path}" timed out after 30 seconds'
    if result.returncode != 0:
        return f"Process exited with code {result.returncode}"
    if not result.stdout and not result.stderr:
        return f"Process exited with code {result.returncode} No output produced"
    return f'STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}'