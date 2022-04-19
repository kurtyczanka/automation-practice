import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver

scenarios('../features/shopping flow/shopping flow.feature')

