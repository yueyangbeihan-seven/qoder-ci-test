import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """测试健康检查端点"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'

def test_register(client):
    """测试用户注册"""
    response = client.post('/register',
        json={'username': 'testuser', 'password': 'testpass'})
    assert response.status_code == 200
    assert response.json['status'] == 'ok'

def test_login_success(client):
    """测试登录成功"""
    client.post('/register',
        json={'username': 'loginuser', 'password': 'pass123'})
    response = client.post('/login',
        json={'username': 'loginuser', 'password': 'pass123'})
    assert response.status_code == 200
    assert response.json['status'] == 'ok'

def test_login_wrong_password(client):
    """测试密码错误"""
    client.post('/register',
        json={'username': 'wronguser', 'password': 'correct'})
    response = client.post('/login',
        json={'username': 'wronguser', 'password': 'wrong'})
    assert response.status_code == 401
