import os

def read_file_tool(filePath: str):
    """
    Read files.
    """
    return file_tool("read", None, filePath)
    
def file_tool(operation: str, body: str, filePath: str):
    """
    Read or write files.
    """
    try:
        if operation == "read":
            with open(filePath, "r") as f:
                return f.read()
        elif operation == "write":
            with open(filePath, "w") as f:
                f.write(body)
                return f"File {filePath} written successfully"
        else:
            raise ValueError("Invalid operation")
    except Exception as e:
        return str(e)

def directory_write_tool(directory_path: str):
    """
    Create a directory.
    """
    try:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            return f"Directory '{directory_path}' has been created successfully."
        return f"Directory '{directory_path}' already exists."
    except Exception as e:
        return str(e)

def list_all_files(directory: str):
    """
    Recursively lists all files in the given directory.
    """
    file_list = []
    try:
        for root, _, files in os.walk(directory):
            for file in files:
                file_list.append(os.path.join(root, file))
    except Exception as e:
        return str(e)
    return file_list

def delete_file(file_path: str):
    """
    Deletes the specified file.
    """
    try:
        os.remove(file_path)
        return f"Deleted: {file_path}"
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except PermissionError:
        return f"Permission denied: {file_path}"
    except Exception as e:
        return f"Error deleting file {file_path}: {e}"
