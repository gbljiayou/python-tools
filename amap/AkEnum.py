import enum


class AKEnum(enum.Enum):
    MT_DISTINCE_AK = 'a66ad92abc1ec3bb814f1c1a5d49c76c', '美团-路线距离AK'
    DISTINCE_AK = '963bee9c3de8124c58b5402fcf4fcb96', '测试-路线距离AK'

    def __init__(self, value, desc):
        self._cn_name = value
        self._desc = desc

    @property
    def value(self):
        return self._cn_name

    @property
    def desc(self):
        return self._desc


if __name__ == "__main__":
    print(AKEnum.MT_DISTINCE_AK.value)
