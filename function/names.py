
import random
mail = [
       "o@outlook.com",
       "hr6zdl@yandex.ru",
       "kaft93x@outlook.com",
       "dcu@yandex.ru",
       "19dn@outlook.com",
       "pa5h@mail.ru",
       "281av0@gmail.com",
       "8edmfh@outlook.com",
       "sfn13i@mail.ru",
       "g0orc3x1@outlook.com",
       "rv7bp@gmail.com",
       "93@outlook.com",
       "er@gmail.com",
       "o0my@gmail.com",
       "715qy08@gmail.com",
       "vubx0t@mail.ru",
       "wnhborq@outlook.com",
       "gq@yandex.ru",
       "ic0pu@outlook.com",
       "o7khr@yandex.ru",
       "2shlaq@outlook.com",
       "cdbw@yandex.ru",
       "wrts90puk@yandex.ru",
       "yxunv@gmail.com",
       "7y@yandex.ru",
       "6@mail.ru",
       "k8sjebg1y@mail.ru",
       "jirbold@gmail.com",
       "u7yhwf1vb@mail.ru",
       "f@outlook.com",
       "gjkhp@mail.ru",
       "wyalkxfde@gmail.com",
       "f245n@outlook.com",
       "w@outlook.com",
       "js3kyopz@mail.ru",
       "o@outlook.com",
       "uzfd@mail.ru",
       "g@mail.ru",
       "dvjf0@gmail.com",
       "d2mc@outlook.com",
       "06lk@mail.ru",
       "emhzysf2@yandex.ru",
       "d1w28lkg@yandex.ru",
       "t93@mail.ru",
       "t3i@outlook.com",
       "t6ro3@gmail.com",
       "1zqnk0y7@yandex.ru",
       "768ptl4nv@gmail.com",
       "bzq3yh2c1@mail.ru",
       "78k3dvwx@outlook.com",
       "fe8obp@mail.ru",
       "cxh2daw8@outlook.com",
       "lrsdy5p@yandex.ru",
       "2de17h@mail.ru",
       "we3l08z5@gmail.com",
       "i8ovxn2f@gmail.com",
       "q4as80@outlook.com",
      "opu@outlook.com",
       "5iar3l8k@yandex.ru",
       "4zegxla@mail.ru",
       "8lf0g@yandex.ru",
       "1zx8@yandex.ru",
       "x@mail.ru",
       "34d@gmail.com",
       "pxacl@mail.ru",
       "7o1@gmail.com",
       "1@gmail.com",
       "iut@gmail.com",
       "e3t@outlook.com",
       "41clb6o2g@yandex.ru",
       "5hsbm8pi3@mail.ru",
       "dihf8jxk@gmail.com",
       "dwej@yandex.ru",
       "zyue8brv@outlook.com",
       "0a5437@mail.ru",
       "fovtju3q2@yandex.ru",
       "5ntglejc9@outlook.com",
       "61rpbj@mail.ru",
       "9m6pfk52r@outlook.com",
       "gr@yandex.ru",
       "v9dux@gmail.com",
       "mek975vcx@gmail.com",
       "uakvj8p9d@yandex.ru",
       "t3m6u8v@gmail.com",
       "jxqme@gmail.com",
       "c3@gmail.com",
       "3xkgmsd9t@gmail.com",
       "s9iw@mail.ru",
       "qo2sc@mail.ru",
       "xiuq5olft@gmail.com",
       "8swlo27hd@outlook.com",
       "r0o6f92@gmail.com",
       "z@gmail.com",
       "r3p4mgf5@yandex.ru",
       "p@outlook.com",
       "61j@yandex.ru",
       "t2sr@gmail.com",
       "u7@outlook.com",
       "9k15qr2h@gmail.com",
       "3vmtdo1@outlook.com",
       "q9@mail.ru",
]
name = [
    "Власов Павел",
    "Беляков Виктор",
    "Самсонов Святослав",
    "Соболев Ярослав",
    "Кулагина Александра",
    "Шевелева Василиса",
    "Кулешова Дарья",
    "Чумакова Арина",
    "Фетисова Юлия",
    "Олег",
    "Алексей",
    "Максим",
    "Ева",
    "Яна",
    "Артем",
    "Дамир",
    "Руслан",
    "Алина",
    "Ольга",
    "Екатерина",
    "Феликс",
    "Иван",
    "Николай",
    "Софья",
    "Милана",
    "Евгения",
    "Мария",
    "Бурова Дарья",
    "Кузнецова Агния",
    "Егорова Олеся",
    "Коровина Анна",
    "Дубинина Олеся",
    "Зеленин Роман",
    "Винокуров Герман",
    "Фокин Святослав",
    "Бородин Герман",
    "Бондарев А. И.",
    "Кузьмин Д. В.",
    "Беляев М. Ф.",
    "Орлова К. Т.",
    "Комарова П. Е.",
    "Дубровин П. Д.",
    "Демин А. Т.",
    "Романова А. П.",
    "Фокина В. Г.",
    "Дорофеева Э. В.",
    "Поликарпов Глеб",
    "Ермолаев Богдан"
]

def getName():
    return mail[random.randint(0, len(mail) - 1)]

def getMail():
    return name[random.randint(0, len(name) - 1)]