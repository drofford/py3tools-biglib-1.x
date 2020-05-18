# import logging
import re

from biglib import logger


class Properties:
    """This is a class designed to hold a collection of properties.

    The collection can be loaded from a file by use of a helper or
    inserted one by one via the Properties#put function.
    """

    def __init__(self):
        """The no arguments/default constructor."""

        self.items = dict()

    def get(self, prop_name, evaluate=True):
        """Returns the value of the named property.

        Retrieves the value of the property with the given name from the
        collection.

        If the parameter evaluate is truthy, then if the value contains
        a replaceable string (that is of the form ${...}), the identifier
        between the braces will be looked up in the collection and if
        found, its value will replace the ``${...}`` sequence. If not found,
        the ${...} sequence will be left intact.

        Parameters
        ----------
        key : str, required
            The name of the property whose value is to be retrieved
        evaluate : bool, optional, defaults to True.
            a flag indicate whether string replacements should be
            performed.

        Returns
        -------
        property value : str
            the value of the named property. If the evaluate flag was
            truthy, any string replacements will have been performed.

        Limitations
        -----------
        1. This is only one iteration of these replacements performed.
        2. The property name between the braces must already exsit in the
           collection. Forward references are not currently supported.
        """

        logger.debug("""GET: prop_name="{}", evaluate={}""".format(prop_name, evaluate))

        def repl(matchobj):
            logger.debug("""    repl called with matchobj="{}" """.format(matchobj))
            prop_name = str(matchobj.group(0))[2:-1]
            logger.debug("""    prop_name = "{}" """.format(prop_name))

            if prop_name in self.items:
                prop_value = self.items[prop_name]
                logger.debug(
                    """    replaced "{}" with "{}" """.format(
                        matchobj.group(0), prop_value
                    )
                )
                return prop_value

            logger.debug("""No value found for "{}" """.format(matchobj.group(0)))
            return matchobj.group(0)

        prop_val = None

        if prop_name in self.items:
            prop_val = self.items[prop_name]
            logger.debug(
                """prop_name="{}", evaluate={}, prop_val="{}" """.format(
                    prop_name, evaluate, prop_val
                )
            )
            if evaluate:
                if re.search("\\${[^}]+}", prop_val):
                    logger.debug("""  value contains at least one ${variable-name}""")
                    prop_val = re.sub("\\${[^}]+}", repl, prop_val)
                    logger.debug("""  resultant string is "{}" """.format(prop_val))
                else:
                    logger.debug(
                        """  value does NOT contain at least one ${variable-name}"""
                    )

        return prop_val

    def put(self, prop_name, prop_value):
        """Store the value for the named property in the collection.

        Stores the given value as the value of the property with the
        given name in the collection. String replacement is not
        performed on put.

        Parameters
        ----------
        prop_name : str, required
            The name of the property to be updated.
        prop_val : str, required
            The value to which the property should be set..
        """

        key = prop_name.strip()
        val = prop_value.strip()

        logger.debug("""PUT: key="{}", value="{}" """.format(key, val))

        old = self.items[key] if key in self.items else None
        self.items[key] = val
        return old

    def has_variable_refs(self):
        """Checks if any property value contains a string replacement.

        Returns
        -------
        bool
            True  : if at least one property contained a string replacement
                    sequence.

            False : otherwise.
        """

        for k in self.items.keys():
            v = self.items[k]
            if re.search("\\${[^}]+}", v):
                return True
        return False

    def names(self):
        """Return of sorted list of property names."""

        return list(sorted(self.items.keys()))

    def __len__(self):
        """Returns the number of properties in the collection."""

        return len(self.items)
