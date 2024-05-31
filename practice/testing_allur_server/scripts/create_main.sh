curl -X 'POST' \
  'http://localhost:5050/allure-docker-service/projects' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": "testing_allur_server"
}'