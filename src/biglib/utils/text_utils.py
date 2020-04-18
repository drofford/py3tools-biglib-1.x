def pluralize(txt, /, verbs=[], nouns=[], count=0):
    """
    Function:
        to return a string where the verb and noun have been set based on a count.

    Parameters:
        txt         this is the template string to be used. There are
                    there placeholders that can be used:
                        {verb}
                        {noun}
                        {count}.

        verbs       this is a tuple containing (the plural verb form, the singular verb form). If it contains
                    only one value, that value will be for both plural and singular forms. It can also be a
                    string rather than a tuple, in which case will used be for both plural and singular forms.

        nouns       this is a tuple containing (the plural noun form, the singular noun form). If it contains
                    only one value, that value will be for both plural and singular forms. It can also be a
                    string rather than a tuple, in which case will used be for both plural and singular forms.

        count       this is the count, used to select between the plural and singular forms.

    Returns:
        the formatted string

    Examples:

        1.  suppose you have have a number of cars. You could use:

            print(pluralize("There {verb} {count} {noun}", ("are", "is"), ("things","thing"), number_of_things))

        2.  suppose you have have a number of cakes. You could use:

            print(pluralize("You {verb} {count} {noun}", ("have", "have"), ("cakes","cake"), number_of_cakes))
            print(pluralize("You {verb} {count} {noun}", ("have",), ("cakes","cake"), number_of_cakes))
            print(pluralize("You {verb} {count} {noun}", "have", ("cakes","cake"), number_of_cakes))
    """

    def picker(count, array):
        result = "x0"  # kludge
        if array is None:
            result = "x1"  # kludge
        elif isinstance(array, tuple) or isinstance(array, list):
            if len(array) == 0:
                result = "x2"  # kludge
            elif len(array) == 1:
                result = array[0]
            else:
                result = array[1 if count == 1 else 0]
        elif isinstance(array, str):
            result = array
        else:
            result = "x3"
        return result

    verb = picker(count, verbs)
    noun = picker(count, nouns)

    return txt.format(verb=verb, noun=noun, count=count)


def join(in_array, /, quoted: bool=True, separator: str=", ", conjunction:str="", oxford_comma:bool=True) -> str:
    """
    Joins together two or more strings, using the specified separator (default is ", "). Optionally, the last two
    elements can be joined by a word instead of a separator (default is no); in this case, you can also add the
    "Oxford comma" after the last but one element and before the conjunction word (default is yes).

    Parameters:

        :param in_array         this is a list/tuple of strings to be joined.

        :param quoted           if True, strings are enclosed in quote characters (") before being joined. The
                                default is True.

        :param separator        defines the character(s) used to separate any two elements. The default is ", ".

        :param conjunction      if specified as a non blank length, the last two strings will be separated with
                                the conjunction word instead of the separator character(s). If the oxford_comma
                                parameter is specified as True, the separator character(s) will be included. The
                                default conjunction word is "" (so just use separator character(s).

        :param oxford_comma     if a non-blank conjunction word has been specified, it will be preceded by the separator
                                character(s) if this parameter is True. Otherwise, the separator character(s) will be
                                omitted before the conjunction word.

    Returns:
        string result
    """
    quoter = lambda t: '"' + t + '"' if quoted else t

    if in_array is None or len(in_array) == 0:
        return quoter("")

    array = [quoter(x) for x in in_array]

    if len(array) == 1:
        return array[0]

    if len(array) == 2:
        if conjunction:
            return array[0] + " " + conjunction + " " + array[1]
        else:
            return separator.join(array)

    result = separator.join(array[:-1])
    if oxford_comma or not conjunction:
        result += separator
    else:
        result += " "
    result += conjunction + (" " if conjunction else "")
    result += array[-1]
    return result
