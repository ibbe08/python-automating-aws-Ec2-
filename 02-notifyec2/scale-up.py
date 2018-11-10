# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonautomation')
as_client =session.client('autoscaling')

as_client.execute_policy(AutoScalingGroupName='Notifyec2 Autoscaling Group', PolicyName= 'Scale Up')
