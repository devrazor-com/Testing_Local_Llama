import requests

# Define the API endpoint of the local server
api_url = "http://localhost:11434/api/chat"

# Define the payload with the model name specified
payload = {
    "model": "llama3.1",
    "messages": [
        {"role": "user", "content": "What the capital city of Canada?"}
    ],
    "stream": False
}
headers = {
    "Content-Type": "application/json"
}

# Make the request to the local server
response = requests.post(api_url, json=payload, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Print the response from the server
    print(response.json())
else:
    # Print an error message
    print(f"Error: {response.status_code}, Message: {response.text}")
