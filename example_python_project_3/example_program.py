from googlesearch import search

def main():
    query = "Python dependency conflicts"
    print(f"Searching for: {query}")
    for i, result in enumerate(search(query, num_results=5), start=1):
        print(f"{i}. {result}")

if __name__ == "__main__":
    main()
