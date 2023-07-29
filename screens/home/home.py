from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivy.lang import Builder

from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='a8f0c27e0bb945638e37a95015c0c923')


class home(Screen):
    Builder.load_file("C:/Users/agust/OneDrive/Documentos/olraNews/tutorial-env/screens/home/home.kv")
    
    def __init__(self, **kw):
        super().__init__(**kw)

        olraTitle = MDLabel(
            text="Olra News",
            font_name= "C:/Users/agust/OneDrive/Documentos/olraNews/tutorial-env/fonts/Poppins/Poppins-Bold.ttf",
            pos_hint= {"center_y":.95},
            halign="center",
            font_style="H5",
            bold = True
        )

        self.ids.news_recent.add_widget(olraTitle)

        # /v2/everything
        all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
        
        print(all_articles)
        
        sources = newsapi.get_sources()

        print(sources)
        