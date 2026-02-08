1. Install dependencies: `uv sync`
2. Run test and generate report: `uv run pytest -s -vv -n auto --alluredir test-report .`
3. Show report: `uv run allure serve test-report`
