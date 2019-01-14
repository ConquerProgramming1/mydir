def mydir(item = __builtins__, private = False):
    ''' 
    A more readable and useful version of dir(), this presents useful information about an object or class.
    If no object or class is provided, defaults to showing info about builtins.
    
    By default doesn't show private (underscored) items. Pass 'private = True' to see private items.
    '''
    methods = []
    attributes = []
    classes = []
    exceptions = []
    
    for name in [symbol for symbol in sorted(dir(item), key=str.lower) if private or symbol[0] != '_']:
        try:
            pointer = getattr(item, name)
        except AttributeError as e:
            # We get here with Series.index, which blows up for some reason.
            # For now, assume in this case that it's a class.
            classes.append(name)
            continue

        if isinstance(pointer, type):
            # Some types like __builtins__.basestring can't be instantiated.
            thing = None
            try: thing = pointer()
            except: pass

            # Explicit check for 'is not None' because pandas classes raise an exception with an if check.
            if thing is not None and isinstance(thing, Exception):
                exceptions.append(name)
            else:
                classes.append(name)

        elif callable(pointer):
            methods.append(name)
        else:
            attributes.append(name)

    try:
        print(item.__name__)
    except:
        print(item.__class__)

    temp = "{}()"
    methods = [temp.format(method) for method in methods]
    if methods:
        print(f'  {len(methods)} methods:')
        print('    ' + '\n    '.join(methods))

    if classes:
        print(f'\n  {len(classes)} classes:')
        print('    ' + '\n    '.join(classes))

    if attributes:
        print(f'\n  {len(attributes)} attributes:')
        print('    ' + '\n    '.join(attributes))

    if exceptions:
        print(f'\n  {len(exceptions)} exceptions:')
        print('    ' + '\n    '.join(exceptions))


if __name__ == '__main__':
    # When this is run as a script, this serves as a test of the output.
    help(mydir)
    mydir()