import os
from student import Student
from student_list import StudentList
from file_manager import FileManager


def test_student_str_and_to_dict():
    s = Student("Ivan", "0631112233", "ivan@gmail.com", "KB-251")
    assert str(s) == "Name = Ivan, Phone = 0631112233, Email = ivan@gmail.com, Group = KB-251"
    d = s.to_dict()
    assert d["name"] == "Ivan"
    assert d["group"] == "KB-251"


def test_student_list_add_and_sort():
    sl = StudentList()
    sl.add_student(Student("Vlad", "0634", "v@", "KB"))
    sl.add_student(Student("Dima", "0633", "d@", "KB"))
    sl.add_student(Student("Ivan", "0631", "i@", "KB"))

    assert len(sl) == 3
    assert sl.students[0].name == "Dima"
    assert sl.students[1].name == "Ivan"
    assert sl.students[2].name == "Vlad"


def test_student_list_delete():
    sl = StudentList()
    sl.add_student(Student("Dima", "0633", "d@", "KB"))
    sl.add_student(Student("Ivan", "0631", "i@", "KB"))

    assert sl.delete_student("Ivan") is True
    assert len(sl) == 1
    assert sl.students[0].name == "Dima"
    assert sl.delete_student("NonExisting") is False


def test_student_list_update():
    sl = StudentList()
    sl.add_student(Student("Ivan", "0631", "i@", "KB"))
    assert sl.update_student("Ivan", new_name="Anton") is True
    assert sl.students[0].name == "Anton"


def test_file_manager_save_and_load(tmp_path):
    test_csv = tmp_path / "test_lab_03.csv"
    sl = StudentList()
    sl.add_student(Student("Dima", "0633334455", "dima@gmail.com", "KB-251"))
    sl.add_student(Student("Vlad", "0634445566", "vlad@gmail.com", "KB-251"))

    FileManager.save_to_csv(str(test_csv), sl)
    assert os.path.exists(test_csv)

    loaded_list = FileManager.load_from_csv(str(test_csv))
    assert len(loaded_list) == 2
    assert loaded_list.students[0].name == "Dima"
    assert loaded_list.students[1].name == "Vlad"