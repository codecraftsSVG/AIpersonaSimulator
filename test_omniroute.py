import httpx

api_key = "sk-2579f09f764b7a65-b159f0-2e5bb2"
base_url = "http://localhost:20128/v1"

def test_omniroute():
    try:
        endpoint = f"{base_url.rstrip('/')}/chat/completions"
        print(f"Testing Omniroute connection at {endpoint}...")
        with httpx.Client(timeout=15.0) as client:
            resp = client.post(
                endpoint,
                headers={"Authorization": f"Bearer {api_key}"},
                json={
                    "model": "auto",
                    "messages": [
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": "Say hello!"}
                    ],
                    "temperature": 0.7,
                    "max_tokens": 50
                }
            )
            print("Response status code:", resp.status_code)
            print("Response text:", resp.text)
    except Exception as e:
        print("Error connecting to Omniroute:", e)

if __name__ == "__main__":
    test_omniroute()
