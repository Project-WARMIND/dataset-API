from app.arguments import argparse
from app.api.main import start_flask


def main():
    args = argparse()
    start_flask()
