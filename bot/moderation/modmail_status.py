"""Module containing a single Enum class for Modmails."""

from enum import Enum


class ModmailStatus(Enum):
    """An Enum class representing all the different statuses for Modmails."""
    OPEN = 1
    ASSIGNED = 2
    CLOSED = 3
