docker run -p 5050:5050 -e CHECK_RESULTS_EVERY_SECONDS=NONE -e KEEP_HISTORY=1 \
           -v ${PWD}/projects:/app/projects \
           frankescobar/allure-docker-service

docker run -p 5252:5252 -e ALLURE_DOCKER_PUBLIC_API_URL=http://localhost:5050 \
           frankescobar/allure-docker-service-ui