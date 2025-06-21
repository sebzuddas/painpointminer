import requests

def elevenlabs_tts(text):
    # Call ElevenLabs API here
    response = requests.post("https://api.elevenlabs.io/...", data={"text": text})
    return response.json

def run_langflow(input_value: str) -> dict:
    url = "http://localhost:7868/api/v1/run/ad33df2b-888e-4251-9b36-dbf4f4e54160"
    payload = {
        "input_value": input_value,
        "output_type": "chat",
        "input_type": "chat"
    }
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    except ValueError as e:
        return {"error": f"Error parsing response: {e}"}

