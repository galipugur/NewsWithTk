import tkinter as tk
import requests
from bs4 import BeautifulSoup

target_url = "https://news.ycombinator.com"
news_list = []

def make_request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def get_news_link(url):
    links = make_request(url)
    for link in links.find_all("a"):
        news_link = link.get("href")
        if news_link:
            if "http" in news_link:
                news_list.append(news_link)
                #print(news_link)
    return news_list

def news_button():
    for news in get_news_link(target_url):
        news_text.insert(tk.END, news + "\n")

#window
window = tk.Tk()
window.title("Hacker News")
window.config(background="light blue")
window.minsize(width=500, height=600)

#label
title_label = tk.Label(text="HERE NEW NEWS")
title_label.config(bg="black", fg="White", font=("Arial",15,"bold"))
title_label.pack(padx=5, pady=5)

#button
get_news_button = tk.Button(text="Press for News", command=news_button)
get_news_button.pack(padx=5, pady=5)

#text
news_text = tk.Text(width=50, height=35)
news_text.pack(padx=10, pady=10)



#get_news_link(target_url)

window.mainloop()