#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 14:22:03 2018

@author: earsch

Function to automatically create common details for Tanzania maps
-lat, longitude ticks
-coastline
-border Tanzania and Tanga

"""

import cartopy.crs as ccrs
import cartopy
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature
import cartopy.feature as cfeature

def tanzania_plot(ax, high, no_x = False, no_y = False):   
    
    coast_10m = cfeature.NaturalEarthFeature('physical', 'coastline', '10m',
                                         edgecolor = 'black')

    fname = r'/nfs/see-fs-02_users/earsch/Documents/Leeds/Tanga Project/Data/GIS_Maps/Tanga'
    tanga_feature = ShapelyFeature(Reader(fname).geometries(),
                                   ccrs.PlateCarree(), edgecolor = 'black')
    
    ax.add_feature(cartopy.feature.BORDERS, linewidth = 0.5)
    # set up latitude and longtiude ticks and format
    
    if no_y == False:
        ax.set_yticks([-10, -6, -2], crs=ccrs.PlateCarree())
        lat_formatter = LatitudeFormatter()
        ax.yaxis.set_major_formatter(lat_formatter)
    
    if no_x == False:
        ax.set_xticks([29, 34, 39], crs=ccrs.PlateCarree())
        lon_formatter = LongitudeFormatter()
        ax.xaxis.set_major_formatter(lon_formatter)
        
    # add tanga shapefile
    ax.add_feature(tanga_feature, facecolor = 'none', linewidth = 0.5)
    
    if high == True:
        ax.add_feature(coast_10m, facecolor = 'none')
    else:
        ax.add_feature(cartopy.feature.COASTLINE)

def tanga_plot(ax, high):   
    
    coast_10m = cfeature.NaturalEarthFeature('physical', 'coastline', '10m',
                                         edgecolor = 'black')

    fname = r'/nfs/see-fs-02_users/earsch/Documents/Leeds/Tanga Project/Data/GIS_Maps/Tanga'
    tanga_feature = ShapelyFeature(Reader(fname).geometries(),
                                   ccrs.PlateCarree(), edgecolor = 'black')
    
    ax.add_feature(cartopy.feature.BORDERS, linewidth = 0.5)
    # set up latitude and longtiude ticks and format
    ax.set_yticks([-6, -5, -4], crs=ccrs.PlateCarree())
    lat_formatter = LatitudeFormatter()
    ax.yaxis.set_major_formatter(lat_formatter)
    ax.set_xticks([37,38, 39], crs=ccrs.PlateCarree())
    lon_formatter = LongitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    # add tanga shapefile
    ax.add_feature(tanga_feature, facecolor = 'none', linewidth = 0.5)
    
    if high == True:
        ax.add_feature(coast_10m, facecolor = 'none')
    else:
        ax.add_feature(cartopy.feature.COASTLINE)