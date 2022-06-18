# instagram 에 사용되는 xPath 모음
class InstagramXpath:
    REGISTER_BUTTON = "//button[text()='가입하기']"
    REGISTER_BY_EMAIL = "//span[text()='이메일']"
    REGISTER_EMAIL_INPUT = "//input[@name='email']"
    REGISTER_NEXT = "//button[text()='다음']"
    REGISTER_EMAIL_CODE_INPUT = "//input[@name='emailConfirmationCode']"
    REGISTER_NAME_INPUT = "//input[@name='fullName']"
    REGISTER_PASSWORD_INPUT = "//input[@name='password']"
    REGISTER_MONTH_SELECT = "//select[@title='월:']"
    REGISTER_DATE_SELECT = "//select[@title='일:']"
    REGISTER_YEAR_SELECT = "//select[@title='연도:']"
    REGISTER_AGREE_TERMS = "//input[@type='checkbox']"

    LOGIN_BUTTON = "//button[text()='로그인']"
    LOGIN_USERNAME_INPUT = "//input[@name='username']"
    LOGIN_PASSWORD_INPUT = "//input[@name='password']"
    LOGIN_SUBMIT_BUTTON = "//button[@type='submit']"

    SAVE_INFO_LATER = "//button[text()='나중에 하기']"
    CANCEL = "//button[text()='취소']"
    LIKE = "//a[contains(@href,'/liked_by/')]"
    LATER = "//button[text()='나중에 하기']"
    FOLLOW = "//div[text()='팔로우']"
