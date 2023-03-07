class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_value = 0

        for i in range(len(value)):
            if rom_val[value[i]] > rom_val[value[i - 1]]:
                int_value += rom_val[value[i]] - 2*rom_val[value[ i - 1]]
            else:
                int_value += rom_val[value[i]]

        return cls(int_value)

    @classmethod
    def from_string(cls, value):
        pass
