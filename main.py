from bs4 import BeautifulSoup  # для парсинга полученного кода
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from requests import get  # для получения html-кода
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import threading

GUN_VANS_URL = 'https://gtalens.com/map/gun-vans'
VANS_COUNT = 30


class Van:
    def __init__(self):
        response = get(GUN_VANS_URL)
        self.van_html = BeautifulSoup(response.text, 'html.parser')
        self.van_location = 'None'

    def get_van_assortment(self):
        van_sales = self.van_html.find('div', class_="content mx-3 mt-3 text-xs").get_text(separator='\n')
        print(van_sales)
        return van_sales

    def get_van_location(self):
        vans = self.van_html.find('div', class_=f'text-sm text-white').get_text().replace(' ', '').replace('\n', ' ')
        print(vans)
        print(threading.current_thread())
        self.van_location = vans
        return vans


van = Van()


class VanScreen(MDScreen):
    vans = van.get_van_location()
    source = f'img\\{vans.split()[0]}.png'


class MainScreen(MDScreen):
    pass


class DealersScreen(MDScreen):
    pass


class GtaHelperApp(MDApp):

    def build(self):
        sm = MDScreenManager(transition=FadeTransition())
        sm.add_widget(VanScreen(name='van_screen'))
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(DealersScreen(name='dealers_screen'))
        return sm


if __name__ == '__main__':
    GtaHelperApp().run()
