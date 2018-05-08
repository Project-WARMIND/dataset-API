from argparse import ArgumentParser


def argparse():
    parser = ArgumentParser(description="Project-WARMIND dataset-API")
    parser.add_argument("--test", action="store_true", help="Tests API")
    args = parser.parse_args()
    return args
