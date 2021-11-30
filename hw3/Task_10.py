"""������� ������� circumference, ������� ��������� ����� ����������
���� ������ ������ ���� ��������� ����������� ���������� DistanceError � ���������� 'radius can`t less than 0'"""
from math import pi


class DistanceError(Exception):
    pass


def circumference(r):
    if r < 0:
        raise DistanceError('radius can`t less than 0')
    return pi * (2 * r)
