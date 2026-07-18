import pytest
from student import *


def setup_function():
    students.clear()


def test_add_student():
    assert add_student(1, "Alice") == True


def test_add_duplicate_student():
    add_student(1, "Alice")
    assert add_student(1, "Bob") == False


def test_search_existing_student():
    add_student(1, "Alice")
    assert search_student(1) == "Alice"


def test_search_non_existing_student():
    assert search_student(5) is None


def test_remove_existing_student():
    add_student(1, "Alice")
    assert remove_student(1) == True


def test_remove_non_existing_student():
    assert remove_student(5) == False


def test_update_existing_student():
    add_student(1, "Alice")
    assert update_student(1, "Bob") == True


def test_updated_name():
    add_student(1, "Alice")
    update_student(1, "Bob")
    assert search_student(1) == "Bob"


def test_update_non_existing_student():
    assert update_student(10, "John") == False


def test_student_count():
    add_student(1, "Alice")
    add_student(2, "Bob")
    assert len(students) == 2