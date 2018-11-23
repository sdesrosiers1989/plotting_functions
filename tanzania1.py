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

import iris

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

def tanga_plot(ax, high, no_x = False, no_y = False, subset = False):   
    
    coast_10m = cfeature.NaturalEarthFeature('physical', 'coastline', '10m',
                                         edgecolor = 'black')

    fname = r'/nfs/see-fs-02_users/earsch/Documents/Leeds/Tanga Project/Data/GIS_Maps/Tanga'
    tanga_feature = ShapelyFeature(Reader(fname).geometries(),
                                   ccrs.PlateCarree(), edgecolor = 'black')
    
    ax.add_feature(cartopy.feature.BORDERS, linewidth = 0.5)
    # set up latitude and longtiude ticks and format
    
    
    # add tanga shapefile
    ax.add_feature(tanga_feature, facecolor = 'none', linewidth = 0.5)
    
    if high == True:
        ax.add_feature(coast_10m, facecolor = 'none')
    else:
        ax.add_feature(cartopy.feature.COASTLINE)
    
    if no_y == False:
        ax.set_yticks([-6, -5, -4], crs=ccrs.PlateCarree())
        lat_formatter = LatitudeFormatter()
        ax.yaxis.set_major_formatter(lat_formatter)
    
    if no_x == False:
        ax.set_xticks([37,38, 39], crs=ccrs.PlateCarree())
        lon_formatter = LongitudeFormatter()
        ax.xaxis.set_major_formatter(lon_formatter)
        
    if subset == False:
        ax.set_ylim([-6.25,-3.75])
        ax.set_xlim([-1, 1.25])
        
def plot_africa(ax, high, no_x = False, no_y = False, Tanga = True,
                yticks = [-10, -6, -2], xticks =[29, 34, 39]):   
    
    coast_10m = cfeature.NaturalEarthFeature('physical', 'coastline', '10m',
                                         edgecolor = 'black')

    fname = r'/nfs/see-fs-02_users/earsch/Documents/Leeds/Tanga Project/Data/GIS_Maps/Tanga'
    tanga_feature = ShapelyFeature(Reader(fname).geometries(),
                                   ccrs.PlateCarree(), edgecolor = 'black')
    
    ax.add_feature(cartopy.feature.BORDERS, linewidth = 0.5)
    # set up latitude and longtiude ticks and format
    
    if no_y == False:
        ax.set_yticks(yticks, crs=ccrs.PlateCarree())
        lat_formatter = LatitudeFormatter()
        ax.yaxis.set_major_formatter(lat_formatter)
    
    if no_x == False:
        ax.set_xticks(xticks, crs=ccrs.PlateCarree())
        lon_formatter = LongitudeFormatter()
        ax.xaxis.set_major_formatter(lon_formatter)
        
    # add tanga shapefile
    if Tanga == True:
        ax.add_feature(tanga_feature, facecolor = 'none', linewidth = 0.5)
    
    if high == True:
        ax.add_feature(coast_10m, facecolor = 'none')
    else:
        ax.add_feature(cartopy.feature.COASTLINE)
        
def extract_tanz(cube, circ = True):
    def tanzania_lat(input):
        return -12.0 < input < -0.75
    
    if circ == False:
        def tanzania_long(input):
            return 28. < input < 42.
    else:
        def tanzania_long(input):
            return 388. < input < 402.
    
    out = cube.extract(iris.Constraint(latitude = tanzania_lat, 
                                        longitude = tanzania_long))
    return out

def extract_tanga(cube, circ = True):
    def tanga_lat(input):
        return -6.5 < input < -3.5
  
    if circ == False:
        def tanga_long(input):
            return 36.8 < input < 39.39
    else:
        def tanga_long(input):
            return 396.8 < input < 399.4
    
    out = cube.extract(iris.Constraint(latitude = tanga_lat, 
                                        longitude = tanga_long))
    return out

def get_cbax(fig, ax, orientation = 'horizontal', last_ax = [], dif = 0.03, h_w = 0.03):
    ''' Find placement of colourbar axis so it lines up with subplots
    #left, bottom, width, height'''
          
    place = ax.get_position()
    
    if orientation == 'horizontal':
        if len(last_ax) > 0 :
            ax2 = last_ax[0]
            place2 = ax2.get_position()
            cbax = fig.add_axes([place.x0, place.y0 - dif, place2.x1 - place.x0, h_w])
        else:
            cbax = fig.add_axes([place.x0, place.y0 - dif, place.x1 - place.x0, h_w])
        
    if orientation == 'vertical' and len(last_ax) == 0:
        cbax = fig.add_axes([place.x1 + dif, place.y0, h_w, place.y1 - place.y0])
    elif orientation == 'vertical':
        ax2 = last_ax[0]
        place2 = ax2.get_position()
        cbax = fig.add_axes([place.x1 + dif, place2.y0, h_w, place.y1 - place2.y0])
    return cbax