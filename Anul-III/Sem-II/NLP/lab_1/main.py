import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

BASE_LINK = 'https://www.imdb.com/'
TOP_CHART_LINK = BASE_LINK + 'chart/top/'
REVIEW_LINK = BASE_LINK + 'title/{}/reviews/_ajax?paginationKey={}'


def get_top_movies():
    try:
        main_page = urlopen(TOP_CHART_LINK).read()
        soup_search = BeautifulSoup(main_page, 'html.parser')
        top_table = soup_search.select_one('table[data-caller-name] tbody')
        top_elements = top_table.find_all('tr')

        top_list = []
        for top_element in top_elements:
            title_element = top_element.select_one('.titleColumn').a
            title = title_element.text
            external_id = title_element['href'].split('/title/')[1].split('/')[0]
            # print(title, external_id)

            rating_element = top_element.select_one('.ratingColumn.imdbRating').strong
            rating_description = rating_element['title']
            rating_value = float(rating_element.text)
            # print(rating_description, rating_value)

            top_list.append({
                'title': title,
                'id': external_id,
                'description': rating_description,
                'rating': rating_value
            })

        # search for top250movies
        return top_list

    except Exception as e:
        print(e.args)


# make this a generator by yielding a page from the server to a dict
def get_movie_reviews(movie_id):
    print('enter in the get movie reviews')
    user_review_list = []
    pagination = ''
    while True:
        try:
            review_page = urlopen(REVIEW_LINK.format(movie_id, pagination)).read()
            soup_search = BeautifulSoup(review_page, 'html.parser')
            review_list = soup_search.select('div.lister-list > div.lister-item')
            pagination = soup_search.select_one('div.load-more-data')['data-key']

            if pagination:
                print(pagination)
            else:
                print('There is no pagination available')
        except Exception as e:
            print(e.args)
            for review_element in review_list:
                print('review_element')
                # print('Processing')
                review_id = review_element['data-review-id']
                review_link = review_element.a['href']
                review_value = review_element.select_one('span.rating-other-user-rating > span')
                review_value = int(review_value.text) if review_value is not None else None
                review_title = review_element.a.text.strip()

                username_reviewer = review_element.select_one('span.display-name-link').a.text.strip()
                date = review_element.select_one('span.review-date').text

                review_text = review_element.select_one('div.text.show-more__control')
                review_text = review_text.text if review_text is not None else None

                # print(review_id, review_link, review_value, review_title, username_reviewer, date)
                # print('\n\n\n')
                user_review_list.append({
                    'id': review_id,
                    'link': review_link,
                    'value': review_value,
                    'title': review_title,
                    'username': username_reviewer,
                    'date': date,
                    # 'text': review_text
                })

            return user_review_list


def get_movies_review(movie_id_list):
    # for movie_id in movie_id_list:
    #     yield get_movie_reviews(movie_id)
    #     print(movie_id, 'done')
    get_movie_reviews(movie_id_list[0])
    print(movie_id_list[0], 'done')


top_movies_list = get_top_movies()
# for movie in top_movies_list:
#     print(movie)
# for element in get_movies_review([top_movie['id'] for top_movie in top_movies_list]):
#     print(element)

get_movies_review([top_movie['id'] for top_movie in top_movies_list])

