# mydir
Improved version of dir(), developed while teaching Python to help students.

I love ``dir()``, I hate ``dir()``.

One of the first things I teach students, whether new or experienced programmers, is the triad of built in functions critical for figuring things out in Python:

1. ``type()``
2. ``dir()``
3. ``help()``

Of these, ``dir()`` is the function I use more than any other, whether in class or while doing my own programming. It's absolutely critical. And yet it annoys the hell out of me.

*dir* is short for *directory*, and provides a list of all the names associated with an object in Python, which are the attributes and methods you can use with that object.

## What don't I like about dir()?

Here's the output of ``dir()`` when called on ``list``, one of the early objects I talk about in class:

    print(dir(int))

    ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
    
What's wrong with that for students? Let me count the ways...

1. The listing starts with the underscore items, which are items for the implementor of the object that you aren't supposed to use (especially as a new programmer). To make matters worse, underscores come first in the sorting, so **all the items you shouldn't use are listed first** and you have to scan through until you find the first non-underscored item. In this case, you have to skip 62 items to get to the 8 item you can actually use.

2. The listing doesn't differentiate between attributes and methods. In **every single class**, students ask, "How do we know which ones are methods and which are attributes?"

3. The output is ugly and hard to read, which is particularly offensive for people who are trying to learn to program.

## My answer: mydir()

Eventually I got tired of spending several minutes explaining all these problems to students, and over the years I developed my own version of ``dir()`` to address the issues. Seeing me use it, students started asking if they could use it in their own coding. To my surprise, I started finding myself using it when doing development, and I found myself discovering things about objects that I'd never noticed before.

Here's the output of ``mydir()`` for a ``list``:

    from mydir import mydir

    mydir(list)

    list
      11 methods:
        append()
        clear()
        copy()
        count()
        extend()
        index()
        insert()
        pop()
        remove()
        reverse()
        sort()
        
Which do you prefer?

This makes things *so* much nicer for students (and for their instructors...)

If you want to see the private (underscored) items, you can do so:

    mydir(list, private=True)

    list
      43 methods:
        __add__()
        __contains__()
        __delattr__()
        __delitem__()
        __dir__()
        __eq__()
        __format__()
        __ge__()
        __getattribute__()
        __getitem__()
        __gt__()
        __iadd__()
        __imul__()
        __init__()
        __init_subclass__()
        __iter__()
        __le__()
        __len__()
        __lt__()
        __mul__()
        __ne__()
        __new__()
        __reduce__()
        __reduce_ex__()
        __repr__()
        __reversed__()
        __rmul__()
        __setattr__()
        __setitem__()
        __sizeof__()
        __str__()
        __subclasshook__()
        append()
        clear()
        copy()
        count()
        extend()
        index()
        insert()
        pop()
        remove()
        reverse()
        sort()

      1 classes:
        __class__

      2 attributes:
        __doc__
        __hash__
        
Notice that classes and attributes are separated out from methods.

## Future plans
I intend to make some additions:

* More format options, such as a compact display of the items.
* The option to return data instead of automatically printing the items.
* Update to use the [inspect module](https://docs.python.org/3.7/library/inspect.html#module-inspect).

Suggestions and patches welcome!
