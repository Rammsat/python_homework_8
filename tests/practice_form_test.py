from demoqa_tests.model.pages import practice_form


def test_student_registration_form():
    practice_form.given_opened()

    # WHEN
    practice_form.type_firstname('World')
    practice_form.type_lastname('Peace')
    practice_form.type_email('qwe@mail.com')

    practice_form.select_gender('Male')

    practice_form.type_phone_number('9998887755')

    practice_form.click_on_datepicker()
    practice_form.pick_month('May')
    practice_form.pick_year('1999')
    practice_form.pick_day(11)

    practice_form.type_subject('English')

    practice_form.select_hobby('Sports')

    practice_form.scroll_to_address()
    practice_form.type_address('Some address')

    practice_form.upload_picture('resources/image.PNG')

    practice_form.select_state('NCR')
    practice_form.select_city('Delhi')

    practice_form.submit()

    # THEN

    practice_form.assert_fields(
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
