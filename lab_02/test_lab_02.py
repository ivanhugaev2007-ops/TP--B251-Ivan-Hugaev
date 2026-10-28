import os
from lab_02 import addElemToSortedList, deleteElem, findPosition, load_from_csv, save_to_csv


def test_findPosition():
    data = [
        {"name": "Dima", "phone": "0633", "email": "d@", "group": "KB"},
        {"name": "Ivan", "phone": "0631", "email": "i@", "group": "KB"},
        {"name": "Vlad", "phone": "0634", "email": "v@", "group": "KB"},
    ]
    assert findPosition(data, "Anton") == 0
    assert findPosition(data, "Ilia") == 1
    assert findPosition(data, "Zak") == 3


def test_addElemToSortedList():
    data = [
        {"name": "Dima", "phone": "0633", "email": "d@", "group": "KB"},
        {"name": "Ivan", "phone": "0631", "email": "i@", "group": "KB"},
    ]
    new_student = {"name": "Ilia", "phone": "0632", "email": "il@", "group": "KB"}
    addElemToSortedList(data, new_student)
    assert len(data) == 3
    assert data[1]["name"] == "Ilia"


def test_deleteElem_success():
    data = [
        {"name": "Dima", "phone": "0633", "email": "d@", "group": "KB"},
        {"name": "Ivan", "phone": "0631", "email": "i@", "group": "KB"},
    ]
    assert deleteElem(data, "Ivan") is True
    assert len(data) == 1
    assert data[0]["name"] == "Dima"


def test_deleteElem_not_found():
    data = [{"name": "Dima", "phone": "0633", "email": "d@", "group": "KB"}]
    assert deleteElem(data, "Unknown") is False
    assert len(data) == 1


def test_csv_save_and_load(tmp_path):
    test_file = tmp_path / "test_lab_02.csv"
    initial_data = [
        {"name": "Dima", "phone": "0633", "email": "d@", "group": "KB"},
        {"name": "Vlad", "phone": "0634", "email": "v@", "group": "KB"},
    ]
    save_to_csv(str(test_file), initial_data)
    assert os.path.exists(test_file)

    loaded = load_from_csv(str(test_file))
    assert len(loaded) == 2
    assert loaded[0]["name"] == "Dima"
    assert loaded[1]["name"] == "Vlad"