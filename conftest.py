import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    # Добавляем считывание параметра --language из командной строки (по умолчанию 'en')
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: e.g. es, fr, ru, en")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    
    # Настраиваем параметры Chrome для смены языка интерфейса
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    
    print(f"\nStart chrome browser for test with language: {user_language}..")
    browser = webdriver.Chrome(options=options)
    
    yield browser
    
    print("\nQuit browser..")
    browser.quit()
