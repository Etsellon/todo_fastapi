from fastapi import HTTPException


class Tasks_not_found_exception(HTTPException):
    def __init__(self):
        super().__init__(404, "Задача не найдена", None)


class Incorrect_data_exception(HTTPException):
    def __init__(self):
        super().__init__(400, "Некорректные данные", None)
