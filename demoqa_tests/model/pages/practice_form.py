from selene import have, command
from selene.support.shared import browser
from demoqa_tests.model.controls import dropdown
from demoqa_tests.model.controls import date_picker
from demoqa_tests.utils import path_to_file


def given_opened():
    browser.open('/automation-practice-form')


def submit():
    browser.element('#submit').press_enter()


def select_state(value):
    dropdown.select('#state', by_text=value)


def select_city(value):
    dropdown.select('#city', by_text=value)


def input_data(element, data):
    browser.element(element).type(data)


def choose_gender(gender):
    browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()


def choose_hobby(hobby):
    browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobby)).click()


def pick_month(month):
    browser.element('.react-datepicker__month-select').click()
    date_picker.date('.react-datepicker__month-select', month)


def pick_year(year):
    browser.element('.react-datepicker__year-select').click()
    date_picker.date('.react-datepicker__year-select', year)


def pick_day(day):
    browser.element(f'.react-datepicker__day--0{day}').click()


def click(selector):
    browser.element(selector).click()


def input_subject(subject):
    browser.element('#subjectsInput').type(subject).press_enter()


def upload_picture(path_to_picture):
    path_to_file.create_path('#uploadPicture', path_to_picture)


def validation_of_fields(*args):
    browser.element('.table').all('td').even.should(have.texts(args))
