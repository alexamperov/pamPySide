import os, struct

class Database:
    def __init__(self):
        self.fVars = []
        self.keyPhrase = "Ы7м:чpТfрь}Kг%rЪqЯм!СМCР17.ЕPЬЫдФКдРxзШ2MFЮ{NЪCБbь+e,бUg0i3ЩCцHы"
        self.openDB()

    def openFile(self, fn, mode):
        try:
            if 'ReadOnly' in str(mode):
                self.file = open(fn, 'rb')
            elif 'WriteOnly' in str(mode):
                self.file = open(fn, 'wb')
            else:
                return False
            self.keyOffset = 0
            return True
        except:
            return False

    def closeFile(self):
        if self.file:
            self.file.close()
            self.file = None

    def getStr(self):
        # Читаем длину (4 байта, big-endian)
        length_bytes = self.file.read(4)
        if len(length_bytes) < 4:
            return ""
        length = struct.unpack('>I', length_bytes)[0]

        if length == 0xFFFFFFFF:
            return ""

        # Читаем данные строки
        string_bytes = self.file.read(length)
        if len(string_bytes) < length:
            return ""

        # Декодируем UTF-16BE
        try:
            self.buffer = string_bytes.decode('utf-16be')
        except UnicodeDecodeError:
            # Пробуем UTF-16LE
            try:
                self.buffer = string_bytes.decode('utf-16le')
            except UnicodeDecodeError:
                # Пробуем с BOM
                self.buffer = (b'\xfe\xff' + string_bytes).decode('utf-16be')

        return self.crypt(self.buffer)

    def getInt(self):
        s = self.getStr()
        try:
            return int(s) if s else 0
        except:
            return 0

    def crypt(self, data):
        """Точная эмуляция C++ кода с защитой от выхода за пределы"""
        result = ""
        for i in range(len(data)):
            # Если keyOffset в пределах строки, берем символ, иначе 0
            if 0 <= self.keyOffset < len(self.keyPhrase):
                key_char = ord(self.keyPhrase[self.keyOffset])
            else:
                key_char = 0  # Эмулируем неопределенное поведение C++

            # XOR операция
            xor_val = ord(data[i]) ^ key_char
            result += chr(xor_val)
            self.shiftKeyOffset()
        return result

    def shiftKeyOffset(self):
        """Точная копия C++ кода: if (keyPhrase.count() != keyOffset) keyOffset++; else keyOffset = 0;"""
        if len(self.keyPhrase) != self.keyOffset:
            self.keyOffset += 1
        else:
            self.keyOffset = 0

    def openDB(self, fn="C:\\Users\\theAmperov\\PyCharmProjects\\PySideTest\\tabs\\VariantList.pam-db"):
        """Открытие файла базы данных"""

        if not os.path.exists(fn):
            return False

        if self.openFile(fn, 'ReadOnly'):
            # Читаем сигнатуру
            signature = self.getStr()

            if signature == "pam-db":

                # Читаем версию
                self.fVersion = self.getStr()

                # Читаем состояние проверки
                self.checkState = self.getInt()

                # Читаем размеры таблицы
                rows = self.getInt()
                cols = self.getInt()

                # Очищаем таблицу
                self.fVars.clear()
                self.fVars = [[] for _ in range(rows)]

                # Читаем данные
                for i in range(rows):
                    if len(self.fVars[i]) == 0:
                        self.fVars[i] = ["" for _ in range(cols)]

                    for j in range(cols):
                        value = self.getStr()
                        self.fVars[i][j] = value

                self.closeFile()
                return True
            else:
                self.closeFile()
                return False
        else:
            return False
