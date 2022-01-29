from unittest import mock
from sunday.lib import try_me

def test_try_me():
    with mock.patch('builtins.input', return_value='golf'):
        assert try_me() == 'CORRECT!'
