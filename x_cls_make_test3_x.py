class x_cls_make_test3_x:
    def __init__(self, ctx: object | None = None) -> None:
        # preserve backwards compatibility while accepting a context
        self._ctx = ctx

    def run(self) -> str:
        return "Hello world!"


def main() -> str:
    return x_cls_make_test3_x().run()


if __name__ == "__main__":
    print(main())
