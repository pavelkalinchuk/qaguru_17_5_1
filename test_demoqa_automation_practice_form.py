import time

from selene import browser, be, have


def test_name():
    browser.element('[id="firstName"]').click().type("Pavel")
    browser.element('[id="lastName"]').click().type("Kalinchuk")
    assert browser.element('[id="firstName"]').should(be.visible).should(have.value('Pavel'))
    assert browser.element('[id="lastName"]').should(be.visible).should(have.value('Kalinchuk'))


def test_email():
    browser.element('[id="userEmail"]').click().type("pavelkalinchuk@mail.tst")
    assert browser.element('[id="userEmail"]').should(be.visible).should(have.value('pavelkalinchuk@mail.tst'))


def test_gender():
    browser.element('label[for="gender-radio-1"]').click()
    assert browser.element('#gender-radio-1').should(be.selected)


def test_mobile():
    browser.element('#userNumber').click().type("99-23-67-0")
    assert browser.element('#userNumber').should(be.visible).should(have.value('99-23-67-0'))


def test_date_of_birth():
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker-popper').should(be.visible)
    browser.element('.react-datepicker__month-select').should(be.visible).element('[value="0"]').click()
    browser.element('.react-datepicker__year-select').should(be.visible).element('[value="2000"]').click()
    browser.element('.react-datepicker__week').should(be.visible).element('.react-datepicker__day.react-datepicker__day--001').click()
    assert browser.element('#dateOfBirthInput').should(have.value('01 Jan 2000'))


'''
def test_subject():
    pass


def test_hobbies():
    pass


def test_pictures():
    pass


def test_current_address():
    pass


def test_state_nd_city():
    pass


def test_submit():
    pass
'''
