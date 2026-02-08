import allure
from faker import Faker
from playwright.sync_api import Page, expect

from login import login


@allure.title("Login valid")
@allure.tag("Login")
def test_login_valid(page: Page):
    page.set_viewport_size({"width": 1920, "height": 1080})

    login(page)

    with allure.step("Open browser"):
        page.goto("https://practice.qabrains.com/ecommerce/login")

    with allure.step("Check and validate email field"):
        expect(page.locator("#email")).to_be_visible()
        expect(page.locator("#email")).to_be_enabled()
        page.fill(selector="#email", value="test@qabrains.com")

    with allure.step("Check and validate password field"):
        expect(page.locator("#password")).to_be_visible()
        expect(page.locator("#password")).to_be_enabled()
        page.fill(selector="#password", value="Password123")

    login_page_bytes = page.screenshot()
    allure.attach(
        login_page_bytes,
        name="login valid page",
        attachment_type=allure.attachment_type.PNG,
    )

    with allure.step("Check and validate login button"):
        expect(page.locator("button[type='submit']")).to_be_visible()
        expect(page.locator("button[type='submit']")).to_be_enabled()
        page.click(selector="button[type='submit']")


@allure.title("Login invalid")
@allure.tag("Login")
def test_login_invalid(page: Page):
    page.set_viewport_size({"width": 1920, "height": 1080})

    login(page)

    with allure.step("Open browser"):
        page.goto("https://practice.qabrains.com/ecommerce/login")

    with allure.step("Create fake data"):
        faker = Faker()

    with allure.step("Check and validate email field"):
        expect(page.locator("#email")).to_be_visible()
        expect(page.locator("#email")).to_be_enabled()
        page.fill(selector="#email", value=faker.email())

    with allure.step("Check and validate password field"):
        expect(page.locator("#password")).to_be_visible()
        expect(page.locator("#password")).to_be_enabled()
        page.fill(selector="#password", value=faker.password(8, True, True, True, True))

    with allure.step("Check and validate login button"):
        expect(page.locator("button[type='submit']")).to_be_visible()
        expect(page.locator("button[type='submit']")).to_be_enabled()
        page.click(selector="button[type='submit']")

    with allure.step("Check and validate notification invalid"):
        expect(
            page.locator(
                "body > div.ecommerce-auth-layout > div > div > div > form > div > div:nth-child(1) > p"
            )
        ).to_have_text("Username is incorrect.")

        expect(
            page.locator(
                "body > div.ecommerce-auth-layout > div > div > div > form > div > div:nth-child(2) > p"
            )
        ).to_have_text("Password is incorrect.")

        expect(page.locator("body > section > ol > li")).to_have_text(
            "Neither email nor password matched."
        )

    login_page_bytes = page.screenshot()
    allure.attach(
        login_page_bytes,
        name="login invalid page",
        attachment_type=allure.attachment_type.PNG,
    )
