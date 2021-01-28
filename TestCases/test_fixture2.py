import pytest


@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    @pytest.mark.smoke
    @pytest.mark.xfail(reason="Math as it is =(")
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        assert 1==2

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_second_smiling_faces(self, prepare_faces):
        assert 2==2
