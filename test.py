from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.async_api import async_playwright
import re
import asyncio

# type1のテスト
async def type1(page):
    # ケース作成
    await page.locator(".col > .button-open").first.click()
    await page.locator(".py-0 > .v-input > .v-input__control > .v-input__slot").click()
    await page.locator(".py-0 > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("Type1_Case1")
    await page.get_by_role("button", name="作成", exact=True).click()
    await page.get_by_role("radiogroup").get_by_text("バリアフリートイレ").click()
    await page.get_by_role("button", name="次へ").click()
    await page.wait_for_load_state()
    # 空間選択画面
    await page.get_by_role("button", name="閉じる").click()
    await page.get_by_role("button", name="器具選択").click()
    await page.wait_for_load_state()
    # 器具選択画面
    await page.get_by_role("button", name="計算開始").click()
    await page.wait_for_selector("span.project-name")
    # 結果一覧画面
    await page.wait_for_selector(".row.v-image.v-responsive__content")
    await page.screenshot(path="結果一覧.png", full_page=True)
    await page.get_by_role("link", name="詳しく見る").first.click()
    await page.wait_for_load_state()
    # 詳細画面
    await page.wait_for_timeout(5000)
    await page.screenshot(path="詳細.png", full_page=True)
    await page.get_by_role("button", name="カートに追加").click()
    await page.get_by_role("link", name="カート Badge").click()
    await page.wait_for_load_state()
    # カート画面
    await page.get_by_role("button", name="データ出力").click()
    await page.locator("div:nth-child(11) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
    await page.locator("div:nth-child(12) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
    await page.locator("div:nth-child(13) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
    await page.locator("div:nth-child(14) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
    await page.locator("div:nth-child(15) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
    # ダウンロード
    async with page.expect_download() as download_info:
        await page.get_by_role("button", name="ダウンロード").click()
    download = await download_info.value
    await download.save_as("./downloaded/" + download.suggested_filename)
    # プロジェクト画面に戻る

async def input_type2(page, width, depth, door, doorPos, cl, la, num):
    await page.locator("div:nth-child(2) > .pa-2 > .row > div:nth-child(2) > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill(width)
    await page.locator("div:nth-child(3) > .pa-2 > .row > div:nth-child(2) > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill(depth)
    if door == False:
        await page.locator(".v-input--selection-controls__ripple").first.click()
    else:
        await page.locator("div:nth-child(3) > .v-radio > .v-input--selection-controls__input > .v-input--selection-controls__ripple").first.click()
    if doorPos == "left":
        await page.locator("div:nth-child(6) > .v-input__control > .v-input__slot > .v-input--radio-group__input > .row > div > .v-radio > .v-input--selection-controls__input > .v-input--selection-controls__ripple").first.click()
    else:
        await page.locator("div:nth-child(6) > .v-input__control > .v-input__slot > .v-input--radio-group__input > .row > div:nth-child(3) > .v-radio > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
    if cl == "wall":
        await page.locator("div:nth-child(2) > .pr-0 > .v-radio > .v-input--selection-controls__input > .v-input--selection-controls__ripple").first.click()
    else:    
        await page.locator("div:nth-child(2) > .row > .pr-0 > .v-radio > .v-input--selection-controls__input > .v-input--selection-controls__ripple").first.click()
    if la == "counter":
        await page.locator("div:nth-child(6) > .v-input__control > .v-input__slot > .v-input--radio-group__input > div > .row > .pr-0 > .v-radio > .v-input--selection-controls__input > .v-input--selection-controls__ripple").first.click()
    else:
        await page.locator("div:nth-child(6) > .v-input__control > .v-input__slot > .v-input--radio-group__input > div:nth-child(2) > .row > .pr-0 > .v-radio > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
    await page.locator("div:nth-child(3) > div > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill(num)

# type2のテスト
async def type2(page, width, depth, door, doorPos, cl, la, num, index):
    # ケース作成
    await page.locator(".col > .button-open").first.click()
    await page.locator(".py-0 > .v-input > .v-input__control > .v-input__slot").click()
    await page.locator(".py-0 > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("Type2_Case" + index)
    await page.get_by_role("button", name="作成", exact=True).click()
    await page.get_by_text("一般トイレ", exact=True).click()
    await page.get_by_role("button", name="次へ").click()
    await page.get_by_text("男性トイレ").click()
    await page.get_by_role("button", name="次へ").click()
    await page.wait_for_load_state()
    # 計算条件選択
    await input_type2(page, width, depth, door, doorPos, cl, la, num)
    await page.get_by_role("button", name="この条件で設計する").click()
    # 結果一覧画面
    await page.wait_for_selector("text=レイアウト計算条件")
    await page.wait_for_timeout(5000)
    await page.screenshot(path="./output/" + index + "/結果一覧.png", full_page=True)
    await page.get_by_role("link", name="プランを見る").first.click()
    await page.wait_for_load_state()
    # 詳細画面
    await page.wait_for_selector("#toolbar-fullscreenTool")
    await page.wait_for_timeout(5000)
    await page.screenshot(path="./output/" + index + "/詳細.png", full_page=True)
    await page.get_by_role("button", name="カートに追加").click()
    await page.get_by_role("link", name="カート Badge").click()
    await page.wait_for_load_state()
    # カート画面
    await page.get_by_role("button", name="データ出力").click()
    await page.locator("div:nth-child(11) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
    await page.locator("div:nth-child(12) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
    await page.locator("div:nth-child(13) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
    await page.locator("div:nth-child(14) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
    await page.locator("div:nth-child(15) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
    # ダウンロード
    async with page.expect_download() as download_info:
        await page.get_by_role("button", name="ダウンロード").click()
    download = await download_info.value
    await download.save_as("./output/"+ index + "/" + download.suggested_filename)
    # プロジェクト画面に戻る
    await page.get_by_role("link", name="プロジェクト").click()
    await page.wait_for_load_state()

async def calcurate(width, depth, door, doorPos, cl, la, num, index):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        # context = await browser.new_context()
        context = await browser.new_context(
            record_video_dir="./videos",
            record_video_size={"height": 768, "width": 1024},
        )
        page = await context.new_page()
        page.set_default_timeout(120000)
        # 認証画面
        await page.goto("https://dev-a-spec.lixil.com/")
        await page.wait_for_url("https://dev-a-spec.lixil.com/dev_authenticate/")
        await page.get_by_label("認証").click()
        await page.get_by_label("認証").fill("c9w$pDMciZT%")
        await page.get_by_label("認証").press("Enter")
        await page.wait_for_load_state()
        # TOP画面
        await page.locator("button").filter(has_text=re.compile(r"^JP$")).click()
        await page.get_by_role("button", name="設計を始める →").first.click()
        await page.get_by_role("link", name="同意して始める").click()
        await page.wait_for_load_state()
        # MyLIXIL
        await page.get_by_placeholder("メールアドレス").click()
        await page.get_by_placeholder("メールアドレス").fill("k36795284@gmail.com")
        await page.get_by_role("button", name="次へ").click()
        await page.locator("input[name=\"password\"]").click()
        await page.locator("input[name=\"password\"]").fill("1111_tkhr_1010")
        await page.get_by_role("button", name="次へ").click()
        await page.wait_for_load_state()
        # プロジェクト画面
        # プロジェクト作成
        await page.get_by_role("button", name="設計する").click()
        await page.get_by_role("button", name="次へ").click()
        await page.get_by_placeholder("プロジェクト名").click()
        await page.get_by_placeholder("プロジェクト名").fill("test_playwright")
        await page.get_by_placeholder("メモ欄").click()
        await page.get_by_placeholder("メモ欄").fill("test")
        await page.get_by_role("button", name="作成", exact=True).click()
        await page.wait_for_load_state()
        await type2(page, width, depth, door, doorPos, cl, la, num, index)

        # ---------------------
        await context.close()
        await browser.close()

async def main():
    task1 = asyncio.create_task(calcurate("7000", "3000", False, "right", "wall", "wall", "100", "1"))
    task2 = asyncio.create_task(calcurate("5000", "5000", True, "left", "floor", "counter", "200", "2"))
    task3 = asyncio.create_task(calcurate("4000", "7000", True, "left", "wall", "wall", "250", "3"))
    await task1
    await task2
    await task3

asyncio.run(main())