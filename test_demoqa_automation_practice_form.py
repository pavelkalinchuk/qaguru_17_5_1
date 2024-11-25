from selene import browser, be, have


def test_positive_text():
    browser.element('[id="firstName"]').click().type("Pavel")
    browser.element('[id="lastName"]').click().type("Kalinchuk")
    assert browser.element('[id="firstName"]').should(be.visible).should(have.value('Pavel'))
    assert browser.element('[id="lastName"]').should(be.visible).should(have.value('Kalinchuk'))