import csv
import os


destination= 'D:\VS\\'
device_type=''
device_file=''
part_ID_Description={}


class Codec:
    def __init__(self,**kwargs):
        self.kwargs=kwargs


    def cts_dx80(destination,device_file):
            device_file=os.path.join(destination,'DX80\\'+'DX80.csv')
            with open(device_file,'r') as device_info:
                for row in device_info:
                    row=row.strip('\n')
                    (key, val)=row.split(',')
                    part_ID_Description[key]=val
                return part_ID_Description


    def cts_sx80(destination,device_type,device_file):
        if device_type== 'xyz':
            device_file=os.path.join(destination,'xyz/'+'xyz.csv')
            with open(device_file,'r') as device_info:
                for row in device_info:
                    row=row.strip('\n')
                    (key, val)=row.split(',')
                    part_ID_Description[key]=val
                return part_ID_Description       

    def cts_sx20(destination,device_type,device_file):
        if device_type== 'xyz':
            device_file=os.path.join(destination,'xyz/'+'xyz.csv')
            with open(device_file,'r') as device_info:
                for row in device_info:
                    row=row.strip('\n')
                    (key, val)=row.split(',')
                    part_ID_Description[key]=val
                return part_ID_Description 


    def cts_sx10(destination,device_type,device_file):
        if device_type== 'xyz':
            device_file=os.path.join(destination,'xyz/'+'xyz.csv')
            with open(device_file,'r') as device_info:
                for row in device_info:
                    row=row.strip('\n')
                    (key, val)=row.split(',')
                    part_ID_Description[key]=val
                return part_ID_Description 


    def cts_mx800(destination,device_type,device_file):
        if device_type== 'xyz':
            device_file=os.path.join(destination,'xyz/'+'xyz.csv')
            with open(device_file,'r') as device_info:
                for row in device_info:
                    row=row.strip('\n')
                    (key, val)=row.split(',')
                    part_ID_Description[key]=val
                return part_ID_Description 


    def cts_mx700(destination,device_file):
        device_file=os.path.join(destination,'MX700\\'+'MX700.csv')
        with open(device_file,'r') as device_info:
                for row in device_info:
                    row=row.strip('\n')
                    (key, val)=row.split(',')
                    part_ID_Description[key]=val
                return part_ID_Description 


    def cts_rmkitmini(destination,device_type,device_file):
        if device_type== 'xyz':
            device_file=os.path.join(destination,'xyz/'+'xyz.csv')
            with open(device_file,'r') as device_info:
                for row in device_info:
                    row=row.strip('\n')
                    (key, val)=row.split(',')
                    part_ID_Description[key]=val
                return part_ID_Description 

    def cts_rmkitplus(destination,device_type,device_file):
        if device_type== 'xyz':
            device_file=os.path.join(destination,'xyz/'+'xyz.csv')
            with open(device_file,'r') as device_info:
                for row in device_info:
                    row=row.strip('\n')
                    (key, val)=row.split(',')
                    part_ID_Description[key]=val
                return part_ID_Description 

    def cts_rmkitusb(destination,device_type,device_file):
        if device_type== 'xyz':
            device_file=os.path.join(destination,'xyz/'+'xyz.csv')
            with open(device_file,'r') as device_info:
                for row in device_info:
                    row=row.strip('\n')
                    (key, val)=row.split(',')
                    part_ID_Description[key]=val
                return part_ID_Description