from app.arguments import argparse
from tests.main import test
from app.api.main import start_flask


def main():
    args = argparse()
    if args.test:
        test()
    else:
        start_flask()
