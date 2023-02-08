TREES = [
    {
        "name": "Ель",
        "height": 2.55,
        "age": 5
    },
    {
        "name": "Сосна меловая",
        "height": 7,
        "age": 4
    },
    {
        "name": "Кедр",
        "height": 44,
        "age": 155
    },
    {
        "name": "Туя",
        "height": 2.05,
        "age": 10
    }
]


class ConiferousTree:
    """
    Создание и подготовка к работе базового класса "ConiferousTree".
    В нём будут содержаться все хвойные деревья, кроме редкого вида
    """
    def __init__(self, name: str, height: float, age: int):
        """
        Констурктор класса ConiferousTree
        :param name: Вид дерева
        :param height: высота
        :param age: возраст
        """
        self.height = height
        self.age = age
        self.name = name

    def cut_off_branches(self, branches: bool) -> str:
        """
        Срезать сухие ветви с дерева
        Наследуется дочерним классом PineChalk
        """
        if branches is True:
            ...
            return f'Все сухие сучья срезаны'
        return f'На данном дереве нет сухих ветвей'

    def cut_tree(self) -> str:
        """Срезать дерево"""
        ...
        return f'Дерево {self.name} срезано'

    def __str__(self) -> str:
        """
        Содержит в себе информацию о дереве (высота и возраст).
        Далее наследуется классом PineChalk
        """
        return f'Хвойное дерево "{self.name}" высотой - {self.height} и возрастом - {self.age}'

    def __repr__(self) -> str:
        """
        Возвращает валидную Питон-строку для данного класа ConiferousTree
        Наследуется дочерним классом ChalkPine
        """
        return f'{self.__class__.__name__}(name={self.name!r}, height={self.height}, age={self.age})'


class ChalkPine(ConiferousTree):
    """
    Создание и подготовка к работе дочернего класса "ChalkPine".
    Объекты данного класса - это редкий вид деревьев "Сосна меловая"
    """
    def __init__(self, name: str, height: float, age: int):
        """
        Констурктор дочернего класса PineChalk, на основе класса ConiferousTree.
        Унаследует все аргументы, новых не имеет
        """
        super().__init__(name, height, age)

    def cut_tree(self) -> str:
        """
        Срезать определенное дерево. Данный вид Хвойных деревьев срезать нельзя.
        Был перегружен метод cut_tree, чтобы этого не допустить
         """
        ...
        return f'Данный тип деревьев (Сосна меловая) срезать запрещено!'

    def __str__(self) -> str:
        """
        Был перегружен магический метод __str__ из-за другого вида информации
        """
        return f'"Сосна меловая высотой" - {self.height} и возрастом - {self.age}'


if __name__ == "__main__":
    list_tree = []            #список деревьев
    list_chalk_pine = []      #список Меловых сосен
    for tree in TREES:
        if tree["name"] == "Сосна меловая":
            list_chalk_pine.append(ChalkPine(name=tree["name"], height=tree["height"], age=tree["age"]))  #добавляем объекты класса ChalkPine в список
        else:
            list_tree.append(ConiferousTree(name=tree["name"], height=tree["height"], age=tree["age"]))  #остальные деревья делаем объектами класса ConiferousTree
    print("В нашем саду растут такие деревья:")   #перечисляем наши деревья со своими характеристиками
    for tree in list_tree:
        print(tree)
    print("А так же редкий вид деревьев:")
    for tree in list_chalk_pine:
        print(tree)

    print(list_tree[1].cut_tree())   #убираем старое дерево с сада
    del(list_tree[1])

    print(list_chalk_pine[0].cut_tree())    #проверяем, можем ли мы срезать редкий вид деревьев

    print("У нашей ели есть сухие сучья, нам нужно их убрать")
    print(list_tree[0].cut_off_branches(True))
    pass
