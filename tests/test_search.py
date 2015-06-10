import json

from models import Product


def _create_product(lat, lng, delta_id, tags=None):
    p = Product('567d07d533d541dd8ad4753622e76243' + delta_id,
                '4aa53e646bf84faca9a76c020b0682de',
                'testing and testing',
                0.99,
                0.66,
                lng,
                lat)
    if tags:
        p.tags = tags

    return p


def test_api(client):
    # setting up index
    from server.api import searcher
    lat = 41.8723889
    lng = 12.48018019999995
    items = [
        _create_product(41.876748, 12.469616, '1', tags=['ho']),
        _create_product(41.878522, 12.489014, '2', tags=['hej', 'ho']),  # 1km
        _create_product(41.863123, 12.500882, '3', tags=['hej'])  # 2km
    ]

    for item in items:
        searcher.idx.insert(int(item.id, 16),
                            (item.lat, item.lng,
                             item.lat, item.lng),
                            obj=item)

    # 1 km no tag
    res = client.get(
        '/search?count=10&radius=1001&lng={lng}&lat={lat}'.format(lng=lng, lat=lat))

    assert res.status_code == 200
    data = json.loads(res.data)
    assert len(data['products']) == 2

    # 2 km no tag
    res = client.get(
        '/search?count=10&radius=2001&lng={lng}&lat={lat}'.format(lng=lng, lat=lat))

    assert res.status_code == 200
    data = json.loads(res.data)
    assert len(data['products']) == 3

    # 2 km, tag hej
    res = client.get(
        '/search?count=10&radius=2001&lng={lng}&lat={lat}&tags[]=hej'.format(lng=lng, lat=lat))

    assert res.status_code == 200
    data = json.loads(res.data)
    assert len(data['products']) == 2

    # 2 km, tag ho
    res = client.get(
        '/search?count=10&radius=2001&lng={lng}&lat={lat}&tags[]=ho'.format(lng=lng, lat=lat))

    assert res.status_code == 200
    data = json.loads(res.data)
    assert len(data['products']) == 2

    # 1 km, tag ho
    res = client.get(
        '/search?count=10&radius=1001&lng={lng}&lat={lat}&tags[]=ho'.format(lng=lng, lat=lat))

    assert res.status_code == 200
    data = json.loads(res.data)
    assert len(data['products']) == 2

    # 1 km, tag hej
    res = client.get(
        '/search?count=10&radius=1001&lng={lng}&lat={lat}&tags[]=hej'.format(lng=lng, lat=lat))

    assert res.status_code == 200
    data = json.loads(res.data)
    assert len(data['products']) == 1
    assert data['products'][0]['id'] == '567d07d533d541dd8ad4753622e762432'
    assert data['products'][0]['popularity'] == 0.99
    assert data['products'][0]['quantity'] == 0.66
    assert data['products'][0]['shop'][
        'id'] == '4aa53e646bf84faca9a76c020b0682de'
    assert data['products'][0]['shop']['lat'] == 41.878522
    assert data['products'][0]['shop']['lng'] == 12.489014
    assert data['products'][0]['title'] == 'testing and testing'
    assert len(data['products'][0].keys()) == 5
    assert len(data['products'][0]['shop'].keys()) == 3
