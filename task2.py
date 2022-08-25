from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import re
import networkx as nx
import matplotlib.pyplot as plt
import time
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np

#Installerer webdriver, som gjør det mulig for koden og bruke javascripts i en nettleser
driver = webdriver.Chrome(ChromeDriverManager().install())

# Scroller ned i nettleseren
def scrolldown():
    for i in range(30):
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(.3)

# Får koden til å vente til den har samlet alle hashtags på nettsiden
def wait():
    WebDriverWait(driver, 40).until(
        EC.presence_of_all_elements_located(
            #Xpath utrykk for å finne hashtags på twitter
            (By.XPATH, "//div[@class='css-1dbjc4n r-16y2uox r-1wbh5a2 r-1ny4l3l']")
        ))

def findHashtags(initial_tag, steps, G):
    initial_tag = initial_tag.lower()
    #Lager en kø som inneholder neste hashtag som skal besøkes
    queue = [initial_tag]

    visited_tags = set()
    visited_tags.add(initial_tag)
    G.add_node(initial_tag)
    
    while len(visited_tags) < steps:
        # Velger første hashtag i køen og åpner twitter siden for den taggen
        current_tag = queue.pop(0).lower()
        visited_tags.add(current_tag)
        url = f'https://twitter.com/hashtag/{current_tag}?src=hashtag_click'
        driver.get(url)

        wait()
        scrolldown()

        # Samler alle tags på siden
        bs = BeautifulSoup(driver.page_source, 'html.parser')
        hashtags = bs.find_all('a', {'href': re.compile('\/hashtag\/.*')})

        # Legger alle tags inn i køen hvis den ikke er besøkt allerede
        for i in range(len(hashtags)):
            if i > 20: break
            stripped_tag = hashtags[i].text.lstrip('#').lower()
            G.add_edge(current_tag, stripped_tag)
            if stripped_tag not in visited_tags:
                queue.append(stripped_tag)
                

def main():
    G = nx.Graph()
    #Færre steps gir kortere kjøretid, men mindre fullstendig graf
    steps = 5
    # Verdiene kan byttes ut hvis det er ønskelig å starte på andre hashtags
    startNode1 = "USA"
    startNode2 = "Norway"
    findHashtags(startNode1, steps, G)
    findHashtags(startNode2, steps, G)

    #Resizes nodes based on degree, just for visuals
    size_nodes = np.asarray([G.degree()[n]*100 for n in G.nodes()])
    
    options = {
        "with_labels": True,
        "node_size": size_nodes,
    }

    name = "graphNetwork"
    nx.write_graphml(G, f"{name}.graphml")
    
    nx.draw(G, **options)
    plt.show()
    driver.quit()

if __name__ == "__main__":
    main()