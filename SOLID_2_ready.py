

class Person:
    def __init__(self, name, age, sex, height, weight, address):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.address = address

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_sex(self, sex):
        self.sex = sex

    def set_height(self, height):
        self.height = height

    def set_weight(self, weight):
        self.weight = weight

    def set_address(self, address):
        self.address = address

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_sex(self):
        return self.sex

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_address(self):
        return self.address



class Document:
    def __init__(self, id, type, creation_date, modification_date, author, content):
        self.id = id
        self.type = type
        self.creation_date = creation_date
        self.modification_date = modification_date
        self.author = author
        self.content = content

    def set_id(self, id):
        self.id = id

    def set_type(self, type):
        self.type = type

    def set_creation_date(self, creation_date):
        self.creation_date = creation_date

    def set_modification_date(self, modification_date):
        self.modification_date = modification_date

    def set_author(self, author):
        self.author = author

    def set_content(self, content):
        self.content = content

    def get_id(self):
        return self.id

    def get_type(self):
        return self.type

    def get_creation_date(self):
        return self.creation_date

    def get_modification_date(self):
        return self.modification_date

    def get_author(self):
        return self.author

    def get_content(self):
        return self.content



class Library:
    def __init__(self):
        self.documents = []

    def add_document(self, document):
        self.documents.append(document)

    def remove_document(self, document):
        self.documents.remove(document)

    def find_document_by_id(self, id):
        for document in self.documents:
            if document.get_id() == id:
                return document
        return None

    def find_document_by_type(self, type):
        result = []
        for document in self.documents:
            if document.get_type() == type:
                result.append(document)
        return result

    def find_document_by_author(self, author):
        result = []
        for document in self.documents:
            if document.get_author() == author:
                result.append(document)
        return result

    def find_document_by_content(self, content):
        result = []
        for document in self.documents:
            if content in document.get_content():
                result.append(document)
        return result