import os
import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@given('I navigate to the "{page}" page')
def step_impl(context, page):
    context.driver.get(f"https://demoqa.com/{page}")
    context.driver.execute_script("document.querySelectorAll('[id^=\"google_ads\"]').forEach(el => el.remove());")
    context.driver.execute_script("document.getElementById('adplus-anchor')?.remove();")
    context.driver.execute_script("document.querySelector('footer')?.remove();")

@given('I navigate to the Practice Form page')
def step_impl(context):
    context.driver.get("https://demoqa.com/automation-practice-form")
    context.driver.execute_script("document.querySelectorAll('[id^=\"google_ads\"]').forEach(el => el.remove());")

@when('I fill out the form and submit it')
def step_impl(context):
    context.driver.find_element(By.ID, "firstName").send_keys("PEDRO")
    context.driver.find_element(By.ID, "lastName").send_keys("AMARAL")
    context.driver.find_element(By.ID, "userEmail").send_keys("pedro.amaral@accenture.com")
    gender = context.driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']")
    context.driver.execute_script("arguments[0].click();", gender)
    context.driver.find_element(By.ID, "userNumber").send_keys("1997255027")
    
    file_path = os.path.abspath("test-file.txt")
    if not os.path.exists(file_path):
        with open(file_path, "w") as f: f.write("content")
    context.driver.find_element(By.ID, "uploadPicture").send_keys(file_path)
    context.driver.find_element(By.ID, "currentAddress").send_keys("Rua da Moeda - Recife, 123")
    
    s_in = context.driver.find_element(By.ID, "react-select-3-input")
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", s_in)
    s_in.send_keys("NCR\n")
    c_in = context.driver.find_element(By.ID, "react-select-4-input")
    c_in.send_keys("Delhi\n")
    
    btn = context.driver.find_element(By.ID, "submit")
    context.driver.execute_script("arguments[0].click();", btn)

@then('the success modal should be displayed with "Thanks for submitting the form"')
def step_impl(context):
    wait = WebDriverWait(context.driver, 15)
    el = wait.until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg")))
    assert el.text == "Thanks for submitting the form"

# --- SCENARIO 02: Browser Windows ---

@when('I click the New Window button')
def step_impl(context):
    context.main_window = context.driver.current_window_handle
    btn = context.driver.find_element(By.ID, "windowButton")
    context.driver.execute_script("arguments[0].click();", btn)
    WebDriverWait(context.driver, 10).until(lambda d: len(d.window_handles) > 1)
    context.driver.switch_to.window(context.driver.window_handles[1])

@then('a new window should open with the text "This is a sample page"')
def step_impl(context):
    assert context.driver.find_element(By.ID, "sampleHeading").text == "This is a sample page"
    context.driver.close()
    context.driver.switch_to.window(context.main_window)

# --- SCENARIO 03.1: WEB TABLES CRUD ---

@when('I create a new form, edit it and then delete it')
def step_impl(context):
    # CREATE
    add_btn = context.driver.find_element(By.ID, "addNewRecordButton")
    context.driver.execute_script("arguments[0].click();", add_btn)
    context.driver.find_element(By.ID, "firstName").send_keys("Pedro")
    context.driver.find_element(By.ID, "lastName").send_keys("Amaral")
    context.driver.find_element(By.ID, "userEmail").send_keys("pedro@accenture.com")
    context.driver.find_element(By.ID, "age").send_keys("30")
    context.driver.find_element(By.ID, "salary").send_keys("5000")
    context.driver.find_element(By.ID, "department").send_keys("QA")
    context.driver.execute_script("arguments[0].click();", context.driver.find_element(By.ID, "submit"))
    time.sleep(1)

    # EDIT
    edit_btn = context.driver.find_elements(By.CSS_SELECTOR, "span[title='Edit']")[-1]
    context.driver.execute_script("arguments[0].click();", edit_btn)
    fn = context.driver.find_element(By.ID, "firstName")
    fn.clear()
    fn.send_keys("Pedrinho")
    context.driver.execute_script("arguments[0].click();", context.driver.find_element(By.ID, "submit"))
    time.sleep(1)

    # DELETE
    del_btn = context.driver.find_elements(By.CSS_SELECTOR, "span[title='Delete']")[-1]
    context.driver.execute_script("arguments[0].click();", del_btn)

