import pytest
from playwright.sync_api import sync_playwright, expect
import re
import logging
import time
import csv

# ワーカー別ロガーを定義する
def _get_logger(worker_id):
    logger = logging.getLogger("logger_{}".format(worker_id))    
    handler = logging.FileHandler(filename="test.log")  
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.setLevel(logging.INFO)  
    logger.addHandler(handler)
    return logger

@pytest.fixture(scope="function")
def page():
    # login処理
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(800000)
        # 認証画面
        page.goto("https://dev-a-spec.lixil.com/")
        page.wait_for_url("https://dev-a-spec.lixil.com/dev_authenticate/")
        page.get_by_label("認証").click()
        page.get_by_label("認証").fill("c9w$pDMciZT%")
        page.get_by_label("認証").press("Enter")
        page.wait_for_load_state()
        # TOP画面
        page.locator("button").filter(has_text=re.compile(r"^JP$")).click()
        page.get_by_role("button", name="設計を始める →").first.click()
        page.get_by_role("link", name="同意して始める").click()
        page.wait_for_load_state()
        # MyLIXIL
        page.get_by_placeholder("メールアドレス").click()
        page.get_by_placeholder("メールアドレス").fill("k36795284@gmail.com")
        page.get_by_role("button", name="次へ").click()
        page.locator("input[name=\"password\"]").click()
        page.locator("input[name=\"password\"]").fill("1111_tkhr_1010")
        page.get_by_role("button", name="次へ").click()
        page.wait_for_load_state()
        yield page
        browser.close()

# with open('./test_case_type2.csv') as f:
#     reader = csv.reader(f)
#     type2_params_list = [tuple(row) for row in reader]

