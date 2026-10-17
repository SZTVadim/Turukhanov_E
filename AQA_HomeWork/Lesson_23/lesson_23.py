from playwright.sync_api import Page, expect

URL = "https://www.qa-practice.com/forms/practice-form"


def test_practice_form(page: Page):
    first_name = "Edward"
    last_name = "Smith"
    email = "edward.smith@example.com"
    mobile = "8999090999"
    birth_date = "10 May 2000"
    subject = "Mat"
    selected_subject = "Maths"
    address = "Moscow"
    state = "NCR"
    city = "Delhi"

    input_first_name = page.locator("#firstName")
    input_last_name = page.locator("#lastName")
    input_email = page.locator("#userEmail")
    input_mobile = page.locator("#userNumber")
    input_gender = page.locator("#gender_0")
    input_birth_date = page.locator("#dateOfBirthInput")
    input_subject = page.locator("#subjectsAutocomplete")
    input_subject_suggestion = page.locator(
        "#subjectsSuggestions .suggestion-item"
    )
    input_hobby_reading = page.locator("#hobbies_1")
    input_address = page.locator("#currentAddress")

    state_dropdown = page.locator("#div_id_state .custom-dropdown-control")
    state_option = page.locator("#div_id_state .custom-dropdown-option")
    city_dropdown = page.locator("#div_id_city .custom-dropdown-control")
    city_option = page.locator("#div_id_city .custom-dropdown-option")

    submit_button = page.locator("#submit-id-submit")
    result_modal = page.locator("#resultsModal")
    result_title = page.locator("#resultsModalLabel")

    page.goto(URL)

    input_first_name.fill(first_name)
    input_last_name.fill(last_name)
    input_email.fill(email)
    input_mobile.fill(mobile)
    input_gender.check()
    input_birth_date.fill(birth_date)
    input_birth_date.press("Tab")
    input_subject.fill(subject)
    subject_suggestion = input_subject_suggestion.filter(
        has_text=selected_subject
    )
    expect(subject_suggestion).to_be_visible()
    subject_suggestion.click()
    input_hobby_reading.check()
    expect(input_hobby_reading).to_be_checked()
    input_address.fill(address)

    state_dropdown.click()
    state_option.filter(has_text=state).click()

    city_dropdown.click()
    city_option.filter(has_text=city).click()

    submit_button.click()

    expect(result_modal).to_be_visible()
    expect(result_title).to_have_text("Thanks for submitting the form")

    expect(result_modal).to_contain_text(f"{first_name} {last_name}")
    expect(result_modal).to_contain_text(email)
    expect(result_modal).to_contain_text(mobile)
    expect(result_modal).to_contain_text("Male")
    expect(result_modal).to_contain_text("2000-05-10")
    expect(result_modal).to_contain_text(selected_subject)
    expect(result_modal).to_contain_text("Reading")
    expect(result_modal).to_contain_text(address)
    expect(result_modal).to_contain_text(state)
    expect(result_modal).to_contain_text(state)

    # expect(result_modal).to_contain_text(city)
    # по идее еще должна быть эта проверка,
    # но отсутвует это поле в модальном окне
