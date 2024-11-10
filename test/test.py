
import requests


def check_server(url, expected_status, expected_text=None):
    try:
        response = requests.get(url)
        assert response.status_code == expected_status
        if expected_text:
            assert expected_text in response.text
        print(f"{url} passed.")
        return True
    except AssertionError:
        print(f"{url} failed.")
        return False


def check_response_time(url, max_response_time=1):
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
    server1_status_text = check_server("http://nginx_container:8080", 200, "Welcome to Server 1")
    server1_response_time = check_response_time("http://nginx_container:8080")
    server2_status_text = check_server("http://nginx_container:8081", 404, "Page Not Found")
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
