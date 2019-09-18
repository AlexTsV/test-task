class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def should_be_login_page_url(self):
        assert 'https://www.yclients.com/signin' == self.browser.current_url, 'does not main page url'

    def switch_to_new_window(self):
        new_window = self.browser.window_handles[1]
        self.browser.switch_to_window(new_window)

    def close_current_window(self):
        self.browser.close()
