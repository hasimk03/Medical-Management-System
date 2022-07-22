import requests
import json



def access_API():

    URL = "https://rapidapi.p.rapidapi.com/api/Search/WebSearchAPI"
    HEADERS = {
    'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
    'x-rapidapi-key': "Your-X-RapidAPI-Key"
    }

    query = "taylor swift"
    page_number = 1
    page_size = 10
    auto_correct = True
    safe_search = False

    querystring = {"q": query,
               "pageNumber": page_number,
               "pageSize": page_size,
               "autoCorrect": auto_correct,
               "safeSearch": safe_search}
    response = requests.get(URL, headers=HEADERS, params=querystring).json()

    print(response)

    total_count = response["totalCount"]

    for web_page in response["value"]:
        url = web_page["url"]
        title = web_page["title"]
        description = web_page["description"]
        body = web_page["body"]
        date_published = web_page["datePublished"]
        language = web_page["language"]
        is_safe = web_page["isSafe"]
        provider = web_page["provider"]["name"]
        print("Url: {}. Title: {}.".format(url, title))

def main():
    print("")
    access_API()



if __name__ == "__main__":
    main()