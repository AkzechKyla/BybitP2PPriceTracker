import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def handle_modal(driver):
    """Wait for the modal to appear and confirm it."""
    try:
        wait = WebDriverWait(driver, 20)
        btn = driver.find_element(
            By.XPATH,
            "/html/body/div[14]/div/div[2]/div/div[2]/div/div/div/div/button",
        )
        wait.until(EC.element_to_be_clickable(btn))
        btn.click()
        print("Confirmed the modal.")
    except Exception as e:
        print("Error handling modal:", e)


def main():
    url = "https://www.bybit.com/en/fiat/trade/otc/sell/USDT/PHP"
    driver = uc.Chrome()

    try:
        driver.get(url)
        handle_modal(driver)
    except Exception as e:
        print("Unexpected error:", e)
    finally:
        input("Press Enter to close the browser...")
        driver.quit()


if __name__ == "__main__":
    main()
