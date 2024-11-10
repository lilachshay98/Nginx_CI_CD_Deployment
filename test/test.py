import requests
from bs4 import BeautifulSoup

# constants
SERVER1_TITLE = "Welcome!"
SERVER1_BODY = "Hooray! You have successfully reached server 1"
SERVER2_TITLE = "Page Not Found"
SERVER2_BODY = "Oops! The page you are looking for could not be found on Server 2"


def check_server(url, expected_status, expected_title=None, expected_body_text=None):
    """
    A general test for the server which checks if the server responds with the expected
    status, title, and body text.
    Parameters:
    - url (str): The URL to check.
    - expected_status (int): The expected HTTP status code.
    - expected_title (str, optional): The expected text in the <title> tag.
    - expected_body_text (str, optional): The expected text in the <body> tag.

    Returns:
    - bool: True if all checks pass, False otherwise.
    """
    try:
        response = requests.get(url)
        assert response.status_code == expected_status

        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Check <title> tag content
        if expected_title:
            assert soup.title and expected_title in soup.title.string, \
                f"Title '{soup.title.string}' does not match expected '{expected_title}'"

        # Check <body> text content
        if expected_body_text:
            body_text = soup.body.get_text(strip=True)
            assert expected_body_text in body_text, f"Body text does not contain expected '{expected_body_text}'"

        print(f"{url} passed.")
        return True
    except (AssertionError, requests.exceptions.RequestException) as e:
        print(f"{url} failed: {e}")
        return False


def check_response_time(url, max_response_time=1):
    """
        Checks if the server at the given URL responds within the specified time limit.
        Parameters:
        - url (str): The URL of the server to check.
        - max_response_time (float): The maximum allowed response time in seconds.

        Returns:
        - bool: True if the server responded within the time limit, False otherwise.
        """
    try:
        # Send a request to the server with a specified timeout (default unless specified)
        response = requests.get(url, timeout=max_response_time)
        print(f"{url} responded in {response.elapsed.total_seconds()} seconds.")
        return True
    except requests.exceptions.Timeout:
        # If the server did not respond within the timeout, print an error message
        print(f"{url} failed due to timeout (>{max_response_time} seconds).")
        return False


def main():
    server1_status_text = check_server("http://nginx_container:8080", 200, SERVER1_TITLE, SERVER1_BODY)
    server1_response_time = check_response_time("http://nginx_container:8080")
    server2_status_text = check_server("http://nginx_container:8081", 404, SERVER2_TITLE, SERVER2_BODY)
    server2_response_time = check_response_time("http://nginx_container:8081")

    all_tests_passed = all([server1_status_text, server1_response_time, server2_status_text, server2_response_time])

    if all_tests_passed:
        with open("/output/succeeded", "w") as f:
            f.write("succeeded")
    else:
        with open("/output/fail", "w") as f:
            f.write("fail")


if __name__ == "__main__":
    main()
