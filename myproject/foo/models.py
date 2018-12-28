# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=1024, blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True, null=True)
    startdate = models.DateTimeField(blank=True, null=True)
    run_freq = models.IntegerField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    activationkey = models.CharField(max_length=1024, blank=True, null=True)
    registration_hash = models.CharField(max_length=1024, blank=True, null=True)
    subscription_id = models.ForeignKey('Subscriptions', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'company'

class Activity(models.Model):
    activity_id=models.CharField(max_length=1024,blank=True,null=True)
    datetime = models.DateTimeField(db_column='DateTime', blank=True, null=True)  # Field name made lowercase.
    company_id = models.ForeignKey(Company, models.DO_NOTHING,blank=True, null=True)

    class Meta:
        db_table = 'activity'

class Pingresults(models.Model):
    hostname = models.CharField(db_column='HostName', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    ip_adress_ipv6 = models.CharField(db_column='Ip_adress_IPv6', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    ip_adress_ipv4 = models.CharField(db_column='Ip_adress_Ipv4', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    activity_id = models.ForeignKey(Activity, models.DO_NOTHING, db_column='Company_id_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'pingresults'


class Subscriptions(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'subscriptions'


class User(models.Model):
    name = models.CharField(max_length=1024, blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=254, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=2048, blank=True, null=True)
    role = models.CharField(max_length=1024, blank=True, null=True)
    status = models.CharField(max_length=1024, blank=True, null=True)
    company_id_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'user'



class Employees(models.Model):
    employee_id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=1024, blank=True, null=True)
    last_name = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        db_table = 'employees'


class Mobile2(models.Model):
    text = models.CharField(max_length=1024, blank=True, null=True)
    mobile_id = models.ForeignKey(Employees, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'mobile2'


class AdExtractor(models.Model):
    Hostname=models.CharField(max_length=2048, blank=True, null=True)
    Os_title=models.CharField(max_length=2048, blank=True, null=True)
    Password_Last_set=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    Logon=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    When_created=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    When_changed=models.DateTimeField(auto_now_add=True, blank=True, null=True)
    Active_Directory_path=models.CharField(max_length=2048, blank=True, null=True)
    activity_id_id=models.ForeignKey(Activity,blank=True,null=True)

    class Meta:
        db_table = 'adextractor'
