# import flask module
import logging

from flask import Flask, request, abort

import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def alertmanager_webhook():
    """
    Endpoint to receive webhooks from Alertmanager.
    Prints the payload to stdout.
    """
    if not request.is_json:
        logger.warning("Received request without 'application/json' content type.")
        abort(400, "Bad Request: Expected JSON payload")

    try:
        # Get the JSON payload
        payload = request.get_json()

        # Print the entire payload to STDOUT
        logger.info("===== ALERTMANAGER WEBHOOK RECEIVED =====")
        print(payload)
        logger.info("=========================================")

        # Respond to Alertmanager
        return "Webhook received successfully", 200

    except Exception as e:
        logger.error(f"Error processing webhook: {e}")
        abort(500, "Internal Server Error")

# run the application
if __name__ == "__main__":
    port = int(os.environ.get("FLASK_PORT", 5000))
    app.run(host='0.0.0.0', port=port)
