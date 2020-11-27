# Simpsons ImDB link
# https://www.imdb.com/title/tt0096697/episodes?season=1

from requests import get
from bs4 import BeautifulSoup
import pandas as pd

#print(episode_containers[0].a['title']) # Title
#print(episode_containers[0].meta['content']) # Episode Number
#print(episode_containers[0].find('div', class_='airdate').text.strip()) # Air Date
#print(episode_containers[0].find('span', class_='ipl-rating-star__rating').text) # Episode Rating
#print(episode_containers[0].find('span', class_='ipl-rating-star__total-votes').text) # Total No. Of Votes
#print(episode_containers[0].find('div', class_='item_description').text.strip()) # Episode Description

# Initializing the series that the loop will populate
simpsons_episodes = []

# For every season in the series-- range depends on the show
for sn in range(1,2):
    # Request from the server the content of the web page by using get(), and store the server’s response in the variable response
    response = get('https://www.imdb.com/title/tt0096697/episodes?season=' + str(sn))

    # Parse the content of the request with BeautifulSoup
    page_html = BeautifulSoup(response.text, 'html.parser')

    # Select all the episode containers from the season's page
    episode_containers = page_html.find_all('div', class_='info')

    # For each episode in each season
    for episodes in episode_containers:
            # Get the info of each episode on the page
            season = sn
            episode_number = episodes.meta['content']
            title = episodes.a['title']
            airdate = episodes.find('div', class_='airdate').text.strip()
            rating = episodes.find('span', class_='ipl-rating-star__rating').text
            total_votes = episodes.find('span', class_='ipl-rating-star__total-votes').text
            desc = episodes.find('div', class_='item_description').text.strip()
            # Compiling the episode info
            episode_data = [season, episode_number, title, airdate, rating, total_votes, desc]

            # Append the episode info to the complete dataset
            simpsons_episodes.append(episode_data)


#simpsons_episodes = pd.DataFrame(simpsons_episodes, columns=['season', 'episode_no', 'title', 'airdate', 'rating',
#                                                             'total_votes', 'desc'])
print(simpsons_episodes)
simpsons_episodes.to_pickle("./simpsons_episodes.pkl")