# @pytest.mark.parametrize("sex, size, door, doorPos, cl, la, sk, num, index", type2_params_list[0:2])
# def test_scenario_type2(page, sex, size, door, doorPos, cl, la, sk, num, index, worker_id):
#     # プロジェクト作成
#     page.get_by_role("button", name="設計する").click()
#     page.get_by_role("button", name="次へ").click()
#     page.get_by_placeholder("プロジェクト名").click()
#     page.get_by_placeholder("プロジェクト名").fill("playwright_test")
#     page.get_by_placeholder("メモ欄").click()
#     page.get_by_placeholder("メモ欄").fill("test")
#     page.get_by_role("button", name="作成", exact=True).click()
#     page.wait_for_load_state()
#     # ケース作成
#     page.locator(".col > .button-open").first.click()
#     page.locator(".py-0 > .v-input > .v-input__control > .v-input__slot").click()
#     page.locator(".py-0 > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("Type2_Case" + index)
#     page.get_by_role("button", name="作成", exact=True).click()
#     page.get_by_text("一般トイレ", exact=True).click()
#     page.get_by_role("button", name="次へ").click()
#     if sex == "male":
#         page.get_by_text("男性トイレ").click()
#     else:
#         page.get_by_text("女性トイレ").click()
#     page.wait_for_load_state()
#     page.get_by_role("button", name="次へ").click()
#     page.wait_for_load_state()
#     ## 計算条件選択
#     # 空間サイズ入力
#     if size == "superHorizontal":
#         page.locator("div:nth-child(2) > .pa-2 > .row > div:nth-child(2) > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("8000")
#         page.locator("div:nth-child(3) > .pa-2 > .row > div:nth-child(2) > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("3000")
#     elif size == "horizontal":
#         page.locator("div:nth-child(2) > .pa-2 > .row > div:nth-child(2) > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("7000")
#         page.locator("div:nth-child(3) > .pa-2 > .row > div:nth-child(2) > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("4000")
#     elif size == "square":
#         page.locator("div:nth-child(2) > .pa-2 > .row > div:nth-child(2) > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("5000")
#         page.locator("div:nth-child(3) > .pa-2 > .row > div:nth-child(2) > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("5000")
#     elif size == "vertical":
#         page.locator("div:nth-child(2) > .pa-2 > .row > div:nth-child(2) > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("4000")
#         page.locator("div:nth-child(3) > .pa-2 > .row > div:nth-child(2) > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("7000")
#     else:
#         page.locator("div:nth-child(2) > .pa-2 > .row > div:nth-child(2) > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("3000")
#         page.locator("div:nth-child(3) > .pa-2 > .row > div:nth-child(2) > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("8000")
#     # ドアタイプ入力
#     if door == "doorless":
#         page.locator(".v-input--selection-controls__ripple").first.click()
#     else:
#         page.locator("div:nth-child(3) > .v-radio > .v-input--selection-controls__input > .v-input--selection-controls__ripple").first.click()
#     # ドア位置入力
#     if doorPos == "left":
#         page.locator("div:nth-child(6) > .v-input__control > .v-input__slot > .v-input--radio-group__input > .row > div > .v-radio > .v-input--selection-controls__input > .v-input--selection-controls__ripple").first.click()
#     else:
#         page.locator("div:nth-child(6) > .v-input__control > .v-input__slot > .v-input--radio-group__input > .row > div:nth-child(3) > .v-radio > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
#     # 大便器タイプ入力
#     if cl == "wall":
#         page.locator("div:nth-child(2) > .pr-0 > .v-radio > .v-input--selection-controls__input > .v-input--selection-controls__ripple").first.click()
#     else:    
#         page.locator("div:nth-child(2) > .row > .pr-0 > .v-radio > .v-input--selection-controls__input > .v-input--selection-controls__ripple").first.click()
#     # 洗面器タイプ入力
#     if la == "counter":
#         page.locator("div:nth-child(6) > .v-input__control > .v-input__slot > .v-input--radio-group__input > div > .row > .pr-0 > .v-radio > .v-input--selection-controls__input > .v-input--selection-controls__ripple").first.click()
#     else:
#         page.locator("div:nth-child(6) > .v-input__control > .v-input__slot > .v-input--radio-group__input > div:nth-child(2) > .row > .pr-0 > .v-radio > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
#     #　掃除用流し入力
#     page.get_by_role("button", name="なし").click()
#     if la == "presence":
#         page.get_by_role("option", name="あり").click()
#     #  利用人員入力
#     page.locator("div:nth-child(3) > div > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill(num)
#     page.get_by_role("button", name="この条件で設計する").click()
#     calculation_start = time.time()
#     # 結果一覧画面
#     page.wait_for_selector("text=レイアウト計算条件")
#     calculation_end = time.time()
#     page.wait_for_timeout(3000)
#     page.screenshot(path="./output_type2/" + index + "/結果一覧.png", full_page=True)
#     page.get_by_role("link", name="プランを見る").first.click()
#     page.wait_for_load_state()
#     # 詳細画面
#     page.wait_for_selector("#toolbar-fullscreenTool")
#     show_3d_end = time.time()
#     page.wait_for_timeout(3000)
#     page.screenshot(path="./output_type2/" + index + "/3D詳細.png", full_page=True)
#     page.get_by_role("tab", name="2D平面図").click()
#     show_2d_start = time.time()
#     page.wait_for_selector("#toolbar-cameraSubmenuTool")
#     show_2d_end = time.time()
#     page.wait_for_timeout(3000)
#     page.screenshot(path="./output_type2/" + index + "/2D詳細.png", full_page=True)
#     page.get_by_role("button", name="カートに追加").click()
#     page.get_by_role("link", name="カート Badge").click()
#     page.wait_for_load_state()
#     # カート画面
#     page.get_by_role("button", name="データ出力").click()
#     page.locator("div:nth-child(11) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
#     page.locator("div:nth-child(12) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
#     page.locator("div:nth-child(13) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
#     page.locator("div:nth-child(14) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
#     page.locator("div:nth-child(15) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
#     # ダウンロード
#     dl_start = time.time()
#     with page.expect_download() as download_info:
#         page.get_by_role("button", name="ダウンロード").click()
#     download = download_info.value
#     download.save_as("./output_type2/"+ index + "/" + download.suggested_filename)
#     dl_end = time.time()
#     # プロジェクト画面に戻る
#     page.get_by_role("link", name="プロジェクト").click()
#     page.wait_for_load_state()

#     # ワーカー別ログファイルにログ出力を行う
#     # ワーカープロセスID,URL,タイトル
#     logger = _get_logger(worker_id)
#     logger.info('worker:{} content:{} calculation_time:{} show_3d_time:{} show_2d_time:{} dl_time:{}'.format(worker_id, "Type1_pack_" + index, calculation_end - calculation_start, show_3d_end - calculation_end, show_2d_end - show_2d_start, dl_end - dl_start))
#     page.close()


