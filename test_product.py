import time

import allure
from playwright.sync_api import expect, Browser

from login import login


@allure.testcase("Product card")
@allure.title("All Products Displayed")
@allure.tag("Product")
def test_product_card(browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})

    login(page)

    with allure.step("Check and validate current url"):
        expect(page).to_have_url("https://practice.qabrains.com/ecommerce")

    with allure.step("Check and validate button favourite"):
        expect(page.locator("button:has(svg)").nth(2)).to_be_visible()
        expect(page.locator("button:has(svg)").nth(2)).to_be_enabled()

        page.locator("button:has(svg)").nth(2).click()
        expect(page.locator("ol > li")).to_be_visible()
        expect(page.locator("ol > li")).to_have_text("Added to favorites")

        time.sleep(5)

        page.locator("button:has(svg)").nth(2).click()
        expect(page.locator("ol > li")).to_be_visible()
        expect(page.locator("ol > li")).to_have_text("Removed from favorites")

    with allure.step("Check image link is clickable"):
        expect(
            page.locator("a[href='/ecommerce/product-details?id=1']").nth(0)
        ).to_be_visible()
        expect(
            page.locator("a[href='/ecommerce/product-details?id=1']").nth(0)
        ).to_be_enabled()
        page.locator("a[href='/ecommerce/product-details?id=1']").nth(0).click()

    with allure.step("Check image visible"):
        expect(page.locator("img[alt='Sample Shirt Name']")).to_be_visible()

    with allure.step("Check product name visible"):
        expect(
            page.locator("a[href='/ecommerce/product-details?id=1']").nth(1)
        ).to_be_visible()

    with allure.step("Check short description product visible"):
        expect(
            page.locator("a[href='/ecommerce/product-details?id=1']").nth(2)
        ).to_be_visible()

    with allure.step("Check price product visible"):
        expect(page.locator("text=$49.99")).to_have_text("$49.99")

    with allure.step("Check price product visible"):
        expect(page.locator("text=$49.99")).to_have_text("$49.99")

    with allure.step("Check price product visible"):
        expect(page.get_by_role("button", name="Add to cart").first).to_have_text(
            "Add to cart"
        )
        expect(page.get_by_role("button", name="Add to cart").first).to_be_visible()
        expect(page.get_by_role("button", name="Add to cart").first).to_be_enabled()
