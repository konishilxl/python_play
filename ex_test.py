from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.async_api import async_playwright
import re
import asyncio
import csv
import time

# type1_standardのテスト
async def type1_standard(page, cltype, clseries, cllining, hr, aw, lhr, lhrlining, la, lalining, hd, uset, us, os, index):
    # ケース作成
    await page.locator(".col > .button-open").first.click()
    await page.locator(".py-0 > .v-input > .v-input__control > .v-input__slot").click()
    await page.locator(".py-0 > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("Type1_Case" + index)
    await page.get_by_role("button", name="作成", exact=True).click()
    await page.get_by_role("radiogroup").get_by_text("バリアフリートイレ").click()
    await page.get_by_role("button", name="次へ").click()
    await page.wait_for_load_state()
    # 空間選択画面
    await page.get_by_role("button", name="閉じる").click()
    # 間口
    await page.locator("div:nth-child(1) > .row > .col > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("3500")
    # 奥行き
    await page.locator("div:nth-child(2) > .row > .col > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("3500")
    # 有効開口
    await page.get_by_role("button", name="900").click()
    await page.get_by_text("850").click()
    # 入口位置
    await page.locator("div").filter(has_text=re.compile(r"^R$")).locator("div").nth(1).click()
    # 扉種類
    await page.get_by_role("button", name="片引き戸").click()
    await page.get_by_text("引き込み戸").click()
    # 空間選択完了
    await page.get_by_role("button", name="器具選択").click()
    await page.wait_for_load_state()
    ## 器具選択画面
    # 大便器タイプ
    await page.get_by_role("button", name="壁掛け").click()
    await page.get_by_role("option", name="床置き").click()
    await page.get_by_role("button", name="床置き").click()
    if cltype == "wall":
        await page.get_by_role("option", name="壁掛け").click()
    elif cltype == "floor":
        await page.get_by_role("option", name="床置き").click()
    # 大便器シリーズ
    await page.get_by_role("button", name="シリーズ").click()
    if clseries == "pub_hl":
        await page.get_by_role("option", name="パブリック向け壁掛便器 HL").click()
    elif clseries == "pub":
        await page.get_by_role("option", name="パブリック向け壁掛便器", exact=True).click()
    elif clseries == "quickwall":
        await page.get_by_role("option", name="クイックタンク式壁掛便器").click()
    elif clseries == "western":
        await page.get_by_role("option", name="壁掛式洋風便器").click()
    elif clseries == "wheel1":
        await page.get_by_role("option", name="車いす対応便器").first.click()
    elif clseries == "wheel2":
        await page.get_by_role("option", name="車いす対応便器").nth(1).click()
    elif clseries == "tankless":
        await page.get_by_role("option", name="パブリック向けタンクレストイレ").click()
    elif clseries == "quickfloor":
        await page.get_by_role("option", name="クイックタンク式床置便器").click()
    # 大便器ライニング
    await page.get_by_role("button", name="ライニング").click()
    await page.wait_for_timeout(1000)
    if cllining == "presence":
        await page.get_by_role("option", name="あり").click()
    elif cllining == "absence":
        await page.get_by_role("option", name="なし").click()
    # はねあげ手すり
    await page.get_by_role("button", name="はね上げ式手すり").click()
    if hr == "KF-H470EH60J":
        await page.get_by_role("option", name="KF-H470EH60J").click()
    elif hr == "KF-471EH60JU":
        await page.get_by_role("option", name="KF-471EH60JU").click()
    elif hr == "KF-471EH70JU":
        await page.get_by_role("option", name="KF-471EH70JU").click()
    # 手洗器
    await page.locator("div:nth-child(3) > div:nth-child(2) > div > div > div > .v-input > .v-input__control > .v-input__slot").first.click()
    await page.get_by_role("option", name="AWL-71U3AM").click()
    await page.get_by_role("button", name="AWL-71U3AM").click()
    await page.wait_for_timeout(1000)
    if aw == "presence":
        await page.get_by_role("option", name="AWL-71U3AM").click()
    elif aw == "absence":
        await page.get_by_role("option", name="なし").click()
    # L型手すり
    await page.get_by_role("button", name="L型手すり").click()
    if lhr == "KF-920AE70D12J":
        await page.get_by_role("option", name="KF-920AE70D12J").click()
    elif lhr == "KF-922AE80J":
        await page.get_by_role("option", name="KF-922AER80J").click()
    elif lhr == "KF-H920AE70D12J":
        await page.get_by_role("option", name="KF-H920AER70D12J").click()
    elif lhr == "KF-926AE80D25J":
        await page.get_by_role("option", name="KF-926AE80D25J").click()
    elif lhr == "KF-927AE80J":
        await page.get_by_role("option", name="KF-927AER80J").click()
    # L型手すりライニング
    await page.get_by_role("button", name="手すり側ライニング").click()
    await page.wait_for_timeout(1000)
    if lhrlining == "presence":
        await page.get_by_role("option", name="あり").click()
    elif lhrlining == "absence":
        await page.get_by_role("option", name="なし").click()
    # 洗面器
    await page.get_by_role("button", name="カウンター一体形洗面器").click()
    await page.get_by_role("option", name="車椅子対応洗面器").click()
    await page.get_by_role("button", name="車椅子対応洗面器").click()
    if la == "counter":
        await page.get_by_role("option", name="カウンター一体形洗面器").click()
    elif la == "wheel":
        await page.get_by_role("option", name="車椅子対応洗面器").click()
    # 洗面器ライニング
    await page.get_by_role("button", name="洗面器ライニング").click()
    await page.wait_for_timeout(1000)
    if lalining == "presence":
        await page.get_by_role("option", name="あり").click()
    elif lalining == "absence":
        await page.get_by_role("option", name="なし").click()
    # ハンドドライヤー
    await page.get_by_role("button", name="KS-580AH").click()
    await page.wait_for_timeout(1000)
    if hd == "presence":
        await page.get_by_role("option", name="KS-580AH").click()
    elif hd == "absence":
        await page.get_by_role("option", name="なし").click()
    # 子連れ配慮
    if uset == "set":
        await page.locator(".col-sm-8 > .v-input > .v-input__control > .v-input__slot").first.click()
        await page.get_by_role("option", name="ベビーキープ＋おむつ交換台", exact=True).click()
    elif uset == "cbset":
        await page.locator(".col-sm-8 > .v-input > .v-input__control > .v-input__slot").first.click()
        await page.get_by_role("option", name="ベビーキープ＋おむつ交換台＋チェンジングボード").click()
    # ユニバーサルシート
    if us == "presence":
        await page.locator("div:nth-child(4) > div > div > .col-sm-4 > .v-input > .v-input__control > .v-input__slot").click()
        await page.wait_for_timeout(1000)
        await page.get_by_role("option", name="あり").click()
    # オストメイト
    if os == "presence":
        await page.locator("div:nth-child(5) > div > div > .col-sm-8 > .v-input > .v-input__control > .v-input__slot").click()
        await page.wait_for_timeout(1000)
        await page.get_by_role("option", name="あり").click()
    # 計算実行
    await page.get_by_role("button", name="計算開始").click()
    # 結果一覧画面
    await page.wait_for_selector("text=※計算結果は、参考位置であり現場確認が必要です。")
    await page.wait_for_timeout(10000)
    await page.screenshot(path="./output_type1_standard/" + index + "/結果一覧.png", full_page=True)
    await page.get_by_role("link", name="詳しく見る").first.click()
    await page.wait_for_load_state()
    # 詳細画面
    await page.wait_for_selector("#toolbar-fullscreenTool")
    await page.wait_for_timeout(10000)
    await page.screenshot(path="./output_type1_standard/" + index + "/詳細.png", full_page=True)
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
    await download.save_as("./output_type1_standard/" + index + "/" + download.suggested_filename)
    # プロジェクト画面に戻る
    await page.get_by_role("link", name="プロジェクト").click()
    await page.wait_for_load_state()

# type1_packのテスト
async def type1_pack(page, cltype, clseries, os, hd, uset, us, cb, index):
    # ケース作成
    await page.locator(".col > .button-open").first.click()
    await page.locator(".py-0 > .v-input > .v-input__control > .v-input__slot").click()
    await page.locator(".py-0 > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("Type1_pack_Case" + index)
    await page.get_by_role("button", name="作成", exact=True).click()
    await page.get_by_role("radiogroup").get_by_text("バリアフリートイレ").click()
    await page.get_by_role("button", name="次へ").click()
    await page.wait_for_load_state()
    # 空間選択画面
    await page.get_by_role("button", name="閉じる").click()
    # 間口
    await page.locator("div:nth-child(1) > .row > .col > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("3500")
    # 奥行き
    await page.locator("div:nth-child(2) > .row > .col > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("3500")
    # 有効開口
    await page.get_by_role("button", name="900").click()
    await page.get_by_text("850").click()
    # 入口位置
    await page.locator("div").filter(has_text=re.compile(r"^R$")).locator("div").nth(1).click()
    # 扉種類
    await page.get_by_role("button", name="片引き戸").click()
    await page.get_by_text("引き込み戸").click()
    # 空間選択完了
    await page.get_by_role("button", name="器具選択").click()
    await page.wait_for_load_state()
    ## 器具選択画面
    # 大便器タイプ
    await page.wait_for_timeout(1000)
    await page.get_by_role("button", name="壁掛け").click()
    await page.get_by_role("option", name="多機能トイレパック").click()
    # 大便器シリーズ
    await page.get_by_role("button", name="シリーズ").click()
    if clseries == "pack_hl":
        await page.get_by_role("option", name="パブリック向け壁掛便器 HL").click()
    elif clseries == "pack_hc":
        await page.get_by_role("option", name="PTWC-HC10").click()
    # オストメイト
    await page.get_by_role("button", name="なし").first.click()
    await page.wait_for_timeout(1000)
    if os == "presence":
        await page.get_by_role("option", name="あり").click()
    elif os == "absence":
        await page.get_by_role("option", name="なし").click()
    # ハンドドライヤー
    await page.get_by_role("button", name="KS-580AH").click()
    await page.wait_for_timeout(1000)
    if hd == "presence":
        await page.get_by_role("option", name="KS-580AH").click()
    elif hd == "absence":
        await page.get_by_role("option", name="なし").click()
    # 子連れ配慮
    if uset == "set":
        await page.locator(".col-sm-8 > .v-input > .v-input__control > .v-input__slot").first.click()
        await page.get_by_role("option", name="ベビーキープ＋おむつ交換台", exact=True).click()
    elif uset == "cbset":
        await page.locator(".col-sm-8 > .v-input > .v-input__control > .v-input__slot").first.click()
        await page.get_by_role("option", name="ベビーキープ＋おむつ交換台＋チェンジングボード").click()
    # ユニバーサルシート
    if us == "presence":
        await page.locator("div:nth-child(4) > div > div > .col-sm-4 > .v-input > .v-input__control > .v-input__slot").click()
        await page.wait_for_timeout(1000)
        await page.get_by_role("option", name="あり").click()
    # チェンジングボード
    if cb == "presence":
        await page.locator("div:nth-child(5) > .col-sm-4 > .v-input > .v-input__control > .v-input__slot").click()
        await page.wait_for_timeout(1000)
        await page.get_by_role("option", name="あり").click()
    # 計算実行
    await page.get_by_role("button", name="計算開始").click()
    # 結果一覧画面
    await page.wait_for_selector("text=※計算結果は、参考位置であり現場確認が必要です。")
    await page.wait_for_timeout(10000)
    await page.screenshot(path="./output_type1_pack/" + index + "/結果一覧.png", full_page=True)
    await page.get_by_role("link", name="詳しく見る").first.click()
    await page.wait_for_load_state()
    # 詳細画面
    await page.wait_for_selector("#toolbar-fullscreenTool")
    await page.wait_for_timeout(10000)
    await page.screenshot(path="./output_type1_pack/" + index + "/詳細.png", full_page=True)
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
    await download.save_as("./output_type1_pack/" + index + "/" + download.suggested_filename)
    # プロジェクト画面に戻る
    await page.get_by_role("link", name="プロジェクト").click()
    await page.wait_for_load_state()

async def input_type2(page, size, door, doorPos, cl, la, num, sk):
    # 空間サイズ入力
    if size == "superHorizontal":
        await page.locator("div:nth-child(2) > .pa-2 > .row > div:nth-child(2) > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("8000")
        await page.locator("div:nth-child(3) > .pa-2 > .row > div:nth-child(2) > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("3000")
    elif size == "horizontal":
        await page.locator("div:nth-child(2) > .pa-2 > .row > div:nth-child(2) > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("7000")
        await page.locator("div:nth-child(3) > .pa-2 > .row > div:nth-child(2) > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("4000")
    elif size == "square":
        await page.locator("div:nth-child(2) > .pa-2 > .row > div:nth-child(2) > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("5000")
        await page.locator("div:nth-child(3) > .pa-2 > .row > div:nth-child(2) > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("5000")
    elif size == "vertical":
        await page.locator("div:nth-child(2) > .pa-2 > .row > div:nth-child(2) > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("4000")
        await page.locator("div:nth-child(3) > .pa-2 > .row > div:nth-child(2) > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("7000")
    else:
        await page.locator("div:nth-child(2) > .pa-2 > .row > div:nth-child(2) > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("3000")
        await page.locator("div:nth-child(3) > .pa-2 > .row > div:nth-child(2) > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("8000")
    # ドアタイプ入力
    if door == "doorless":
        await page.locator(".v-input--selection-controls__ripple").first.click()
    else:
        await page.locator("div:nth-child(3) > .v-radio > .v-input--selection-controls__input > .v-input--selection-controls__ripple").first.click()
    # ドア位置入力
    if doorPos == "left":
        await page.locator("div:nth-child(6) > .v-input__control > .v-input__slot > .v-input--radio-group__input > .row > div > .v-radio > .v-input--selection-controls__input > .v-input--selection-controls__ripple").first.click()
    else:
        await page.locator("div:nth-child(6) > .v-input__control > .v-input__slot > .v-input--radio-group__input > .row > div:nth-child(3) > .v-radio > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
    # 大便器タイプ入力
    if cl == "wall":
        await page.locator("div:nth-child(2) > .pr-0 > .v-radio > .v-input--selection-controls__input > .v-input--selection-controls__ripple").first.click()
    else:    
        await page.locator("div:nth-child(2) > .row > .pr-0 > .v-radio > .v-input--selection-controls__input > .v-input--selection-controls__ripple").first.click()
    # 洗面器タイプ入力
    if la == "counter":
        await page.locator("div:nth-child(6) > .v-input__control > .v-input__slot > .v-input--radio-group__input > div > .row > .pr-0 > .v-radio > .v-input--selection-controls__input > .v-input--selection-controls__ripple").first.click()
    else:
        await page.locator("div:nth-child(6) > .v-input__control > .v-input__slot > .v-input--radio-group__input > div:nth-child(2) > .row > .pr-0 > .v-radio > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
    #　掃除用流し入力

    #  利用人員入力
    await page.locator("div:nth-child(3) > div > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill(num)

# type2のテスト
async def type2(page, sex, size, door, doorPos, cl, la, num, sk, index):
    # ケース作成
    await page.locator(".col > .button-open").first.click()
    await page.locator(".py-0 > .v-input > .v-input__control > .v-input__slot").click()
    await page.locator(".py-0 > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("Type2_Case" + index)
    await page.get_by_role("button", name="作成", exact=True).click()
    await page.get_by_text("一般トイレ", exact=True).click()
    await page.get_by_role("button", name="次へ").click()
    if sex == "male":
        await page.get_by_text("男性トイレ").click()
    else:
        await page.get_by_text("女性トイレ").click()
    await page.wait_for_load_state()
    await page.get_by_role("button", name="次へ").click()
    await page.wait_for_load_state()
    # 計算条件選択
    await input_type2(page, size, door, doorPos, cl, la, num, sk)
    await page.get_by_role("button", name="この条件で設計する").click()
    start_time = time.time()
    # 結果一覧画面
    await page.wait_for_selector("text=レイアウト計算条件")
    await page.wait_for_timeout(3000)
    await page.screenshot(path="./output_type2/" + index + "/結果一覧.png", full_page=True)
    await page.get_by_role("link", name="プランを見る").first.click()
    await page.wait_for_load_state()
    # 詳細画面
    await page.wait_for_selector("#toolbar-fullscreenTool")
    end_time = time.time()
    print(f"Operation time: {end_time - start_time} seconds")
    await page.wait_for_timeout(3000)
    await page.screenshot(path="./output_type2/" + index + "/3D詳細.png", full_page=True)
    await page.get_by_role("tab", name="2D平面図").click()
    await page.wait_for_selector("#toolbar-cameraSubmenuTool")
    await page.wait_for_timeout(3000)
    await page.screenshot(path="./output_type2/" + index + "/2D詳細.png", full_page=True)
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
    await download.save_as("./output_type2/"+ index + "/" + download.suggested_filename)
    # プロジェクト画面に戻る
    await page.get_by_role("link", name="プロジェクト").click()
    await page.wait_for_load_state()

async def calculate(sex, size, door, doorPos, cl, la, sk, num, index):
# async def calculate(cltype, clseries, cllining, hr, aw, lhr, lhrlining, la, lalining, hd, uset, us, os, index):
# async def calculate(cltype, clseries, os, hd, uset, us, cb, index):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        # context = await browser.new_context(
        #     record_video_dir="./videos",
        #     record_video_size={"height": 768, "width": 1024},
        # )
        page = await context.new_page()
        page.set_default_timeout(800000)
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
        await type2(page, sex, size, door, doorPos, cl, la, num, sk, index)
        # await type1_standard(page, cltype, clseries, cllining, hr, aw, lhr, lhrlining, la, lalining, hd, uset, us, os, index)
        # await type1_pack(page, cltype, clseries, os, hd, uset, us, cb, index)
        # ---------------------
        await context.close()
        await browser.close()

async def main():
    with open('./test_case_type2.csv') as f:
        reader = csv.reader(f)
        params_list = [row for row in reader]

    tasks = [calculate(*params) for params in params_list[0:1]]

    await asyncio.gather(*tasks)


asyncio.run(main())