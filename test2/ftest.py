import pytest
import allure


@allure.feature('Функциональное тестирование')
@allure.story(    'Ввод суммы для конвертации, получение результата, проверка того, что использовалась    введенная нами сумма')
@pytest.fixture(scope="session", autouse=True)
def set_up(request):
    x=100
    print("инит")
    def resource_teardown():
        print("resource_teardown")
    request.addfinalizer(resource_teardown)


@allure.step('Запуск браузера Chrome, открытие и загрузка страницы с кальулятором.')
@pytest.allure.step('1make_some_data_foo')

def test_01(set_up):
    y=90
    print (str(y))
    assert 100==100
@pytest.allure.step('2make_some_data_foo')
def test_02(set_up):

    assert 200==200

@pytest.allure.step('3make_some_data_foo')
def test_03(set_up):

    print("ytr")
    assert 300 == 300
@pytest.allure.step('4make_some_data_foo')
def test_04(set_up):
    assert 400 ==400
