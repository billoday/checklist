

class ScreenDraw:
    def __init__(self):
        self.buffer = ''
        self.magic_char = '\033[F'
        self.num_lines = 0
        self.num_lines_to_wipe = 0

    def print(self, fmt_str):
        if '\n' in fmt_str:
            num_new_lines = fmt_str.count('\n') + 1
        else:
            num_new_lines = 1
        self.buffer += f'{fmt_str}\n'
        self.num_lines += num_new_lines

    def _wipe(self):
        if self.num_lines_to_wipe > 0:
            full_wipe = self.num_lines_to_wipe * self.magic_char
            print(full_wipe, end='', flush=True)
            self.num_lines_to_wipe = 0

    def draw(self):
        self._wipe()
        print(self.buffer)
        self.num_lines_to_wipe = self.num_lines
        self.num_lines = 0

