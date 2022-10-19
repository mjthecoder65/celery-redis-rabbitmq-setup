import pytest
from starlette.testclient import TestClient
from fastapi import FastAPI
from main import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client  # testing happens here