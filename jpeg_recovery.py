class JPEGRecovery:

    def __init__(self, source: str):
        self.source = source

    def recover_as(self, dest: str):
        with open(self.source, 'rb') as fd:
            with open(dest, 'wb') as dfd:
                offset = 0
                while True:
                    chunk = fd.read(1024)
                    if not chunk:
                        break

                    if offset == 3:
                        offset = 0
                        chunk = chunk[::-1]

                    offset += 1
                    dfd.write(chunk)

    def recover(self):
        with open(self.source, 'rb+') as fd:
            offset = 3
            while True:
                fd.seek(offset * 1024)
                chunk = fd.read(1024)
                if not chunk:
                    break

                fd.seek(offset * 1024)
                fd.write(chunk[::-1])
                offset += 3
