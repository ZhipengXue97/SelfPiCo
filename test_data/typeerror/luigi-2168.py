module_name = os.path.basename(sys.argv[0]).rsplit('.', 1)[0]
d = d.replace(b'(c__main__', "(c" + module_name)