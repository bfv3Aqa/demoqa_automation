from selenium.webdriver.common.by import By


class TextBoxPageLocators:
	# form fields
	FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
	EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
	CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
	PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
	SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

	# created from
	CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
	CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
	CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
	CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
	EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title ='Expand all']")
	COLLAPSE_ALL_BUTTON = (By.CSS_SELECTOR, "button[title ='Collapse all']")
	ITEM_LIST = (By.CSS_SELECTOR, "span[class= 'rct-title']")
	CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
	TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
	OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class= 'text-success']")


class RadioButtonPageLocators:
	# radio buttons and result span
	RADIO_YES = (By.CSS_SELECTOR, "label[class^='custom-control'][for='yesRadio']")
	RADIO_IMPRESSIVE = (By.CSS_SELECTOR, "label[class^='custom-control'][for='impressiveRadio']")
	RADIO_NO = (By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
	OUTPUT_RESULT = (By.CSS_SELECTOR, "p span[class='text-success']")


class WebTablesPageLocators:
	# add form buttons and fields
	ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
	FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
	LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
	USER_EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
	AGE = (By.CSS_SELECTOR, "input[id='age']")
	SALARY = (By.CSS_SELECTOR, "input[id='salary']")
	DEPARTMENT = (By.CSS_SELECTOR, "input[id = 'department']")
	SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

	# table
	FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
	SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='searchBox']")
	DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
	ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
	NO_ROWS_FOUND = (By.CSS_SELECTOR, "div[class ='rt-noData']")
	COUNT_ROW_LIST = (By.CSS_SELECTOR, "select[aria-label='rows per page']")

	# update

	UPDATE_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")


class ButtonsPageLocators:
	# buttons

	DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
	RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id = 'rightClickBtn']")
	CLICK_ME_BUTTON = "//div[3]/button"
	DOUBLE_CLICK_OUTPUT_MESSAGE = (By.CSS_SELECTOR, "p[id = 'doubleClickMessage']")
	RIGHT_CLICK_OUTPUT_MESSAGE = (By.CSS_SELECTOR, "p[id = 'rightClickMessage']")
	CLICK_ME_OUTPUT_MESSAGE = (By.CSS_SELECTOR, "p[id = 'dynamicClickMessage']")


class LinksPageLocators:

	# links labels

	SIMPLE_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")
	BAD_REQUEST = (By.CSS_SELECTOR, "a[id = 'bad-request']")


class UploadAndDownloadPageLocators:

	DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "a[id='downloadButton']")
	UPLOAD_BUTTON = (By.CSS_SELECTOR, "input[id = 'uploadFile']")
	UPLOAD_PATH_LABEL = (By.CSS_SELECTOR, "p[id = 'uploadedFilePath']")
	DOWNLOAD_FILE = (By.CSS_SELECTOR, "a[id = 'downloadButton']")


class DynamicPropertiesPageLocators:

	COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, "button[id = 'colorChange']")
	VISIBLE_AFTER_FIVE_SEC_BUTTON = (By.CSS_SELECTOR, "button[id = 'visibleAfter']")
	ENABLE_BUTTON = (By.CSS_SELECTOR, "button[id = 'enableAfter']")
