import pytest
import pytest_check
import allure
import func_api as api
import func_ui as ui
import random

symb = 'zxcvbnmasdfghjklqwertyuiop'


class RESULT:
    name_prj = ''
    check_dir = '/test_res'
    create_flag = False
    send_flag = False
    delete_flag = False
    clean_flag = False
    gen_flag = False


def init_data():
    response = RESULT
    for i in range(6):
        response.name_prj += random.choice(symb)
    print(response.name_prj)
    return response


def init_invalid():
    invalid = RESULT
    for i in range(6):
        invalid.name_prj += random.choice(symb)
    return invalid


class Test_API:

    @allure.epic("Валидки")
    @allure.story("Рбота с валидными значениями")
    @allure.title('Тестирование отправки корректных данных в новый проект')
    @pytest.mark.parametrize("name_prj, check_dir,res", [(init_data().name_prj, init_data().check_dir, 200),
                                              (init_data().name_prj, init_data().check_dir, 200),
                                              (init_data().name_prj, init_data().check_dir, 200),
                                              (init_data().name_prj, init_data().check_dir, 200)])
    def test_upload_files(self, upload_json, name_prj, check_dir, res):
        with allure.step("Создание нового проекта"):
            create_flag = api.create_project(name_prj)
            assert create_flag == 200
        with allure.step("Отправка файлов"):
            send_flag = api.send_test_allure(name_prj, check_dir)
        with allure.step("Проверка ответов сервера"):
            pytest_check.equal(send_flag, 200)
            api.delete_test_project(name_prj)





    # @allure.story("Тестирование UI")
    # @pytest.mark.parametrize("foo,name_step, res", [(ui.check_title(), 'Проверка названия сервера', True),
    #                                                 (ui.check_theme(), 'Тестирование изменения темы', True),
    #                                                 (ui.check_window(),
    #                                                  'Тестирование отступов при изменении размера окна', True),
    #                                                 (ui.check_create_project(),
    #                                                  'Создание проекта через интерфейс', True),
    #                                                 (ui.check_delete_project(),
    #                                                  'Удаление сучествующего проекта через интерфейс', True),
    #                                                 (ui.check_slide_panel(),
    #                                                  'Тестирование вспомогательной выдвижной панели', True)])
    # def test_ui(self, foo, name_step, res):
    #     with allure.step(name_step):
    #         pytest_check.equal(foo, res)


    