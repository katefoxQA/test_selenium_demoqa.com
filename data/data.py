from dataclasses import dataclass


@dataclass
class Person:
    full_name: str
    first_name: str
    last_name: str
    email: str
    age: int
    salary: int
    department: str
    cur_addr: str
    per_addr: str

@dataclass
class Color:
    color_name: list = None

@dataclass
class Date:
    day: str
    month: str
    year: str
    time: str

@dataclass
class PersonForm:
    first_name: str
    last_name: str
    email: str
    mobile: int
    cur_addr: str

@dataclass
class Subject:
    subject_name: list = None

@dataclass
class State:
    state_name: list = None

@dataclass
class City:
    city_name: list = None

@dataclass
class NegativeEmail:
    negative_email: list = None





