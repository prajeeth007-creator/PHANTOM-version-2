import requests

def search_github(query):
    url = f"https://api.github.com/search/repositories?q={query}"

    try:
        response = requests.get(url)
        data = response.json()

        results = []
        for repo in data["items"][:5]:
            results.append(repo["full_name"])

        return results

    except Exception as e:
        return [f"GitHub search failed: {str(e)}"]