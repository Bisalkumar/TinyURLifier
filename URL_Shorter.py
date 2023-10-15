import requests
import time
import pyperclip

def make_tiny(url):
    request_url = 'https://tinyurl.com/api-create.php'
    headers = {"User-Agent": "URLShortener/1.0"}
    response = requests.get(request_url, params={'url': url}, headers=headers, timeout=10)
    response.raise_for_status()  # Raises an HTTPError if one occurred
    return response.text

def main():
    while True:  # Infinite loop to keep asking the user for input
        url = input("Please enter a URL to shorten (or 'exit' to quit): ")

        if url.lower() == 'exit':
            print("Exiting program.")
            break

        try:
            tinyurl = make_tiny(url)
            print(f"{url} -> {tinyurl}")
            pyperclip.copy(tinyurl)
            print("Shortened URL has been copied to clipboard!")
            time.sleep(0.5)  # introduce a slight delay to be polite to the API
        except requests.HTTPError:
            print(f"HTTP error for {url}")
        except requests.ConnectionError:
            print(f"Connection error for {url}")
        except requests.Timeout:
            print(f"Timeout for {url}")
        except Exception as e:
            print(f"An unexpected error occurred for {url}: {e}")

if __name__ == '__main__':
    main()
