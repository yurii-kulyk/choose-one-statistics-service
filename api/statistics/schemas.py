from enum import Enum

from core.schemas import CamelModel


class EventType(Enum):
    WON = 'WON'
    SELECTED = 'SELECTED'
    TOOK_PART = 'TOOK_PART'
    TOOK_PART_IN_POLL = 'TOOK_PART_IN_POLL'


class CreateUpdateOptionSchema(CamelModel):
    poll_id: int
    option_id: int
    event_type: EventType


class CalculatedOptionSchema(CamelModel):
    option_id: int
    choose_percentage: int
    win_percentage: int


class ResponseOptionSchema(CamelModel):
    poll_id: int
    option_id: int
    selected_times: int
    won_times: int
    took_part_times: int

    class Config:
        orm_mode = True
