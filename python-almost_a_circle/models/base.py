#!/usr/bin/python3
"""Defines the Base class, the root of all other classes in this project."""
import json
import csv


class Base:
    """Manage the `id` attribute for all future classes.

    This class serves as the base for every other class in this project
    and centralizes the `id` management and (de)serialization logic that
    is shared across all subclasses.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): The identity of the new instance. If `None` is
                given, `id` will be set with an auto-incremented value.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of the list, or "[]" if
                the list is `None` or empty.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of a list of objects to file.

        The filename is `<cls.__name__>.json`.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string.

        Args:
            json_string (str): A JSON string representing a list of
                dictionaries.

        Returns:
            list: The list represented by `json_string`, or an empty list
                if `json_string` is `None` or empty.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance of `cls` with all attributes already set.

        Args:
            **dictionary (dict): Key/value pairs of attributes to set on
                the new instance.

        Returns:
            Base: A new instance with attributes set from `dictionary`.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from `<cls.__name__>.json`.

        Returns:
            list: A list of instances, or an empty list if the file
                doesn't exist.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = cls.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        The filename is `<cls.__name__>.csv`.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w", newline="") as csvfile:
            if cls.__name__ == "Rectangle":
                fields = ["id", "width", "height", "x", "y"]
            else:
                fields = ["id", "size", "x", "y"]
            writer = csv.writer(csvfile)
            if list_objs is None or len(list_objs) == 0:
                writer.writerow([])
            else:
                for obj in list_objs:
                    row = [getattr(obj, field) for field in fields]
                    writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances loaded from `<cls.__name__>.csv`.

        Returns:
            list: A list of instances, or an empty list if the file
                doesn't exist.
        """
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                reader = csv.reader(csvfile)
                list_dicts = []
                for row in reader:
                    if not row:
                        continue
                    list_dicts.append(
                        {key: int(value) for key, value in
                         zip(fields, row)})
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a Turtle window and draw all given Rectangles and Squares.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        import turtle

        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for _ in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for _ in range(2):
                turt.forward(sq.size)
                turt.left(90)
                turt.forward(sq.size)
                turt.left(90)

        turtle.exitonclick()