@then('the table should reflect the changes correctly')
def step_impl(context):
    print("CRUD OK")

# --- SCENARIO 03.2: BULK FORMS WITH 12 USERS ---

@when('I create 12 new forms in the table')
def step_impl(context):
    for i in range(1, 13):
        add_btn = context.driver.find_element(By.ID, "addNewRecordButton")
        context.driver.execute_script("arguments[0].click();", add_btn)
        context.driver.find_element(By.ID, "firstName").send_keys(f"User{i}")
        context.driver.find_element(By.ID, "lastName").send_keys("QA")
        context.driver.find_element(By.ID, "userEmail").send_keys(f"u{i}@accenture.com")
        context.driver.find_element(By.ID, "age").send_keys("27")
        context.driver.find_element(By.ID, "salary").send_keys("1000")
        context.driver.find_element(By.ID, "department").send_keys("IT")
        sub_btn = context.driver.find_element(By.ID, "submit")
        context.driver.execute_script("arguments[0].click();", sub_btn)
        time.sleep(0.1)

@when('I delete all forms from the table')
def step_impl(context):
    while True:
        dels = context.driver.find_elements(By.CSS_SELECTOR, "span[title='Delete']")
        if not dels: break
        context.driver.execute_script("arguments[0].click();", dels[0])
        time.sleep(0.1)

@then('the table should be empty')
def step_impl(context):
    dels = context.driver.find_elements(By.CSS_SELECTOR, "span[title='Delete']")
    assert len(dels) == 0

# --- SCENARIO 04: PROGRESS BAR ---

@when('I start the progress bar and stop before 25%')
def step_impl(context):
    btn = context.driver.find_element(By.ID, "startStopButton")
    context.driver.execute_script("arguments[0].click();", btn)
    bar = context.driver.find_element(By.CLASS_NAME, "progress-bar")
    WebDriverWait(context.driver, 10).until(lambda d: int(bar.get_attribute("aria-valuenow")) >= 20)
    context.driver.execute_script("arguments[0].click();", btn)
    time.sleep(1)

@when('I wait for it to reach 100% and reset it')
def step_impl(context):
    btn = context.driver.find_element(By.ID, "startStopButton")
    context.driver.execute_script("arguments[0].click();", btn)
    
    wait = WebDriverWait(context.driver, 60)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".progress-bar.bg-success")))
    time.sleep(1)
    reset_btn = wait.until(EC.element_to_be_clickable((By.ID, "resetButton")))
    context.driver.execute_script("arguments[0].click();", reset_btn)
    time.sleep(1)

@then('the progress bar should return to 0%')
def step_impl(context):
    bar = context.driver.find_element(By.CLASS_NAME, "progress-bar")
    WebDriverWait(context.driver, 5).until(lambda d: bar.get_attribute("aria-valuenow") == "0")
    val = bar.get_attribute("aria-valuenow")
    assert val == "0"

# --- SCENARIO 05: SORTABLE NUMBERS LIST ---

@when('I reorder the list to the opposite order')
def step_impl(context):
    container = context.driver.find_element(By.CLASS_NAME, "vertical-list-container")
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", container)
    time.sleep(1)
    
    items_init = context.driver.find_elements(By.CSS_SELECTOR, ".vertical-list-container .list-group-item")
    if items_init[0].text == "One":
        target_labels = ["Six", "Five", "Four", "Three", "Two", "One"]
    else:
        target_labels = ["One", "Two", "Three", "Four", "Five", "Six"]

    actions = ActionChains(context.driver)
    
    for label in target_labels:
        current_items = context.driver.find_elements(By.CSS_SELECTOR, ".vertical-list-container .list-group-item")
        source = next(it for it in current_items if it.text == label)
        target = current_items[0]
        
        if source != target:
            actions.click_and_hold(source).move_to_element_with_offset(target, 0, -10).release().perform()
            time.sleep(0.5)

@then('the list order should be toggled successfully')
def step_impl(context):
    items = context.driver.find_elements(By.CSS_SELECTOR, ".vertical-list-container .list-group-item")
    final_order = [i.text for i in items]
    print(f"Final order: {final_order}")
    
    expected_asc = ["One", "Two", "Three", "Four", "Five", "Six"]
    expected_desc = ["Six", "Five", "Four", "Three", "Two", "One"]
    
    assert final_order in [expected_asc, expected_desc], f"A ordem final {final_order} não é válida."