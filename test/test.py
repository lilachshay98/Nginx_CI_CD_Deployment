
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


def main():
    server1 = check_server("http://nginx_container:8080", 200, "Welcome to Server 1")
    server2 = check_server("http://nginx_container:8081", 404, "Page Not Found")
    
    if server1 and server2:
        with open("/output/succeeded", "w") as f:
            f.write("succeeded")
    else:
        with open("/output/fail", "w") as f:
            f.write("fail")


if __name__ == "__main__":
    main()
