from typing import Any
from flask import Flask, jsonify

app = Flask(__name__)

def main() -> None:
    """main entry program function

        Args:
        Returns:
            None
    """
    app.run()

@app.route('/', methods=['GET'])
def v():
    return jsonify({'status': 200, 'message': 'ok'})

if __name__ == '__main__':
    main() # run main function