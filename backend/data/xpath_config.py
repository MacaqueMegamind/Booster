class XPATHLoginEmail:
    """
    Link to auth form:
    https://www.ozon.ru/ozonid
    """
    StartPage = "https://www.ozon.ru/ozonid"
    AUTH_FORM = "//section[@class='csma-ozon-id-page-anonymous']"
    INPUT_FORM = "//input[@name='email']"
    SIGN_IN_EMAIL_BUTTON = "//div[contains(text(), 'Sign in by email')]/ancestor::button[1]"
    SIGN_IN_BUTTON = "//button[@type='submit']"
    INPUT_CODE_FORM = "//input[@name='otp']"


class XPATHLogin:
    """
    Link to auth form:
    https://www.ozon.ru/ozonid
    """
    StartPage = "https://www.ozon.ru/ozonid"
    AUTH_FORM = "//section[@class='csma-ozon-id-page-anonymous']"
    INPUT_FORM = "//input[@name='autocomplete']"
    SIGN_IN_BUTTON = "//button[@type='submit']"
    INPUT_CODE_FORM = "//input[@name='otp']"


class XPATHAddProduct:
    """
    These are the favorites and add to cart buttons
    """
    XPATH_BUTTON_CART = "//div[contains(text(), 'Добавить в корзину')]/ancestor::button[1]"
    XPATH_BUTTON_FAVORITE = "//button[@aria-label='Добавить в избранное']"


class XPATHRegistration:
    """
    Link to registration form:
    https://www.ozon.ru/ozonid
    """
    StartPage = "https://www.ozon.ru/ozonid"
    AUTH_FORM = "//section[@class='csma-ozon-id-page-anonymous']"
    INPUT_FORM = "//input[@name='autocomplete']"
    SIGN_IN_BUTTON = "//button[@type='submit']"
    AGREEMENT_BUTTON = "//input[@name='agreement']/ancestor::label[1]"
    ADVERTISEMENT_BUTTON = "//input[@name='advertising']/ancestor::label[1]"
    INPUT_CODE_FORM = "//input[@name='otp']"
    REGISTRATION_BUTTON = "//button[@type='submit']"
