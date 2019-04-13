from flask_app.camera.gcp_vision_multi_img import proccess_picture

# def test_status(client):
#     assert client.get('/api/status').data == b"status"
#     # client.get('/api/snap')
#
def test_register_in_ocean(client):
    client.get('/api/register')

# def test_process_pictures():
#     result = proccess_picture()