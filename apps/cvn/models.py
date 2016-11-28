from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, \
    RegexValidator


class Citizen(models.Model):
    NUMERO_CNV = models.IntegerField()

    TIPO_DOC_MADRE = models.CharField(max_length=2, validators=[
        RegexValidator(
            regex='^[0-9]{2}$',
            message='Numero de 2 digitos',
        ),
    ], null=True, blank=True)

    NUMERO_DOC_MADRE = models.CharField(max_length=35, validators=[
        RegexValidator(
            regex='^[a-zA-Z0-9]{1,35}$',
            message='Numero de 2 digitos',
        ),
    ], null=True, blank=True)

    PRIMER_APELLIDO_MADRE = models.CharField(max_length=40, null=True,
                                             blank=True)
    SEGUNDO_APELLIDO_MADRE = models.CharField(max_length=40, null=True,
                                              blank=True)
    PRENOMBRES_MADRE = models.CharField(max_length=50, null=True, blank=True)

    SEXO_NACIDO = models.CharField(max_length=2, validators=[
        RegexValidator(
            regex='^[0-9]{2}$',
            message='Numero de 2 digitos',
        ),
    ], null=True, blank=True)

    FECHA_NACIDO = models.CharField(max_length=8, null=True, blank=True)
    HORA_NACIDO = models.CharField(max_length=6, null=True, blank=True)

    PESO_NACIDO = models.PositiveIntegerField(validators=[
        MinValueValidator(500), MaxValueValidator(8000)
    ], null=True, blank=True)

    TALLA_NACIDO = models.PositiveIntegerField(validators=[
        MinValueValidator(25), MaxValueValidator(99)
    ], null=True, blank=True)

    APGAR_UNO_NACIDO = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(0), MaxValueValidator(10)
    ], null=True, blank=True)

    APGAR_CINCO_NACIDO = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(0), MaxValueValidator(10)
    ], null=True, blank=True)

    ETNIA_NACIDO = models.CharField(max_length=6, null=True, blank=True)
    NU_NACIDO_PERIM_CEFALICO = models.DecimalField(max_digits=4,
                                                   decimal_places=2, null=True,
                                                   blank=True)
    NU_NACIDO_PERIM_TORACICO = models.DecimalField(max_digits=4,
                                                   decimal_places=2, null=True,
                                                   blank=True)
    NU_TEMPERATURA = models.PositiveSmallIntegerField(validators=[
        RegexValidator(
            regex='^[0-9]{1,2}$',
            message='Numero de 2 digitos',
        ),
    ], null=True, blank=True)
    CO_RESULTADO_EF = models.CharField(max_length=2, null=True, blank=True)
    NU_EDAD_EXAMEN_FISICO = models.PositiveSmallIntegerField(validators=[
        RegexValidator(
            regex='^[0-9]{1,2}$',
            message='Numero de 2 digitos',
        ),
    ], null=True, blank=True)
    CO_UM_EDAD = models.CharField(max_length=2, null=True, blank=True)

    DURACION_EMBARAZO_PARTO = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(20), MaxValueValidator(42)
    ], null=True, blank=True)

    ATIENDE_PARTO = models.CharField(max_length=2, null=True, blank=True)
    CONDICION_PARTO = models.CharField(max_length=2, null=True, blank=True)
    TIPO_PARTO = models.CharField(max_length=2, null=True, blank=True)
    FINANCIADOR_PARTO = models.CharField(max_length=2, null=True, blank=True)
    CO_POSICION_PARTO = models.CharField(max_length=2, null=True, blank=True)

    IN_PARTOGRAMA = models.PositiveSmallIntegerField('PARTG', default=0,
                                                     null=True, blank=True)
    IN_ACOMPANA_PARTO = models.PositiveSmallIntegerField('APARTO', default=0,
                                                         null=True, blank=True)

    CO_DURACION_PARTO = models.CharField(max_length=2, null=True, blank=True)
    IN_EPISIOTOMIA_PARTO = models.CharField(max_length=2, null=True, blank=True)
    IN_DESGARRO_PARTO = models.CharField(max_length=2, null=True, blank=True)
    CO_ALUMBRAMIENTO_PARTO = models.CharField(max_length=2, null=True,
                                              blank=True)
    IN_PLACENTA_PARTO = models.CharField(max_length=2, null=True, blank=True)
    IN_EESS_PROCEDENCIA = models.CharField(max_length=2, null=True, blank=True)
    CO_EESS_PROCENDENCIA = models.CharField(max_length=8, null=True, blank=True)
    CODIGO_LOCAL = models.CharField(max_length=8, null=True, blank=True)
    CODIGO_RENAES = models.CharField(max_length=8, null=True, blank=True)
    CODIGO_OPERACION = models.CharField(max_length=2, null=True, blank=True)
    CREATE_BY = models.CharField(max_length=15, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
