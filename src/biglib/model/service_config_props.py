import attr


@attr.s
class ServiceConfigProps:
    props = attr.ib(default=attr.Factory(dict))

    def __len__(self) -> int:
        return len(self.props)

    def __str__(self) -> str:
        return str(self.props)

    def __getitem__(self, name: str) -> [bool, object]:
        try:
            return True, self.props[name]
        except KeyError:
            return False, [f"Property not found: {name}"]

    def __setitem__(self, name: str, value: str) -> None:
        self.props[name] = value

    def get(self, name: str) -> [bool, object]:
        try:
            return True, self.props[name]
        except KeyError:
            return False, [f"Property not found: {name}"]

    def put(self, name, value) -> None:
        self.props[name] = value

    def prop_names(self):
        return sorted(self.props.keys())

    def reset(self) -> None:
        self.props = dict()
