# azure-testing
![CircleCI](https://circleci.com/gh/azurelism/azure-testing.svg?style=shield&circle-token=277926b20a516528cc6e98b6d0daf052f9b3bfc9)](https://circleci.com/gh/azurelism/azure-testing)

- Language: Python
- Core Framework: pytest
- UI Interactions: Page Object Module

# Deployment
1. Enter the command in cmd being located in the folder path
`pip install -r requirements.txt`
2. Enter the command in cmd being located in the project folder path `pytest`
   - --browser <firefox, chrome, edge> to choose different browser, default is chrome
   - --html= (for pytest html reporting, for example, "--html=./reports/report.html")
# Dockerize
1. Make sure to specify the driver inside `tests/conftest.py` file with the browser container_name in docker-compose.yml
```
driver = webdriver.Remote(
   command_executor='http://chrome:4444/wd/hub', 
   desired_capabilities=caps, 
   options=chrome_options)
```
2. Run `docker-compose up -d --build`
3. Execute `docker-compose exec pytest bash` to connect to the pytest container
4. Run command to execute test `pytest --html=./reports/dev-report.html --browser chrome`
5. Execute `docker-compose down` when you want to quit