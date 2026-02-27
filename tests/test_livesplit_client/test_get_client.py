from splitguides.livesplit_client import get_client


def test_get_client():
    client = get_client("TCP", "servername", 12, 2)
    assert client.connection.server == "servername"
    assert client.connection.port == 12
    assert client.connection.timeout == 2