# with open('./test_case_type1_standard.csv') as f:
#     reader = csv.reader(f)
#     type1_standard_params_list = [tuple(row) for row in reader]

# @pytest.mark.parametrize("cltype, clseries, cllining, hr, aw, lhr, lhrlining, la, lalining, hd, uset, us, os, index", type1_standard_params_list[0:2])
# def test_scenario_type1_standard(page, cltype, clseries, cllining, hr, aw, lhr, lhrlining, la, lalining, hd, uset, us, os, index, worker_id):
#     # プロジェクト作成
#     page.get_by_role("button", name="設計する").click()
#     page.get_by_role("button", name="次へ").click()
#     page.get_by_placeholder("プロジェクト名").click()
#     page.get_by_placeholder("プロジェクト名").fill("playwright_test")
#     page.get_by_placeholder("メモ欄").click()
#     page.get_by_placeholder("メモ欄").fill("test")
#     page.get_by_role("button", name="作成", exact=True).click()
#     page.wait_for_load_state()
#     # ケース作成
#     page.locator(".col > .button-open").first.click()
#     page.locator(".py-0 > .v-input > .v-input__control > .v-input__slot").click()
#     page.locator(".py-0 > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("Type1_Case" + index)
#     page.get_by_role("button", name="作成", exact=True).click()
#     page.get_by_role("radiogroup").get_by_text("バリアフリートイレ").click()
#     page.get_by_role("button", name="次へ").click()
#     page.wait_for_load_state()
#     # 空間選択画面
#     page.get_by_role("button", name="閉じる").click()
#     # 間口
#     page.locator("div:nth-child(1) > .row > .col > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("3500")
#     # 奥行き
#     page.locator("div:nth-child(2) > .row > .col > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("3500")
#     # 有効開口
#     page.get_by_role("button", name="900").click()
#     page.get_by_text("850").click()
#     # 入口位置
#     page.locator("div").filter(has_text=re.compile(r"^R$")).locator("div").nth(1).click()
#     # 扉種類
#     page.get_by_role("button", name="片引き戸").click()
#     page.get_by_text("引き込み戸").click()
#     # 空間選択完了
#     page.get_by_role("button", name="器具選択").click()
#     page.wait_for_load_state()
#     ## 器具選択画面
#     # 大便器タイプ
#     page.get_by_role("button", name="壁掛け").click()
#     page.get_by_role("option", name="床置き").click()
#     page.get_by_role("button", name="床置き").click()
#     if cltype == "wall":
#         page.get_by_role("option", name="壁掛け").click()
#     elif cltype == "floor":
#         page.get_by_role("option", name="床置き").click()
#     # 大便器シリーズ
#     page.get_by_role("button", name="シリーズ").click()
#     if clseries == "pub_hl":
#         page.get_by_role("option", name="パブリック向け壁掛便器 HL").click()
#     elif clseries == "pub":
#         page.get_by_role("option", name="パブリック向け壁掛便器", exact=True).click()
#     elif clseries == "quickwall":
#         page.get_by_role("option", name="クイックタンク式壁掛便器").click()
#     elif clseries == "western":
#         page.get_by_role("option", name="壁掛式洋風便器").click()
#     elif clseries == "wheel1":
#         page.get_by_role("option", name="車いす対応便器").first.click()
#     elif clseries == "wheel2":
#         page.get_by_role("option", name="車いす対応便器").nth(1).click()
#     elif clseries == "tankless":
#         page.get_by_role("option", name="パブリック向けタンクレストイレ").click()
#     elif clseries == "quickfloor":
#         page.get_by_role("option", name="クイックタンク式床置便器").click()
#     # 大便器ライニング
#     page.get_by_role("button", name="ライニング").click()
#     page.wait_for_timeout(1000)
#     if cllining == "presence":
#         page.get_by_role("option", name="あり").click()
#     elif cllining == "absence":
#         page.get_by_role("option", name="なし").click()
#     # はねあげ手すり
#     page.get_by_role("button", name="はね上げ式手すり").click()
#     if hr == "KF-H470EH60J":
#         page.get_by_role("option", name="KF-H470EH60J").click()
#     elif hr == "KF-471EH60JU":
#         page.get_by_role("option", name="KF-471EH60JU").click()
#     elif hr == "KF-471EH70JU":
#         page.get_by_role("option", name="KF-471EH70JU").click()
#     # 手洗器
#     page.locator("div:nth-child(3) > div:nth-child(2) > div > div > div > .v-input > .v-input__control > .v-input__slot").first.click()
#     page.get_by_role("option", name="AWL-71U3AM").click()
#     page.get_by_role("button", name="AWL-71U3AM").click()
#     page.wait_for_timeout(1000)
#     if aw == "presence":
#         page.get_by_role("option", name="AWL-71U3AM").click()
#     elif aw == "absence":
#         page.get_by_role("option", name="なし").click()
#     # L型手すり
#     page.get_by_role("button", name="L型手すり").click()
#     if lhr == "KF-920AE70D12J":
#         page.get_by_role("option", name="KF-920AE70D12J").click()
#     elif lhr == "KF-922AE80J":
#         page.get_by_role("option", name="KF-922AER80J").click()
#     elif lhr == "KF-H920AE70D12J":
#         page.get_by_role("option", name="KF-H920AER70D12J").click()
#     elif lhr == "KF-926AE80D25J":
#         page.get_by_role("option", name="KF-926AE80D25J").click()
#     elif lhr == "KF-927AE80J":
#         page.get_by_role("option", name="KF-927AER80J").click()
#     # L型手すりライニング
#     page.get_by_role("button", name="手すり側ライニング").click()
#     page.wait_for_timeout(1000)
#     if lhrlining == "presence":
#         page.get_by_role("option", name="あり").click()
#     elif lhrlining == "absence":
#         page.get_by_role("option", name="なし").click()
#     # 洗面器
#     page.get_by_role("button", name="カウンター一体形洗面器").click()
#     page.get_by_role("option", name="車椅子対応洗面器").click()
#     page.get_by_role("button", name="車椅子対応洗面器").click()
#     if la == "counter":
#         page.get_by_role("option", name="カウンター一体形洗面器").click()
#     elif la == "wheel":
#         page.get_by_role("option", name="車椅子対応洗面器").click()
#     # 洗面器ライニング
#     page.get_by_role("button", name="洗面器ライニング").click()
#     page.wait_for_timeout(1000)
#     if lalining == "presence":
#         page.get_by_role("option", name="あり").click()
#     elif lalining == "absence":
#         page.get_by_role("option", name="なし").click()
#     # ハンドドライヤー
#     page.get_by_role("button", name="KS-580AH").click()
#     page.wait_for_timeout(1000)
#     if hd == "presence":
#         page.get_by_role("option", name="KS-580AH").click()
#     elif hd == "absence":
#         page.get_by_role("option", name="なし").click()
#     # 子連れ配慮
#     if uset == "set":
#         page.locator(".col-sm-8 > .v-input > .v-input__control > .v-input__slot").first.click()
#         page.get_by_role("option", name="ベビーキープ＋おむつ交換台", exact=True).click()
#     elif uset == "cbset":
#         page.locator(".col-sm-8 > .v-input > .v-input__control > .v-input__slot").first.click()
#         page.get_by_role("option", name="ベビーキープ＋おむつ交換台＋チェンジングボード").click()
#     # ユニバーサルシート
#     if us == "presence":
#         page.locator("div:nth-child(4) > div > div > .col-sm-4 > .v-input > .v-input__control > .v-input__slot").click()
#         page.wait_for_timeout(1000)
#         page.get_by_role("option", name="あり").click()
#     # オストメイト
#     if os == "presence":
#         page.locator("div:nth-child(5) > div > div > .col-sm-8 > .v-input > .v-input__control > .v-input__slot").click()
#         page.wait_for_timeout(1000)
#         page.get_by_role("option", name="あり").click()
#     # 計算実行
#     page.get_by_role("button", name="計算開始").click()
#     calculation_start = time.time()
#     # 結果一覧画面
#     page.wait_for_selector("text=※計算結果は、参考位置であり現場確認が必要です。")
#     calculation_end = time.time()
#     page.wait_for_timeout(10000)
#     page.screenshot(path="./output_type1_standard/" + index + "/結果一覧.png", full_page=True)
#     page.get_by_role("link", name="詳しく見る").first.click()
#     show_2d_start = time.time()
#     page.wait_for_load_state()
#     # 詳細画面
#     page.wait_for_selector("#toolbar-fullscreenTool")
#     show_3d_end = time.time()
#     page.wait_for_function("document.querySelectorAll('#toolbar-fullscreenTool').length >= 2")
#     show_2d_end = time.time()
#     page.wait_for_timeout(10000)
#     page.screenshot(path="./output_type1_standard/" + index + "/詳細.png", full_page=True)
#     page.get_by_role("button", name="カートに追加").click()
#     page.get_by_role("link", name="カート Badge").click()
#     page.wait_for_load_state()
#     # カート画面
#     page.get_by_role("button", name="データ出力").click()
#     page.locator("div:nth-child(11) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
#     page.locator("div:nth-child(12) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
#     page.locator("div:nth-child(13) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
#     page.locator("div:nth-child(14) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
#     page.locator("div:nth-child(15) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
#     # ダウンロード
#     dl_start = time.time()
#     with page.expect_download() as download_info:
#         page.get_by_role("button", name="ダウンロード").click()
#     download = download_info.value
#     download.save_as("./output_type1_standard/" + index + "/" + download.suggested_filename)
#     dl_end = time.time()
#     # プロジェクト画面に戻る
#     page.get_by_role("link", name="プロジェクト").click()
#     page.wait_for_load_state()

