import pytest

expected_response = {
    'products': [
        {
            'title': 'tea',
            'count': 3
        }
    ]
}

@pytest.fixture()
def db():
    return {}

def test_available_tee_response_dict(db):
    assert isinstance(response, dict)


def test_available_tee_products_in_response(response):
    assert 'products' in response, f'fields in response {list(response.keys())}'

#
    assert len(response) == 1
    assert isinstance(response['products'], list)
    products = response['products']
    assert len(products) == 1
    product = products[0]
    assert isinstance(product, dict)
    assert product['title'] == 'tea'
    assert product['count'] == 3
    assert len(product) == 2
