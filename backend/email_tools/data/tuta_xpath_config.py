class XPATH_SignUp:
    """
    Link to registration form:
    https://app.tuta.com/login
    """
    StartPage = "https://app.tuta.com/login"
    SIGN_UP_BUTTON = "//button[contains(text(), 'Sign up')]"
    FREE_PLAN_BUTTON = "//div[@class='plans-grid']/div[1]/descendant::button[contains(text(), 'Select')]"
    CHECKBOX_1 = "//div[@class='dialog-contentButtonsBottom']/div[1]/descendant::input[@type='checkbox']"
    CHECKBOX_2 = "//div[@class='dialog-contentButtonsBottom']/div[2]/descendant::input[@type='checkbox']"
    RULES_OK_BUTTON = "//div[contains(@class, 'dialog-buttons')]/descendant::button[contains(text(), 'Ok')]"
    INPUT_EMAIL = "//div[@id='signup-account-dialog']/descendant::input[@aria-label='Email address']"
    INPUT_PASSWORD = "//div[@id='signup-account-dialog']/descendant::input[@aria-label='Set password']"
    REPEAT_PASSWORD = "//div[@id='signup-account-dialog']/descendant::input[@aria-label='Repeat password']"
    SIGN_UP_CHECKBOX_1 = "//div[@id='signup-account-dialog']/descendant::label[contains(text(),'I have read and agree to the following documents:')]/input[@type='checkbox']"
    SIGN_UP_CHECKBOX_2 = "//div[@id='signup-account-dialog']/descendant::label[contains(text(),'I am at least 16 years old.')]/input[@type='checkbox']"
    NEXT_BUTTON = "//div[@id='signup-account-dialog']/descendant::button[contains(text(), 'Next')]"
    EMAIL_TEXT = "//div[@id='signup-account-dialog']/descendant::div[contains(@class, 'text-field')][1]/descendant::small/div"
    RECOVERY_DIV = "//div[@id='wizardDialogContent']/descendant::div[contains(@class, 'text-break')]"

    # XPATH for waiting for the page to load
    LOGIN_FORM = "//div[@aria-label='Login']"
    ACCOUNT_PLAN_FORM = "//div[@class='plans-grid']"
    APPLY_RULES_DIALOG = "//div[@class='dialog-contentButtonsBottom']"
    EMAIL_LABEL = "//div[@id='signup-account-dialog']/descendant::div[contains(@class, 'text-field')][1]/descendant::label[contains(text(), 'Email address')]"
    RECOVERY_WIZARD = "//div[@id='wizardDialogContent']"


class Email_State:
    """
    Link to email state:
    https://app.tuta.com/login
    """
    NO_EMAIL = 'Enter preferred email address'
    EMAIL_AVAILABLE = 'Email address is available.'
    EMAIL_TAKEN = 'Email address is not available.'
    EMAIL_VALIDATING = 'Validating email address...'
