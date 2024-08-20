from pathlib import Path
from flask import Flask, request

app = Flask(__name__)

storage_path = Path("/path/to/where/files/are/stored")

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

@app.route('/validate', methods=['GET'])
def validate():
    incoming_file = request.args.get('file')
    if incoming_file:
        incoming_file = Path(incoming_file)
        if validate_file(incoming_file) is True:
            # Run code here to store the file in the database
            return "File is valid", 200
        else:
            return "This file failed the validation check", 400
    else:
        return "No file path provided", 400

if __name__ == "__main__":
    app.run()
