from oauthlib.oauth2 import WebApplicationClient

def main():
    # Simple OAuth2 client setup
    client_id = "demo-client-id"
    client = WebApplicationClient(client_id)
    print("OAuthLib client created successfully:", client.client_id)

if __name__ == "__main__":
    main()
