class main:
    def __init__(self) -> None:
        print("main")

    class inner:
        def __init__(self) -> None:
            print("inner")

        def test(self):
            print("right")

m = main()
i = m.inner()
i.test()