import json
import pytest

def test_get_root(client):
    response = client.get('/')
    assert response.status_code == 200

@pytest.mark.dependency
def test_create_model(client,get_superuser_token_headers, face_by_face_model, created_item_data):
    r = client.post(
        '/models/',
        data=json.dumps(face_by_face_model),
        headers=get_superuser_token_headers
        )

    response = r.json()
    assert r.status_code == 201
    assert 'id' in response
    assert 'Location' in r.headers
    # set the values to be used by the rest of the tests
    created_item_data['id'] = response['id']
    created_item_data['location'] = r.headers['location']


@pytest.mark.dependency(depends=['test_create_model'])
def test_get_models(client, get_superuser_token_headers):
  r = client.get('/models/', headers=get_superuser_token_headers)

  assert r.status_code == 200

  assert r.headers['link'] == '<http://https://api.pollination.cloud/models?page=2&per_page=25>; rel="next",<http://https://api.pollination.cloud/models?page=1&per_page=25>; rel="last"'

  response = r.json()

  assert len(response) == 1

@pytest.mark.dependency(depends=['test_create_model'])
def test_get_model(client, get_superuser_token_headers, created_item_data):
    location = created_item_data['location']
    rid = created_item_data['id']
    r = client.get(
        f"{location}",
        headers=get_superuser_token_headers
    )

    assert r.status_code == 200

    response = r.json()
    assert response['type'] == 'Model'
    assert response['id'] == rid
    assert response['face_count'] == 6
    created_item_data['faces_url'] = response['faces_url']

@pytest.mark.dependency(depends=['test_get_model'])
def test_get_faces(client, get_superuser_token_headers, created_item_data):
    location = created_item_data['faces_url']
    r = client.get(
      f"{location}",
      headers=get_superuser_token_headers
    )

    assert r.status_code == 200

    assert r.headers['link'] == '<http://https://api.pollination.cloud/models?page=2&per_page=25>; rel="next",<http://https://api.pollination.cloud/models?page=1&per_page=25>; rel="last"'

    response = r.json()
    assert len(response) == 6

@pytest.mark.dependency(depends=['test_get_faces'])
def test_delete_model(client, get_superuser_token_headers, created_item_data):
    mid = created_item_data['id']
    r = client.delete(
      f"/models/{mid}",
      headers=get_superuser_token_headers
    )

    assert r.status_code == 204

    location = created_item_data['faces_url']
    r = client.get(
      f"{location}",
      headers=get_superuser_token_headers
    )

    assert r.status_code == 200
    
    response = r.json()
    assert len(response) == 0

    location = created_item_data['location']
    rid = created_item_data['id']
    r = client.get(
        f"{location}",
        headers=get_superuser_token_headers
    )

    assert r.status_code == 404