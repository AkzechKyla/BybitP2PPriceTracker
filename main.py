import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def handle_modal(driver):
    """Wait for the modal to appear and confirm it."""
    try:
        wait = WebDriverWait(driver, 10)
        confirm_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ant-btn-primary"))
        )
        driver.execute_script("arguments[0].click();", confirm_button)
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
