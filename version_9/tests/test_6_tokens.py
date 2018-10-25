# tests/test_6_tokens.py

def test_list_tokens(client, global_data):
    rv = client.get('/api/v1/tokens',
        headers={'Authorization': global_data['token']}
    )
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert "tokens" in json_data
    assert len(json_data["tokens"]) == 1
    global_data['token_id'] = json_data["tokens"][0]["id"]


def test_delete_token_notfound(client, global_data):
    rv = client.delete('/api/v1/tokens/123469',
        headers={'Authorization': global_data['token']}
    )
    assert rv.status_code == 404


def test_delete_token_ok(client, global_data):
    rv = client.delete('/api/v1/tokens/'+str(global_data['token_id']),
        headers={'Authorization': global_data['token']}
    )
    assert rv.status_code == 200


def test_delete_all_tokens(client, global_data):
    rv = client.delete('/api/v1/tokens',
        headers={'Authorization': global_data['token_admin']}
    )
    assert rv.status_code == 200