# -*- coding: utf-8 -*-

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models


class Encuestador(models.Model):
    #id = models.IntegerField(primary_key=True, db_column=u'Id') # Field name made lowercase.
    nombre = models.CharField(db_column=u'Nombre', blank=True, max_length=300) # Field name made lowercase.
    
    def __unicode__(self):
        return self.nombre

    class Meta:
        db_table = u'Encuestador'
        verbose_name = u'Encuestador'
        verbose_name_plural = u'Encuestadores'


class Sector(models.Model):
    #id = models.IntegerField(primary_key=True, db_column=u'Id') # Field name made lowercase.
    nombre = models.CharField(db_column=u'Nombre', blank=True, max_length=300) # Field name made lowercase.

    def __unicode__(self):
        return self.nombre
    
    class Meta:
        db_table = u'Sector'
        verbose_name = u'Sector'
        verbose_name_plural = u'Sectores'


class Colonia(models.Model):
    #id = models.IntegerField(primary_key=True, db_column=u'Id') # Field name made lowercase.
    nombre = models.CharField(db_column=u'Nombre', blank=True, max_length=300) # Field name made lowercase.

    def __unicode__(self):
        return self.nombre
    
    class Meta:
        db_table = u'Colonia'
        verbose_name = u'Colonia'
        verbose_name_plural = u'Colonias'


class Parentesco(models.Model):
    #id = models.IntegerField(primary_key=True, db_column=u'Id') # Field name made lowercase.
    nombre = models.CharField(db_column=u'Nombre', blank=True, max_length=300) # Field name made lowercase.

    def __unicode__(self):
        return self.nombre

    class Meta:
        db_table = u'Parentesco'
        verbose_name = u'Parentesco'
        verbose_name_plural = u'Parentescos'


class Religion(models.Model):
    #id = models.IntegerField(primary_key=True, db_column=u'Id') # Field name made lowercase.
    nombre = models.CharField(db_column=u'Nombre', blank=True, max_length=300) # Field name made lowercase.

    def __unicode__(self):
        return self.nombre

    class Meta:
        db_table = u'Religion'
        verbose_name = u'Religion'
        verbose_name_plural = u'Religiones'


class Sexo(models.Model):
    #id = models.IntegerField(primary_key=True, db_column=u'Id') # Field name made lowercase.
    nombre = models.CharField(db_column=u'Nombre', blank=True, max_length=300) # Field name made lowercase.

    def __unicode__(self):
        return self.nombre

    class Meta:
        db_table = u'Sexo'
        verbose_name = u'Sexo'
        verbose_name_plural = u'Sexos'


class Calle(models.Model):
    #id = models.IntegerField(primary_key=True, db_column=u'Id') # Field name made lowercase.
    nombre = models.CharField(db_column=u'Nombre', blank=True, max_length=300) # Field name made lowercase.
    colonia = models.ForeignKey(Colonia, null=False, db_column=u'IdColonia', blank=False) # Field name made lowercase.
    sector = models.ForeignKey(Sector, null=False, db_column=u'IdSector', blank=False) # Field name made lowercase.

    def __unicode__(self):
        return u'%s : %s (%s, %s)' % (self.id, self.nombre, self.colonia, self.sector )

    class Meta:
        db_table = u'Calle'
        verbose_name = u'Calle'
        verbose_name_plural = u'Calles'

class Encuesta(models.Model):
    #id = models.IntegerField(primary_key=True, db_column=u'Id') # Field name made lowercase.
    fecha = models.DateTimeField(null=True, db_column=u'Fecha', blank=True) # Field name made lowercase.
    encuestador = models.ForeignKey(Encuestador, null=True, db_column=u'IdEncuestador', blank=True) # Field name made lowercase.
    observacion = models.TextField(db_column=u'Observacion', blank=True) # Field name made lowercase.

    def __unicode__(self):
        return u'%s : %s, \"%s\"' % (self.id, self.fecha, self.observacion )

    class Meta:
        db_table = u'Encuesta'
        verbose_name = u'Encuesta'
        verbose_name_plural = u'Encuestas'


class Familia(models.Model):
    #id = models.IntegerField(primary_key=True, db_column=u'Id') # Field name made lowercase.
    nombre = models.CharField(db_column=u'Nombre', blank=True, max_length=300) # Field name made lowercase.
    calle = models.ForeignKey(Calle, null=False, db_column=u'IdCalle', blank=False) # Field name made lowercase.
    encuesta = models.ForeignKey(Encuesta, null=False, db_column=u'IdEncuesta', blank=False) # Field name made lowercase.
    noext = models.CharField(db_column=u'NoExt', blank=True, max_length=300) # Field name made lowercase.
    noint = models.CharField(db_column=u'NoInt', blank=True, max_length=300) # Field name made lowercase.
    lote = models.CharField(db_column=u'Lote', blank=True, max_length=300) # Field name made lowercase.

    def __unicode__(self):
        return u'%s : \"%s\"' % (self.id, self.nombre)

    class Meta:
        db_table = u'Familia'
        verbose_name = u'Familia'
        verbose_name_plural = u'Familias'


class Persona(models.Model):
    #id = models.IntegerField(primary_key=True, db_column=u'Id') # Field name made lowercase.
    parentesco = models.ForeignKey(Parentesco, null=False, db_column=u'IdParentesco', blank=False) # Field name made lowercase.
    nombre = models.CharField(db_column=u'Nombre', blank=True, max_length=300) # Field name made lowercase.
    edad = models.IntegerField(null=True, db_column=u'Edad', blank=True) # Field name made lowercase.
    sexo = models.ForeignKey(Sexo, null=False, db_column=u'IdSexo', blank=False) # Field name made lowercase.
    religion = models.ForeignKey(Religion, null=False, db_column=u'IdReligion', blank=False) # Field name made lowercase.
    lugarorigen = models.CharField(db_column=u'LugarOrigen', blank=True, max_length=300) # Field name made lowercase.
    familia = models.ForeignKey(Familia, null=False, db_column=u'IdFamilia', blank=False) # Field name made lowercase.

    def __unicode__(self):
        return u'%s : \"%s\", (%s, %s)' % (self.id, self.nombre, self.familia, self.parentesco)

    class Meta:
        db_table = u'Persona'
        verbose_name = u'Persona'
        verbose_name_plural = u'Personas'

