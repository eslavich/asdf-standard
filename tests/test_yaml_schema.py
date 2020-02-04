import pytest

from common import load_yaml, YAML_SCHEMA_PATH, list_schema_paths


@pytest.mark.parametrize("path", list_schema_paths(YAML_SCHEMA_PATH))
def test_yaml_schema(path):
    # Asserting no exceptions here
    load_yaml(path)
