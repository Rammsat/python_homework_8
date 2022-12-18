from demoqa_tests.model.pages import practice_form
from demoqa_tests.utils.scroll import scroll_to


def test_student_registration_form():
    practice_form.given_opened()

    # WHEN
    practice_form.input_data('#firstName', 'World')
    practice_form.input_data('#lastName', 'Peace')
    practice_form.input_data('#userEmail', 'qwe@mail.com')

    practice_form.choose_gender('Male')

    practice_form.input_data('#userNumber', '9998887755')

    practice_form.click('#dateOfBirthInput')
    practice_form.pick_month('May')
    practice_form.pick_year('1999')
    practice_form.pick_day(11)

    practice_form.input_subject('English')

    practice_form.choose_hobby('Sports')

    scroll_to('#currentAddress')
    practice_form.input_data('#currentAddress', 'Some address')

    practice_form.upload_picture('resources/image.PNG')

    practice_form.select_state('NCR')
    practice_form.select_city('Delhi')

    practice_form.submit()

    # THEN

    practice_form.validation_of_fields(
            'World Peace',
            'qwe@mail.com',
            'Male',
            '9998887755',
            '11 May,1999',
            'English',
            'Sports',
            'image.PNG',
            'Some address',
            'NCR Delhi'
    )
