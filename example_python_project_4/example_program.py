
import click
import idna
import requests

@click.command()
@click.option("--domain", prompt="Enter a domain", help="Domain name to test with IDNA encoding")
def check_domain(domain):
    # Using IDNA 3.x encoding (feature not available in older IDNA)
    ascii_domain = idna.encode(domain, uts46=True).decode()
    print(f"Encoded domain: {ascii_domain}")

    # Simple HTTP GET using requests 2.22.0
    print("Making a request...")
    try:
        response = requests.get(f"https://{ascii_domain}")
        print("Status code:", response.status_code)
    except Exception as e:
        print("Error during request:", e)

if __name__ == "__main__":
    check_domain()