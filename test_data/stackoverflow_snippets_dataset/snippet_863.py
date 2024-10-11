# Extracted from https://stackoverflow.com/questions/384759/how-do-i-convert-a-pil-image-into-a-numpy-array
def imshow(img):
    img = img / 2 + 0.5     # unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()

