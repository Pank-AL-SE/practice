import pytest
import pytest_check
import allure
import func_api as api
import func_ui as ui

create_flag = False
send_flag = False
delete_flag = False
clean_flag = False
gen_flag = False
@allure.epic("Testing_docker_allure")
class TestAPI:
    @allure.title('Тестирование отправки корректных данных в новый проект')
    def test_upload_files(self):
        with allure.step("Создание нового проекта"):
            create_flag = api.create_project()
        with allure.step("Отправка файлов"):
            send_flag = api.send_test_allure()
        with allure.step("Проверка ответов сервера"):
            pytest_check.equal(create_flag, send_flag, True)

    @allure.title('Пробное удаление')
    def test_delete_project(self):
        with allure.step("Создание нового проекта"):
            create_flag = api.create_project()
        with allure.step("Удаление тестового проекта"):
            delete_flag = api.delete_test_project()
        with allure.step("Проверка ответов сервера"):
            pytest_check.equal(create_flag, delete_flag, True)

    @allure.title('Отчистка истории в существующем проекте')
    def test_clean_history(self):
        with allure.step("Создание нового проекта"):
            create_flag = api.create_project()
        with allure.step("Чистка истории проекта"):
            clean_flag = api.delete_test_project()
        with allure.step("Проверка ответов сервера"):
            pytest_check.equal(create_flag, clean_flag, True)

    @allure.title('Проверка генерация отчёта')
    def test_generation_result(self):
        with allure.step("Создание нового проекта"):
            create_flag = api.create_project()
        with allure.step("Генерирование отчета"):
            gen_flag = api.delete_test_project()
        with allure.step("Проверка ответов сервера"):
            pytest_check.equal(create_flag, gen_flag, True)

    @allure.story("Тестирование UI")
    @pytest.mark.parametrize("foo,name_step, res", [(ui.check_title(),'Проверка названия сервера',True),
                                                    (ui.check_theme(),'Тестирование изменения темы',True),
                                                    (ui.check_window(),'Тестирование отступов при изменении размера окна',True),
                                                    (ui.check_create_project(),'Создание проекта через интерфейс',True),
                                                    (ui.check_delete_project(),'Удаление сучествующего проекта через интерфейс',True),
                                                    (ui.check_slide_panel(),'Тестирование вспомогательной выдвижной панели',True)])
    def test_UI(self, foo, name_step, res):
        with allure.step(name_step):
            pytest_check.equal(foo, res)


    