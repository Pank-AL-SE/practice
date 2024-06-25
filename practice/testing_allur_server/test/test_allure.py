import pytest_check
import allure
import pytest
from test_lib import gen_data_prj as generator
from test_lib import func_api as api
from test_lib import func_ui as ui
import logging

# logger = logging.Logger


class Test_API:

    @pytest.mark.parametrize("project_name, project_dir", [(generator.gen_valid_data().name_prj,
                                                            generator.gen_valid_data().check_dir)])
    @allure.title('Тестирование отправки корректных данных в новый проект и генерации отчета')
    def test_valid_upload(self, create_test_project, project_name, project_dir):
        # print("name of test project is --"+init_valid_data+"--")
        with allure.step("Создание нового проекта"):
            create_test_project(project_name)
        with allure.step("Отправка файлов"):
            send_flag = api.send_test_allure(project_name, project_dir)
            pytest_check.equal(send_flag, 200)
        with allure.step("Генерация отчета"):
            gen_flag = api.gen_our_res(project_name)
            pytest_check.equal(gen_flag, 200)
        with allure.step("Очищение результата"):
            clean_hist_flag = api.clean_history(project_name)
            pytest_check.equal(clean_hist_flag, 200)
        with allure.step("Отчищение результатов"):
            clean_res_flag = api.clean_results(project_name)
            pytest_check.equal(clean_res_flag, 200)

    @pytest.mark.parametrize("project_name", [(generator.gen_invalid_data().name_prj)])
    @allure.title('Создание проекта с невалидным именем')
    def test_invalid_name(self, create_test_project, project_name):

        with allure.step("Создание проекта c не валидным значением"):
            create_test_project(project_name)
            search_flag = api.search_project(project_name)
            pytest_check.equal(search_flag, 404)

    @pytest.mark.parametrize("project_name", [(generator.gen_longlong_data().name_prj)])
    @allure.title('Создание проекта с 500 символьным именем')
    def test_longlong_name(self, create_test_project, project_name):
        print("name of test project is --" + project_name + "--")
        with allure.step("Создание проекта"):
            create_test_project(project_name)
        with allure.step("Удаление"):
            del_flag = api.delete_test_project(project_name)
            pytest_check.equal(del_flag, 200)

    @allure.title('Создание проекта с различным нулевыми именами')
    @pytest.mark.parametrize("name_prj", [(''), (' ')])
    def test_zero_name(self, create_test_project, name_prj):
        print("name of test project is --" + name_prj + "--")
        with allure.step("Создание проеекта"):
            create_test_project(name_prj)
            search_flag = api.search_project(name_prj)
            pytest_check.equal(search_flag, 404)

    @pytest.mark.parametrize("project_name", [(generator.gen_valid_data().name_prj)])
    @allure.title('Создание 2 проекта с одинаковым именем')
    def test_double_name(self,create_test_project, project_name):
        print("name of test project is --" + project_name + "--")
        with allure.step("Создание нового проекта"):
            create_test_project(project_name)
            search_flag = api.search_project(project_name)
            pytest_check.equal(search_flag, 200)
        with allure.step("Создание второго проекта"):
            create_flag = api.create_project(project_name)
            pytest_check.equal(create_flag, 400)
        with allure.step("Удаление тестового проекта"):
            del_flag = api.delete_test_project(project_name)
            pytest_check.equal(del_flag, 200)

    @pytest.mark.parametrize("project_name, dir_name", [(generator.gen_valid_data().name_prj,
                                                         generator.gen_invalid_data().check_dir)])
    @allure.title('Отправка невалидных файлов')
    def test_send_invalid_files(self, create_test_project, project_name, dir_name):
        print("name of test project is --" + project_name + "--")
        with allure.step("Создание нового проекта"):
            create_test_project(project_name)
            search_flag = api.search_project(project_name)
            pytest_check.equal(search_flag, 200)
        with allure.step("Отправка файлов"):
            send_flag = api.send_test_allure(project_name, dir_name)
            pytest_check.equal(send_flag, 400)
        with allure.step("Удаление тестового проекта"):
            del_flag = api.delete_test_project(project_name)
            pytest_check.equal(del_flag, 200)

    @pytest.mark.parametrize("project_name, dir_name", [(generator.gen_valid_data().name_prj,
                                                         generator.gen_valid_data().check_dir)])
    @allure.title('Двойное удаление одного проекта файлов')
    def test_double_delete(self, create_test_project, project_name, dir_name):
        print("name of test project is --" + project_name+ "--")
        with allure.step("Создание нового проекта"):
            create_test_project(project_name)
            search_flag = api.search_project(project_name)
            pytest_check.equal(search_flag, 200)
        with allure.step("Удаление тестового проекта"):
            del_flag = api.delete_test_project(project_name)
            pytest_check.equal(del_flag, 200)
        with allure.step("Второе удаление тестового проекта"):
            del_flag = api.delete_test_project(project_name)
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




    