from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
from fake_useragent import UserAgent


class Driver(uc.Chrome):
    def __init__(self, options: uc.ChromeOptions = uc.ChromeOptions(), fake: bool = True) -> None:
        self.options: uc.ChromeOptions = options
        if fake:
            user_argument = UserAgent()
            self.options.add_argument("user-agent="+user_argument.random)
        self.manager = ChromeDriverManager()
        super().__init__(driver_executable_path=self.manager.install(), use_subprocess=True, options=self.options)

    def __del__(self):
        try:
            super().__del__()
        except OSError:
            pass
