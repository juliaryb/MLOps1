from settings import Settings


def test_settings_are_loaded_correctly():
    settings = Settings()  # check if settings load correctly

    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "My MLOps App (Test)"
    assert settings.API_KEY == "fake-api-key-for-testing"
