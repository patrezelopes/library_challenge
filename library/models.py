from datetime import datetime, timezone
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    class Meta:
        unique_together = [['name', 'author']]

    def __str__(self):
        return ("{} por {}").format(self.name, self.author)



class Client(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class RentBook(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    rented_at = models.DateTimeField()
    give_back_at = models.DateTimeField(null=True, blank=True)


    class Meta:
        unique_together = [['client', 'book', 'rented_at']]

    def __str__(self):
        return ("{} - {}").format(self.book.name, self.client.name)

    def late(self):
        rented_at = self.rented_at
        give_back_at = self.give_back_at
        if self.give_back_at:
            late = give_back_at - rented_at
        else:
            late = datetime.now(timezone.utc)-rented_at
        return late.days

    def finerate(self):
        late = self.late()
        if late <= 0:
            fine=0
            rate = 0
        elif late <= 3:
            fine= 0.03
            rate= 0.002
        elif late <= 5:
            fine = 0.05
            rate = 0.004
        else:
            fine = 0.07
            rate = 0.006
        return '{:.5f}'.format(fine+rate*late)