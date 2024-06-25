run_API:
	pytest test/test_allure.py -k Test_API
run_UI:
	pytest test/test_allure.py -k Test_UI
result_API:
	pytest --alluredir=./res test/test_allure.py -k Test_API
	python3 test_lib/upload_json.py
result_UI:
	pytest --alluredir=./res test/test_allure.py -k Test_UI
	python3 test_lib/upload_json.py
result_all:
	pytest --alluredir=./res test/test_allure.py
	python3 test_lib/upload_json.py
result_upload:
	python3 test_lib/upload_json.py
clean:
	rm res/*