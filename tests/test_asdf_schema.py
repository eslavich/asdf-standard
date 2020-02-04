import pytest

from common import load_yaml, SCHEMAS_PATH


@pytest.mark.parametrize("path", SCHEMAS_PATH.glob("asdf-schema-*.yaml"))
def test_asdf_schema(path):
    # Asserting no exceptions here
    load_yaml(path)
