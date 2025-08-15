import logging

def test_hello():
    logging.basicConfig(level=logging.INFO)
    logging.info("Hi, Test Running at it's best")
    assert "hello".upper() == "HELLO"
