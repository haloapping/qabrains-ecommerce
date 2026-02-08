import allure
from playwright.sync_api import Page, expect

from login import login


def test_add_to_cart_and_checkout(page: Page):
    page.set_viewport_size({"width": 1920, "height": 1080})

    login(page)

    with allure.step("Check and validate current url"):
        expect(page).to_have_url("https://practice.qabrains.com/ecommerce")

    with allure.step("Check and validate number of cart icon"):
        expect(page.locator("span.bg-qa-clr")).not_to_be_visible()

    product_name = (
        page.locator("a[href^='/ecommerce/product-details']").nth(1).inner_text()
    )
    product_price = page.locator("span.text-lg.font-bold.text-black").first.inner_text()

    with allure.step("Check and validate Add to cart button"):
        expect(page.get_by_role("button", name="Add to cart").first).to_be_visible()
        expect(page.get_by_role("button", name="Add to cart").first).to_be_enabled()
        page.get_by_role("button", name="Add to cart").first.click()

    with allure.step("Check and validate number of cart icon"):
        expect(page.locator("span.bg-qa-clr")).to_be_visible()
        expect(page.locator("span.bg-qa-clr")).to_have_text("1")

    with allure.step("Check and validate cart icon"):
        expect(page.locator("span[role='button']").first).to_be_visible()
        expect(page.locator("span[role='button']").first).to_be_enabled()
        page.locator("span[role='button']").first.click()

    with allure.step("Check and validate current url"):
        expect(page).to_have_url("https://practice.qabrains.com/ecommerce/cart")

    with allure.step("Check and validate detail cart"):
        expect(page.locator("h3.font-bold.font-oswald.text-lg")).to_have_text(
            product_name
        )

        expect(page.locator("p.font-bold.font-oswald.text-lg").nth(0)).to_have_text(
            product_price
        )

        expect(page.locator("p.font-bold.font-oswald.text-lg").nth(1)).to_have_text(
            "$49.99"
        )

    with allure.step("Check and validate checkout button"):
        expect(page.get_by_role("button", name="Checkout")).to_be_visible()
        expect(page.get_by_role("button", name="Checkout")).to_be_enabled()
        page.get_by_role("button", name="Checkout").click()

    with allure.step("Check and validate checkout form"):
        expect(page.locator("div:nth-child(1) > label")).to_have_text("Email")
        expect(page.locator("div:nth-child(1) > input")).to_be_disabled()
        expect(page.locator("div:nth-child(1) > input")).to_have_value(
            "test@qabrains.com"
        )

        expect(page.locator("div:nth-child(2) > label")).to_have_text("First Name")
        expect(page.locator("div:nth-child(2) > input")).to_have_attribute(
            "placeholder", "Ex. John"
        )
        page.locator("div:nth-child(2) > input").fill("Jane")

        expect(page.locator("div:nth-child(3) > label")).to_have_text("Last Name")
        expect(page.locator("div:nth-child(3) > input")).to_have_attribute(
            "placeholder", "Ex. Doe"
        )
        page.locator("div:nth-child(3) > input").fill("Doe")

        expect(page.locator("div:nth-child(4) > label")).to_have_text("Zip Code")
        expect(page.locator("div:nth-child(4) > input")).to_have_value("1207")

        expect(page.get_by_role("button", name="Continue")).to_be_visible()
        expect(page.get_by_role("button", name="Continue")).to_be_enabled()
        page.get_by_role("button", name="Continue").click()
