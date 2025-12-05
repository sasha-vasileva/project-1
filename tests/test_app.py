from app import create_app


def test_index_get():
    app = create_app({'TESTING': True})
    client = app.test_client()
    rv = client.get('/')

    assert rv.status_code == 200
    assert b'Find out' in rv.data or b'Year' in rv.data


def test_post_leap_year():
    app = create_app({'TESTING': True})
    client = app.test_client()
    rv = client.post('/', data={'year': '2000'})
    # esperamos el texto 'Yes' (or 'No')
    assert (b'Yes' in rv.data) or (b'No' in rv.data)


def test_post_invalid():
    app = create_app({'TESTING': True})
    client = app.test_client()
    rv = client.post('/', data={'year': '0'})
    assert b'Invalid' in rv.data
