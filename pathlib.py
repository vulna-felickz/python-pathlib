# Python version: 3.9.19
# OS: GNU/Linux RHEL8 4.18.0-553.5.1.el8_10.x86_64
from pathlib import Path

# The storage path is defined internally by an environment variable; here is a placeholder
storage_path = Path("/path/to/where/files/are/stored")

# Define a function to validate the file path provided
def validate_file(file: Path) -> bool:
    file = Path(file) if isinstance(file, str) else file  # Pre-empt accidental string inputs
    file = file.resolve()  # Get full path for validation

    # Fail if file doesn't exist
    if not file.exists():
        return False

    # Use path to storage location as reference
    basepath = list(storage_path.parents)[-2]  # This can be made stricter eventually
    if str(file).startswith(str(basepath)):
        return True
    else:
        return False

# How it's used in the script
incoming_file = Path("some_file.txt")  # Can be partial path, or full path on system

if validate_file(incoming_file) is True:
    """
    Run code here to store the file in the database
    """
    return True
else:
    raise Exception("This file failed the validation check")
