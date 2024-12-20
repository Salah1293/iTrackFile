# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Clerkorderdoctype(models.Model):
    doctype = models.CharField(db_column='DocType', max_length=4, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    doctypedescription = models.CharField(db_column='DocTypeDescription', max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClerkOrderDoctype'


class Deputyclerknames(models.Model):
    name = models.CharField(db_column='Name', max_length=61, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    code = models.DecimalField(db_column='CODE', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DeputyClerkNames'


class ExpungedCases(models.Model):
    casenumber = models.CharField(db_column='CASENUMBER', max_length=54, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EXPUNGED_CASES'


class Fmbrain(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    connection = models.TextField(db_column='Connection', db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    matchthreshold = models.IntegerField(db_column='MatchThreshold')  # Field name made lowercase.
    matchmincount = models.IntegerField(db_column='MatchMinCount')  # Field name made lowercase.
    filteredwordminsize = models.IntegerField(db_column='FilteredWordMinSize')  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=20, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    imagepath = models.TextField(db_column='ImagePath', db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    nextsetupimage = models.IntegerField(db_column='NextSetupImage')  # Field name made lowercase.
    othersettings = models.TextField(db_column='OtherSettings', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    deleted = models.BooleanField(db_column='Deleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FMBrain'


class Fmsystemsetting(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    value = models.TextField(db_column='Value', db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FMSystemSetting'


class Fmuserpreference(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=50, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    classificationsort = models.IntegerField(db_column='ClassificationSort')  # Field name made lowercase.
    contenttypesort = models.IntegerField(db_column='ContentTypeSort')  # Field name made lowercase.
    othersettings = models.TextField(db_column='OtherSettings', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FMUserPreference'





class ImageRecsNotToImport(models.Model):
    casenumber = models.CharField(db_column='CASENUMBER', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    label = models.CharField(db_column='LABEL', max_length=25, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IMAGE_RECS_NOT_TO_IMPORT'





class PvcapBatchstatistic1(models.Model):
    batchstatisticid = models.BigAutoField(db_column='BATCHSTATISTICID', primary_key=True)  # Field name made lowercase.
    batchid = models.BigIntegerField(db_column='BATCHID')  # Field name made lowercase.
    statistictype = models.CharField(db_column='STATISTICTYPE', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    jobid = models.BigIntegerField(db_column='JOBID')  # Field name made lowercase.
    stepid = models.IntegerField(db_column='STEPID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    workstation = models.CharField(db_column='WORKSTATION', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    start = models.DateTimeField(db_column='START', blank=True, null=True)  # Field name made lowercase.
    end = models.DateTimeField(db_column='END', blank=True, null=True)  # Field name made lowercase.
    value = models.BigIntegerField(db_column='VALUE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVCAP_BATCHSTATISTIC_1'





class PvcapJobstepgroups1(models.Model):
    jobid = models.BigIntegerField(db_column='JOBID')  # Field name made lowercase.
    stepid = models.IntegerField(db_column='STEPID', primary_key=True)  # Field name made lowercase. The composite primary key (STEPID, JOBID, GROUPID) found, that is not supported. The first column is selected.
    groupid = models.IntegerField(db_column='GROUPID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVCAP_JOBSTEPGROUPS_1'
        unique_together = (('stepid', 'jobid', 'groupid'),)


class PvcapJobstepusers1(models.Model):
    jobid = models.BigIntegerField(db_column='JOBID')  # Field name made lowercase.
    stepid = models.IntegerField(db_column='STEPID', primary_key=True)  # Field name made lowercase. The composite primary key (STEPID, JOBID, USERID) found, that is not supported. The first column is selected.
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVCAP_JOBSTEPUSERS_1'
        unique_together = (('stepid', 'jobid', 'userid'),)


class PvcapJobstep1(models.Model):
    stepid = models.IntegerField(db_column='STEPID', primary_key=True)  # Field name made lowercase. The composite primary key (STEPID, JOBID) found, that is not supported. The first column is selected.
    jobid = models.BigIntegerField(db_column='JOBID')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    steptypeid = models.SmallIntegerField(db_column='STEPTYPEID')  # Field name made lowercase.
    isautomated = models.BooleanField(db_column='ISAUTOMATED')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='ISDELETED')  # Field name made lowercase.
    isstartstep = models.BooleanField(db_column='ISSTARTSTEP')  # Field name made lowercase.
    nextstepid = models.IntegerField(db_column='NEXTSTEPID', blank=True, null=True)  # Field name made lowercase.
    agepriority = models.BigIntegerField(db_column='AGEPRIORITY')  # Field name made lowercase.
    steppriority = models.BigIntegerField(db_column='STEPPRIORITY')  # Field name made lowercase.
    uiproperties = models.TextField(db_column='UIPROPERTIES', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    stepproperties = models.TextField(db_column='STEPPROPERTIES', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    isallusers = models.BooleanField(db_column='ISALLUSERS')  # Field name made lowercase.
    failjobstepid = models.IntegerField(db_column='FAILJOBSTEPID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVCAP_JOBSTEP_1'
        unique_together = (('stepid', 'jobid'),)



class PvdmAnnotes11(models.Model):
    annoteid = models.AutoField(db_column='ANNOTEID', primary_key=True)  # Field name made lowercase.
    objid = models.IntegerField(db_column='OBJID')  # Field name made lowercase.
    pagenum = models.IntegerField(db_column='PAGENUM')  # Field name made lowercase.
    annotedata = models.BinaryField(db_column='ANNOTEDATA', blank=True, null=True)  # Field name made lowercase.
    annotetext = models.TextField(db_column='ANNOTETEXT', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_ANNOTES_1_1'


class PvdmAnnotes110(models.Model):
    annoteid = models.AutoField(db_column='ANNOTEID', primary_key=True)  # Field name made lowercase.
    objid = models.IntegerField(db_column='OBJID')  # Field name made lowercase.
    pagenum = models.IntegerField(db_column='PAGENUM')  # Field name made lowercase.
    annotedata = models.BinaryField(db_column='ANNOTEDATA', blank=True, null=True)  # Field name made lowercase.
    annotetext = models.TextField(db_column='ANNOTETEXT', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_ANNOTES_1_10'


class PvdmAnnotes112(models.Model):
    annoteid = models.AutoField(db_column='ANNOTEID', primary_key=True)  # Field name made lowercase.
    objid = models.IntegerField(db_column='OBJID')  # Field name made lowercase.
    pagenum = models.IntegerField(db_column='PAGENUM')  # Field name made lowercase.
    annotedata = models.BinaryField(db_column='ANNOTEDATA', blank=True, null=True)  # Field name made lowercase.
    annotetext = models.TextField(db_column='ANNOTETEXT', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_ANNOTES_1_12'


class PvdmAnnotes113(models.Model):
    annoteid = models.AutoField(db_column='ANNOTEID', primary_key=True)  # Field name made lowercase.
    objid = models.IntegerField(db_column='OBJID')  # Field name made lowercase.
    pagenum = models.IntegerField(db_column='PAGENUM')  # Field name made lowercase.
    annotedata = models.BinaryField(db_column='ANNOTEDATA', blank=True, null=True)  # Field name made lowercase.
    annotetext = models.TextField(db_column='ANNOTETEXT', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_ANNOTES_1_13'


class PvdmAnnotes114(models.Model):
    annoteid = models.AutoField(db_column='ANNOTEID', primary_key=True)  # Field name made lowercase.
    objid = models.IntegerField(db_column='OBJID')  # Field name made lowercase.
    pagenum = models.IntegerField(db_column='PAGENUM')  # Field name made lowercase.
    annotedata = models.BinaryField(db_column='ANNOTEDATA', blank=True, null=True)  # Field name made lowercase.
    annotetext = models.TextField(db_column='ANNOTETEXT', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_ANNOTES_1_14'


class PvdmAnnotes115(models.Model):
    annoteid = models.AutoField(db_column='ANNOTEID', primary_key=True)  # Field name made lowercase.
    objid = models.IntegerField(db_column='OBJID')  # Field name made lowercase.
    pagenum = models.IntegerField(db_column='PAGENUM')  # Field name made lowercase.
    annotedata = models.BinaryField(db_column='ANNOTEDATA', blank=True, null=True)  # Field name made lowercase.
    annotetext = models.TextField(db_column='ANNOTETEXT', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_ANNOTES_1_15'


class PvdmAnnotes116(models.Model):
    annoteid = models.AutoField(db_column='ANNOTEID', primary_key=True)  # Field name made lowercase.
    objid = models.IntegerField(db_column='OBJID')  # Field name made lowercase.
    pagenum = models.IntegerField(db_column='PAGENUM')  # Field name made lowercase.
    annotedata = models.BinaryField(db_column='ANNOTEDATA', blank=True, null=True)  # Field name made lowercase.
    annotetext = models.TextField(db_column='ANNOTETEXT', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_ANNOTES_1_16'


class PvdmAnnotes12(models.Model):
    annoteid = models.AutoField(db_column='ANNOTEID', primary_key=True)  # Field name made lowercase.
    objid = models.IntegerField(db_column='OBJID')  # Field name made lowercase.
    pagenum = models.IntegerField(db_column='PAGENUM')  # Field name made lowercase.
    annotedata = models.BinaryField(db_column='ANNOTEDATA', blank=True, null=True)  # Field name made lowercase.
    annotetext = models.TextField(db_column='ANNOTETEXT', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_ANNOTES_1_2'


class PvdmAnnotes13(models.Model):
    annoteid = models.AutoField(db_column='ANNOTEID', primary_key=True)  # Field name made lowercase.
    objid = models.IntegerField(db_column='OBJID')  # Field name made lowercase.
    pagenum = models.IntegerField(db_column='PAGENUM')  # Field name made lowercase.
    annotedata = models.BinaryField(db_column='ANNOTEDATA', blank=True, null=True)  # Field name made lowercase.
    annotetext = models.TextField(db_column='ANNOTETEXT', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_ANNOTES_1_3'


class PvdmAnnotes14(models.Model):
    annoteid = models.AutoField(db_column='ANNOTEID', primary_key=True)  # Field name made lowercase.
    objid = models.IntegerField(db_column='OBJID')  # Field name made lowercase.
    pagenum = models.IntegerField(db_column='PAGENUM')  # Field name made lowercase.
    annotedata = models.BinaryField(db_column='ANNOTEDATA', blank=True, null=True)  # Field name made lowercase.
    annotetext = models.TextField(db_column='ANNOTETEXT', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_ANNOTES_1_4'


class PvdmAnnotes15(models.Model):
    annoteid = models.AutoField(db_column='ANNOTEID', primary_key=True)  # Field name made lowercase.
    objid = models.IntegerField(db_column='OBJID')  # Field name made lowercase.
    pagenum = models.IntegerField(db_column='PAGENUM')  # Field name made lowercase.
    annotedata = models.BinaryField(db_column='ANNOTEDATA', blank=True, null=True)  # Field name made lowercase.
    annotetext = models.TextField(db_column='ANNOTETEXT', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_ANNOTES_1_5'


class PvdmAnnotes16(models.Model):
    annoteid = models.AutoField(db_column='ANNOTEID', primary_key=True)  # Field name made lowercase.
    objid = models.IntegerField(db_column='OBJID')  # Field name made lowercase.
    pagenum = models.IntegerField(db_column='PAGENUM')  # Field name made lowercase.
    annotedata = models.BinaryField(db_column='ANNOTEDATA', blank=True, null=True)  # Field name made lowercase.
    annotetext = models.TextField(db_column='ANNOTETEXT', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_ANNOTES_1_6'


class PvdmAnnotes17(models.Model):
    annoteid = models.AutoField(db_column='ANNOTEID', primary_key=True)  # Field name made lowercase.
    objid = models.IntegerField(db_column='OBJID')  # Field name made lowercase.
    pagenum = models.IntegerField(db_column='PAGENUM')  # Field name made lowercase.
    annotedata = models.BinaryField(db_column='ANNOTEDATA', blank=True, null=True)  # Field name made lowercase.
    annotetext = models.TextField(db_column='ANNOTETEXT', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_ANNOTES_1_7'


class PvdmAnnotes18(models.Model):
    annoteid = models.AutoField(db_column='ANNOTEID', primary_key=True)  # Field name made lowercase.
    objid = models.IntegerField(db_column='OBJID')  # Field name made lowercase.
    pagenum = models.IntegerField(db_column='PAGENUM')  # Field name made lowercase.
    annotedata = models.BinaryField(db_column='ANNOTEDATA', blank=True, null=True)  # Field name made lowercase.
    annotetext = models.TextField(db_column='ANNOTETEXT', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_ANNOTES_1_8'


class PvdmAnnotes19(models.Model):
    annoteid = models.AutoField(db_column='ANNOTEID', primary_key=True)  # Field name made lowercase.
    objid = models.IntegerField(db_column='OBJID')  # Field name made lowercase.
    pagenum = models.IntegerField(db_column='PAGENUM')  # Field name made lowercase.
    annotedata = models.BinaryField(db_column='ANNOTEDATA', blank=True, null=True)  # Field name made lowercase.
    annotetext = models.TextField(db_column='ANNOTETEXT', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_ANNOTES_1_9'


class PvdmArchives1(models.Model):
    archiveid = models.AutoField(db_column='ARCHIVEID', primary_key=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='STARTTIME')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='ENDTIME')  # Field name made lowercase.
    runtime = models.DateTimeField(db_column='RUNTIME')  # Field name made lowercase.
    archivedata = models.TextField(db_column='ARCHIVEDATA', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    archivetype = models.SmallIntegerField(db_column='ARCHIVETYPE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_ARCHIVES_1'


class PvdmBadlogins1(models.Model):
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    attempttime = models.DateTimeField(db_column='ATTEMPTTIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_BADLOGINS_1'


class PvdmCode1(models.Model):
    codeid = models.CharField(db_column='CODEID', primary_key=True, max_length=36)  # Field name made lowercase.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    codetype = models.SmallIntegerField(db_column='CODETYPE')  # Field name made lowercase.
    codename = models.CharField(db_column='CODENAME', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    codetext = models.TextField(db_column='CODETEXT', db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_CODE_1'


class PvdmConfiginfo1(models.Model):
    configid = models.AutoField(db_column='CONFIGID', primary_key=True)  # Field name made lowercase.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    configtype = models.CharField(db_column='CONFIGTYPE', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    configinfo = models.TextField(db_column='CONFIGINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_CONFIGINFO_1'


class PvdmCounters1(models.Model):
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    countertype = models.IntegerField(db_column='COUNTERTYPE')  # Field name made lowercase.
    counterval = models.IntegerField(db_column='COUNTERVAL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_COUNTERS_1'


class PvdmCustomcounters1(models.Model):
    key = models.CharField(db_column='KEY', primary_key=True, max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    counter = models.BigIntegerField(db_column='COUNTER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_CUSTOMCOUNTERS_1'


class PvdmDgprojs1(models.Model):
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    lastloaddocid = models.IntegerField(db_column='LASTLOADDOCID')  # Field name made lowercase.
    dgprojjob = models.CharField(db_column='DGPROJJOB', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_DGPROJS_1'





class PvdmDirmgrjobs1(models.Model):
    dirmgrjobid = models.AutoField(db_column='DIRMGRJOBID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    monitorpath = models.TextField(db_column='MONITORPATH', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    workstation = models.CharField(db_column='WORKSTATION', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    jobinfo = models.TextField(db_column='JOBINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='ISACTIVE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_DIRMGRJOBS_1'


class PvdmDiscreasons1(models.Model):
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    reason = models.CharField(db_column='REASON', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_DISCREASONS_1'


class PvdmDiscrecips1(models.Model):
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    recip = models.CharField(db_column='RECIP', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_DISCRECIPS_1'


class PvdmDocassocs1(models.Model):
    associd = models.AutoField(db_column='ASSOCID', primary_key=True)  # Field name made lowercase.
    assocname = models.CharField(db_column='ASSOCNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    sourceprojid = models.IntegerField(db_column='SOURCEPROJID')  # Field name made lowercase.
    searchprojid = models.IntegerField(db_column='SEARCHPROJID')  # Field name made lowercase.
    associnfo = models.TextField(db_column='ASSOCINFO', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_DOCASSOCS_1'


class PvdmDocgrants1(models.Model):
    grantid = models.CharField(db_column='GRANTID', primary_key=True, max_length=36)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CREATETIME')  # Field name made lowercase.
    expiretime = models.DateTimeField(db_column='EXPIRETIME', blank=True, null=True)  # Field name made lowercase.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    indexinfo = models.CharField(db_column='INDEXINFO', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    grantinfo = models.TextField(db_column='GRANTINFO', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_DOCGRANTS_1'


class PvdmDocseclevs1(models.Model):
    dslid = models.AutoField(db_column='DSLID', primary_key=True)  # Field name made lowercase.
    dslname = models.CharField(db_column='DSLNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    autocriteria = models.TextField(db_column='AUTOCRITERIA', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    applymode = models.IntegerField(db_column='APPLYMODE', blank=True, null=True)  # Field name made lowercase.
    applymethod = models.SmallIntegerField(db_column='APPLYMETHOD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_DOCSECLEVS_1'




class PvdmEformpkgDef1(models.Model):
    pkgdefid = models.AutoField(db_column='PKGDEFID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ispublish = models.BooleanField(db_column='ISPUBLISH')  # Field name made lowercase.
    ispublic = models.BooleanField(db_column='ISPUBLIC')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='ISDELETED')  # Field name made lowercase.
    expiration = models.DateTimeField(db_column='EXPIRATION')  # Field name made lowercase.
    settings = models.TextField(db_column='SETTINGS', db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_EFORMPKG_DEF_1'


class PvdmEformpkgInst1(models.Model):
    pkginstid = models.CharField(db_column='PKGINSTID', primary_key=True, max_length=36)  # Field name made lowercase.
    pkgdefid = models.IntegerField(db_column='PKGDEFID')  # Field name made lowercase.
    iscomplete = models.BooleanField(db_column='ISCOMPLETE')  # Field name made lowercase.
    expiration = models.DateTimeField(db_column='EXPIRATION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_EFORMPKG_INST_1'


class PvdmEforms1(models.Model):
    eformid = models.AutoField(db_column='EFORMID', primary_key=True)  # Field name made lowercase.
    eformname = models.CharField(db_column='EFORMNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ispublish = models.BooleanField(db_column='ISPUBLISH')  # Field name made lowercase.
    ispublic = models.BooleanField(db_column='ISPUBLIC')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='ISDELETED')  # Field name made lowercase.
    expiration = models.DateTimeField(db_column='EXPIRATION')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_EFORMS_1'


class PvdmEformversions1(models.Model):
    eformversionid = models.AutoField(db_column='EFORMVERSIONID', primary_key=True)  # Field name made lowercase.
    eformid = models.IntegerField(db_column='EFORMID')  # Field name made lowercase.
    version = models.CharField(db_column='VERSION', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    settings = models.TextField(db_column='SETTINGS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdatetime = models.DateTimeField(db_column='CREATEDATETIME')  # Field name made lowercase.
    createdby = models.CharField(db_column='CREATEDBY', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    comments = models.TextField(db_column='COMMENTS', db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    storage = models.TextField(db_column='STORAGE', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_EFORMVERSIONS_1'


class PvdmEncryptkeys1(models.Model):
    keyid = models.AutoField(db_column='KEYID', primary_key=True)  # Field name made lowercase.
    keytype = models.IntegerField(db_column='KEYTYPE')  # Field name made lowercase.
    keyname = models.CharField(db_column='KEYNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    keyvalue = models.CharField(db_column='KEYVALUE', max_length=4000, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    keyinfo = models.TextField(db_column='KEYINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_ENCRYPTKEYS_1'


class PvdmErmfilesets1(models.Model):
    ermfilesetid = models.AutoField(db_column='ERMFILESETID', primary_key=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='WORKSTATION', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    ermjobid = models.IntegerField(db_column='ERMJOBID')  # Field name made lowercase.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    ermjobname = models.CharField(db_column='ERMJOBNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    dgname = models.CharField(db_column='DGNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    dgfilesetname = models.CharField(db_column='DGFILESETNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    filesprocessed = models.TextField(db_column='FILESPROCESSED', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    datetimestarted = models.DateTimeField(db_column='DATETIMESTARTED')  # Field name made lowercase.
    datetimefinished = models.DateTimeField(db_column='DATETIMEFINISHED')  # Field name made lowercase.
    totaldocs = models.IntegerField(db_column='TOTALDOCS')  # Field name made lowercase.
    totalpages = models.IntegerField(db_column='TOTALPAGES')  # Field name made lowercase.
    totalbytes = models.FloatField(db_column='TOTALBYTES')  # Field name made lowercase.
    totaltime = models.IntegerField(db_column='TOTALTIME')  # Field name made lowercase.
    imported = models.BooleanField(db_column='IMPORTED')  # Field name made lowercase.
    processed = models.BooleanField(db_column='PROCESSED', blank=True, null=True)  # Field name made lowercase.
    removedfromdg = models.BooleanField(db_column='REMOVEDFROMDG')  # Field name made lowercase.
    trashuserid = models.IntegerField(db_column='TRASHUSERID', blank=True, null=True)  # Field name made lowercase.
    trashdatetime = models.DateTimeField(db_column='TRASHDATETIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_ERMFILESETS_1'


class PvdmErmjobs1(models.Model):
    ermjobid = models.AutoField(db_column='ERMJOBID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    monitorpath = models.TextField(db_column='MONITORPATH', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    workstation = models.CharField(db_column='WORKSTATION', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    jobinfo = models.TextField(db_column='JOBINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='ISACTIVE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_ERMJOBS_1'


class PvdmErmolfiles1(models.Model):
    olfileid = models.AutoField(db_column='OLFILEID', primary_key=True)  # Field name made lowercase.
    ermjobid = models.IntegerField(db_column='ERMJOBID')  # Field name made lowercase.
    filename = models.TextField(db_column='FILENAME', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    filedata = models.BinaryField(db_column='FILEDATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_ERMOLFILES_1'


class PvdmFoldercontentsDoc1(models.Model):
    parentid = models.CharField(db_column='PARENTID', primary_key=True, max_length=36)  # Field name made lowercase. The composite primary key (PARENTID, CHILDDOCID, PROJID) found, that is not supported. The first column is selected.
    childdocid = models.IntegerField(db_column='CHILDDOCID')  # Field name made lowercase.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_FOLDERCONTENTS_DOC_1'
        unique_together = (('parentid', 'childdocid', 'projid'),)


class PvdmFoldercontentsFld1(models.Model):
    parentid = models.CharField(db_column='PARENTID', primary_key=True, max_length=36)  # Field name made lowercase. The composite primary key (PARENTID, CHILDFOLDERID, PROJID) found, that is not supported. The first column is selected.
    childfolderid = models.CharField(db_column='CHILDFOLDERID', max_length=36)  # Field name made lowercase.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_FOLDERCONTENTS_FLD_1'
        unique_together = (('parentid', 'childfolderid', 'projid'),)


class PvdmFolders1(models.Model):
    folderid = models.CharField(db_column='FOLDERID', primary_key=True, max_length=36)  # Field name made lowercase.
    foldername = models.CharField(db_column='FOLDERNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CREATEDATE')  # Field name made lowercase.
    securelist = models.TextField(db_column='SECURELIST', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    scparentid = models.CharField(db_column='SCPARENTID', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_FOLDERS_1'


class PvdmGroupmemb1(models.Model):
    groupid = models.IntegerField(db_column='GROUPID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_GROUPMEMB_1'


class PvdmGrouppermission1(models.Model):
    groupid = models.IntegerField(db_column='GROUPID', primary_key=True)  # Field name made lowercase. The composite primary key (GROUPID, APPOBJECTID) found, that is not supported. The first column is selected.
    appobjectid = models.CharField(db_column='APPOBJECTID', max_length=36)  # Field name made lowercase.
    permissionlevel = models.IntegerField(db_column='PERMISSIONLEVEL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_GROUPPERMISSION_1'
        unique_together = (('groupid', 'appobjectid'),)


class PvdmGroups1(models.Model):
    groupid = models.AutoField(db_column='GROUPID', primary_key=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='GROUPNAME', unique=True, max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    groupsettings = models.TextField(db_column='GROUPSETTINGS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_GROUPS_1'


class PvdmIntdefs1(models.Model):
    intdefid = models.AutoField(db_column='INTDEFID', primary_key=True)  # Field name made lowercase.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    defname = models.CharField(db_column='DEFNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    keycombo = models.CharField(db_column='KEYCOMBO', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    definfo = models.TextField(db_column='DEFINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_INTDEFS_1'


class PvdmLockouts1(models.Model):
    lockoutid = models.AutoField(db_column='LOCKOUTID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    lockouttime = models.DateTimeField(db_column='LOCKOUTTIME')  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_LOCKOUTS_1'


class PvdmMapDocsEformpkginsts1(models.Model):
    docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    pkginstid = models.CharField(db_column='PKGINSTID', max_length=36)  # Field name made lowercase.
    itemorder = models.IntegerField(db_column='ITEMORDER')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_MAP_DOCS_EFORMPKGINSTS_1'


class PvdmMigrations1(models.Model):
    migid = models.AutoField(db_column='MIGID', primary_key=True)  # Field name made lowercase.
    migname = models.CharField(db_column='MIGNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    doclist = models.TextField(db_column='DOCLIST', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    submittime = models.DateTimeField(db_column='SUBMITTIME', blank=True, null=True)  # Field name made lowercase.
    submitinfo = models.TextField(db_column='SUBMITINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    finishtime = models.DateTimeField(db_column='FINISHTIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_MIGRATIONS_1'


class PvdmMsgcappolicysets1(models.Model):
    setid = models.AutoField(db_column='SETID', primary_key=True)  # Field name made lowercase.
    setname = models.CharField(db_column='SETNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    policyinfo = models.TextField(db_column='POLICYINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    policycount = models.IntegerField(db_column='POLICYCOUNT')  # Field name made lowercase.
    createdatetime = models.DateTimeField(db_column='CREATEDATETIME')  # Field name made lowercase.
    createdby = models.CharField(db_column='CREATEDBY', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    comments = models.TextField(db_column='COMMENTS', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_MSGCAPPOLICYSETS_1'


class PvdmMsgfilesets1(models.Model):
    msgfilesetid = models.AutoField(db_column='MSGFILESETID', primary_key=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='WORKSTATION', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    policysetid = models.IntegerField(db_column='POLICYSETID')  # Field name made lowercase.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    policysetname = models.CharField(db_column='POLICYSETNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    dgname = models.CharField(db_column='DGNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    dgfilesetname = models.CharField(db_column='DGFILESETNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    datetimestarted = models.DateTimeField(db_column='DATETIMESTARTED')  # Field name made lowercase.
    datetimefinished = models.DateTimeField(db_column='DATETIMEFINISHED')  # Field name made lowercase.
    totaldocs = models.IntegerField(db_column='TOTALDOCS')  # Field name made lowercase.
    totalmessages = models.IntegerField(db_column='TOTALMESSAGES')  # Field name made lowercase.
    totalbytes = models.FloatField(db_column='TOTALBYTES')  # Field name made lowercase.
    totaltime = models.IntegerField(db_column='TOTALTIME')  # Field name made lowercase.
    imported = models.BooleanField(db_column='IMPORTED')  # Field name made lowercase.
    compression = models.BooleanField(db_column='COMPRESSION')  # Field name made lowercase.
    encryptkeyname = models.CharField(db_column='ENCRYPTKEYNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    filesetversion = models.CharField(db_column='FILESETVERSION', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    trashuserid = models.IntegerField(db_column='TRASHUSERID', blank=True, null=True)  # Field name made lowercase.
    trashdatetime = models.DateTimeField(db_column='TRASHDATETIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_MSGFILESETS_1'


class PvdmNotifications0(models.Model):
    notifyid = models.AutoField(db_column='NOTIFYID', primary_key=True)  # Field name made lowercase.
    recuserid = models.IntegerField(db_column='RECUSERID')  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    notifytime = models.DateTimeField(db_column='NOTIFYTIME')  # Field name made lowercase.
    notifyinfo = models.TextField(db_column='NOTIFYINFO', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_NOTIFICATIONS_0'


class PvdmNotifications1(models.Model):
    notifyid = models.AutoField(db_column='NOTIFYID', primary_key=True)  # Field name made lowercase.
    recuserid = models.IntegerField(db_column='RECUSERID')  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    notifytime = models.DateTimeField(db_column='NOTIFYTIME')  # Field name made lowercase.
    notifyinfo = models.TextField(db_column='NOTIFYINFO', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_NOTIFICATIONS_1'




class PvdmPermissiongroup1(models.Model):
    permissiongroupid = models.CharField(db_column='PERMISSIONGROUPID', primary_key=True, max_length=36)  # Field name made lowercase.
    appid = models.IntegerField(db_column='APPID')  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SORTORDER')  # Field name made lowercase.
    supergroupid = models.CharField(db_column='SUPERGROUPID', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_PERMISSIONGROUP_1'


class PvdmPermissionsupergroup1(models.Model):
    supergroupid = models.CharField(db_column='SUPERGROUPID', primary_key=True, max_length=36)  # Field name made lowercase.
    appid = models.IntegerField(db_column='APPID')  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SORTORDER')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_PERMISSIONSUPERGROUP_1'


class PvdmPermission1(models.Model):
    permissionid = models.AutoField(db_column='PERMISSIONID', primary_key=True)  # Field name made lowercase.
    permissiongroupid = models.CharField(db_column='PERMISSIONGROUPID', max_length=36)  # Field name made lowercase.
    appobjectid = models.CharField(db_column='APPOBJECTID', max_length=36)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=250, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    permissiontype = models.IntegerField(db_column='PERMISSIONTYPE')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SORTORDER')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_PERMISSION_1'


class PvdmProjects1(models.Model):
    projid = models.AutoField(db_column='PROJID', primary_key=True)  # Field name made lowercase.
    projname = models.CharField(db_column='PROJNAME', unique=True, max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    projattrs = models.TextField(db_column='PROJATTRS', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    projtype = models.IntegerField(db_column='PROJTYPE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_PROJECTS_1'


class PvdmRecretlists1(models.Model):
    listid = models.AutoField(db_column='LISTID', primary_key=True)  # Field name made lowercase.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    createdatetime = models.DateTimeField(db_column='CREATEDATETIME')  # Field name made lowercase.
    policysetname = models.CharField(db_column='POLICYSETNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    policyname = models.CharField(db_column='POLICYNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    doccount = models.IntegerField(db_column='DOCCOUNT')  # Field name made lowercase.
    retinfo = models.TextField(db_column='RETINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    authby = models.CharField(db_column='AUTHBY', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    authdatetime = models.DateTimeField(db_column='AUTHDATETIME', blank=True, null=True)  # Field name made lowercase.
    completedatetime = models.DateTimeField(db_column='COMPLETEDATETIME', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='COMMENTS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_RECRETLISTS_1'


class PvdmRecretpolicysets1(models.Model):
    setid = models.AutoField(db_column='SETID', primary_key=True)  # Field name made lowercase.
    setname = models.CharField(db_column='SETNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    policyinfo = models.TextField(db_column='POLICYINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    policycount = models.IntegerField(db_column='POLICYCOUNT')  # Field name made lowercase.
    createdatetime = models.DateTimeField(db_column='CREATEDATETIME')  # Field name made lowercase.
    createdby = models.CharField(db_column='CREATEDBY', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    comments = models.TextField(db_column='COMMENTS', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_RECRETPOLICYSETS_1'


class PvdmRessecrights1(models.Model):
    rightid = models.AutoField(db_column='RIGHTID', primary_key=True)  # Field name made lowercase.
    resid = models.IntegerField(db_column='RESID')  # Field name made lowercase.
    restype = models.SmallIntegerField(db_column='RESTYPE')  # Field name made lowercase.
    recipid = models.IntegerField(db_column='RECIPID')  # Field name made lowercase.
    reciptype = models.SmallIntegerField(db_column='RECIPTYPE')  # Field name made lowercase.
    rights = models.IntegerField(db_column='RIGHTS')  # Field name made lowercase.
    rightdata = models.TextField(db_column='RIGHTDATA', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_RESSECRIGHTS_1'


class PvdmSearches1(models.Model):
    searchid = models.AutoField(db_column='SEARCHID', primary_key=True)  # Field name made lowercase.
    searchname = models.CharField(db_column='SEARCHNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    shared = models.BooleanField(db_column='SHARED')  # Field name made lowercase.
    searchtype = models.IntegerField(db_column='SEARCHTYPE')  # Field name made lowercase.
    searchinfo = models.TextField(db_column='SEARCHINFO', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    projects = models.TextField(db_column='PROJECTS', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_SEARCHES_1'


class PvdmSectrackdoc1(models.Model):
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    optime = models.DateTimeField(db_column='OPTIME')  # Field name made lowercase.
    optype = models.CharField(db_column='OPTYPE', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    recipient = models.CharField(db_column='RECIPIENT', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(db_column='REASON', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.
    indexdata = models.TextField(db_column='INDEXDATA', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    pagestart = models.IntegerField(db_column='PAGESTART')  # Field name made lowercase.
    pageend = models.IntegerField(db_column='PAGEEND')  # Field name made lowercase.
    sourcehost = models.CharField(db_column='SOURCEHOST', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    notes = models.TextField(db_column='NOTES', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_SECTRACKDOC_1'


class PvdmSectrackgen1(models.Model):
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    optime = models.DateTimeField(db_column='OPTIME')  # Field name made lowercase.
    optype = models.CharField(db_column='OPTYPE', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    opinfo = models.TextField(db_column='OPINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sourcehost = models.CharField(db_column='SOURCEHOST', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SECTRACKGEN_1'


class PvdmSessions0(models.Model):
    sessionid = models.CharField(db_column='SESSIONID', primary_key=True, max_length=36)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CREATETIME')  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UPDATETIME')  # Field name made lowercase.
    sessiondata = models.TextField(db_column='SESSIONDATA', db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    pingtime = models.DateTimeField(db_column='PINGTIME', blank=True, null=True)  # Field name made lowercase.
    licenses = models.IntegerField(db_column='LICENSES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SESSIONS_0'


class PvdmSessions1(models.Model):
    sessionid = models.CharField(db_column='SESSIONID', primary_key=True, max_length=36)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CREATETIME')  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UPDATETIME')  # Field name made lowercase.
    licenses = models.IntegerField(db_column='LICENSES', blank=True, null=True)  # Field name made lowercase.
    pingtime = models.DateTimeField(db_column='PINGTIME', blank=True, null=True)  # Field name made lowercase.
    sessiondata = models.TextField(db_column='SESSIONDATA', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    agentid = models.IntegerField(db_column='AGENTID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SESSIONS_1'


class PvdmSettings1(models.Model):
    settingid = models.AutoField(db_column='SETTINGID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    secure = models.SmallIntegerField(db_column='SECURE')  # Field name made lowercase.
    value = models.TextField(db_column='VALUE', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SETTINGS_1'


class PvdmSignatures1(models.Model):
    sigid = models.CharField(db_column='SIGID', primary_key=True, max_length=36)  # Field name made lowercase.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    objid = models.IntegerField(db_column='OBJID')  # Field name made lowercase.
    signame = models.CharField(db_column='SIGNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    siguserid = models.IntegerField(db_column='SIGUSERID')  # Field name made lowercase.
    sigbitmap = models.BinaryField(db_column='SIGBITMAP', blank=True, null=True)  # Field name made lowercase.
    siginfo = models.TextField(db_column='SIGINFO', db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    sigdatetime = models.DateTimeField(db_column='SIGDATETIME')  # Field name made lowercase.
    sigsourceip = models.CharField(db_column='SIGSOURCEIP', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    dochash = models.CharField(db_column='DOCHASH', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    sighash = models.CharField(db_column='SIGHASH', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SIGNATURES_1'


class PvdmSystemvalue1(models.Model):
    varname = models.CharField(db_column='VARNAME', primary_key=True, max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    varvalue = models.TextField(db_column='VARVALUE', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYSTEMVALUE_1'


class PvdmSysArchives(models.Model):
    archiveid = models.AutoField(db_column='ARCHIVEID', primary_key=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='STARTTIME')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='ENDTIME')  # Field name made lowercase.
    runtime = models.DateTimeField(db_column='RUNTIME')  # Field name made lowercase.
    archivedata = models.TextField(db_column='ARCHIVEDATA', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    archivetype = models.SmallIntegerField(db_column='ARCHIVETYPE')  # Field name made lowercase.
    entparentid = models.IntegerField(db_column='ENTPARENTID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_ARCHIVES'


class PvdmSysAutoimplogs(models.Model):
    logid = models.AutoField(db_column='LOGID', primary_key=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='WORKSTATION', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    sourcedgname = models.CharField(db_column='SOURCEDGNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    sourcedgpath = models.TextField(db_column='SOURCEDGPATH', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='STARTTIME')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='ENDTIME')  # Field name made lowercase.
    loadstatus = models.SmallIntegerField(db_column='LOADSTATUS')  # Field name made lowercase.
    message = models.TextField(db_column='MESSAGE', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    size = models.FloatField(db_column='SIZE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_AUTOIMPLOGS'


class PvdmSysAutoimppaths(models.Model):
    aipid = models.AutoField(db_column='AIPID', primary_key=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='WORKSTATION', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='ISACTIVE')  # Field name made lowercase.
    path = models.TextField(db_column='PATH', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_AUTOIMPPATHS'


class PvdmSysAutoschedule(models.Model):
    scheduleid = models.AutoField(db_column='SCHEDULEID', primary_key=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='WORKSTATION', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    operation = models.CharField(db_column='OPERATION', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    repeattype = models.CharField(db_column='REPEATTYPE', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    repeatcount = models.IntegerField(db_column='REPEATCOUNT')  # Field name made lowercase.
    repeattypedetail = models.CharField(db_column='REPEATTYPEDETAIL', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    procorder = models.IntegerField(db_column='PROCORDER')  # Field name made lowercase.
    nextrundatetime = models.DateTimeField(db_column='NEXTRUNDATETIME')  # Field name made lowercase.
    lastrundatetime = models.DateTimeField(db_column='LASTRUNDATETIME')  # Field name made lowercase.
    laststatus = models.TextField(db_column='LASTSTATUS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_AUTOSCHEDULE'


class PvdmSysBackupjobs(models.Model):
    jobid = models.AutoField(db_column='JOBID', primary_key=True)  # Field name made lowercase.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    jobname = models.CharField(db_column='JOBNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    backuptype = models.SmallIntegerField(db_column='BACKUPTYPE')  # Field name made lowercase.
    backupinfo = models.TextField(db_column='BACKUPINFO', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    repeattype = models.CharField(db_column='REPEATTYPE', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    repeatcount = models.IntegerField(db_column='REPEATCOUNT')  # Field name made lowercase.
    repeattypedetail = models.CharField(db_column='REPEATTYPEDETAIL', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    nextrundatetime = models.DateTimeField(db_column='NEXTRUNDATETIME')  # Field name made lowercase.
    lastrundatetime = models.DateTimeField(db_column='LASTRUNDATETIME')  # Field name made lowercase.
    laststatus = models.TextField(db_column='LASTSTATUS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_BACKUPJOBS'


class PvdmSysBackuplogs(models.Model):
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    jobname = models.CharField(db_column='JOBNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    runtime = models.DateTimeField(db_column='RUNTIME')  # Field name made lowercase.
    utilization = models.FloatField(db_column='UTILIZATION')  # Field name made lowercase.
    backupinfo = models.TextField(db_column='BACKUPINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_BACKUPLOGS'


class PvdmSysDeletequeue(models.Model):
    queueid = models.AutoField(db_column='QUEUEID', primary_key=True)  # Field name made lowercase.
    queuetime = models.DateTimeField(db_column='QUEUETIME')  # Field name made lowercase.
    path = models.TextField(db_column='PATH', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    queueinfo = models.TextField(db_column='QUEUEINFO', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    userinfo = models.CharField(db_column='USERINFO', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_DELETEQUEUE'


class PvdmSysDocopqueue(models.Model):
    tableident = models.BigAutoField(db_column='TABLEIDENT', primary_key=True)  # Field name made lowercase.
    queuedatetime = models.DateTimeField(db_column='QUEUEDATETIME')  # Field name made lowercase.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    startdocid = models.IntegerField(db_column='STARTDOCID')  # Field name made lowercase.
    enddocid = models.IntegerField(db_column='ENDDOCID')  # Field name made lowercase.
    proctype = models.IntegerField(db_column='PROCTYPE')  # Field name made lowercase.
    procinfo = models.TextField(db_column='PROCINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    procinfohash = models.CharField(db_column='PROCINFOHASH', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_DOCOPQUEUE'


class PvdmSysEntities(models.Model):
    entid = models.AutoField(db_column='ENTID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    entsettings = models.IntegerField(db_column='ENTSETTINGS')  # Field name made lowercase.
    entattrs = models.TextField(db_column='ENTATTRS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    startdate = models.DateTimeField(db_column='STARTDATE')  # Field name made lowercase.
    lastarchive = models.DateTimeField(db_column='LASTARCHIVE', blank=True, null=True)  # Field name made lowercase.
    entparentid = models.IntegerField(db_column='ENTPARENTID', blank=True, null=True)  # Field name made lowercase.
    billingattrs = models.TextField(db_column='BILLINGATTRS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_ENTITIES'


class PvdmSysEntparauemails(models.Model):
    auemailid = models.AutoField(db_column='AUEMAILID', primary_key=True)  # Field name made lowercase.
    auid = models.IntegerField(db_column='AUID')  # Field name made lowercase.
    entparentid = models.IntegerField(db_column='ENTPARENTID')  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_ENTPARAUEMAILS'


class PvdmSysEntparauentities(models.Model):
    auid = models.IntegerField(db_column='AUID')  # Field name made lowercase.
    entparentid = models.IntegerField(db_column='ENTPARENTID')  # Field name made lowercase.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_ENTPARAUENTITIES'


class PvdmSysEntparauphones(models.Model):
    auphoneid = models.AutoField(db_column='AUPHONEID', primary_key=True)  # Field name made lowercase.
    auid = models.IntegerField(db_column='AUID')  # Field name made lowercase.
    entparentid = models.IntegerField(db_column='ENTPARENTID')  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_ENTPARAUPHONES'


class PvdmSysEntparauthusers(models.Model):
    auid = models.AutoField(db_column='AUID', primary_key=True)  # Field name made lowercase.
    entparentid = models.IntegerField(db_column='ENTPARENTID')  # Field name made lowercase.
    auname = models.CharField(db_column='AUNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=4096, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    specifyphone = models.BooleanField(db_column='SPECIFYPHONE')  # Field name made lowercase.
    accread = models.BooleanField(db_column='ACCREAD')  # Field name made lowercase.
    accreadwrite = models.BooleanField(db_column='ACCREADWRITE')  # Field name made lowercase.
    accftp = models.BooleanField(db_column='ACCFTP')  # Field name made lowercase.
    allentities = models.BooleanField(db_column='ALLENTITIES')  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LASTUPDATED')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_ENTPARAUTHUSERS'


class PvdmSysEntparchangelogs(models.Model):
    logid = models.AutoField(db_column='LOGID', primary_key=True)  # Field name made lowercase.
    entparentid = models.IntegerField(db_column='ENTPARENTID')  # Field name made lowercase.
    changetime = models.DateTimeField(db_column='CHANGETIME')  # Field name made lowercase.
    changeinfo = models.TextField(db_column='CHANGEINFO', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    changenotes = models.TextField(db_column='CHANGENOTES', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_ENTPARCHANGELOGS'


class PvdmSysEntparents(models.Model):
    entparentid = models.AutoField(db_column='ENTPARENTID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    parentsettings = models.IntegerField(db_column='PARENTSETTINGS')  # Field name made lowercase.
    parentattrs = models.TextField(db_column='PARENTATTRS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    startdate = models.DateTimeField(db_column='STARTDATE')  # Field name made lowercase.
    optout = models.BooleanField(db_column='OPTOUT', blank=True, null=True)  # Field name made lowercase.
    commemail = models.BooleanField(db_column='COMMEMAIL', blank=True, null=True)  # Field name made lowercase.
    commemailcallback = models.BooleanField(db_column='COMMEMAILCALLBACK', blank=True, null=True)  # Field name made lowercase.
    commphone = models.BooleanField(db_column='COMMPHONE', blank=True, null=True)  # Field name made lowercase.
    commphonecallback = models.BooleanField(db_column='COMMPHONECALLBACK', blank=True, null=True)  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LASTUPDATED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_ENTPARENTS'


class PvdmSysEntparsamemails(models.Model):
    samemailid = models.AutoField(db_column='SAMEMAILID', primary_key=True)  # Field name made lowercase.
    samid = models.IntegerField(db_column='SAMID')  # Field name made lowercase.
    entparentid = models.IntegerField(db_column='ENTPARENTID')  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_ENTPARSAMEMAILS'


class PvdmSysEntparsamphones(models.Model):
    samphoneid = models.AutoField(db_column='SAMPHONEID', primary_key=True)  # Field name made lowercase.
    samid = models.IntegerField(db_column='SAMID')  # Field name made lowercase.
    entparentid = models.IntegerField(db_column='ENTPARENTID')  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_ENTPARSAMPHONES'


class PvdmSysEntparsamusers(models.Model):
    samid = models.AutoField(db_column='SAMID', primary_key=True)  # Field name made lowercase.
    entparentid = models.IntegerField(db_column='ENTPARENTID')  # Field name made lowercase.
    samname = models.CharField(db_column='SAMNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=4096, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    specifyphone = models.BooleanField(db_column='SPECIFYPHONE')  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LASTUPDATED')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_ENTPARSAMUSERS'


class PvdmSysEntsamemails(models.Model):
    samemailid = models.AutoField(db_column='SAMEMAILID', primary_key=True)  # Field name made lowercase.
    samid = models.IntegerField(db_column='SAMID')  # Field name made lowercase.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_ENTSAMEMAILS'


class PvdmSysEntsamphones(models.Model):
    samphoneid = models.AutoField(db_column='SAMPHONEID', primary_key=True)  # Field name made lowercase.
    samid = models.IntegerField(db_column='SAMID')  # Field name made lowercase.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_ENTSAMPHONES'


class PvdmSysEntsamusers(models.Model):
    samid = models.AutoField(db_column='SAMID', primary_key=True)  # Field name made lowercase.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    samname = models.CharField(db_column='SAMNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=4000, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    specifyphone = models.BooleanField(db_column='SPECIFYPHONE')  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LASTUPDATED')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_ENTSAMUSERS'


class PvdmSysEntsettings(models.Model):
    settingid = models.AutoField(db_column='SETTINGID', primary_key=True)  # Field name made lowercase.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    secure = models.SmallIntegerField(db_column='SECURE')  # Field name made lowercase.
    value = models.TextField(db_column='VALUE', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_ENTSETTINGS'


class PvdmSysErmprocerrors(models.Model):
    logid = models.AutoField(db_column='LOGID', primary_key=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='WORKSTATION', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    sourcefile = models.TextField(db_column='SOURCEFILE', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    ermjobid = models.IntegerField(db_column='ERMJOBID')  # Field name made lowercase.
    ermjobname = models.CharField(db_column='ERMJOBNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    errortime = models.DateTimeField(db_column='ERRORTIME')  # Field name made lowercase.
    message = models.TextField(db_column='MESSAGE', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_ERMPROCERRORS'


class PvdmSysFeaturesets(models.Model):
    fsid = models.AutoField(db_column='FSID', primary_key=True)  # Field name made lowercase.
    fsname = models.CharField(db_column='FSNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    exclusions = models.TextField(db_column='EXCLUSIONS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_FEATURESETS'


class PvdmSysFtqueue(models.Model):
    tableident = models.BigAutoField(db_column='TABLEIDENT', primary_key=True)  # Field name made lowercase.
    queuedatetime = models.DateTimeField(db_column='QUEUEDATETIME')  # Field name made lowercase.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.
    dupeid = models.IntegerField(db_column='DUPEID')  # Field name made lowercase.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    filesetid = models.IntegerField(db_column='FILESETID')  # Field name made lowercase.
    proctype = models.IntegerField(db_column='PROCTYPE')  # Field name made lowercase.
    procinfo = models.TextField(db_column='PROCINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    isdone = models.IntegerField(db_column='ISDONE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_FTQUEUE'


class PvdmSysFulltextqueue(models.Model):
    queueid = models.AutoField(db_column='QUEUEID', primary_key=True)  # Field name made lowercase.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    queuedatetime = models.DateTimeField(db_column='QUEUEDATETIME')  # Field name made lowercase.
    operation = models.IntegerField(db_column='OPERATION')  # Field name made lowercase.
    docid = models.CharField(db_column='DOCID', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    datatype = models.CharField(db_column='DATATYPE', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    datainfo = models.TextField(db_column='DATAINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_FULLTEXTQUEUE'


class PvdmSysGlobaladmins(models.Model):
    adminid = models.AutoField(db_column='ADMINID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    fullname = models.CharField(db_column='FULLNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='ISDELETED')  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    usersettings = models.TextField(db_column='USERSETTINGS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    notifications = models.IntegerField(db_column='NOTIFICATIONS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_GLOBALADMINS'


class PvdmSysHostingconfigs(models.Model):
    configid = models.AutoField(db_column='CONFIGID', primary_key=True)  # Field name made lowercase.
    configtype = models.SmallIntegerField(db_column='CONFIGTYPE')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    value = models.TextField(db_column='VALUE', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_HOSTINGCONFIGS'


class PvdmSysImportmaps(models.Model):
    imid = models.AutoField(db_column='IMID', primary_key=True)  # Field name made lowercase.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    fromdgcustid = models.CharField(db_column='FROMDGCUSTID', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    fromdgcustname = models.CharField(db_column='FROMDGCUSTNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_IMPORTMAPS'


class PvdmSysImportqueue(models.Model):
    queueid = models.AutoField(db_column='QUEUEID', primary_key=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='WORKSTATION', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    queuetime = models.DateTimeField(db_column='QUEUETIME')  # Field name made lowercase.
    path = models.TextField(db_column='PATH', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    queueinfo = models.TextField(db_column='QUEUEINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    disabled = models.BooleanField(db_column='DISABLED', blank=True, null=True)  # Field name made lowercase.
    lasterror = models.TextField(db_column='LASTERROR', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_IMPORTQUEUE'


class PvdmSysLic(models.Model):
    licid = models.AutoField(db_column='LICID', primary_key=True)  # Field name made lowercase.
    prodid = models.SmallIntegerField(db_column='PRODID')  # Field name made lowercase.
    prodver = models.SmallIntegerField(db_column='PRODVER')  # Field name made lowercase.
    qty = models.SmallIntegerField(db_column='QTY')  # Field name made lowercase.
    serialnum = models.CharField(db_column='SERIALNUM', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    liccheck = models.CharField(db_column='LICCHECK', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    licdate = models.DateTimeField(db_column='LICDATE')  # Field name made lowercase.
    licdatecheck = models.CharField(db_column='LICDATECHECK', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    namedusage = models.CharField(db_column='NAMEDUSAGE', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    identcode = models.CharField(db_column='IDENTCODE', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    authcode = models.CharField(db_column='AUTHCODE', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_LIC'


class PvdmSysListdocs(models.Model):
    listid = models.CharField(db_column='LISTID', primary_key=True, max_length=36)  # Field name made lowercase. The composite primary key (LISTID, ENTID, PROJID, DOCID) found, that is not supported. The first column is selected.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_LISTDOCS'
        unique_together = (('listid', 'entid', 'projid', 'docid'),)


class PvdmSysLists(models.Model):
    tableident = models.BigAutoField(db_column='TABLEIDENT', primary_key=True)  # Field name made lowercase.
    listid = models.CharField(db_column='LISTID', max_length=36)  # Field name made lowercase.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    listname = models.CharField(db_column='LISTNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    listtype = models.IntegerField(db_column='LISTTYPE')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='STARTDATE')  # Field name made lowercase.
    listownerid = models.IntegerField(db_column='LISTOWNERID')  # Field name made lowercase.
    listinfo = models.TextField(db_column='LISTINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    locked = models.BooleanField(db_column='LOCKED')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_LISTS'


class PvdmSysMailqueue(models.Model):
    queueid = models.CharField(db_column='QUEUEID', primary_key=True, max_length=36)  # Field name made lowercase.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    queuedatetime = models.DateTimeField(db_column='QUEUEDATETIME')  # Field name made lowercase.
    dispsender = models.CharField(db_column='DISPSENDER', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    disprecipient = models.CharField(db_column='DISPRECIPIENT', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    dispsubject = models.CharField(db_column='DISPSUBJECT', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    msginfo = models.TextField(db_column='MSGINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_MAILQUEUE'


class PvdmSysMaintlogs(models.Model):
    logid = models.AutoField(db_column='LOGID', primary_key=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='WORKSTATION', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    maintname = models.CharField(db_column='MAINTNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    maintinfo = models.TextField(db_column='MAINTINFO', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    starttime = models.DateTimeField(db_column='STARTTIME')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='ENDTIME')  # Field name made lowercase.
    finishstatus = models.SmallIntegerField(db_column='FINISHSTATUS')  # Field name made lowercase.
    message = models.TextField(db_column='MESSAGE', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_MAINTLOGS'


class PvdmSysMaintqueue(models.Model):
    queueid = models.AutoField(db_column='QUEUEID', primary_key=True)  # Field name made lowercase.
    queuetime = models.DateTimeField(db_column='QUEUETIME')  # Field name made lowercase.
    maintname = models.CharField(db_column='MAINTNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    mainthash = models.CharField(db_column='MAINTHASH', unique=True, max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    maintinfo = models.TextField(db_column='MAINTINFO', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_MAINTQUEUE'


class PvdmSysMigdgs(models.Model):
    migid = models.CharField(db_column='MIGID', primary_key=True, max_length=36)  # Field name made lowercase. The composite primary key (MIGID, ENTID, DGID) found, that is not supported. The first column is selected.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_MIGDGS'
        unique_together = (('migid', 'entid', 'dgid'),)


class PvdmSysMiglists(models.Model):
    migid = models.CharField(db_column='MIGID', primary_key=True, max_length=36)  # Field name made lowercase. The composite primary key (MIGID, ENTID, LISTID) found, that is not supported. The first column is selected.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    listid = models.CharField(db_column='LISTID', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_MIGLISTS'
        unique_together = (('migid', 'entid', 'listid'),)


class PvdmSysMigprojs(models.Model):
    migid = models.CharField(db_column='MIGID', primary_key=True, max_length=36)  # Field name made lowercase. The composite primary key (MIGID, ENTID, PROJID) found, that is not supported. The first column is selected.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    startobjid = models.IntegerField(db_column='STARTOBJID')  # Field name made lowercase.
    startdocid = models.IntegerField(db_column='STARTDOCID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_MIGPROJS'
        unique_together = (('migid', 'entid', 'projid'),)


class PvdmSysMigs(models.Model):
    tableident = models.BigAutoField(db_column='TABLEIDENT', primary_key=True)  # Field name made lowercase.
    migid = models.CharField(db_column='MIGID', max_length=36)  # Field name made lowercase.
    migname = models.CharField(db_column='MIGNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    entname = models.CharField(db_column='ENTNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    submitdate = models.DateTimeField(db_column='SUBMITDATE')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='STARTDATE', blank=True, null=True)  # Field name made lowercase.
    finishdate = models.DateTimeField(db_column='FINISHDATE', blank=True, null=True)  # Field name made lowercase.
    holddate = models.DateTimeField(db_column='HOLDDATE')  # Field name made lowercase.
    submituserid = models.IntegerField(db_column='SUBMITUSERID')  # Field name made lowercase.
    submitusername = models.CharField(db_column='SUBMITUSERNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    submitinfo = models.TextField(db_column='SUBMITINFO', db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    run_docs = models.IntegerField(db_column='RUN_DOCS', blank=True, null=True)  # Field name made lowercase.
    run_bytes = models.FloatField(db_column='RUN_BYTES', blank=True, null=True)  # Field name made lowercase.
    run_seconds = models.IntegerField(db_column='RUN_SECONDS', blank=True, null=True)  # Field name made lowercase.
    run_info = models.TextField(db_column='RUN_INFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    run_status = models.SmallIntegerField(db_column='RUN_STATUS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_MIGS'


class PvdmSysProcesslocks(models.Model):
    processid = models.CharField(db_column='PROCESSID', primary_key=True, max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    workstation = models.CharField(db_column='WORKSTATION', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    locktime = models.DateTimeField(db_column='LOCKTIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_PROCESSLOCKS'


class PvdmSysProcqueue(models.Model):
    entryid = models.CharField(db_column='ENTRYID', primary_key=True, max_length=36)  # Field name made lowercase.
    entrytime = models.DateTimeField(db_column='ENTRYTIME')  # Field name made lowercase.
    entityid = models.IntegerField(db_column='ENTITYID')  # Field name made lowercase.
    entrytype = models.IntegerField(db_column='ENTRYTYPE')  # Field name made lowercase.
    entryname = models.CharField(db_column='ENTRYNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    entryhash = models.CharField(db_column='ENTRYHASH', unique=True, max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    entryinfo = models.TextField(db_column='ENTRYINFO', db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    skipentry = models.BooleanField(db_column='SKIPENTRY')  # Field name made lowercase.
    errorinfo = models.TextField(db_column='ERRORINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_PROCQUEUE'


class PvdmSysStorageutil(models.Model):
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    runtime = models.DateTimeField(db_column='RUNTIME')  # Field name made lowercase.
    utilization = models.FloatField(db_column='UTILIZATION')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_STORAGEUTIL'


class PvdmSysSynctaskwaiting(models.Model):
    tableident = models.BigAutoField(db_column='TABLEIDENT', primary_key=True)  # Field name made lowercase.
    taskdatetime = models.DateTimeField(db_column='TASKDATETIME')  # Field name made lowercase.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.
    tasktype = models.SmallIntegerField(db_column='TASKTYPE')  # Field name made lowercase.
    taskid = models.CharField(db_column='TASKID', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    taskinfo = models.TextField(db_column='TASKINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_SYNCTASKWAITING'


class PvdmSysSystem(models.Model):
    varname = models.CharField(db_column='VARNAME', primary_key=True, max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    varvalue = models.TextField(db_column='VARVALUE', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_SYSTEM'


class PvdmSysTaskprojqueue(models.Model):
    tableident = models.BigAutoField(db_column='TABLEIDENT', primary_key=True)  # Field name made lowercase.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    tasktype = models.SmallIntegerField(db_column='TASKTYPE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_TASKPROJQUEUE'


class PvdmSysTemplates(models.Model):
    templateid = models.AutoField(db_column='TEMPLATEID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='TYPE')  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    templatepwd = models.TextField(db_column='TEMPLATEPWD', db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    path = models.TextField(db_column='PATH', db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    ispublish = models.BooleanField(db_column='ISPUBLISH')  # Field name made lowercase.
    createdatetime = models.DateTimeField(db_column='CREATEDATETIME')  # Field name made lowercase.
    createdby = models.CharField(db_column='CREATEDBY', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    components = models.TextField(db_column='COMPONENTS', db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_TEMPLATES'


class PvdmSysUrlmaps(models.Model):
    url = models.CharField(db_column='URL', primary_key=True, max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    mapinfo = models.TextField(db_column='MAPINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_SYS_URLMAPS'


class PvdmUsagecount1(models.Model):
    username = models.CharField(db_column='USERNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    optype = models.SmallIntegerField(db_column='OPTYPE')  # Field name made lowercase.
    opnumber = models.IntegerField(db_column='OPNUMBER')  # Field name made lowercase.
    optime = models.DateTimeField(db_column='OPTIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_USAGECOUNT_1'


class PvdmUserfeatures1(models.Model):
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    featureid = models.IntegerField(db_column='FEATUREID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_USERFEATURES_1'


class PvdmUserpermission1(models.Model):
    userid = models.IntegerField(db_column='USERID', primary_key=True)  # Field name made lowercase. The composite primary key (USERID, APPOBJECTID) found, that is not supported. The first column is selected.
    appobjectid = models.CharField(db_column='APPOBJECTID', max_length=36)  # Field name made lowercase.
    permissionlevel = models.IntegerField(db_column='PERMISSIONLEVEL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_USERPERMISSION_1'
        unique_together = (('userid', 'appobjectid'),)


class PvdmUsersettings1(models.Model):
    settingid = models.AutoField(db_column='SETTINGID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    value = models.TextField(db_column='VALUE', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_USERSETTINGS_1'



class PvdmUsertokens1(models.Model):
    tokenid = models.CharField(db_column='TOKENID', max_length=36)  # Field name made lowercase.
    tokencode = models.CharField(db_column='TOKENCODE', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID')  # Field name made lowercase.
    appident = models.CharField(db_column='APPIDENT', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CREATETIME')  # Field name made lowercase.
    accesstime = models.DateTimeField(db_column='ACCESSTIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_USERTOKENS_1'


class PvdmWfprecondDef1(models.Model):
    wfpreconddefid = models.AutoField(db_column='WFPRECONDDEFID', primary_key=True)  # Field name made lowercase.
    wfdefid = models.IntegerField(db_column='WFDEFID')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    queryval = models.TextField(db_column='QUERYVAL', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    lastquerydocid = models.IntegerField(db_column='LASTQUERYDOCID')  # Field name made lowercase.
    docselection = models.SmallIntegerField(db_column='DOCSELECTION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_WFPRECOND_DEF_1'


class PvdmWfDef1(models.Model):
    wfdefid = models.AutoField(db_column='WFDEFID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    projid = models.IntegerField(db_column='PROJID')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='ISACTIVE')  # Field name made lowercase.
    layoutxml = models.TextField(db_column='LAYOUTXML', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_WF_DEF_1'


class PvdmWfHistory1(models.Model):
    wfinstid = models.IntegerField(db_column='WFINSTID')  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    entrytime = models.DateTimeField(db_column='ENTRYTIME')  # Field name made lowercase.
    history = models.TextField(db_column='HISTORY', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_WF_HISTORY_1'


class PvdmWfInst1(models.Model):
    wfinstid = models.AutoField(db_column='WFINSTID', primary_key=True)  # Field name made lowercase.
    wfdefid = models.IntegerField(db_column='WFDEFID')  # Field name made lowercase.
    docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='STARTTIME')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='ENDTIME', blank=True, null=True)  # Field name made lowercase.
    history = models.TextField(db_column='HISTORY', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_WF_INST_1'


class PvdmWspostcondDef1(models.Model):
    wspostconddefid = models.AutoField(db_column='WSPOSTCONDDEFID', primary_key=True)  # Field name made lowercase.
    wsdefid = models.IntegerField(db_column='WSDEFID')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    queryval = models.TextField(db_column='QUERYVAL', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    transwsdefid = models.IntegerField(db_column='TRANSWSDEFID')  # Field name made lowercase.
    sequencenum = models.IntegerField(db_column='SEQUENCENUM')  # Field name made lowercase.
    pcxml = models.TextField(db_column='PCXML', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_WSPOSTCOND_DEF_1'


class PvdmWstaskDef1(models.Model):
    wstaskdefid = models.AutoField(db_column='WSTASKDEFID', primary_key=True)  # Field name made lowercase.
    wsdefid = models.IntegerField(db_column='WSDEFID')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sequencenum = models.IntegerField(db_column='SEQUENCENUM')  # Field name made lowercase.
    groupnum = models.IntegerField(db_column='GROUPNUM')  # Field name made lowercase.
    tasktype = models.IntegerField(db_column='TASKTYPE')  # Field name made lowercase.
    tasktypeinfo = models.TextField(db_column='TASKTYPEINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_WSTASK_DEF_1'


class PvdmWsDef1(models.Model):
    wsdefid = models.AutoField(db_column='WSDEFID', primary_key=True)  # Field name made lowercase.
    wfdefid = models.IntegerField(db_column='WFDEFID')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    wspartid = models.IntegerField(db_column='WSPARTID')  # Field name made lowercase.
    graphic = models.CharField(db_column='GRAPHIC', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    initialws = models.BooleanField(db_column='INITIALWS')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='ISDELETED')  # Field name made lowercase.
    maxqueuetranstime = models.IntegerField(db_column='MAXQUEUETRANSTIME')  # Field name made lowercase.
    maxqueuetranswsid = models.IntegerField(db_column='MAXQUEUETRANSWSID')  # Field name made lowercase.
    maxqueuenotifytime = models.IntegerField(db_column='MAXQUEUENOTIFYTIME')  # Field name made lowercase.
    maxqueuenotifyinfo = models.TextField(db_column='MAXQUEUENOTIFYINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    maxowntranstime = models.IntegerField(db_column='MAXOWNTRANSTIME')  # Field name made lowercase.
    maxowntranswsid = models.IntegerField(db_column='MAXOWNTRANSWSID')  # Field name made lowercase.
    maxownnotifytime = models.IntegerField(db_column='MAXOWNNOTIFYTIME')  # Field name made lowercase.
    maxownnotifyinfo = models.TextField(db_column='MAXOWNNOTIFYINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PVDM_WS_DEF_1'


class PvdmWsInst1(models.Model):
    wsinstid = models.AutoField(db_column='WSINSTID', primary_key=True)  # Field name made lowercase.
    wfinstid = models.IntegerField(db_column='WFINSTID')  # Field name made lowercase.
    wsdefid = models.IntegerField(db_column='WSDEFID')  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='STARTTIME')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='ENDTIME', blank=True, null=True)  # Field name made lowercase.
    ownername = models.CharField(db_column='OWNERNAME', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OWNERID', blank=True, null=True)  # Field name made lowercase.
    info = models.TextField(db_column='INFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ownnotify = models.BooleanField(db_column='OWNNOTIFY', blank=True, null=True)  # Field name made lowercase.
    queuenotify = models.BooleanField(db_column='QUEUENOTIFY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_WS_INST_1'


class PvExport(models.Model):
    casenumber = models.CharField(db_column='CASENUMBER', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    label = models.CharField(db_column='LABEL', max_length=25, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    docid = models.IntegerField(db_column='DOCID', blank=True, null=True)  # Field name made lowercase.
    dgname = models.CharField(db_column='DGNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    filename = models.CharField(db_column='FILENAME', max_length=900, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='ORDERDATE', blank=True, null=True)  # Field name made lowercase.
    judgename = models.CharField(db_column='JUDGENAME', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sealed = models.CharField(db_column='SEALED', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    defendantcompany = models.CharField(db_column='DEFENDANTCOMPANY', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    defendantlastname = models.CharField(db_column='DEFENDANTLASTNAME', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    defendantfirstname = models.CharField(db_column='DEFENDANTFIRSTNAME', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    defendantmiddle = models.CharField(db_column='DEFENDANTMIDDLE', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    defendantsuffix = models.CharField(db_column='DEFENDANTSUFFIX', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    plaintiffcompany = models.CharField(db_column='PLAINTIFFCOMPANY', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    plaintifflastname = models.CharField(db_column='PLAINTIFFLASTNAME', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    plaintifffirstname = models.CharField(db_column='PLAINTIFFFIRSTNAME', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    plaintiffmiddle = models.CharField(db_column='PLAINTIFFMIDDLE', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    plaintiffsuffix = models.CharField(db_column='PLAINTIFFSUFFIX', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    subjectcompany = models.CharField(db_column='SUBJECTCOMPANY', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    subjectlastname = models.CharField(db_column='SUBJECTLASTNAME', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    subjectfirstname = models.CharField(db_column='SUBJECTFIRSTNAME', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    subjectmiddle = models.CharField(db_column='SUBJECTMIDDLE', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    subjectsuffix = models.CharField(db_column='SUBJECTSUFFIX', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    roa_code = models.CharField(db_column='ROA_CODE', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    roa_date = models.DateTimeField(db_column='ROA_DATE', blank=True, null=True)  # Field name made lowercase.
    doctitle = models.CharField(db_column='DOCTITLE', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    scandate = models.DateTimeField(db_column='SCANDATE', blank=True, null=True)  # Field name made lowercase.
    judgeinitials = models.CharField(db_column='JUDGEINITIALS', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PV_EXPORT'


class PvSysAutoschedule(models.Model):
    scheduleid = models.AutoField(db_column='SCHEDULEID', primary_key=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='WORKSTATION', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    operation = models.CharField(db_column='OPERATION', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    repeattype = models.CharField(db_column='REPEATTYPE', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    repeatcount = models.IntegerField(db_column='REPEATCOUNT')  # Field name made lowercase.
    repeattypedetail = models.CharField(db_column='REPEATTYPEDETAIL', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    procorder = models.IntegerField(db_column='PROCORDER')  # Field name made lowercase.
    nextrundatetime = models.DateTimeField(db_column='NEXTRUNDATETIME')  # Field name made lowercase.
    lastrundatetime = models.DateTimeField(db_column='LASTRUNDATETIME')  # Field name made lowercase.
    laststatus = models.TextField(db_column='LASTSTATUS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PV_SYS_AUTOSCHEDULE'


class PvSysMailqueue(models.Model):
    queueid = models.CharField(db_column='QUEUEID', primary_key=True, max_length=36)  # Field name made lowercase.
    entid = models.IntegerField(db_column='ENTID')  # Field name made lowercase.
    queuedatetime = models.DateTimeField(db_column='QUEUEDATETIME')  # Field name made lowercase.
    dispsender = models.CharField(db_column='DISPSENDER', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    disprecipient = models.CharField(db_column='DISPRECIPIENT', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    dispsubject = models.CharField(db_column='DISPSUBJECT', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    msginfo = models.TextField(db_column='MSGINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PV_SYS_MAILQUEUE'


class PvSysMaintlogs(models.Model):
    logid = models.AutoField(db_column='LOGID', primary_key=True)  # Field name made lowercase.
    workstation = models.CharField(db_column='WORKSTATION', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    maintname = models.CharField(db_column='MAINTNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    maintinfo = models.TextField(db_column='MAINTINFO', db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='STARTTIME')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='ENDTIME')  # Field name made lowercase.
    finishstatus = models.SmallIntegerField(db_column='FINISHSTATUS')  # Field name made lowercase.
    message = models.TextField(db_column='MESSAGE', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PV_SYS_MAINTLOGS'


class PvSysMaintqueue(models.Model):
    queueid = models.AutoField(db_column='QUEUEID', primary_key=True)  # Field name made lowercase.
    queuetime = models.DateTimeField(db_column='QUEUETIME')  # Field name made lowercase.
    maintname = models.CharField(db_column='MAINTNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    mainthash = models.CharField(db_column='MAINTHASH', unique=True, max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    maintinfo = models.TextField(db_column='MAINTINFO', db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PV_SYS_MAINTQUEUE'


class PvUserPreferences1(models.Model):
    userid = models.IntegerField(db_column='USERID', primary_key=True)  # Field name made lowercase. The composite primary key (USERID, PRODUCTID) found, that is not supported. The first column is selected.
    preferences = models.TextField(db_column='PREFERENCES', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    productid = models.SmallIntegerField(db_column='PRODUCTID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PV_USER_PREFERENCES_1'
        unique_together = (('userid', 'productid'),)


class Migrationhistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', primary_key=True, max_length=150, db_collation='Latin1_General_CI_AS')  # Field name made lowercase. The composite primary key (MigrationId, ContextKey) found, that is not supported. The first column is selected.
    contextkey = models.CharField(db_column='ContextKey', max_length=300, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    model = models.BinaryField(db_column='Model')  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=32, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '__MigrationHistory'
        unique_together = (('migrationid', 'contextkey'),)








# class PvcapBatch1(models.Model):
#     batchid = models.BigAutoField(db_column='BATCHID', primary_key=True)  # Field name made lowercase.
#     internalname = models.CharField(db_column='INTERNALNAME', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     name = models.CharField(db_column='NAME', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='DESCRIPTION', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     userdate = models.DateTimeField(db_column='USERDATE', blank=True, null=True)  # Field name made lowercase.
#     path = models.TextField(db_column='PATH', db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
#     isdeleted = models.BooleanField(db_column='ISDELETED')  # Field name made lowercase.
#     isnew = models.BooleanField(db_column='ISNEW')  # Field name made lowercase.
#     retainstats = models.BooleanField(db_column='RETAINSTATS')  # Field name made lowercase.
#     adminpriority = models.BigIntegerField(db_column='ADMINPRIORITY')  # Field name made lowercase.
#     status = models.SmallIntegerField(db_column='STATUS')  # Field name made lowercase.
#     jobid = models.BigIntegerField(db_column='JOBID')  # Field name made lowercase.
#     jobstart = models.DateTimeField(db_column='JOBSTART')  # Field name made lowercase.
#     stepid = models.IntegerField(db_column='STEPID')  # Field name made lowercase.
#     stepstart = models.DateTimeField(db_column='STEPSTART')  # Field name made lowercase.
#     checkedoutbydatetime = models.DateTimeField(db_column='CHECKEDOUTBYDATETIME', blank=True, null=True)  # Field name made lowercase.
#     checkedoutbyuserid = models.IntegerField(db_column='CHECKEDOUTBYUSERID', blank=True, null=True)  # Field name made lowercase.
#     checkedoutbyworkstation = models.CharField(db_column='CHECKEDOUTBYWORKSTATION', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     scheduleddestruction = models.DateTimeField(db_column='SCHEDULEDDESTRUCTION', blank=True, null=True)  # Field name made lowercase.
#     size = models.BigIntegerField(db_column='SIZE')  # Field name made lowercase.
#     lastupdate = models.DateTimeField(db_column='LASTUPDATE')  # Field name made lowercase.
#     documentcount = models.BigIntegerField(db_column='DOCUMENTCOUNT', blank=True, null=True)  # Field name made lowercase.
#     pagecount = models.BigIntegerField(db_column='PAGECOUNT', blank=True, null=True)  # Field name made lowercase.
#     imagecount = models.BigIntegerField(db_column='IMAGECOUNT', blank=True, null=True)  # Field name made lowercase.
#     delayprocessing = models.DateTimeField(db_column='DELAYPROCESSING', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'PVCAP_BATCH_1'


# class PvcapIndexvalue1(models.Model):
#     jobid = models.BigIntegerField(db_column='JOBID')  # Field name made lowercase.
#     indexid = models.BigIntegerField(db_column='INDEXID')  # Field name made lowercase.
#     value = models.CharField(db_column='VALUE', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     batchid = models.BigIntegerField(db_column='BATCHID')  # Field name made lowercase.
#     documentid = models.BigIntegerField(db_column='DOCUMENTID')  # Field name made lowercase.
#     detailsetid = models.CharField(db_column='DETAILSETID', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     confidence = models.FloatField(db_column='CONFIDENCE', blank=True, null=True)  # Field name made lowercase.
#     rowindex = models.IntegerField(db_column='ROWINDEX', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'PVCAP_INDEXVALUE_1'


# class PvcapIndex1(models.Model):
#     indexid = models.BigIntegerField(db_column='INDEXID', primary_key=True)  # Field name made lowercase. The composite primary key (INDEXID, JOBID) found, that is not supported. The first column is selected.
#     jobid = models.BigIntegerField(db_column='JOBID')  # Field name made lowercase.
#     fieldname = models.CharField(db_column='FIELDNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
#     fieldtype = models.IntegerField(db_column='FIELDTYPE')  # Field name made lowercase.
#     indexproperties = models.TextField(db_column='INDEXPROPERTIES', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     isdeleted = models.BooleanField(db_column='ISDELETED')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'PVCAP_INDEX_1'
#         unique_together = (('indexid', 'jobid'),)




# class PvcapJob1(models.Model):
#     jobid = models.BigAutoField(db_column='JOBID', primary_key=True)  # Field name made lowercase.
#     name = models.CharField(db_column='NAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
#     description = models.CharField(db_column='DESCRIPTION', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     comment = models.TextField(db_column='COMMENT', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     modifieddatetime = models.DateTimeField(db_column='MODIFIEDDATETIME', blank=True, null=True)  # Field name made lowercase.
#     modifiedbyname = models.IntegerField(db_column='MODIFIEDBYNAME', blank=True, null=True)  # Field name made lowercase.
#     modifiedbyglobaladmin = models.BooleanField(db_column='MODIFIEDBYGLOBALADMIN', blank=True, null=True)  # Field name made lowercase.
#     createdbydatetime = models.DateTimeField(db_column='CREATEDBYDATETIME')  # Field name made lowercase.
#     createdbyname = models.IntegerField(db_column='CREATEDBYNAME')  # Field name made lowercase.
#     createdbyglobaladmin = models.BooleanField(db_column='CREATEDBYGLOBALADMIN')  # Field name made lowercase.
#     checkedoutbydatetime = models.DateTimeField(db_column='CHECKEDOUTBYDATETIME', blank=True, null=True)  # Field name made lowercase.
#     checkedoutbyname = models.IntegerField(db_column='CHECKEDOUTBYNAME', blank=True, null=True)  # Field name made lowercase.
#     checkedoutbyglobaladmin = models.BooleanField(db_column='CHECKEDOUTBYGLOBALADMIN', blank=True, null=True)  # Field name made lowercase.
#     isactive = models.BooleanField(db_column='ISACTIVE')  # Field name made lowercase.
#     isdeleted = models.BooleanField(db_column='ISDELETED')  # Field name made lowercase.
#     properties = models.TextField(db_column='PROPERTIES', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     agepriority = models.BigIntegerField(db_column='AGEPRIORITY')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'PVCAP_JOB_1'
