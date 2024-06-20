import pytest
import pytest_check
import allure
import func_api as api
import func_ui as ui
import random

# def init_data():
#     response = RESULT
#     for i in range(6):
#         response.name_prj += random.choice(symb)
#     print(response.name_prj)
#     return response
#
#
# def init_invalid():
#     invalid = RESULT
#     for i in range(6):
#         invalid.name_prj += random.choice(symb)
#     return invalid



class Test_API:

    @allure.title('Тестирование отправки корректных данных в новый проект и генерации отчета')
    def test_valid_upload(self, init_valid_data):
        print("name of test project is --"+init_valid_data.name_prj+"--")
        with allure.step("Создание нового проекта"):
            create_flag = api.create_project(init_valid_data.name_prj)
            pytest_check.equal(create_flag, 201)
        with allure.step("Отправка файлов"):
            send_flag = api.send_test_allure(init_valid_data.name_prj, init_valid_data.check_dir)
            pytest_check.equal(send_flag, 200)
        with allure.step("Генерация отчета"):
            gen_flag = api.gen_our_res(init_valid_data.name_prj)
            pytest_check.equal(gen_flag, 200)
        with allure.step("Очищение результата"):
            clean_hist_flag = api.clean_history(init_valid_data.name_prj)
            pytest_check.equal(clean_hist_flag, 200)
        with allure.step("Отчищение результатов"):
            clean_res_flag = api.clean_results(init_valid_data.name_prj)
            pytest_check.equal(clean_res_flag, 200)
        with allure.step("Удаление тестового проекта"):
            del_flag = api.delete_test_project(init_valid_data.name_prj)
            pytest_check.equal(del_flag, 200)

    @allure.title('Создание проекта с невалидным именем')
    def test_invalid_name(self, init_invalid_data):
        print("name of test project is --" + init_invalid_data.name_prj + "--")
        with allure.step("Создание проекта c не валидным значением"):
            create_flag = api.create_project(init_invalid_data.name_prj)
            pytest_check.equal(create_flag, 400)

    @allure.title('Создание проекта с 500 символьным именем')
    def test_invalid_name(self, init_longlong_data):
        print("name of test project is --" + init_longlong_data.name_prj + "--")
        with allure.step("Создание проекта"):
            create_flag = api.create_project(init_longlong_data.name_prj)
            pytest_check.equal(create_flag, 201)

    @allure.title('Создание проекта с различным нулевыми именами')
    @pytest.mark.parametrize("name_prj", [(''), (' ')])
    def test_zero_name(self, name_prj):
        print("name of test project is --" + name_prj + "--")
        with allure.step("Создание проеекта"):
            create_flag = api.create_project(name_prj)
            pytest_check.equal(create_flag, 400)

    @allure.title('Создание 2 проекта с одинаковым именем')
    def test_double_name(self, init_valid_data):
        print("name of test project is --" + init_valid_data.name_prj + "--")
        with allure.step("Создание нового проекта"):
            create_flag = api.create_project(init_valid_data.name_prj)
            pytest_check.equal(create_flag, 201)
        with allure.step("Создание второго проекта"):
            create_flag = api.create_project(init_valid_data.name_prj)
            pytest_check.equal(create_flag, 400)
        with allure.step("Удаление тестового проекта"):
            del_flag = api.delete_test_project(init_valid_data.name_prj)
            pytest_check.equal(del_flag, 200)

    @allure.title('Отправка невалидных файлов')
    def test_send_invalid_files(self, init_valid_data, init_invalid_data):
        print("name of test project is --" + init_valid_data.name_prj + "--")
        with allure.step("Создание нового проекта"):
            create_flag = api.create_project(init_valid_data.name_prj)
            pytest_check.equal(create_flag, 201)
        with allure.step("Отправка файлов"):
            send_flag = api.send_test_allure(init_valid_data.name_prj, init_invalid_data.check_dir)
            pytest_check.equal(send_flag, 400)
        with allure.step("Удаление тестового проекта"):
            del_flag = api.delete_test_project(init_valid_data.name_prj)
            pytest_check.equal(del_flag, 200)

    @allure.title('Двойное удаление одного проекта файлов')
    def test_double_delete(self, init_valid_data):
        print("name of test project is --" + init_valid_data.name_prj + "--")
        with allure.step("Создание нового проекта"):
            create_flag = api.create_project(init_valid_data.name_prj)
            pytest_check.equal(create_flag, 201)
        with allure.step("Удаление тестового проекта"):
            del_flag = api.delete_test_project(init_valid_data.name_prj)
            pytest_check.equal(del_flag, 200)
        with allure.step("Второе удаление тестового проекта"):
            del_flag = api.delete_test_project(init_valid_data.name_prj)
            pytest_check.equal(del_flag, 404)

class Test_UI:

    def test_name_server(self):
        with allure.step('Проверка названия сервера'):
            pytest_check.equal(ui.check_title(), True)

    def test_theme(self):
        with allure.step('Изменение темы'):
            pytest_check.equal(ui.check_theme(), True)

    def test_check_window(self):
        with allure.step('Тестирование отступов при изменении размера окна'):
            pytest_check.equal(ui.check_window(), True)

    def test_create_new_proj(self):
        with allure.step('Создание проекта через интерфейс'):
            pytest_check.equal(ui.check_create_project(), True)

    def test_delete_proj(self):
        with allure.step('Удаление сучествующего проекта через интерфейс'):
            pytest_check.equal(ui.check_delete_project(), True)

    def test_slide_panel(self):
        with allure.step('Тестирование вспомогательной выдвижной панели'):
            pytest_check.equal(ui.check_slide_panel(), True)




    