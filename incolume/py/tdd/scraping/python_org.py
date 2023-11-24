#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from pathlib import Path
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import platform


class PythonOrg:
    def __init__(self):
        self.url = 'http://127.0.0.1:8000/www.python.org/'
        os.environ[
            'MOZ_HEADLESS'
        ] = '1'  # faz webdriver executar em background
        self.firefox_desired_capabilities = DesiredCapabilities().FIREFOX
        # self.firefox_desired_capabilities['marionaette'] = (
        #     False if (platform.system().lower() == 'windows') else True
        # )
        try:
            self.firefoxbin = (
                Path(__file__)
                .parents[1]
                .joinpath('geckodrivers', 'geckodriver')
            )
        except FileNotFoundError:
            self.firefoxbin = (
                Path(__file__)
                .parents[1]
                .joinpath('geckodrivers', 'geckodriver.exe')
            )

        self.firefox = webdriver.Firefox(
            # capabilities=self.firefox_desired_capabilities,
            # executable_path=self.firefoxbin,
        )
        self._pythonorg = self.firefox.get(self.url)

    @property
    def pythonorg(self):
        return self._pythonorg

    @property
    def index_title_tagname(self):
        return self.firefox.find_element(
            by=By.TAG_NAME, value='title'
        ).tag_name

    @property
    def index_current_url(self):
        return self.firefox.current_url

    @property
    def index_page_content(self):
        return self.firefox.page_source

    def query_by_class_tier2_dict(self):
        query = self.firefox.find_elements(by=By.CLASS_NAME, value='tier-2')
        result = {
            elem.text: elem.find_element(
                by=By.TAG_NAME, value='a'
            ).get_attribute('href')
            for elem in query
            if elem.text
        }
        return result

    def webchat_freenode(self):
        query = self.firefox.find_element(
            by=By.XPATH,
            value='//*[@id="touchnav-wrapper"]/header/div/'
                  'div[1]/div/div[2]/ul/li/ul/li[3]/a',
        )
        chatonirc = query.get_attribute('href')
        self.firefox.get(chatonirc)
        result = self.firefox.find_element(
            by=By.PARTIAL_LINK_TEXT, value="freenode's webchat"
        )
        return result.get_attribute('href')


if __name__ == '__main__':
    pass
    p = PythonOrg()
    print(p.pythonorg.page_source)
