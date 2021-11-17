import streamlit
from core import BitlyUrlShortner
import os
import dotenv


def main():
    """
    This is the main function.
    """
    streamlit.title("URL SHORTNER")
    dotenv.load_dotenv()
    short_url()


def short_url():
    """
    This is the short url function.
    """
    streamlit.subheader("Shorten URL")
    url = streamlit.text_input("Enter URL")
    if url and url.startswith("http"):
        streamlit.write(
            # Use your own API key from bitly.com
            BitlyUrlShortner(url=url, api_key=os.environ.get("API_KEY")).short_url()
        )
    else:
        streamlit.write("Please enter a valid URL")


if __name__ == "__main__":
    main()
