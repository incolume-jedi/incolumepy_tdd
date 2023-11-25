"""# TODO: Atividade 30: Consumir dados da API httpbin.org.

Proceder com as implementações necessárias para que passe nos testes
"""
from sys import version_info
from unittest import mock

import pytest
from incolume.py.tdd.api_consumption.my_ip_httpbin import (
    HTTPStatus,
    __reference__,
    client,
    get_my_ip,
)

__author__ = '@britodfbr'  # pragma: no cover


@pytest.mark.skipif(
    version_info <= (3, 8, 0),
    reason='This run only Python 3.8 or higher',
)
class TestAPI:
    """Test API."""

    @pytest.fixture()
    def fake_requests(self: 'TestAPI') -> mock.Mock:
        """Fake requests.get."""
        return mock.Mock(
            name='requests.get',
            **{
                'return_value': '2',
                'json.return_value': {'origin': '1.2.3.4'},
                'status_code': HTTPStatus.OK,
            },
        )

    def test_reference_pack(self: 'TestAPI') -> None:
        """Test reference pack."""
        assert 'incolume.py.tdd.api_consumption.my_ip_httpbin' in __reference__

    @mock.patch(f'{__reference__}.requests.get')
    def test_get_my_ip_ip(
        self: 'TestAPI',
        mock_requests_get: mock.Mock,
        fake_requests: mock.Mock,
    ) -> None:
        """Test myip."""
        mock_requests_get.return_value = fake_requests
        assert '1.2.3.4' in get_my_ip()

    @mock.patch(f'{__reference__}.requests.get')
    def test_get_my_ip_called(
        self: 'TestAPI',
        mock_requests_get: mock.Mock,
        fake_requests: mock.Mock,
    ) -> None:
        """Test myip."""
        mock_requests_get.return_value = fake_requests
        get_my_ip()
        mock_requests_get.assert_called_once()

    @mock.patch(f'{__reference__}.requests.get')
    def test_get_my_ip_called_httpbin(
        self: 'TestAPI',
        mock_requests_get: mock.Mock,
        fake_requests: mock.Mock,
    ) -> None:
        """Test myip."""
        mock_requests_get.return_value = fake_requests
        get_my_ip()
        mock_requests_get.assert_called_once_with('https://httpbin.org/ip')

    @pytest.mark.parametrize(
        'entrance',
        [
            HTTPStatus.NOT_FOUND,
            HTTPStatus.HTTP_VERSION_NOT_SUPPORTED,
            HTTPStatus.BAD_REQUEST,
            HTTPStatus.CONFLICT,
            HTTPStatus.FORBIDDEN,
        ],
    )
    @mock.patch(f'{__reference__}.requests.get')
    def test_get_my_ip_status_code(
        self: 'TestAPI',
        mock_requests_get: mock.Mock,
        fake_requests: mock.Mock,
        entrance: HTTPStatus,
    ) -> None:
        """Test myip."""
        fake_requests.status_code = entrance
        mock_requests_get.return_value = fake_requests
        with pytest.raises(client.HTTPException, match=entrance.phrase):
            get_my_ip()
