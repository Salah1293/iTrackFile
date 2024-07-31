from django.db import models
# from django.contrib.auth.models import User



class PvdmDocs11(models.Model):
    docid = models.AutoField(db_column='DOCID', primary_key=True)  # Field name made lowercase.
    docindex1 = models.CharField(db_column='DOCINDEX1', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex2 = models.DateTimeField(db_column='DOCINDEX2', blank=True, null=True)  # Field name made lowercase.
    docindex3 = models.CharField(db_column='DOCINDEX3', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex4 = models.CharField(db_column='DOCINDEX4', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex5 = models.CharField(db_column='DOCINDEX5', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex6 = models.CharField(db_column='DOCINDEX6', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex7 = models.CharField(db_column='DOCINDEX7', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex8 = models.CharField(db_column='DOCINDEX8', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex9 = models.CharField(db_column='DOCINDEX9', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex10 = models.CharField(db_column='DOCINDEX10', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex11 = models.CharField(db_column='DOCINDEX11', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex12 = models.CharField(db_column='DOCINDEX12', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex13 = models.CharField(db_column='DOCINDEX13', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex14 = models.CharField(db_column='DOCINDEX14', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex15 = models.CharField(db_column='DOCINDEX15', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex16 = models.CharField(db_column='DOCINDEX16', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex17 = models.CharField(db_column='DOCINDEX17', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex18 = models.CharField(db_column='DOCINDEX18', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex19 = models.CharField(db_column='DOCINDEX19', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex20 = models.DateTimeField(db_column='DOCINDEX20', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CREATEDATE')  # Field name made lowercase.
    dupeid = models.IntegerField(db_column='DUPEID')  # Field name made lowercase.
    securelist = models.TextField(db_column='SECURELIST', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    checkouttime = models.DateTimeField(db_column='CHECKOUTTIME', blank=True, null=True)  # Field name made lowercase.
    checkoutuserid = models.IntegerField(db_column='CHECKOUTUSERID', blank=True, null=True)  # Field name made lowercase.
    sourcedocid = models.IntegerField(db_column='SOURCEDOCID')  # Field name made lowercase.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    ftindex = models.IntegerField(db_column='FTINDEX')  # Field name made lowercase.
    lockdate = models.DateTimeField(db_column='LOCKDATE', blank=True, null=True)  # Field name made lowercase.
    lockinfo = models.TextField(db_column='LOCKINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destdate = models.DateTimeField(db_column='DESTDATE', blank=True, null=True)  # Field name made lowercase.
    destinfo = models.TextField(db_column='DESTINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destlistid = models.IntegerField(db_column='DESTLISTID', blank=True, null=True)  # Field name made lowercase.
    docindex21 = models.CharField(db_column='DOCINDEX21', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex22 = models.CharField(db_column='DOCINDEX22', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    wftriggerdatetime = models.DateTimeField(db_column='WFTRIGGERDATETIME', blank=True, null=True)  # Field name made lowercase.
    ocrstatus = models.SmallIntegerField(db_column='OCRSTATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_DOCS_1_1'


class PvdmDocs110(models.Model):
    docid = models.AutoField(db_column='DOCID', primary_key=True)  # Field name made lowercase.
    docindex1 = models.CharField(db_column='DOCINDEX1', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CREATEDATE')  # Field name made lowercase.
    dupeid = models.IntegerField(db_column='DUPEID')  # Field name made lowercase.
    securelist = models.TextField(db_column='SECURELIST', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    checkouttime = models.DateTimeField(db_column='CHECKOUTTIME', blank=True, null=True)  # Field name made lowercase.
    checkoutuserid = models.IntegerField(db_column='CHECKOUTUSERID', blank=True, null=True)  # Field name made lowercase.
    sourcedocid = models.IntegerField(db_column='SOURCEDOCID')  # Field name made lowercase.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    ftindex = models.IntegerField(db_column='FTINDEX')  # Field name made lowercase.
    lockdate = models.DateTimeField(db_column='LOCKDATE', blank=True, null=True)  # Field name made lowercase.
    lockinfo = models.TextField(db_column='LOCKINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destdate = models.DateTimeField(db_column='DESTDATE', blank=True, null=True)  # Field name made lowercase.
    destinfo = models.TextField(db_column='DESTINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destlistid = models.IntegerField(db_column='DESTLISTID', blank=True, null=True)  # Field name made lowercase.
    wftriggerdatetime = models.DateTimeField(db_column='WFTRIGGERDATETIME', blank=True, null=True)  # Field name made lowercase.
    docindex2 = models.CharField(db_column='DOCINDEX2', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex3 = models.CharField(db_column='DOCINDEX3', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex4 = models.CharField(db_column='DOCINDEX4', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex5 = models.CharField(db_column='DOCINDEX5', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex6 = models.CharField(db_column='DOCINDEX6', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex7 = models.CharField(db_column='DOCINDEX7', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex8 = models.DateTimeField(db_column='DOCINDEX8', blank=True, null=True)  # Field name made lowercase.
    docindex9 = models.DateTimeField(db_column='DOCINDEX9', blank=True, null=True)  # Field name made lowercase.
    ocrstatus = models.SmallIntegerField(db_column='OCRSTATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_DOCS_1_10'


class PvdmDocs112(models.Model):
    docid = models.AutoField(db_column='DOCID', primary_key=True)  # Field name made lowercase.
    docindex1 = models.CharField(db_column='DOCINDEX1', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex2 = models.DateTimeField(db_column='DOCINDEX2', blank=True, null=True)  # Field name made lowercase.
    docindex3 = models.CharField(db_column='DOCINDEX3', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex4 = models.CharField(db_column='DOCINDEX4', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex5 = models.CharField(db_column='DOCINDEX5', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex6 = models.DateTimeField(db_column='DOCINDEX6', blank=True, null=True)  # Field name made lowercase.
    docindex7 = models.CharField(db_column='DOCINDEX7', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex8 = models.CharField(db_column='DOCINDEX8', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex9 = models.CharField(db_column='DOCINDEX9', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex10 = models.CharField(db_column='DOCINDEX10', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex11 = models.CharField(db_column='DOCINDEX11', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CREATEDATE')  # Field name made lowercase.
    dupeid = models.IntegerField(db_column='DUPEID')  # Field name made lowercase.
    securelist = models.TextField(db_column='SECURELIST', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    checkouttime = models.DateTimeField(db_column='CHECKOUTTIME', blank=True, null=True)  # Field name made lowercase.
    checkoutuserid = models.IntegerField(db_column='CHECKOUTUSERID', blank=True, null=True)  # Field name made lowercase.
    sourcedocid = models.IntegerField(db_column='SOURCEDOCID')  # Field name made lowercase.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    ftindex = models.IntegerField(db_column='FTINDEX')  # Field name made lowercase.
    lockdate = models.DateTimeField(db_column='LOCKDATE', blank=True, null=True)  # Field name made lowercase.
    lockinfo = models.TextField(db_column='LOCKINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destdate = models.DateTimeField(db_column='DESTDATE', blank=True, null=True)  # Field name made lowercase.
    destinfo = models.TextField(db_column='DESTINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destlistid = models.IntegerField(db_column='DESTLISTID', blank=True, null=True)  # Field name made lowercase.
    wftriggerdatetime = models.DateTimeField(db_column='WFTRIGGERDATETIME', blank=True, null=True)  # Field name made lowercase.
    ocrstatus = models.SmallIntegerField(db_column='OCRSTATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_DOCS_1_12'


class PvdmDocs113(models.Model):
    docid = models.AutoField(db_column='DOCID', primary_key=True)  # Field name made lowercase.
    docindex1 = models.CharField(db_column='DOCINDEX1', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex2 = models.CharField(db_column='DOCINDEX2', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex3 = models.CharField(db_column='DOCINDEX3', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex4 = models.CharField(db_column='DOCINDEX4', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CREATEDATE')  # Field name made lowercase.
    dupeid = models.IntegerField(db_column='DUPEID')  # Field name made lowercase.
    securelist = models.TextField(db_column='SECURELIST', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    checkouttime = models.DateTimeField(db_column='CHECKOUTTIME', blank=True, null=True)  # Field name made lowercase.
    checkoutuserid = models.IntegerField(db_column='CHECKOUTUSERID', blank=True, null=True)  # Field name made lowercase.
    sourcedocid = models.IntegerField(db_column='SOURCEDOCID')  # Field name made lowercase.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    ftindex = models.IntegerField(db_column='FTINDEX')  # Field name made lowercase.
    lockdate = models.DateTimeField(db_column='LOCKDATE', blank=True, null=True)  # Field name made lowercase.
    lockinfo = models.TextField(db_column='LOCKINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destdate = models.DateTimeField(db_column='DESTDATE', blank=True, null=True)  # Field name made lowercase.
    destinfo = models.TextField(db_column='DESTINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destlistid = models.IntegerField(db_column='DESTLISTID', blank=True, null=True)  # Field name made lowercase.
    wftriggerdatetime = models.DateTimeField(db_column='WFTRIGGERDATETIME', blank=True, null=True)  # Field name made lowercase.
    ocrstatus = models.SmallIntegerField(db_column='OCRSTATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_DOCS_1_13'


class PvdmDocs114(models.Model):
    docid = models.AutoField(db_column='DOCID', primary_key=True)  # Field name made lowercase.
    docindex1 = models.CharField(db_column='DOCINDEX1', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex2 = models.CharField(db_column='DOCINDEX2', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex3 = models.CharField(db_column='DOCINDEX3', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex4 = models.CharField(db_column='DOCINDEX4', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex5 = models.CharField(db_column='DOCINDEX5', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex6 = models.CharField(db_column='DOCINDEX6', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex7 = models.DateTimeField(db_column='DOCINDEX7', blank=True, null=True)  # Field name made lowercase.
    docindex8 = models.CharField(db_column='DOCINDEX8', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CREATEDATE')  # Field name made lowercase.
    dupeid = models.IntegerField(db_column='DUPEID')  # Field name made lowercase.
    securelist = models.TextField(db_column='SECURELIST', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    checkouttime = models.DateTimeField(db_column='CHECKOUTTIME', blank=True, null=True)  # Field name made lowercase.
    checkoutuserid = models.IntegerField(db_column='CHECKOUTUSERID', blank=True, null=True)  # Field name made lowercase.
    sourcedocid = models.IntegerField(db_column='SOURCEDOCID')  # Field name made lowercase.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    ftindex = models.IntegerField(db_column='FTINDEX')  # Field name made lowercase.
    lockdate = models.DateTimeField(db_column='LOCKDATE', blank=True, null=True)  # Field name made lowercase.
    lockinfo = models.TextField(db_column='LOCKINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destdate = models.DateTimeField(db_column='DESTDATE', blank=True, null=True)  # Field name made lowercase.
    destinfo = models.TextField(db_column='DESTINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destlistid = models.IntegerField(db_column='DESTLISTID', blank=True, null=True)  # Field name made lowercase.
    wftriggerdatetime = models.DateTimeField(db_column='WFTRIGGERDATETIME', blank=True, null=True)  # Field name made lowercase.
    docindex9 = models.CharField(db_column='DOCINDEX9', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex10 = models.CharField(db_column='DOCINDEX10', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex11 = models.CharField(db_column='DOCINDEX11', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex12 = models.CharField(db_column='DOCINDEX12', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ocrstatus = models.SmallIntegerField(db_column='OCRSTATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_DOCS_1_14'


class PvdmDocs115(models.Model):
    docid = models.AutoField(db_column='DOCID', primary_key=True)  # Field name made lowercase.
    docindex1 = models.CharField(db_column='DOCINDEX1', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex2 = models.DateTimeField(db_column='DOCINDEX2', blank=True, null=True)  # Field name made lowercase.
    docindex3 = models.DateTimeField(db_column='DOCINDEX3', blank=True, null=True)  # Field name made lowercase.
    docindex4 = models.DateTimeField(db_column='DOCINDEX4', blank=True, null=True)  # Field name made lowercase.
    docindex5 = models.DateTimeField(db_column='DOCINDEX5', blank=True, null=True)  # Field name made lowercase.
    docindex6 = models.CharField(db_column='DOCINDEX6', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex7 = models.CharField(db_column='DOCINDEX7', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CREATEDATE')  # Field name made lowercase.
    dupeid = models.IntegerField(db_column='DUPEID')  # Field name made lowercase.
    securelist = models.TextField(db_column='SECURELIST', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    checkouttime = models.DateTimeField(db_column='CHECKOUTTIME', blank=True, null=True)  # Field name made lowercase.
    checkoutuserid = models.IntegerField(db_column='CHECKOUTUSERID', blank=True, null=True)  # Field name made lowercase.
    sourcedocid = models.IntegerField(db_column='SOURCEDOCID')  # Field name made lowercase.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    ftindex = models.IntegerField(db_column='FTINDEX')  # Field name made lowercase.
    lockdate = models.DateTimeField(db_column='LOCKDATE', blank=True, null=True)  # Field name made lowercase.
    lockinfo = models.TextField(db_column='LOCKINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destdate = models.DateTimeField(db_column='DESTDATE', blank=True, null=True)  # Field name made lowercase.
    destinfo = models.TextField(db_column='DESTINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destlistid = models.IntegerField(db_column='DESTLISTID', blank=True, null=True)  # Field name made lowercase.
    wftriggerdatetime = models.DateTimeField(db_column='WFTRIGGERDATETIME', blank=True, null=True)  # Field name made lowercase.
    ocrstatus = models.SmallIntegerField(db_column='OCRSTATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_DOCS_1_15'


class PvdmDocs116(models.Model):
    docid = models.AutoField(db_column='DOCID', primary_key=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CREATEDATE')  # Field name made lowercase.
    dupeid = models.IntegerField(db_column='DUPEID')  # Field name made lowercase.
    securelist = models.TextField(db_column='SECURELIST', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    checkouttime = models.DateTimeField(db_column='CHECKOUTTIME', blank=True, null=True)  # Field name made lowercase.
    checkoutuserid = models.IntegerField(db_column='CHECKOUTUSERID', blank=True, null=True)  # Field name made lowercase.
    sourcedocid = models.IntegerField(db_column='SOURCEDOCID')  # Field name made lowercase.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    ftindex = models.IntegerField(db_column='FTINDEX')  # Field name made lowercase.
    lockdate = models.DateTimeField(db_column='LOCKDATE', blank=True, null=True)  # Field name made lowercase.
    lockinfo = models.TextField(db_column='LOCKINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destdate = models.DateTimeField(db_column='DESTDATE', blank=True, null=True)  # Field name made lowercase.
    destinfo = models.TextField(db_column='DESTINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destlistid = models.IntegerField(db_column='DESTLISTID', blank=True, null=True)  # Field name made lowercase.
    wftriggerdatetime = models.DateTimeField(db_column='WFTRIGGERDATETIME', blank=True, null=True)  # Field name made lowercase.
    docindex1 = models.CharField(db_column='DOCINDEX1', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex2 = models.CharField(db_column='DOCINDEX2', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ocrstatus = models.SmallIntegerField(db_column='OCRSTATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_DOCS_1_16'


class PvdmDocs12(models.Model):
    docid = models.AutoField(db_column='DOCID', primary_key=True)  # Field name made lowercase.
    docindex1 = models.CharField(db_column='DOCINDEX1', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex2 = models.DateTimeField(db_column='DOCINDEX2', blank=True, null=True)  # Field name made lowercase.
    docindex3 = models.CharField(db_column='DOCINDEX3', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex4 = models.CharField(db_column='DOCINDEX4', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex5 = models.CharField(db_column='DOCINDEX5', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex6 = models.CharField(db_column='DOCINDEX6', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex7 = models.CharField(db_column='DOCINDEX7', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex8 = models.CharField(db_column='DOCINDEX8', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex9 = models.CharField(db_column='DOCINDEX9', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex10 = models.CharField(db_column='DOCINDEX10', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex11 = models.CharField(db_column='DOCINDEX11', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex12 = models.CharField(db_column='DOCINDEX12', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex13 = models.CharField(db_column='DOCINDEX13', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex14 = models.CharField(db_column='DOCINDEX14', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex15 = models.CharField(db_column='DOCINDEX15', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex16 = models.CharField(db_column='DOCINDEX16', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex17 = models.CharField(db_column='DOCINDEX17', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex18 = models.CharField(db_column='DOCINDEX18', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex19 = models.CharField(db_column='DOCINDEX19', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex20 = models.DateTimeField(db_column='DOCINDEX20', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CREATEDATE')  # Field name made lowercase.
    dupeid = models.IntegerField(db_column='DUPEID')  # Field name made lowercase.
    securelist = models.TextField(db_column='SECURELIST', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    checkouttime = models.DateTimeField(db_column='CHECKOUTTIME', blank=True, null=True)  # Field name made lowercase.
    checkoutuserid = models.IntegerField(db_column='CHECKOUTUSERID', blank=True, null=True)  # Field name made lowercase.
    sourcedocid = models.IntegerField(db_column='SOURCEDOCID')  # Field name made lowercase.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    ftindex = models.IntegerField(db_column='FTINDEX')  # Field name made lowercase.
    lockdate = models.DateTimeField(db_column='LOCKDATE', blank=True, null=True)  # Field name made lowercase.
    lockinfo = models.TextField(db_column='LOCKINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destdate = models.DateTimeField(db_column='DESTDATE', blank=True, null=True)  # Field name made lowercase.
    destinfo = models.TextField(db_column='DESTINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destlistid = models.IntegerField(db_column='DESTLISTID', blank=True, null=True)  # Field name made lowercase.
    docindex21 = models.CharField(db_column='DOCINDEX21', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex22 = models.DateTimeField(db_column='DOCINDEX22', blank=True, null=True)  # Field name made lowercase.
    wftriggerdatetime = models.DateTimeField(db_column='WFTRIGGERDATETIME', blank=True, null=True)  # Field name made lowercase.
    ocrstatus = models.SmallIntegerField(db_column='OCRSTATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_DOCS_1_2'


class PvdmDocs13(models.Model):
    docid = models.AutoField(db_column='DOCID', primary_key=True)  # Field name made lowercase.
    docindex1 = models.CharField(db_column='DOCINDEX1', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex2 = models.DateTimeField(db_column='DOCINDEX2', blank=True, null=True)  # Field name made lowercase.
    docindex3 = models.CharField(db_column='DOCINDEX3', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex4 = models.CharField(db_column='DOCINDEX4', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex5 = models.CharField(db_column='DOCINDEX5', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex6 = models.CharField(db_column='DOCINDEX6', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex7 = models.CharField(db_column='DOCINDEX7', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex8 = models.CharField(db_column='DOCINDEX8', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex9 = models.CharField(db_column='DOCINDEX9', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex10 = models.CharField(db_column='DOCINDEX10', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex11 = models.CharField(db_column='DOCINDEX11', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex12 = models.CharField(db_column='DOCINDEX12', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex13 = models.CharField(db_column='DOCINDEX13', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex14 = models.CharField(db_column='DOCINDEX14', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex15 = models.CharField(db_column='DOCINDEX15', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex16 = models.CharField(db_column='DOCINDEX16', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex17 = models.CharField(db_column='DOCINDEX17', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex18 = models.CharField(db_column='DOCINDEX18', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex19 = models.CharField(db_column='DOCINDEX19', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex20 = models.DateTimeField(db_column='DOCINDEX20', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CREATEDATE')  # Field name made lowercase.
    dupeid = models.IntegerField(db_column='DUPEID')  # Field name made lowercase.
    securelist = models.TextField(db_column='SECURELIST', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    checkouttime = models.DateTimeField(db_column='CHECKOUTTIME', blank=True, null=True)  # Field name made lowercase.
    checkoutuserid = models.IntegerField(db_column='CHECKOUTUSERID', blank=True, null=True)  # Field name made lowercase.
    sourcedocid = models.IntegerField(db_column='SOURCEDOCID')  # Field name made lowercase.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    ftindex = models.IntegerField(db_column='FTINDEX')  # Field name made lowercase.
    lockdate = models.DateTimeField(db_column='LOCKDATE', blank=True, null=True)  # Field name made lowercase.
    lockinfo = models.TextField(db_column='LOCKINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destdate = models.DateTimeField(db_column='DESTDATE', blank=True, null=True)  # Field name made lowercase.
    destinfo = models.TextField(db_column='DESTINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destlistid = models.IntegerField(db_column='DESTLISTID', blank=True, null=True)  # Field name made lowercase.
    docindex21 = models.CharField(db_column='DOCINDEX21', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex22 = models.DateTimeField(db_column='DOCINDEX22', blank=True, null=True)  # Field name made lowercase.
    wftriggerdatetime = models.DateTimeField(db_column='WFTRIGGERDATETIME', blank=True, null=True)  # Field name made lowercase.
    ocrstatus = models.SmallIntegerField(db_column='OCRSTATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_DOCS_1_3'


class PvdmDocs14(models.Model):
    docid = models.AutoField(db_column='DOCID', primary_key=True)  # Field name made lowercase.
    docindex1 = models.CharField(db_column='DOCINDEX1', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex2 = models.DateTimeField(db_column='DOCINDEX2', blank=True, null=True)  # Field name made lowercase.
    docindex3 = models.CharField(db_column='DOCINDEX3', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex4 = models.CharField(db_column='DOCINDEX4', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex5 = models.CharField(db_column='DOCINDEX5', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex6 = models.CharField(db_column='DOCINDEX6', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex7 = models.CharField(db_column='DOCINDEX7', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex8 = models.CharField(db_column='DOCINDEX8', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex9 = models.CharField(db_column='DOCINDEX9', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex10 = models.CharField(db_column='DOCINDEX10', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex11 = models.CharField(db_column='DOCINDEX11', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex12 = models.CharField(db_column='DOCINDEX12', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex13 = models.CharField(db_column='DOCINDEX13', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex14 = models.CharField(db_column='DOCINDEX14', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex15 = models.CharField(db_column='DOCINDEX15', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex16 = models.CharField(db_column='DOCINDEX16', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex17 = models.CharField(db_column='DOCINDEX17', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex18 = models.CharField(db_column='DOCINDEX18', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex19 = models.CharField(db_column='DOCINDEX19', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex20 = models.DateTimeField(db_column='DOCINDEX20', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CREATEDATE')  # Field name made lowercase.
    dupeid = models.IntegerField(db_column='DUPEID')  # Field name made lowercase.
    securelist = models.TextField(db_column='SECURELIST', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    checkouttime = models.DateTimeField(db_column='CHECKOUTTIME', blank=True, null=True)  # Field name made lowercase.
    checkoutuserid = models.IntegerField(db_column='CHECKOUTUSERID', blank=True, null=True)  # Field name made lowercase.
    sourcedocid = models.IntegerField(db_column='SOURCEDOCID')  # Field name made lowercase.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    ftindex = models.IntegerField(db_column='FTINDEX')  # Field name made lowercase.
    lockdate = models.DateTimeField(db_column='LOCKDATE', blank=True, null=True)  # Field name made lowercase.
    lockinfo = models.TextField(db_column='LOCKINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destdate = models.DateTimeField(db_column='DESTDATE', blank=True, null=True)  # Field name made lowercase.
    destinfo = models.TextField(db_column='DESTINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destlistid = models.IntegerField(db_column='DESTLISTID', blank=True, null=True)  # Field name made lowercase.
    docindex21 = models.CharField(db_column='DOCINDEX21', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex22 = models.DateTimeField(db_column='DOCINDEX22', blank=True, null=True)  # Field name made lowercase.
    wftriggerdatetime = models.DateTimeField(db_column='WFTRIGGERDATETIME', blank=True, null=True)  # Field name made lowercase.
    ocrstatus = models.SmallIntegerField(db_column='OCRSTATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_DOCS_1_4'


class PvdmDocs15(models.Model):
    docid = models.AutoField(db_column='DOCID', primary_key=True)  # Field name made lowercase.
    docindex1 = models.CharField(db_column='DOCINDEX1', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex2 = models.CharField(db_column='DOCINDEX2', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex3 = models.CharField(db_column='DOCINDEX3', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex4 = models.CharField(db_column='DOCINDEX4', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CREATEDATE')  # Field name made lowercase.
    dupeid = models.IntegerField(db_column='DUPEID')  # Field name made lowercase.
    securelist = models.TextField(db_column='SECURELIST', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    checkouttime = models.DateTimeField(db_column='CHECKOUTTIME', blank=True, null=True)  # Field name made lowercase.
    checkoutuserid = models.IntegerField(db_column='CHECKOUTUSERID', blank=True, null=True)  # Field name made lowercase.
    sourcedocid = models.IntegerField(db_column='SOURCEDOCID')  # Field name made lowercase.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    ftindex = models.IntegerField(db_column='FTINDEX')  # Field name made lowercase.
    lockdate = models.DateTimeField(db_column='LOCKDATE', blank=True, null=True)  # Field name made lowercase.
    lockinfo = models.TextField(db_column='LOCKINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destdate = models.DateTimeField(db_column='DESTDATE', blank=True, null=True)  # Field name made lowercase.
    destinfo = models.TextField(db_column='DESTINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destlistid = models.IntegerField(db_column='DESTLISTID', blank=True, null=True)  # Field name made lowercase.
    docindex5 = models.DateTimeField(db_column='DOCINDEX5', blank=True, null=True)  # Field name made lowercase.
    docindex6 = models.CharField(db_column='DOCINDEX6', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    wftriggerdatetime = models.DateTimeField(db_column='WFTRIGGERDATETIME', blank=True, null=True)  # Field name made lowercase.
    ocrstatus = models.SmallIntegerField(db_column='OCRSTATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_DOCS_1_5'


class PvdmDocs16(models.Model):
    docid = models.AutoField(db_column='DOCID', primary_key=True)  # Field name made lowercase.
    docindex1 = models.CharField(db_column='DOCINDEX1', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex2 = models.CharField(db_column='DOCINDEX2', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CREATEDATE')  # Field name made lowercase.
    dupeid = models.IntegerField(db_column='DUPEID')  # Field name made lowercase.
    securelist = models.TextField(db_column='SECURELIST', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    checkouttime = models.DateTimeField(db_column='CHECKOUTTIME', blank=True, null=True)  # Field name made lowercase.
    checkoutuserid = models.IntegerField(db_column='CHECKOUTUSERID', blank=True, null=True)  # Field name made lowercase.
    sourcedocid = models.IntegerField(db_column='SOURCEDOCID')  # Field name made lowercase.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    ftindex = models.IntegerField(db_column='FTINDEX')  # Field name made lowercase.
    lockdate = models.DateTimeField(db_column='LOCKDATE', blank=True, null=True)  # Field name made lowercase.
    lockinfo = models.TextField(db_column='LOCKINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destdate = models.DateTimeField(db_column='DESTDATE', blank=True, null=True)  # Field name made lowercase.
    destinfo = models.TextField(db_column='DESTINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destlistid = models.IntegerField(db_column='DESTLISTID', blank=True, null=True)  # Field name made lowercase.
    wftriggerdatetime = models.DateTimeField(db_column='WFTRIGGERDATETIME', blank=True, null=True)  # Field name made lowercase.
    ocrstatus = models.SmallIntegerField(db_column='OCRSTATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_DOCS_1_6'


class PvdmDocs17(models.Model):
    docid = models.AutoField(db_column='DOCID', primary_key=True)  # Field name made lowercase.
    docindex1 = models.CharField(db_column='DOCINDEX1', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex2 = models.CharField(db_column='DOCINDEX2', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex3 = models.CharField(db_column='DOCINDEX3', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex4 = models.CharField(db_column='DOCINDEX4', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex5 = models.CharField(db_column='DOCINDEX5', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CREATEDATE')  # Field name made lowercase.
    dupeid = models.IntegerField(db_column='DUPEID')  # Field name made lowercase.
    securelist = models.TextField(db_column='SECURELIST', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    checkouttime = models.DateTimeField(db_column='CHECKOUTTIME', blank=True, null=True)  # Field name made lowercase.
    checkoutuserid = models.IntegerField(db_column='CHECKOUTUSERID', blank=True, null=True)  # Field name made lowercase.
    sourcedocid = models.IntegerField(db_column='SOURCEDOCID')  # Field name made lowercase.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    ftindex = models.IntegerField(db_column='FTINDEX')  # Field name made lowercase.
    lockdate = models.DateTimeField(db_column='LOCKDATE', blank=True, null=True)  # Field name made lowercase.
    lockinfo = models.TextField(db_column='LOCKINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destdate = models.DateTimeField(db_column='DESTDATE', blank=True, null=True)  # Field name made lowercase.
    destinfo = models.TextField(db_column='DESTINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destlistid = models.IntegerField(db_column='DESTLISTID', blank=True, null=True)  # Field name made lowercase.
    wftriggerdatetime = models.DateTimeField(db_column='WFTRIGGERDATETIME', blank=True, null=True)  # Field name made lowercase.
    ocrstatus = models.SmallIntegerField(db_column='OCRSTATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_DOCS_1_7'


class PvdmDocs18(models.Model):
    docid = models.AutoField(db_column='DOCID', primary_key=True)  # Field name made lowercase.
    docindex1 = models.CharField(db_column='DOCINDEX1', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex2 = models.DateTimeField(db_column='DOCINDEX2', blank=True, null=True)  # Field name made lowercase.
    docindex3 = models.CharField(db_column='DOCINDEX3', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex4 = models.CharField(db_column='DOCINDEX4', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex5 = models.CharField(db_column='DOCINDEX5', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex6 = models.CharField(db_column='DOCINDEX6', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex7 = models.CharField(db_column='DOCINDEX7', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex8 = models.CharField(db_column='DOCINDEX8', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex9 = models.CharField(db_column='DOCINDEX9', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex10 = models.CharField(db_column='DOCINDEX10', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex11 = models.CharField(db_column='DOCINDEX11', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex12 = models.CharField(db_column='DOCINDEX12', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex13 = models.CharField(db_column='DOCINDEX13', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex14 = models.CharField(db_column='DOCINDEX14', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex15 = models.CharField(db_column='DOCINDEX15', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex16 = models.CharField(db_column='DOCINDEX16', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex17 = models.CharField(db_column='DOCINDEX17', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex18 = models.CharField(db_column='DOCINDEX18', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex19 = models.CharField(db_column='DOCINDEX19', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex20 = models.CharField(db_column='DOCINDEX20', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex21 = models.CharField(db_column='DOCINDEX21', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex22 = models.CharField(db_column='DOCINDEX22', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex23 = models.DateTimeField(db_column='DOCINDEX23', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CREATEDATE')  # Field name made lowercase.
    dupeid = models.IntegerField(db_column='DUPEID')  # Field name made lowercase.
    securelist = models.TextField(db_column='SECURELIST', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    checkouttime = models.DateTimeField(db_column='CHECKOUTTIME', blank=True, null=True)  # Field name made lowercase.
    checkoutuserid = models.IntegerField(db_column='CHECKOUTUSERID', blank=True, null=True)  # Field name made lowercase.
    sourcedocid = models.IntegerField(db_column='SOURCEDOCID')  # Field name made lowercase.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    ftindex = models.IntegerField(db_column='FTINDEX')  # Field name made lowercase.
    lockdate = models.DateTimeField(db_column='LOCKDATE', blank=True, null=True)  # Field name made lowercase.
    lockinfo = models.TextField(db_column='LOCKINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destdate = models.DateTimeField(db_column='DESTDATE', blank=True, null=True)  # Field name made lowercase.
    destinfo = models.TextField(db_column='DESTINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destlistid = models.IntegerField(db_column='DESTLISTID', blank=True, null=True)  # Field name made lowercase.
    wftriggerdatetime = models.DateTimeField(db_column='WFTRIGGERDATETIME', blank=True, null=True)  # Field name made lowercase.
    ocrstatus = models.SmallIntegerField(db_column='OCRSTATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_DOCS_1_8'


class PvdmDocs19(models.Model):
    docid = models.AutoField(db_column='DOCID', primary_key=True)  # Field name made lowercase.
    docindex1 = models.CharField(db_column='DOCINDEX1', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex2 = models.CharField(db_column='DOCINDEX2', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    docindex3 = models.CharField(db_column='DOCINDEX3', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CREATEDATE')  # Field name made lowercase.
    dupeid = models.IntegerField(db_column='DUPEID')  # Field name made lowercase.
    securelist = models.TextField(db_column='SECURELIST', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    checkouttime = models.DateTimeField(db_column='CHECKOUTTIME', blank=True, null=True)  # Field name made lowercase.
    checkoutuserid = models.IntegerField(db_column='CHECKOUTUSERID', blank=True, null=True)  # Field name made lowercase.
    sourcedocid = models.IntegerField(db_column='SOURCEDOCID')  # Field name made lowercase.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    ftindex = models.IntegerField(db_column='FTINDEX')  # Field name made lowercase.
    lockdate = models.DateTimeField(db_column='LOCKDATE', blank=True, null=True)  # Field name made lowercase.
    lockinfo = models.TextField(db_column='LOCKINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destdate = models.DateTimeField(db_column='DESTDATE', blank=True, null=True)  # Field name made lowercase.
    destinfo = models.TextField(db_column='DESTINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destlistid = models.IntegerField(db_column='DESTLISTID', blank=True, null=True)  # Field name made lowercase.
    wftriggerdatetime = models.DateTimeField(db_column='WFTRIGGERDATETIME', blank=True, null=True)  # Field name made lowercase.
    ocrstatus = models.SmallIntegerField(db_column='OCRSTATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_DOCS_1_9'


class PvdmObjs11(models.Model):
    objid = models.AutoField(db_column='OBJID', primary_key=True)  # Field name made lowercase.
    docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.
    objtype = models.SmallIntegerField(db_column='OBJTYPE')  # Field name made lowercase.
    hashtype = models.SmallIntegerField(db_column='HASHTYPE')  # Field name made lowercase.
    hashinfo = models.CharField(db_column='HASHINFO', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    filelist = models.TextField(db_column='FILELIST', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    pages = models.IntegerField(db_column='PAGES')  # Field name made lowercase.
    versionnum = models.FloatField(db_column='VERSIONNUM')  # Field name made lowercase.
    versiontime = models.DateTimeField(db_column='VERSIONTIME')  # Field name made lowercase.
    versioncreator = models.CharField(db_column='VERSIONCREATOR', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    versioncomments = models.TextField(db_column='VERSIONCOMMENTS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    trashuserid = models.IntegerField(db_column='TRASHUSERID', blank=True, null=True)  # Field name made lowercase.
    trashdatetime = models.DateTimeField(db_column='TRASHDATETIME', blank=True, null=True)  # Field name made lowercase.
    totalbytes = models.FloatField(db_column='TOTALBYTES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_OBJS_1_1'


class PvdmObjs110(models.Model):
    objid = models.AutoField(db_column='OBJID', primary_key=True)  # Field name made lowercase.
    docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.
    objtype = models.SmallIntegerField(db_column='OBJTYPE')  # Field name made lowercase.
    hashtype = models.SmallIntegerField(db_column='HASHTYPE')  # Field name made lowercase.
    hashinfo = models.CharField(db_column='HASHINFO', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    filelist = models.TextField(db_column='FILELIST', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    pages = models.IntegerField(db_column='PAGES')  # Field name made lowercase.
    versionnum = models.FloatField(db_column='VERSIONNUM')  # Field name made lowercase.
    versiontime = models.DateTimeField(db_column='VERSIONTIME')  # Field name made lowercase.
    versioncreator = models.CharField(db_column='VERSIONCREATOR', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    versioncomments = models.TextField(db_column='VERSIONCOMMENTS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    trashuserid = models.IntegerField(db_column='TRASHUSERID', blank=True, null=True)  # Field name made lowercase.
    trashdatetime = models.DateTimeField(db_column='TRASHDATETIME', blank=True, null=True)  # Field name made lowercase.
    totalbytes = models.FloatField(db_column='TOTALBYTES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_OBJS_1_10'


class PvdmObjs112(models.Model):
    objid = models.AutoField(db_column='OBJID', primary_key=True)  # Field name made lowercase.
    docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.
    objtype = models.SmallIntegerField(db_column='OBJTYPE')  # Field name made lowercase.
    hashtype = models.SmallIntegerField(db_column='HASHTYPE')  # Field name made lowercase.
    hashinfo = models.CharField(db_column='HASHINFO', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    filelist = models.TextField(db_column='FILELIST', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    pages = models.IntegerField(db_column='PAGES')  # Field name made lowercase.
    versionnum = models.FloatField(db_column='VERSIONNUM')  # Field name made lowercase.
    versiontime = models.DateTimeField(db_column='VERSIONTIME')  # Field name made lowercase.
    versioncreator = models.CharField(db_column='VERSIONCREATOR', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    versioncomments = models.TextField(db_column='VERSIONCOMMENTS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    trashuserid = models.IntegerField(db_column='TRASHUSERID', blank=True, null=True)  # Field name made lowercase.
    trashdatetime = models.DateTimeField(db_column='TRASHDATETIME', blank=True, null=True)  # Field name made lowercase.
    totalbytes = models.FloatField(db_column='TOTALBYTES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_OBJS_1_12'


class PvdmObjs113(models.Model):
    objid = models.AutoField(db_column='OBJID', primary_key=True)  # Field name made lowercase.
    docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.
    objtype = models.SmallIntegerField(db_column='OBJTYPE')  # Field name made lowercase.
    hashtype = models.SmallIntegerField(db_column='HASHTYPE')  # Field name made lowercase.
    hashinfo = models.CharField(db_column='HASHINFO', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    filelist = models.TextField(db_column='FILELIST', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    pages = models.IntegerField(db_column='PAGES')  # Field name made lowercase.
    versionnum = models.FloatField(db_column='VERSIONNUM')  # Field name made lowercase.
    versiontime = models.DateTimeField(db_column='VERSIONTIME')  # Field name made lowercase.
    versioncreator = models.CharField(db_column='VERSIONCREATOR', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    versioncomments = models.TextField(db_column='VERSIONCOMMENTS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    trashuserid = models.IntegerField(db_column='TRASHUSERID', blank=True, null=True)  # Field name made lowercase.
    trashdatetime = models.DateTimeField(db_column='TRASHDATETIME', blank=True, null=True)  # Field name made lowercase.
    totalbytes = models.FloatField(db_column='TOTALBYTES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_OBJS_1_13'


class PvdmObjs114(models.Model):
    objid = models.AutoField(db_column='OBJID', primary_key=True)  # Field name made lowercase.
    docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.
    objtype = models.SmallIntegerField(db_column='OBJTYPE')  # Field name made lowercase.
    hashtype = models.SmallIntegerField(db_column='HASHTYPE')  # Field name made lowercase.
    hashinfo = models.CharField(db_column='HASHINFO', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    filelist = models.TextField(db_column='FILELIST', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    pages = models.IntegerField(db_column='PAGES')  # Field name made lowercase.
    versionnum = models.FloatField(db_column='VERSIONNUM')  # Field name made lowercase.
    versiontime = models.DateTimeField(db_column='VERSIONTIME')  # Field name made lowercase.
    versioncreator = models.CharField(db_column='VERSIONCREATOR', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    versioncomments = models.TextField(db_column='VERSIONCOMMENTS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    trashuserid = models.IntegerField(db_column='TRASHUSERID', blank=True, null=True)  # Field name made lowercase.
    trashdatetime = models.DateTimeField(db_column='TRASHDATETIME', blank=True, null=True)  # Field name made lowercase.
    totalbytes = models.FloatField(db_column='TOTALBYTES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_OBJS_1_14'


class PvdmObjs115(models.Model):
    objid = models.AutoField(db_column='OBJID', primary_key=True)  # Field name made lowercase.
    docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.
    objtype = models.SmallIntegerField(db_column='OBJTYPE')  # Field name made lowercase.
    hashtype = models.SmallIntegerField(db_column='HASHTYPE')  # Field name made lowercase.
    hashinfo = models.CharField(db_column='HASHINFO', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    filelist = models.TextField(db_column='FILELIST', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    pages = models.IntegerField(db_column='PAGES')  # Field name made lowercase.
    versionnum = models.FloatField(db_column='VERSIONNUM')  # Field name made lowercase.
    versiontime = models.DateTimeField(db_column='VERSIONTIME')  # Field name made lowercase.
    versioncreator = models.CharField(db_column='VERSIONCREATOR', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    versioncomments = models.TextField(db_column='VERSIONCOMMENTS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    trashuserid = models.IntegerField(db_column='TRASHUSERID', blank=True, null=True)  # Field name made lowercase.
    trashdatetime = models.DateTimeField(db_column='TRASHDATETIME', blank=True, null=True)  # Field name made lowercase.
    totalbytes = models.FloatField(db_column='TOTALBYTES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_OBJS_1_15'


class PvdmObjs116(models.Model):
    objid = models.AutoField(db_column='OBJID', primary_key=True)  # Field name made lowercase.
    docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.
    objtype = models.SmallIntegerField(db_column='OBJTYPE')  # Field name made lowercase.
    hashtype = models.SmallIntegerField(db_column='HASHTYPE')  # Field name made lowercase.
    hashinfo = models.CharField(db_column='HASHINFO', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    filelist = models.TextField(db_column='FILELIST', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    pages = models.IntegerField(db_column='PAGES')  # Field name made lowercase.
    versionnum = models.FloatField(db_column='VERSIONNUM')  # Field name made lowercase.
    versiontime = models.DateTimeField(db_column='VERSIONTIME')  # Field name made lowercase.
    versioncreator = models.CharField(db_column='VERSIONCREATOR', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    versioncomments = models.TextField(db_column='VERSIONCOMMENTS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    trashuserid = models.IntegerField(db_column='TRASHUSERID', blank=True, null=True)  # Field name made lowercase.
    trashdatetime = models.DateTimeField(db_column='TRASHDATETIME', blank=True, null=True)  # Field name made lowercase.
    totalbytes = models.FloatField(db_column='TOTALBYTES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_OBJS_1_16'


class PvdmObjs12(models.Model):
    objid = models.AutoField(db_column='OBJID', primary_key=True)  # Field name made lowercase.
    docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.
    objtype = models.SmallIntegerField(db_column='OBJTYPE')  # Field name made lowercase.
    hashtype = models.SmallIntegerField(db_column='HASHTYPE')  # Field name made lowercase.
    hashinfo = models.CharField(db_column='HASHINFO', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    filelist = models.TextField(db_column='FILELIST', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    pages = models.IntegerField(db_column='PAGES')  # Field name made lowercase.
    versionnum = models.FloatField(db_column='VERSIONNUM')  # Field name made lowercase.
    versiontime = models.DateTimeField(db_column='VERSIONTIME')  # Field name made lowercase.
    versioncreator = models.CharField(db_column='VERSIONCREATOR', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    versioncomments = models.TextField(db_column='VERSIONCOMMENTS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    trashuserid = models.IntegerField(db_column='TRASHUSERID', blank=True, null=True)  # Field name made lowercase.
    trashdatetime = models.DateTimeField(db_column='TRASHDATETIME', blank=True, null=True)  # Field name made lowercase.
    totalbytes = models.FloatField(db_column='TOTALBYTES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_OBJS_1_2'


class PvdmObjs13(models.Model):
    objid = models.AutoField(db_column='OBJID', primary_key=True)  # Field name made lowercase.
    docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.
    objtype = models.SmallIntegerField(db_column='OBJTYPE')  # Field name made lowercase.
    hashtype = models.SmallIntegerField(db_column='HASHTYPE')  # Field name made lowercase.
    hashinfo = models.CharField(db_column='HASHINFO', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    filelist = models.TextField(db_column='FILELIST', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    pages = models.IntegerField(db_column='PAGES')  # Field name made lowercase.
    versionnum = models.FloatField(db_column='VERSIONNUM')  # Field name made lowercase.
    versiontime = models.DateTimeField(db_column='VERSIONTIME')  # Field name made lowercase.
    versioncreator = models.CharField(db_column='VERSIONCREATOR', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    versioncomments = models.TextField(db_column='VERSIONCOMMENTS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    trashuserid = models.IntegerField(db_column='TRASHUSERID', blank=True, null=True)  # Field name made lowercase.
    trashdatetime = models.DateTimeField(db_column='TRASHDATETIME', blank=True, null=True)  # Field name made lowercase.
    totalbytes = models.FloatField(db_column='TOTALBYTES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_OBJS_1_3'


class PvdmObjs14(models.Model):
    objid = models.AutoField(db_column='OBJID', primary_key=True)  # Field name made lowercase.
    docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.
    objtype = models.SmallIntegerField(db_column='OBJTYPE')  # Field name made lowercase.
    hashtype = models.SmallIntegerField(db_column='HASHTYPE')  # Field name made lowercase.
    hashinfo = models.CharField(db_column='HASHINFO', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    filelist = models.TextField(db_column='FILELIST', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    pages = models.IntegerField(db_column='PAGES')  # Field name made lowercase.
    versionnum = models.FloatField(db_column='VERSIONNUM')  # Field name made lowercase.
    versiontime = models.DateTimeField(db_column='VERSIONTIME')  # Field name made lowercase.
    versioncreator = models.CharField(db_column='VERSIONCREATOR', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    versioncomments = models.TextField(db_column='VERSIONCOMMENTS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    trashuserid = models.IntegerField(db_column='TRASHUSERID', blank=True, null=True)  # Field name made lowercase.
    trashdatetime = models.DateTimeField(db_column='TRASHDATETIME', blank=True, null=True)  # Field name made lowercase.
    totalbytes = models.FloatField(db_column='TOTALBYTES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_OBJS_1_4'


class PvdmObjs15(models.Model):
    objid = models.AutoField(db_column='OBJID', primary_key=True)  # Field name made lowercase.
    docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.
    objtype = models.SmallIntegerField(db_column='OBJTYPE')  # Field name made lowercase.
    hashtype = models.SmallIntegerField(db_column='HASHTYPE')  # Field name made lowercase.
    hashinfo = models.CharField(db_column='HASHINFO', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    filelist = models.TextField(db_column='FILELIST', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    pages = models.IntegerField(db_column='PAGES')  # Field name made lowercase.
    versionnum = models.FloatField(db_column='VERSIONNUM')  # Field name made lowercase.
    versiontime = models.DateTimeField(db_column='VERSIONTIME')  # Field name made lowercase.
    versioncreator = models.CharField(db_column='VERSIONCREATOR', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    versioncomments = models.TextField(db_column='VERSIONCOMMENTS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    trashuserid = models.IntegerField(db_column='TRASHUSERID', blank=True, null=True)  # Field name made lowercase.
    trashdatetime = models.DateTimeField(db_column='TRASHDATETIME', blank=True, null=True)  # Field name made lowercase.
    totalbytes = models.FloatField(db_column='TOTALBYTES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_OBJS_1_5'


class PvdmObjs16(models.Model):
    objid = models.AutoField(db_column='OBJID', primary_key=True)  # Field name made lowercase.
    docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.
    objtype = models.SmallIntegerField(db_column='OBJTYPE')  # Field name made lowercase.
    hashtype = models.SmallIntegerField(db_column='HASHTYPE')  # Field name made lowercase.
    hashinfo = models.CharField(db_column='HASHINFO', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    filelist = models.TextField(db_column='FILELIST', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    pages = models.IntegerField(db_column='PAGES')  # Field name made lowercase.
    versionnum = models.FloatField(db_column='VERSIONNUM')  # Field name made lowercase.
    versiontime = models.DateTimeField(db_column='VERSIONTIME')  # Field name made lowercase.
    versioncreator = models.CharField(db_column='VERSIONCREATOR', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    versioncomments = models.TextField(db_column='VERSIONCOMMENTS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    trashuserid = models.IntegerField(db_column='TRASHUSERID', blank=True, null=True)  # Field name made lowercase.
    trashdatetime = models.DateTimeField(db_column='TRASHDATETIME', blank=True, null=True)  # Field name made lowercase.
    totalbytes = models.FloatField(db_column='TOTALBYTES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_OBJS_1_6'


class PvdmObjs17(models.Model):
    objid = models.AutoField(db_column='OBJID', primary_key=True)  # Field name made lowercase.
    docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.
    objtype = models.SmallIntegerField(db_column='OBJTYPE')  # Field name made lowercase.
    hashtype = models.SmallIntegerField(db_column='HASHTYPE')  # Field name made lowercase.
    hashinfo = models.CharField(db_column='HASHINFO', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    filelist = models.TextField(db_column='FILELIST', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    pages = models.IntegerField(db_column='PAGES')  # Field name made lowercase.
    versionnum = models.FloatField(db_column='VERSIONNUM')  # Field name made lowercase.
    versiontime = models.DateTimeField(db_column='VERSIONTIME')  # Field name made lowercase.
    versioncreator = models.CharField(db_column='VERSIONCREATOR', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    versioncomments = models.TextField(db_column='VERSIONCOMMENTS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    trashuserid = models.IntegerField(db_column='TRASHUSERID', blank=True, null=True)  # Field name made lowercase.
    trashdatetime = models.DateTimeField(db_column='TRASHDATETIME', blank=True, null=True)  # Field name made lowercase.
    totalbytes = models.FloatField(db_column='TOTALBYTES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_OBJS_1_7'


class PvdmObjs18(models.Model):
    objid = models.AutoField(db_column='OBJID', primary_key=True)  # Field name made lowercase.
    docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.
    objtype = models.SmallIntegerField(db_column='OBJTYPE')  # Field name made lowercase.
    hashtype = models.SmallIntegerField(db_column='HASHTYPE')  # Field name made lowercase.
    hashinfo = models.CharField(db_column='HASHINFO', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    filelist = models.TextField(db_column='FILELIST', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    pages = models.IntegerField(db_column='PAGES')  # Field name made lowercase.
    versionnum = models.FloatField(db_column='VERSIONNUM')  # Field name made lowercase.
    versiontime = models.DateTimeField(db_column='VERSIONTIME')  # Field name made lowercase.
    versioncreator = models.CharField(db_column='VERSIONCREATOR', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    versioncomments = models.TextField(db_column='VERSIONCOMMENTS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    trashuserid = models.IntegerField(db_column='TRASHUSERID', blank=True, null=True)  # Field name made lowercase.
    trashdatetime = models.DateTimeField(db_column='TRASHDATETIME', blank=True, null=True)  # Field name made lowercase.
    totalbytes = models.FloatField(db_column='TOTALBYTES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_OBJS_1_8'


class PvdmObjs19(models.Model):
    objid = models.AutoField(db_column='OBJID', primary_key=True)  # Field name made lowercase.
    docid = models.IntegerField(db_column='DOCID')  # Field name made lowercase.
    objtype = models.SmallIntegerField(db_column='OBJTYPE')  # Field name made lowercase.
    hashtype = models.SmallIntegerField(db_column='HASHTYPE')  # Field name made lowercase.
    hashinfo = models.CharField(db_column='HASHINFO', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    filelist = models.TextField(db_column='FILELIST', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    pages = models.IntegerField(db_column='PAGES')  # Field name made lowercase.
    versionnum = models.FloatField(db_column='VERSIONNUM')  # Field name made lowercase.
    versiontime = models.DateTimeField(db_column='VERSIONTIME')  # Field name made lowercase.
    versioncreator = models.CharField(db_column='VERSIONCREATOR', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    versioncomments = models.TextField(db_column='VERSIONCOMMENTS', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    trashuserid = models.IntegerField(db_column='TRASHUSERID', blank=True, null=True)  # Field name made lowercase.
    trashdatetime = models.DateTimeField(db_column='TRASHDATETIME', blank=True, null=True)  # Field name made lowercase.
    totalbytes = models.FloatField(db_column='TOTALBYTES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_OBJS_1_9'



class PvdmDg1(models.Model):
    dgid = models.AutoField(db_column='DGID', primary_key=True)  # Field name made lowercase.
    dgname = models.CharField(db_column='DGNAME', unique=True, max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    path = models.TextField(db_column='PATH', db_collation='Latin1_General_CI_AS')  # Field name made lowercase. This field type is a guess.
    type = models.SmallIntegerField(db_column='TYPE')  # Field name made lowercase.
    lastupdatetime = models.DateTimeField(db_column='LASTUPDATETIME', blank=True, null=True)  # Field name made lowercase.
    size = models.FloatField(db_column='SIZE')  # Field name made lowercase.
    readwrite = models.BooleanField(db_column='READWRITE')  # Field name made lowercase.
    origdgname = models.CharField(db_column='ORIGDGNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    encryptkeyname = models.CharField(db_column='ENCRYPTKEYNAME', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    encryptkeyvalue = models.TextField(db_column='ENCRYPTKEYVALUE', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    trashuserid = models.IntegerField(db_column='TRASHUSERID', blank=True, null=True)  # Field name made lowercase.
    trashdatetime = models.DateTimeField(db_column='TRASHDATETIME', blank=True, null=True)  # Field name made lowercase.
    dginfo = models.TextField(db_column='DGINFO', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVDM_DG_1'



class ImagePathExportTmp(models.Model):
    casenumber = models.CharField(db_column='CASENUMBER', max_length=255, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    label = models.CharField(db_column='LABEL', max_length=25, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dgid = models.IntegerField(db_column='DGID')  # Field name made lowercase.
    docid = models.IntegerField(db_column='DOCID', blank=True, null=True)  # Field name made lowercase.
    dgname = models.CharField(db_column='DGNAME', max_length=255, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
    filename = models.CharField(db_column='FILENAME', primary_key=True, max_length=900, db_collation='Latin1_General_CI_AS')  # Field name made lowercase.
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
        db_table = 'IMAGE_PATH_EXPORT_TMP'



class ImageRecsNotToImport1(models.Model):
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
        db_table = 'IMAGE_RECS_NOT_TO_IMPORT_1'

