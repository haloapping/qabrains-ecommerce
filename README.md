1. Install dependencies: `uv sync`
2. Run test and generate report: `pytest -n auto --alluredir test-report -s .`
3. Show report: `allure serve test-report/`
