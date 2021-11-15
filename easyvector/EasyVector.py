import math
from abc import ABC, abstractmethod


class EasyVector(ABC):
    """
    This is the base class which contains every useful method that every vector class should contain.
    """
    @abstractmethod
    def __init__(self) -> None:
        """
        Depending on the dimension, access elements with x, y, z.
        """

    @property
    @abstractmethod
    def normalize(self) -> "EasyVector":
        """
        Creates a normalized version of this vector.
        :rtype: EasyVector
        :return: Normalized vector
        """

    @abstractmethod
    def extend(self, extender: float) -> None:
        """
        Multiplies all elements of the vector by extender.
        :param extender: Amount to multiply the elements.
        """

    @property
    @abstractmethod
    def magnitude(self) -> float:
        """
        :return: Returns the magnitude of this vector.
        """
        pass

    @abstractmethod
    def distance(self, other: "EasyVector") -> float:
        """
        Calculates the distance between two vectors.
        :param other: the other vector
        :return: returns the length
        """

    @abstractmethod
    def determinant(self, other: "EasyVector") -> float:
        """
        Calculates the determinate between 2 vectors
        :param other: the other vector
        :return: Returns the determinant
        """

    @abstractmethod
    def angle(self, other: "EasyVector" = None) -> float:
        """
        If other is None calculates the angle between 0 degrees and 360 degrees with the x-axis.
        Otherwise calculates the angle between the 2 vectors.
        :param other: The other vector.
        :return: Returns an angle.
        """

    @abstractmethod
    def __add__(self, other: "EasyVector") -> "EasyVector":
        """
        Adds each element of this vector with the elements of the other vector.
        :param other: The other vector.
        :return: Returns a new EasyVector.
        """

    @abstractmethod
    def __iadd__(self, other: "EasyVector") -> None:
        """
        Does same as __add__ but with +=.
        """

    @abstractmethod
    def __mul__(self, other: "EasyVector") -> float:
        """
        Creates the scalar between this vector and the other vector.
        :param other: The other vector.
        :return: Returns the scalar.
        """

    @abstractmethod
    def __len__(self) -> int:
        """
        :return: Returns the amount of elements ergo the dimension.
        """

    @abstractmethod
    def __eq__(self, other: "EasyVector") -> bool:
        """
        Checks if both vectors are the same.
        :param other: The other vector.
        :return: Returns true if the vector is the same else false.
        """

    @abstractmethod
    def __getitem__(self, index: int) -> float:
        """
        Gets the item in the specified index, 0 = x, 1 = y, 2 = z.
        :param index: Index number.
        :return: Returns the element.
        """

    @abstractmethod
    def __iter__(self) -> list[float]:
        """
        :return: Returns the iterable going through each element
        """

    @abstractmethod
    def __str__(self) -> str:
        """
        :return: Returns the string representation.
        """

    @abstractmethod
    def __repr__(self) -> str:
        """
        :return: Returns the repr of this vector.
        """


class EasyVector2D(EasyVector):
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self._vec_len = 2

    @property
    def normalize(self) -> "EasyVector2D":
        general = self.magnitude
        return EasyVector2D(self.x / general, self.y / general)

    def extend(self, extender: float):
        self.x *= extender
        self.y *= extender

    @property
    def magnitude(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def distance(self, other: "EasyVector2D") -> float:
        if len(other) != self._vec_len:
            raise IndexError
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def determinant(self, other: "EasyVector2D") -> float:
        return other.x * self.y - other.y * self.x

    def angle(self, other: "EasyVector2D" = None) -> float:
        if not other:
            other = EasyVector2D(1, 0)
        norm_point = self.normalize
        norm_horizontal = other
        dot = norm_point * norm_horizontal
        det = norm_point.determinant(norm_horizontal)
        angle = math.degrees(math.atan2(det, dot))
        return angle

    def __add__(self, other: "EasyVector2D") -> "EasyVector2D":
        return EasyVector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: "EasyVector2D") -> None:
        tmp = self.__add__(other)
        self.x = tmp.x
        self.y = tmp.y

    def __mul__(self, other: "EasyVector2D") -> float:
        return self.x * other.x + self.y * other.y

    def __len__(self) -> int:
        return self._vec_len

    def __iter__(self) -> list[float]:
        yield self.x
        yield self.y

    def __eq__(self, other: "EasyVector2D") -> bool:
        eps = 1e-7
        x_true = (abs(self.x - other.x) < eps)
        y_true = (abs(self.y - other.y) < eps)
        return x_true and y_true

    def __getitem__(self, index: int) -> float:
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError

    def __str__(self) -> str:
        return f"Vector2D: [{self.x}, {self.y}]"

    def __repr__(self) -> str:
        return f"Vector2D(x: float=5.0, y: float=2.3)"

# class EasyVector3D(EasyVector):
#     pass