#     # ワーカー別ログファイルにログ出力を行う
#     # ワーカープロセスID,URL,タイトル
#     logger = _get_logger(worker_id)
#     logger.info('worker:{} content:{} calculation_time:{} show_3d_time:{} show_2d_time:{} dl_time:{}'.format(worker_id, "Type1_standard_" + index, calculation_end - calculation_start, show_3d_end - calculation_end, show_2d_end - show_2d_start, dl_end - dl_start))
#     page.close()

with open('./test_case_type1_pack.csv') as f:
    reader = csv.reader(f)
    type1_pack_params_list = [tuple(row) for row in reader]

@pytest.mark.parametrize("cltype, clseries, os, hd, uset, us, cb, index", type1_pack_params_list[0:2])
def test_scenario_type1_pack(page, cltype, clseries, os, hd, uset, us, cb, index, worker_id):
    # プロジェクト作成
    page.get_by_role("button", name="設計する").click()
    page.get_by_role("button", name="次へ").click()
    page.get_by_placeholder("プロジェクト名").click()
    page.get_by_placeholder("プロジェクト名").fill("playwright_test")
    page.get_by_placeholder("メモ欄").click()
    page.get_by_placeholder("メモ欄").fill("test")
    page.get_by_role("button", name="作成", exact=True).click()
    page.wait_for_load_state()
    # ケース作成
    page.locator(".col > .button-open").first.click()
    page.locator(".py-0 > .v-input > .v-input__control > .v-input__slot").click()
    page.locator(".py-0 > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("Type1_pack_Case" + index)
    page.get_by_role("button", name="作成", exact=True).click()
    page.get_by_role("radiogroup").get_by_text("バリアフリートイレ").click()
    page.get_by_role("button", name="次へ").click()
    page.wait_for_load_state()
    # 空間選択画面
    page.get_by_role("button", name="閉じる").click()
    # 間口
    page.locator("div:nth-child(1) > .row > .col > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("3500")
    # 奥行き
    page.locator("div:nth-child(2) > .row > .col > .v-input > .v-input__control > .v-input__slot > .v-text-field__slot > input").fill("3500")
    # 有効開口
    page.get_by_role("button", name="900").click()
    page.get_by_text("850").click()
    # 入口位置
    page.locator("div").filter(has_text=re.compile(r"^R$")).locator("div").nth(1).click()
    # 扉種類
    page.get_by_role("button", name="片引き戸").click()
    page.get_by_text("引き込み戸").click()
    # 空間選択完了
    page.get_by_role("button", name="器具選択").click()
    page.wait_for_load_state()
    ## 器具選択画面
    # 大便器タイプ
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="壁掛け").click()
    page.get_by_role("option", name="多機能トイレパック").click()
    # 大便器シリーズ
    page.get_by_role("button", name="シリーズ").click()
    if clseries == "pack_hl":
        page.get_by_role("option", name="パブリック向け壁掛便器 HL").click()
    elif clseries == "pack_hc":
        page.get_by_role("option", name="PTWC-HC10").click()
    # オストメイト
    page.get_by_role("button", name="なし").first.click()
    page.wait_for_timeout(1000)
    if os == "presence":
        page.get_by_role("option", name="あり").click()
    elif os == "absence":
        page.get_by_role("option", name="なし").click()
    # ハンドドライヤー
    page.get_by_role("button", name="KS-580AH").click()
    page.wait_for_timeout(1000)
    if hd == "presence":
        page.get_by_role("option", name="KS-580AH").click()
    elif hd == "absence":
        page.get_by_role("option", name="なし").click()
    # 子連れ配慮
    if uset == "set":
        page.locator(".col-sm-8 > .v-input > .v-input__control > .v-input__slot").first.click()
        page.get_by_role("option", name="ベビーキープ＋おむつ交換台", exact=True).click()
    elif uset == "cbset":
        page.locator(".col-sm-8 > .v-input > .v-input__control > .v-input__slot").first.click()
        page.get_by_role("option", name="ベビーキープ＋おむつ交換台＋チェンジングボード").click()
    # ユニバーサルシート
    if us == "presence":
        page.locator("div:nth-child(4) > div > div > .col-sm-4 > .v-input > .v-input__control > .v-input__slot").click()
        page.wait_for_timeout(1000)
        page.get_by_role("option", name="あり").click()
    # チェンジングボード
    if cb == "presence":
        page.locator("div:nth-child(5) > .col-sm-4 > .v-input > .v-input__control > .v-input__slot").click()
        page.wait_for_timeout(1000)
        page.get_by_role("option", name="あり").click()
    # 計算実行
    page.get_by_role("button", name="計算開始").click()
    calculation_start = time.time()
    # 結果一覧画面
    page.wait_for_selector("text=※計算結果は、参考位置であり現場確認が必要です。")
    calculation_end = time.time()
    page.wait_for_timeout(10000)
    page.screenshot(path="./output_type1_pack/" + index + "/結果一覧.png", full_page=True)
    page.get_by_role("link", name="詳しく見る").first.click()
    show_2d_start = time.time()
    page.wait_for_load_state()
    # 詳細画面
    page.wait_for_selector("#toolbar-fullscreenTool")
    show_3d_end = time.time()
    page.wait_for_function("document.querySelectorAll('#toolbar-fullscreenTool').length >= 2")
    show_2d_end = time.time()
    page.wait_for_timeout(10000)
    page.screenshot(path="./output_type1_pack/" + index + "/詳細.png", full_page=True)
    page.get_by_role("button", name="カートに追加").click()
    page.get_by_role("link", name="カート Badge").click()
    page.wait_for_load_state()
    # カート画面
    page.get_by_role("button", name="データ出力").click()
    page.locator("div:nth-child(11) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
    page.locator("div:nth-child(12) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
    page.locator("div:nth-child(13) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
    page.locator("div:nth-child(14) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
    page.locator("div:nth-child(15) > .v-input > .v-input__control > .v-input__slot > .v-input--selection-controls__input > .v-input--selection-controls__ripple").click()
    # ダウンロード
    dl_start = time.time()
    with page.expect_download() as download_info:
        page.get_by_role("button", name="ダウンロード").click()
    download = download_info.value
    download.save_as("./output_type1_pack/" + index + "/" + download.suggested_filename)
    dl_end = time.time()
    # プロジェクト画面に戻る
    page.get_by_role("link", name="プロジェクト").click()
    page.wait_for_load_state()

    # ワーカー別ログファイルにログ出力を行う
    # ワーカープロセスID,URL,タイトル
    logger = _get_logger(worker_id)
    logger.info('worker:{} content:{} calculation_time:{} show_3d_time:{} show_2d_time:{} dl_time:{}'.format(worker_id, "Type1_pack_" + index, calculation_end - calculation_start, show_3d_end - calculation_end, show_2d_end - show_2d_start, dl_end - dl_start))
    page.close()