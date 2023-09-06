# Trading Platform Project

This project simulates a trading platform with RESTful API and WebSocket support.

## Setup and Usage

1. Clone this repository.

2. Build the Docker containers:

   ```bash
   docker-compose build
3. Up the docker container and run the tests
 ```bash
 docker-compose up -d.
(venv) (base) vlodc@MacBook-Air test-trade-platform-vc % docker-compose up -d 
[+] Running 3/3
 ✔ Network test-trade-platform-vc_default    Created                                                                                                         0.0s 
 ✔ Container test-trade-platform-vc-tests-1  Started                                                                                                         0.3s 
 ✔ Container test-trade-platform-vc-api-1    Started                                                                                                         0.3s 
(venv) (base) vlodc@MacBook-Air test-trade-platform-vc % docker-compose exec tests bash
service "tests" is not running
(venv) (base) vlodc@MacBook-Air test-trade-platform-vc % pytest
====================================================================== test session starts =======================================================================
platform darwin -- Python 3.10.9, pytest-7.4.1, pluggy-1.3.0
rootdir: /Users/vlodc/PycharmProjects/test-trade-platform-vc
configfile: pytest.ini
plugins: metadata-3.0.0, anyio-3.7.1, html-4.0.0, asyncio-0.17.1, flask-1.2.0
asyncio: mode=legacy
collected 4 items                                                                                                                                                

tests/test_api.py ....                                                                                                                                     [100%]

======================================================================== warnings summary ========================================================================
../../venv/lib/python3.10/site-packages/pytest_asyncio/plugin.py:186
  /Users/vlodc/venv/lib/python3.10/site-packages/pytest_asyncio/plugin.py:186: DeprecationWarning: The 'asyncio_mode' default value will change to 'strict' in future, please explicitly use 'asyncio_mode=strict' or 'asyncio_mode=auto' in pytest configuration file.
    config.issue_config_time_warning(LEGACY_MODE, stacklevel=2)

tests/test_api.py::test_create_order
  /Users/vlodc/venv/lib/python3.10/site-packages/pytest_asyncio/plugin.py:312: DeprecationWarning: '@pytest.fixture' is applied to <fixture monkeypatch, file=/Users/vlodc/venv/lib/python3.10/site-packages/_pytest/monkeypatch.py, line=29> in 'legacy' mode, please replace it with '@pytest_asyncio.fixture' as a preparation for switching to 'strict' mode (or use 'auto' mode to seamlessly handle all these fixtures as asyncio-driven).
    warnings.warn(

tests/test_api.py::test_create_order
  /Users/vlodc/venv/lib/python3.10/site-packages/starlette/testclient.py:234: DeprecationWarning: There is no current event loop
    loop = asyncio.get_event_loop()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- Generated html report: file:///Users/vlodc/PycharmProjects/test-trade-platform-vc/report.html ----------------------------------
================================================================= 4 passed, 3 warnings in 4.52s ==================================================================
verify the report with the rests

(venv) (base) vlodc@MacBook-Air test-trade-platform-vc % docker-compose up -d 
[+] Running 3/3
 ✔ Network test-trade-platform-vc_default    Created                                                                                                         0.0s 
 ✔ Container test-trade-platform-vc-tests-1  Started                                                                                                         0.3s 
 ✔ Container test-trade-platform-vc-api-1    Started                                                                                                         0.3s 
(venv) (base) vlodc@MacBook-Air test-trade-platform-vc % docker-compose exec tests bash
service "tests" is not running
(venv) (base) vlodc@MacBook-Air test-trade-platform-vc % pytest
====================================================================== test session starts =======================================================================
platform darwin -- Python 3.10.9, pytest-7.4.1, pluggy-1.3.0
rootdir: /Users/vlodc/PycharmProjects/test-trade-platform-vc
configfile: pytest.ini
plugins: metadata-3.0.0, anyio-3.7.1, html-4.0.0, asyncio-0.17.1, flask-1.2.0
asyncio: mode=legacy
collected 4 items                                                                                                                                                

tests/test_api.py ....                                                                                                                                     [100%]

======================================================================== warnings summary ========================================================================
../../venv/lib/python3.10/site-packages/pytest_asyncio/plugin.py:186
  /Users/vlodc/venv/lib/python3.10/site-packages/pytest_asyncio/plugin.py:186: DeprecationWarning: The 'asyncio_mode' default value will change to 'strict' in future, please explicitly use 'asyncio_mode=strict' or 'asyncio_mode=auto' in pytest configuration file.
    config.issue_config_time_warning(LEGACY_MODE, stacklevel=2)

tests/test_api.py::test_create_order
  /Users/vlodc/venv/lib/python3.10/site-packages/pytest_asyncio/plugin.py:312: DeprecationWarning: '@pytest.fixture' is applied to <fixture monkeypatch, file=/Users/vlodc/venv/lib/python3.10/site-packages/_pytest/monkeypatch.py, line=29> in 'legacy' mode, please replace it with '@pytest_asyncio.fixture' as a preparation for switching to 'strict' mode (or use 'auto' mode to seamlessly handle all these fixtures as asyncio-driven).
    warnings.warn(

tests/test_api.py::test_create_order
  /Users/vlodc/venv/lib/python3.10/site-packages/starlette/testclient.py:234: DeprecationWarning: There is no current event loop
    loop = asyncio.get_event_loop()

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- Generated html report: file:///Users/vlodc/PycharmProjects/test-trade-platform-vc/report.html ----------------------------------
