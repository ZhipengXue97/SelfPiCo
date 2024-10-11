if not self.encoding and len(self.content) > 3:
    encoding = guess_json_utf(self.content)