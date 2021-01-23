from main.models import Product, ProductCategory, Seller


# Creating
home_tech = ProductCategory.objects.create(name="Home Electronics")
hobby = ProductCategory.objects.create(name="Musical Instruments")
firm = Seller.objects.create(company_name="Big firm", username="testuser")

tv = Product.objects.create(
    name="Телевизор LED Polarline 20PL12TC черный",
    description="""Телевизор LED Polarline 20PL12TC − компактное устройство, представленное в черном корпусе с диагональю 20" (50 см). Для установки на поверхность используется подставка, размещенная по центру корпуса.""",
    price=6299,
    category=home_tech,
    seller=firm,
)
headphones = Product.objects.create(
    name="Audio-Technica ATH-M30x",
    description="Audio-Technica ATH-M30x – накладные динамические наушники закрытого типа для студийного мониторинга. Эта модель из обновленной M-серии представляет собой профессиональные наушники с чистым звучанием и звукоизоляцией студийного уровня.",
    price=5990,
    category=home_tech,
    seller=firm,
)
audio = Product.objects.create(
    name="Колонки 2.0 Edifier R2700",
    description="Колонки Edifier R2700 - продолжение топовой серии Edifier-Studio. Эта модель трехполосной аудиосистемы в формате 2.0, с наличием триампинга, воспроизводит трехмерное звучание.",
    price=16999,
    category=home_tech,
    seller=firm,
)

guitar = Product(
    name="MGP JG Ash Jaguar",
    description="""Корпус изготовлен из ясеня в мастерской Muzbass. Покрытие корпуса - полиуретановый лак.
Гриф - кленовый с кленовый накладкой. Датчики - BH Custom 60s с магнитами Alnico-5 про-во Ю.Корея. Колки - про-во Ю.Корея. """,
    price=30000,
    category=hobby,
    seller=firm,
)
guitar.save()
bass = Product(
    name="Edwards E-JG-75B Jaguar Bass",
    description="Красивый редкий бас с классным звуком. Есть подкрашенный скол лака, но общее состояние очень хорошее. Удобный гриф. В комплекте новые струны. ",
    price=29000,
    category=hobby,
    seller=firm,
)
bass.save()
e_drums = Product(
    name="ALESIS NITRO MESH KIT",
    description="электроная барабанная установка, 8 дюймовый dual-zone snare + 3 single-zone toms. Kick drumpad в комплекте + басс педаль в комплекте, 10 дюймовые тарелки, ride cymbal, hi-hat, crashw/choke. ",
    price=51000,
    category=hobby,
    seller=firm,
)
e_drums.save()

# Getting with filters
all_products = Product.objects.all()
some_guitar = Product.objects.get(name="MGP JG Ash Jaguar")
Instruments = Product.objects.filter(category__name="Musical Instruments")
Etech = Product.objects.filter(category=home_tech)
