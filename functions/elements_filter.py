from selenium.webdriver.common.by import By

def filter_elements(child_elements):
    filtered_elements = []

    for child_element in child_elements:
        anchor_tag = child_element.find_elements(By.TAG_NAME, "a")
        filtered_elements.append(child_element) if len(anchor_tag) > 0 else None

    return filtered_elements
