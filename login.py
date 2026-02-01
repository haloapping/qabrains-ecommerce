from playwright.sync_api import Page


def login(page: Page):
    page.goto("https://practice.qabrains.com/ecommerce/login")
    page.fill(selector="#email", value="test@qabrains.com")
    page.fill(selector="#password", value="Password123")
    page.click(selector="button[type='submit']")
