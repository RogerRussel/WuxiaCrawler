from .crowler import crowler


class wuxiaworld(crowler):

    url = "http://www.wuxiaworld.com/col-index/"
    path = ".data/wuxiaworld"

    def getIndex(self):
        page = crowler.getUrl(self.url)



        filename = self.path + "/col/index"
        crowler.writeFile(filename, index)
