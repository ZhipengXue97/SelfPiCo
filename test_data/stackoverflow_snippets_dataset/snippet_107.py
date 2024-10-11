# Extracted from https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it
with open('some_file.pkl', "wb") as fp:
    pickle.dump(fig, fp, protocol=4)

