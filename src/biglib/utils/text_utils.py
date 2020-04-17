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
        result = "x0" # kludge
        if array is None:
            result = "x1" # kludge
        elif isinstance(array, tuple) or isinstance(array, list):
            if len(array) == 0:
                result = "x2" # kludge
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
