import allure
from playwright.sync_api import expect, sync_playwright

from login import login


def test_add_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        login(page)

        with allure.step("Check and validate number of cart icon"):
            expect(page.locator("span.bg-qa-clr")).not_to_be_visible()

        product_name = (
            page.locator("a[href^='/ecommerce/product-details']").nth(1).inner_text()
        )
        product_price = page.locator(
            "span.text-lg.font-bold.text-black"
        ).first.inner_text()

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

        with allure.step("Check and validate detail cart"):
            product_cart_name = page.locator(
                "h3.font-bold.font-oswald.text-lg"
            ).inner_text()
            assert product_name == product_cart_name

            product_cart_price = (
                page.locator("p.font-bold.font-oswald.text-lg").nth(0).inner_text()
            )
            assert product_price == product_cart_price

            product_cart_total_price = (
                page.locator("p.font-bold.font-oswald.text-lg").nth(1).inner_text()
            )

            assert product_cart_total_price == "$49.99"
