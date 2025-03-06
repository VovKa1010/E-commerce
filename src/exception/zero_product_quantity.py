class ZeroProductQuantity(Exception):
    def __init__(self, *args):
        self.massage = args[0] if args else "Количество продукта не должно быть 0"
        super().__init__(*args)

    def __str__(self):
        return self.massage
