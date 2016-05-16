from bmi_exceptions import DBException


# this exception should be raised when a project is not found in the db
class ProjectNotFoundException(DBException):
    def __str__(self):
        return "project not found"


# this exception should be raised when an image is not found in the db
class ImageNotFoundException(DBException):
    def __str__(self):
        return "image not found"


# this class is a wrapper for any orm specific exception like sqlalchemy
class ORMException(DBException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "ORM related error = " + self.message
