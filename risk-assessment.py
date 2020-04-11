import arcpy
from arcpy import env
arcpy.CheckOutExtension("spatial")
arcpy.env.overwriteOutput = True
env.workspace = "."
import configparser
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

import ast
D1 = arcpy.Raster(ast.literal_eval(config_ini['Properties']['D1']))
D2 = arcpy.Raster(ast.literal_eval(config_ini['Properties']['D2']))
D3name = ast.literal_eval(config_ini['Properties']['D3name'])
D3param = ast.literal_eval(config_ini['Properties']['D3param'])
D3 = arcpy.Raster(D3name[0]) * D3param[0]
for i in range(1, len(D3name)):
    D3 = D3 + arcpy.Raster(D3name[i]) * D3param[i]
D4 = arcpy.Raster(ast.literal_eval(config_ini['Properties']['D4']))
D5 = arcpy.Raster(ast.literal_eval(config_ini['Properties']['D5']))
D6 = arcpy.Raster(ast.literal_eval(config_ini['Properties']['D6']))
C1 = D1*0.25
C2 = D2*0.2+D3*0.15
C3 = D4*0.15+D5*0.15+D6*0.1
B1 = C1+C2
B2 = C3
res = B1 + B2
res.save("risk.tif")