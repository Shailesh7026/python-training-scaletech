
# pytest mock and patch 
# def test_get_user_data(mocker):
#     mock_res = mocker.Mock()
#     mock_res.json.return_value = {'id': 42, 'name': 'Shailesh'}
    
#     mocker.patch("app.req.get", return_value=mock_res)
    
#     from app import get_user_data
#     result = get_user_data()
    
#     # 4. This will now pass!
#     assert result == {'id': 42, 'name': 'Shailesh'}
  
# unittest mock and patch
from unittest.mock import Mock, patch

def test_get_user_data_built_in():
    # Use standard Mock() instead of mocker.Mock()
    mock_res = Mock()
    mock_res.json.return_value = {"id": 42, "name": "Shailesh"}
    
    with patch("app.req.get", return_value=mock_res):
        from app import get_user_data
        result = get_user_data()
        assert result == {'id': 42, 'name': 'Shailesh'}

    
