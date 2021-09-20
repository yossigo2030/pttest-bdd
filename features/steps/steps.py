from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@given(u'I am in the todos page')
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_argument("--disable_extensions")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.get("https://todomvc.com/examples/angularjs/#/")
    context.driver.implicitly_wait(100)
    # "ljlkl"


@when(u'I add new task "Clean my house"')
def step_impl(context):
    add_task(context, "Clean my house")

def add_task(context, task_name):
    new_to_do_item = context.driver.find_element_by_css_selector("form [placeholder='What needs to be done?']")
    new_to_do_item.click()
    new_to_do_item.send_keys(task_name + "\n")


@then(u'the task "Clean my house" will be added to the list')
def step_impl(context):
    assert(find_clean_my_house_item(context), "clean my house item was not added")

def find_clean_my_house_item(context):
    try:
        item_to_check = context.driver.find_element_by_css_selector(
            "body > ng-view > section > section > ul > li > div > label")
        if item_to_check.text == "Clean my house":
            return True
        else:
            return False
    except:
        return False
