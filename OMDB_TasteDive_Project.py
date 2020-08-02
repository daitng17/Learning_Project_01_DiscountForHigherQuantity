import requests


def get_movies_from_tastedive(movie):
    baseurl = "https://tastedive.com/api/similar"
    para = {"q": movie, "type": "movies", "limit": "5"}
    res = requests.get(baseurl, params=para)
    movie_list = res.json()
    return movie_list


def extract_movie_titles(dict):
    movie_title = [name.values() for name in dict["Similar"]["Results"]]
    return movie_title


def get_related_titles(lst):
    combined_lst = []
    for i in lst:
        for title in extract_movie_titles(get_movies_from_tastedive(i)):
            if title not in combined_lst:
                combined_lst.append(title)
    return combined_lst


def get_movie_data(movie):
    baseurl = "http://www.omdbapi.com/"
    para = {"t": movie, "r": "json"}
    res = requests.get(baseurl, params=para)
    return res.json()


def get_movie_rating(dict):
    rating = 0
    for source in dict["Ratings"]:
        print(source.values())
        if "Rotten Tomatoes" == source.values()[0]:
            rating += int(source.values()[1][:-1])
    return rating


def get_sorted_recommendations(lst):
    output = []
    # output_dict = {}
    for i in get_related_titles(lst):
        output.append(i)
        # output_dict.
    return output  # key=get_movie_rating(get_movie_data(i)), reverse = True)


test = get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

print(test)