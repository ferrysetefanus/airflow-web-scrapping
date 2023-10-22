# import semua library yang dibutuhkan
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import re
import psycopg2
from sqlalchemy import create_engine


driver = webdriver.Chrome()


url = "https://www.youtube.com/results?search_query=teori+konspirasi"
driver.get(url)









