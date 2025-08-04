import sys
import os
import time
import pytest
import json
import uuid
from playwright.sync_api import sync_playwright, expect
from datetime import datetime, timedelta
from pages.base_page import BasePage
from pages.front_page import FrontPage

def test_homepage(page):
    home = FrontPage(page)
    # base = BasePage(page)
    home.goto_home()
    expect(page).to_have_title("STORE")
    home.screenshot("screenshots/test_screenshot_home.jpg")

def test_menu(page):
    home = FrontPage(page)
    home.goto_home()
    home.home_button.click()
    home.screenshot("screenshots/test_screenshot_menu_home.jpg")
    home.contact_button.click()
    home.screenshot("screenshots/test_screenshot_menu_contact.jpg")
    home.contact_close_button.click()
    home.about_button.click()
    home.screenshot("screenshots/test_screenshot_menu_about.jpg")
    home.close_about_button.click()
    home.cart_button.click()
    home.screenshot("screenshots/test_screenshot_menu_cart.jpg")
    home.login_button.click()
    home.screenshot("screenshots/test_screenshot_menu_login.jpg")
    home.close_login_button.click()
    home.signup_button.click()
    home.screenshot("screenshots/test_screenshot_menu_signup.jpg")
    home.close_signup_button.click()