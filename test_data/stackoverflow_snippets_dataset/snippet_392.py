# Extracted from https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder
import sh
sh.rm(sh.glob('/path/to/folder/*'))

