class XPATHLoginEmail:
    """
    Link to auth form:
    https://www.ozon.ru/ozonid
    """
    StartPage = "https://www.ozon.ru/ozonid"
    AUTH_FORM = "//section[@class='csma-ozon-id-page-anonymous']"
    INPUT_FORM = "//input[@name='email']"
    SIGN_IN_EMAIL_BUTTON = "//button[@class='cae3 ga00-a']"
    SIGN_IN_BUTTON = "//button[@type='submit']"
    INPUT_CODE_FORM = "//input[@name='otp']"


class XPATHLoginPhone:
    """
    Link to auth form:
    https://www.ozon.ru/ozonid
    """
    StartPage = "https://www.ozon.ru/ozonid"
    AUTH_FORM = "//section[@class='csma-ozon-id-page-anonymous']"
    INPUT_FORM = "//input[@name='autocomplete']"
    SIGN_IN_BUTTON = "//button[@type='submit']"


class XPATHAddProduct:
    """
    These are the favorites and add to cart buttons
    """
    XPATH_BUTTON_CART = "//button[@class='zj1 b200-a0 b200-b2 b200-a4']"
    XPATH_BUTTON_FAVORITE = "//button[@class='jz7 ag00-a0 ag00-a3']"
