import study.ai


def test_package_importable() -> None:
    assert study.ai.__name__ == "study.ai"
