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
@allure.epic("Testing_docker_allure")
class TestAPI:
    @allure.title('Тестирование отправки корректных данных в новый проект')
    def test_upload_files(self):
        response = RESULT
        for i in range(6):
            response.name_prj += random.choice(symb)
        with allure.step("Создание нового проекта"):
            response.create_flag = api.create_project(response.name_prj)
        with allure.step("Отправка файлов"):
            response.send_flag = api.send_test_allure(response.name_prj, response.check_dir)
        with allure.step("Проверка ответов сервера"):
            pytest_check.equal(response.send_flag, 200)

    @allure.title('Пробное удаление')
    def test_delete_project(self):
        response = RESULT
        for i in range(6):
            response.name_prj += random.choice(symb)
        with allure.step("Создание нового проекта"):
            response.create_flag = api.create_project(response.name_prj)
        with allure.step("Удаление тестового проекта"):
            response.delete_flag = api.delete_test_project(response.name_prj)
        with allure.step("Проверка ответов сервера"):
            pytest_check.equal(response.delete_flag, 200)

    @allure.title('Отчистка истории в существующем проекте')
    def test_clean_history(self):
        response = RESULT
        for i in range(6):
            response.name_prj += random.choice(symb)
        with allure.step("Создание нового проекта"):
            response.create_flag = api.create_project(response.name_prj)
        with allure.step("Чистка истории проекта"):
            response.clean_flag = api.delete_test_project(response.name_prj)
        with allure.step("Проверка ответов сервера"):
            pytest_check.equal(response.clean_flag, 200)

    @allure.title('Проверка генерация отчёта')
    def test_generation_result(self):
        response = RESULT
        for i in range(6):
            response.name_prj += random.choice(symb)
        with allure.step("Создание нового проекта"):
            response.create_flag = api.create_project(response.name_prj)
        with allure.step("Генерирование отчета"):
            response.gen_flag = api.delete_test_project(response.name_prj)
        with allure.step("Проверка ответов сервера"):
            pytest_check.equal(response.gen_flag, 200)

    # @allure.story("Тестирование UI")
    # @pytest.mark.parametrize("foo,name_step, res", [(ui.check_title(),'Проверка названия сервера',True),
    #                                                 (ui.check_theme(),'Тестирование изменения темы',True),
    #                                                 (ui.check_window(),'Тестирование отступов при изменении размера окна',True),
    #                                                 (ui.check_create_project(),'Создание проекта через интерфейс',True),
    #                                                 (ui.check_delete_project(),'Удаление сучествующего проекта через интерфейс',True),
    #                                                 (ui.check_slide_panel(),'Тестирование вспомогательной выдвижной панели',True)])
    # def test_UI(self, foo, name_step, res):
    #     with allure.step(name_step):
    #         pytest_check.equal(foo, res)


    