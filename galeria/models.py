from django.db import models


class Fotografia(models.Model):
    # colocar o nome de cada uma das colunas da tabela 
    nome = models.CharField(max_length=100, null=False, blank=False) # CharField; campo para char (caracteres)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Fotografia [nome={self.nome}]"

#class Question(models.Model):
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField("date published")


#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)


# Create your models here.
