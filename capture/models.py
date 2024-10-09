from django.db import models

# Create your models here.


class PvcapBatch1(models.Model):
    batchid = models.BigAutoField(db_column='BATCHID', primary_key=True)  # Field name made lowercase.
    internalname = models.CharField(db_column='INTERNALNAME', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    userdate = models.DateTimeField(db_column='USERDATE', blank=True, null=True)  # Field name made lowercase.
    path = models.TextField(db_column='PATH', db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='ISDELETED')  # Field name made lowercase.
    isnew = models.BooleanField(db_column='ISNEW')  # Field name made lowercase.
    retainstats = models.BooleanField(db_column='RETAINSTATS')  # Field name made lowercase.
    adminpriority = models.BigIntegerField(db_column='ADMINPRIORITY')  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='STATUS')  # Field name made lowercase.
    jobid = models.BigIntegerField(db_column='JOBID')  # Field name made lowercase.
    jobstart = models.DateTimeField(db_column='JOBSTART')  # Field name made lowercase.
    stepid = models.IntegerField(db_column='STEPID')  # Field name made lowercase.
    stepstart = models.DateTimeField(db_column='STEPSTART')  # Field name made lowercase.
    checkedoutbydatetime = models.DateTimeField(db_column='CHECKEDOUTBYDATETIME', blank=True, null=True)  # Field name made lowercase.
    checkedoutbyuserid = models.IntegerField(db_column='CHECKEDOUTBYUSERID', blank=True, null=True)  # Field name made lowercase.
    checkedoutbyworkstation = models.CharField(db_column='CHECKEDOUTBYWORKSTATION', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    scheduleddestruction = models.DateTimeField(db_column='SCHEDULEDDESTRUCTION', blank=True, null=True)  # Field name made lowercase.
    size = models.BigIntegerField(db_column='SIZE')  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LASTUPDATE')  # Field name made lowercase.
    documentcount = models.BigIntegerField(db_column='DOCUMENTCOUNT', blank=True, null=True)  # Field name made lowercase.
    pagecount = models.BigIntegerField(db_column='PAGECOUNT', blank=True, null=True)  # Field name made lowercase.
    imagecount = models.BigIntegerField(db_column='IMAGECOUNT', blank=True, null=True)  # Field name made lowercase.
    delayprocessing = models.DateTimeField(db_column='DELAYPROCESSING', blank=True, null=True)  # Field name made lowercase.
    iscomplete = models.BooleanField(db_column='ISCOMPLETE', default=False)
    userid = models.IntegerField(db_column='USERID', null=False)


    class Meta:
        managed = False
        db_table = 'PVCAP_BATCH_1'


class PvcapIndexvalue1(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    jobid = models.BigIntegerField(db_column='JOBID')  # Field name made lowercase.
    indexid = models.BigIntegerField(db_column='INDEXID')  # Field name made lowercase.
    value = models.CharField(db_column='VALUE', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    batchid = models.BigIntegerField(db_column='BATCHID')  # Field name made lowercase.
    bundleid = models.BigIntegerField(db_column='BUNDLEID')  # Field name made lowercase.
    detailsetid = models.CharField(db_column='DETAILSETID', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    confidence = models.FloatField(db_column='CONFIDENCE', blank=True, null=True)  # Field name made lowercase.
    rowindex = models.IntegerField(db_column='ROWINDEX', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVCAP_INDEXVALUE_1'
        indexes = [
            models.Index(fields=['bundleid']),  
        ]


class PvcapIndex1(models.Model):
    indexid = models.BigIntegerField(db_column='INDEXID', primary_key=True)  # Field name made lowercase. The composite primary key (INDEXID, JOBID) found, that is not supported. The first column is selected.
    jobid = models.BigIntegerField(db_column='JOBID')  # Field name made lowercase.
    fieldname = models.CharField(db_column='FIELDNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    indexproperties = models.TextField(db_column='INDEXPROPERTIES', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVCAP_INDEX_1'
        unique_together = (('indexid', 'jobid'),)




class PvcapJob1(models.Model):
    jobid = models.BigAutoField(db_column='JOBID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='COMMENT', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    modifieddatetime = models.DateTimeField(db_column='MODIFIEDDATETIME', blank=True, null=True)  # Field name made lowercase.
    modifiedbyname = models.IntegerField(db_column='MODIFIEDBYNAME', blank=True, null=True)  # Field name made lowercase.
    modifiedbyglobaladmin = models.BooleanField(db_column='MODIFIEDBYGLOBALADMIN', blank=True, null=True)  # Field name made lowercase.
    checkedoutbydatetime = models.DateTimeField(db_column='CHECKEDOUTBYDATETIME', blank=True, null=True)  # Field name made lowercase.
    checkedoutbyname = models.IntegerField(db_column='CHECKEDOUTBYNAME', blank=True, null=True)  # Field name made lowercase.
    checkedoutbyglobaladmin = models.BooleanField(db_column='CHECKEDOUTBYGLOBALADMIN', blank=True, null=True)  # Field name made lowercase.
    properties = models.TextField(db_column='PROPERTIES', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVCAP_JOB_1'



class PvcapBundle(models.Model):
    bundleid = models.BigAutoField(db_column='BUNDLEID', primary_key=True)
    batchid = models.IntegerField(db_column='BATCHID', null=False)
    createdate = models.DateTimeField(db_column='CREATEDATE', null=True)
    submit = models.BooleanField(default=False)

    class Meta:
        managed = False  
        db_table = 'PvcapBundle'