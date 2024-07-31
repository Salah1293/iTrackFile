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
    documentid = models.BigIntegerField(db_column='DOCUMENTID')  # Field name made lowercase.
    detailsetid = models.CharField(db_column='DETAILSETID', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    confidence = models.FloatField(db_column='CONFIDENCE', blank=True, null=True)  # Field name made lowercase.
    rowindex = models.IntegerField(db_column='ROWINDEX', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVCAP_INDEXVALUE_1'


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





# class PvdmDg1(models.Model):
#     dgid = models.AutoField(db_column='DGID', primary_key=True)  # Field name made lowercase.
#     dgname = models.CharField(db_column='DGNAME', unique=True, max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
#     path = models.TextField(db_column='PATH', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
#     type = models.SmallIntegerField(db_column='TYPE')  # Field name made lowercase.
#     lastupdatetime = models.DateTimeField(db_column='LASTUPDATETIME', blank=True, null=True)  # Field name made lowercase.
#     size = models.FloatField(db_column='SIZE')  # Field name made lowercase.
#     readwrite = models.BooleanField(db_column='READWRITE')  # Field name made lowercase.
#     origdgname = models.CharField(db_column='ORIGDGNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
#     encryptkeyname = models.CharField(db_column='ENCRYPTKEYNAME', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     encryptkeyvalue = models.TextField(db_column='ENCRYPTKEYVALUE', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     trashuserid = models.IntegerField(db_column='TRASHUSERID', blank=True, null=True)  # Field name made lowercase.
#     trashdatetime = models.DateTimeField(db_column='TRASHDATETIME', blank=True, null=True)  # Field name made lowercase.
#     dginfo = models.TextField(db_column='DGINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'PVDM_DG_1'




# class PvdmObjs15(models.Model):
#     objid = models.AutoField(db_column='OBJID', primary_key=True)  # Field name made lowercase.
#     docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.
#     objtype = models.SmallIntegerField(db_column='OBJTYPE')  # Field name made lowercase.
#     hashtype = models.SmallIntegerField(db_column='HASHTYPE')  # Field name made lowercase.
#     hashinfo = models.CharField(db_column='HASHINFO', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
#     filelist = models.TextField(db_column='FILELIST', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
#     pages = models.IntegerField(db_column='PAGES')  # Field name made lowercase.
#     versionnum = models.FloatField(db_column='VERSIONNUM')  # Field name made lowercase.
#     versiontime = models.DateTimeField(db_column='VERSIONTIME')  # Field name made lowercase.
#     versioncreator = models.CharField(db_column='VERSIONCREATOR', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
#     versioncomments = models.TextField(db_column='VERSIONCOMMENTS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
#     trashuserid = models.IntegerField(db_column='TRASHUSERID', blank=True, null=True)  # Field name made lowercase.
#     trashdatetime = models.DateTimeField(db_column='TRASHDATETIME', blank=True, null=True)  # Field name made lowercase.
#     totalbytes = models.FloatField(db_column='TOTALBYTES', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'PVDM_OBJS_1_5'






# class PvdmObjs113(models.Model):
#     objid = models.AutoField(db_column='OBJID', primary_key=True)  # Field name made lowercase.
#     docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.
#     objtype = models.SmallIntegerField(db_column='OBJTYPE')  # Field name made lowercase.
#     hashtype = models.SmallIntegerField(db_column='HASHTYPE')  # Field name made lowercase.
#     hashinfo = models.CharField(db_column='HASHINFO', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
#     filelist = models.TextField(db_column='FILELIST', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
#     pages = models.IntegerField(db_column='PAGES')  # Field name made lowercase.
#     versionnum = models.FloatField(db_column='VERSIONNUM')  # Field name made lowercase.
#     versiontime = models.DateTimeField(db_column='VERSIONTIME')  # Field name made lowercase.
#     versioncreator = models.CharField(db_column='VERSIONCREATOR', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
#     versioncomments = models.TextField(db_column='VERSIONCOMMENTS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
#     trashuserid = models.IntegerField(db_column='TRASHUSERID', blank=True, null=True)  # Field name made lowercase.
#     trashdatetime = models.DateTimeField(db_column='TRASHDATETIME', blank=True, null=True)  # Field name made lowercase.
#     totalbytes = models.FloatField(db_column='TOTALBYTES', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'PVDM_OBJS_1_13'


# class PvdmObjs114(models.Model):
#     objid = models.AutoField(db_column='OBJID', primary_key=True)  # Field name made lowercase.
#     docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.
#     objtype = models.SmallIntegerField(db_column='OBJTYPE')  # Field name made lowercase.
#     hashtype = models.SmallIntegerField(db_column='HASHTYPE')  # Field name made lowercase.
#     hashinfo = models.CharField(db_column='HASHINFO', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
#     filelist = models.TextField(db_column='FILELIST', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
#     pages = models.IntegerField(db_column='PAGES')  # Field name made lowercase.
#     versionnum = models.FloatField(db_column='VERSIONNUM')  # Field name made lowercase.
#     versiontime = models.DateTimeField(db_column='VERSIONTIME')  # Field name made lowercase.
#     versioncreator = models.CharField(db_column='VERSIONCREATOR', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
#     versioncomments = models.TextField(db_column='VERSIONCOMMENTS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
#     trashuserid = models.IntegerField(db_column='TRASHUSERID', blank=True, null=True)  # Field name made lowercase.
#     trashdatetime = models.DateTimeField(db_column='TRASHDATETIME', blank=True, null=True)  # Field name made lowercase.
#     totalbytes = models.FloatField(db_column='TOTALBYTES', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'PVDM_OBJS_1_14'




# class PvdmDocs15(models.Model):
#     docid = models.AutoField(db_column='DOCID', primary_key=True)  # Field name made lowercase.
#     docindex1 = models.CharField(db_column='DOCINDEX1', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     docindex2 = models.CharField(db_column='DOCINDEX2', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     docindex3 = models.CharField(db_column='DOCINDEX3', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     docindex4 = models.CharField(db_column='DOCINDEX4', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     createdate = models.DateTimeField(db_column='CREATEDATE')  # Field name made lowercase.
#     dupeid = models.IntegerField(db_column='DUPEID')  # Field name made lowercase.
#     securelist = models.TextField(db_column='SECURELIST', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     checkouttime = models.DateTimeField(db_column='CHECKOUTTIME', blank=True, null=True)  # Field name made lowercase.
#     checkoutuserid = models.IntegerField(db_column='CHECKOUTUSERID', blank=True, null=True)  # Field name made lowercase.
#     sourcedocid = models.IntegerField(db_column='SOURCEDOCID')  # Field name made lowercase.
#     dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
#     ftindex = models.IntegerField(db_column='FTINDEX')  # Field name made lowercase.
#     lockdate = models.DateTimeField(db_column='LOCKDATE', blank=True, null=True)  # Field name made lowercase.
#     lockinfo = models.TextField(db_column='LOCKINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     destdate = models.DateTimeField(db_column='DESTDATE', blank=True, null=True)  # Field name made lowercase.
#     destinfo = models.TextField(db_column='DESTINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     destlistid = models.IntegerField(db_column='DESTLISTID', blank=True, null=True)  # Field name made lowercase.
#     docindex5 = models.DateTimeField(db_column='DOCINDEX5', blank=True, null=True)  # Field name made lowercase.
#     docindex6 = models.CharField(db_column='DOCINDEX6', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     wftriggerdatetime = models.DateTimeField(db_column='WFTRIGGERDATETIME', blank=True, null=True)  # Field name made lowercase.
#     ocrstatus = models.SmallIntegerField(db_column='OCRSTATUS', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'PVDM_DOCS_1_5'




# class PvdmDocs113(models.Model):
#     docid = models.AutoField(db_column='DOCID', primary_key=True)  # Field name made lowercase.
#     docindex1 = models.CharField(db_column='DOCINDEX1', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     docindex2 = models.CharField(db_column='DOCINDEX2', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     docindex3 = models.CharField(db_column='DOCINDEX3', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     docindex4 = models.CharField(db_column='DOCINDEX4', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     createdate = models.DateTimeField(db_column='CREATEDATE')  # Field name made lowercase.
#     dupeid = models.IntegerField(db_column='DUPEID')  # Field name made lowercase.
#     securelist = models.TextField(db_column='SECURELIST', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     checkouttime = models.DateTimeField(db_column='CHECKOUTTIME', blank=True, null=True)  # Field name made lowercase.
#     checkoutuserid = models.IntegerField(db_column='CHECKOUTUSERID', blank=True, null=True)  # Field name made lowercase.
#     sourcedocid = models.IntegerField(db_column='SOURCEDOCID')  # Field name made lowercase.
#     dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
#     ftindex = models.IntegerField(db_column='FTINDEX')  # Field name made lowercase.
#     lockdate = models.DateTimeField(db_column='LOCKDATE', blank=True, null=True)  # Field name made lowercase.
#     lockinfo = models.TextField(db_column='LOCKINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     destdate = models.DateTimeField(db_column='DESTDATE', blank=True, null=True)  # Field name made lowercase.
#     destinfo = models.TextField(db_column='DESTINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     destlistid = models.IntegerField(db_column='DESTLISTID', blank=True, null=True)  # Field name made lowercase.
#     wftriggerdatetime = models.DateTimeField(db_column='WFTRIGGERDATETIME', blank=True, null=True)  # Field name made lowercase.
#     ocrstatus = models.SmallIntegerField(db_column='OCRSTATUS', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'PVDM_DOCS_1_13'


# class PvdmDocs114(models.Model):
#     docid = models.AutoField(db_column='DOCID', primary_key=True)  # Field name made lowercase.
#     docindex1 = models.CharField(db_column='DOCINDEX1', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     docindex2 = models.CharField(db_column='DOCINDEX2', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     docindex3 = models.CharField(db_column='DOCINDEX3', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     docindex4 = models.CharField(db_column='DOCINDEX4', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     docindex5 = models.CharField(db_column='DOCINDEX5', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     docindex6 = models.CharField(db_column='DOCINDEX6', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     docindex7 = models.DateTimeField(db_column='DOCINDEX7', blank=True, null=True)  # Field name made lowercase.
#     docindex8 = models.CharField(db_column='DOCINDEX8', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     createdate = models.DateTimeField(db_column='CREATEDATE')  # Field name made lowercase.
#     dupeid = models.IntegerField(db_column='DUPEID')  # Field name made lowercase.
#     securelist = models.TextField(db_column='SECURELIST', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     checkouttime = models.DateTimeField(db_column='CHECKOUTTIME', blank=True, null=True)  # Field name made lowercase.
#     checkoutuserid = models.IntegerField(db_column='CHECKOUTUSERID', blank=True, null=True)  # Field name made lowercase.
#     sourcedocid = models.IntegerField(db_column='SOURCEDOCID')  # Field name made lowercase.
#     dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
#     ftindex = models.IntegerField(db_column='FTINDEX')  # Field name made lowercase.
#     lockdate = models.DateTimeField(db_column='LOCKDATE', blank=True, null=True)  # Field name made lowercase.
#     lockinfo = models.TextField(db_column='LOCKINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     destdate = models.DateTimeField(db_column='DESTDATE', blank=True, null=True)  # Field name made lowercase.
#     destinfo = models.TextField(db_column='DESTINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     destlistid = models.IntegerField(db_column='DESTLISTID', blank=True, null=True)  # Field name made lowercase.
#     wftriggerdatetime = models.DateTimeField(db_column='WFTRIGGERDATETIME', blank=True, null=True)  # Field name made lowercase.
#     docindex9 = models.CharField(db_column='DOCINDEX9', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     docindex10 = models.CharField(db_column='DOCINDEX10', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     docindex11 = models.CharField(db_column='DOCINDEX11', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     docindex12 = models.CharField(db_column='DOCINDEX12', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     ocrstatus = models.SmallIntegerField(db_column='OCRSTATUS', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'PVDM_DOCS_1_14'