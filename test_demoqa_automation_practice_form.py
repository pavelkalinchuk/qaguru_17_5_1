from selene import browser, be, have


def test_name():
    browser.element('[id="firstName"]').click().type("Pavel")
    browser.element('[id="lastName"]').click().type("Kalinchuk")
    assert browser.element('[id="firstName"]').should(be.visible).should(have.value('Pavel'))
    assert browser.element('[id="lastName"]').should(be.visible).should(have.value('Kalinchuk'))


def test_email():
    browser.element('[id="userEmail"]').click().type("pavelkalinchuk@mail.tst")
    assert browser.element('[id="userEmail"]').should(be.visible).should(have.value('pavelkalinchuk@mail.tst'))