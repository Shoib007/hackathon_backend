import enum

@enum.unique
class SectionEnum(enum.Enum):
    SECTION_A = 'SECTION A'
    SECTION_B = 'SECTION B'
    SECTION_C = 'SECTION C'
    SECTION_D = 'SECTION D'
    SECTION_E = 'SECTION E'

    @classmethod
    def choices(cls):
        return [ (sec.value, sec.name) for sec in cls]
    