from src.exception import CoustomException
import sys

try:
    a = 1/0
except Exception as e:
    raise CoustomException(e, sys)
