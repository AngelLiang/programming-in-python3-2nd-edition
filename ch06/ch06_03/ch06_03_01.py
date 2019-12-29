import os
import pickle


class ImageError(Exception):
    pass


class CoordinateError(ImageError):
    pass


class LoadError(ImageError):
    pass


class NoFilenameError(ImageError):
    pass


class ExportError(ImageError):
    pass


class Image:
    def __init__(self, width, height, filename='', background='#FFFFFF'):
        self.filename = filename
        self.__background = background
        self.__data = {}
        self.__width = width
        self.__height = height
        self.__colors = {self.__background}

    @property
    def background(self):
        return self.__background

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def colors(self):
        return set(self.__colors)

    def __getitem__(self, coordinate):
        # 传递给项存储方法的左边是长度为2的序列，并使用断言来确保满足这一约束。
        assert len(coordinate) == 2, 'coordinate should be a 2-tuple'
        # 如果超过取值范围，就产生自定义异常
        if (not (0 < coordinate[0] < self.width) or not (0 <= coordinate[1] < self.height)):
            raise CoordinateError(str(coordinate))
        return self.__data.get(tuple(coordinate), self.__background)

    def save(self, filename=None):
        if filename is not None:
            self.filename = filename
        if not self.filename:
            raise NoFilenameError()

        fh = None
        try:
            fh = open(self.filename, 'rb')
            data = pickle.load(fh)
            (self.__width, self.__height, self.__background, self.__data) = data
            self.__colors = (set(self.__data.values()) | {self.__background})
        except (EnvironmentError, pickle.UnpicklingError) as err:
            raise LoadError(str(err))
        finally:
            if fh is not None:
                fh.close()

    def export(self, filename):
        if filename.lower().endswith('.xpm'):
            self.__export_xpm(filename)
        else:
            raise ExportError('unsupported export format:' +
                              os.path.splitext(filename)[1])


# 如何使用该类
border_color = '#FF0000'  # red
square_color = '#0000FF'  # blue
width, height = 240, 60
midx, midy = width//2, height//2
image = Image(width, height, 'square_ext.img')
for x in range(width):
    for y in range(height):
        if x < 5 or x >= width - 5 or y < 5 or y >= height-5:
            image[x, y] = border_color
        elif midx - 20 < x < midx + 20 and midy - 20 < y < midy + 20:
            image[x, y] = square_color
image.save()
image.export('square_eye.xpm')
