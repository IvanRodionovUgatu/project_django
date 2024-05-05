# Иван Родионов
---

`
In [3]: models.Teacher.objects.all()
Out[3]: <QuerySet [<Teacher: Александр Федоров>, <Teacher: Николай Иванов>, <Teacher: Петр Васильев>]>

In [4]: models.Teacher.objects.first()
Out[4]: <Teacher: Александр Федоров>

In [5]: models.Teacher.objects.last()
Out[5]: <Teacher: Петр Васильев>

In [6]: models.Teacher.objects.count()
Out[6]: 3

In [8]: models.Teacher.objects.order_by('last_name')
Out[8]: <QuerySet [<Teacher: Петр Васильев>, <Teacher: Николай Иванов>, <Teacher: Александр Федоров>]>

In [9]: models.Teacher.objects.order_by('first_name')
Out[9]: <QuerySet [<Teacher: Александр Федоров>, <Teacher: Николай Иванов>, <Teacher: Петр Васильев>]>

In [10]: models.Teacher.objects.order_by('-first_name')
Out[10]: <QuerySet [<Teacher: Петр Васильев>, <Teacher: Николай Иванов>, <Teacher: Александр Федоров>]>

In [11]: models.Teacher.objects.filter(first_name__contains='и')
Out[11]: <QuerySet [<Teacher: Николай Иванов>]>

In [12]: models.Teacher.objects.filter(first_name__iexact='Петр')
Out[12]: <QuerySet [<Teacher: Петр Васильев>]>

In [15]: models.Subject.objects.filter(count_lecture__gt=2)
Out[15]: <QuerySet [<Subject: Математика>, <Subject: История России>, <Subject: Русский язык>]>

In [21]: models.Subject.objects.get(id=1)
Out[21]: <Subject: Математика>

In [23]: models.Subject.objects.filter(id=4).exists()
Out[23]: False

In [25]: models.Teacher.objects.create(first_name='Дивеев', last_name='Григорий', department='Иностранные языки')       
Out[25]: <Teacher: Дивеев Григорий>

In [26]: models.Subject.objects.dates('deadline','day')
Out[26]: <QuerySet [datetime.date(2024, 5, 13), datetime.date(2024, 5, 25), datetime.date(2024, 6, 1)]>

In [27]: models.Subject.objects.dates('deadline','day').reverse()
Out[27]: <QuerySet [datetime.date(2024, 6, 1), datetime.date(2024, 5, 25), datetime.date(2024, 5, 13)]>

In [29]: models.Subject.objects.values('name', 'teacher')
Out[29]: <QuerySet [{'name': 'Математика', 'teacher': 1}, {'name': 'История России', 'teacher': 2}, {'name': 'Русский яз
ык', 'teacher': 3}]>

In [31]: models.Subject.objects.values('name', 'comment')
Out[31]: <QuerySet [{'name': 'Математика', 'comment': 'Нужно обязательно сделать'}, {'name': 'История России', 'comment'
: 'желательно сдать на 5'}, {'name': 'Русский язык', 'comment': 'Можно сделать попозже'}]>

In [33]: models.Subject.objects.exclude(name__contains='а')
Out[33]: <QuerySet [<Subject: История России>, <Subject: Русский язык>]>
`