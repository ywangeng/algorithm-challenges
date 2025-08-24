"""
Question:

Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.
"""


class File:
    def __init__(self, content):
        self.content = content
        self.pointer = 0

    def read7(self):
        if self.pointer >= len(self.content):
            return ""

        chunk = self.content[self.pointer:self.pointer + 7]

        self.pointer += 7
        return chunk


class Reader:
    def __init__(self, file):
        self.file = file
        self.buffer = ''

    def read_n(self, n):
        result = []

        if self.buffer:
            take = min(len(self.buffer), n)
            result.append(self.buffer[:take])
            self.buffer = self.buffer[take:]
            n -= take

        while n > 0:
            chunk = self.file.read7()
            if not chunk:
                break

            take = min(len(chunk), n)
            result.append(chunk[:take])
            n -= take

            if take < len(chunk):
                self.buffer = chunk[take:]
                break

        return ''.join(result)
