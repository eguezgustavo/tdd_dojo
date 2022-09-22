# (a+b)*(a*b)
from example_3.main import weird_operation

def test__weird_operation__returns_6__when_give_2_and_1_and_sum_service_returns_3_and_multiple_service_return_2(mocker):
    # arrange
    number_a = 2
    number_b = 1
    sum_service_mock = mocker.Mock()
    multiple_service_mock = mocker.Mock()
    
    # act
    result = weird_operation(
        sum_service_mock, 
        multiple_service_mock, 
        number_a, 
        number_b
    )
    
    # assert
    sum_service_mock.assert_called_with(number_a, number_b)
    multiple_service_mock.assert_called_with(number_a, number_b)
    assert result == 6
