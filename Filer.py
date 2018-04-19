class Filer:

    @staticmethod
    def writeItemsToFile(items, filename):
        with open(filename, 'w') as f:
            for line in items:
                f.write(str(line) + "\n")

    @staticmethod
    def readItemsFromFileToList(filename):
        with open(filename) as f:
            lst = f.readlines()
            # you may also want to remove whitespace characters like `\n` at the end of each line
            return [x.strip() for x in lst]

    @staticmethod
    def appendItemToFile(item, filename):
        with open(filename, 'a') as f:
            password = str(item) + "\n"
            f.write(password)

    @staticmethod
    def removeItemFromFile(item_to_remove, filename):
        items = Filer.readItemsFromFileToList(filename)
        items.remove(str(item_to_remove))
        Filer.writeItemsToFile(items, filename)