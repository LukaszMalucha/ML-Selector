from selenium.webdriver.common.by import By


class HomePageLocators:

    QUESTION_FORM = By.ID, 'surveyElement'
    FORM_TITLE = By.CLASS_NAME, 'sv_header'
    QUESTION = By.CLASS_NAME, 'sv_q_title'
    FORM_FIELD = By.CLASS_NAME, 'circle'
    NEXT_BUTTON = By.CLASS_NAME, 'sv_next_btn'
    RESULTS = By.ID, 'results'
    COMPLETE_BUTTON = By.CLASS_NAME, 'sv_complete_btn'
