#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 02:10:04 2016

@author: Beiwen Liu
"""
import urllib2
from bs4 import BeautifulSoup
from lxml import html
import operator
def main():
    
    url = "https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePage_false_0&formSourceTag=112&newSearchFromOverviewPage=true&inventorySearchWidgetType=AUTO&entitySelectingHelper.selectedEntity=d2&entitySelectingHelper.selectedEntity2=&zip=30309&distance=50&searchChanged=true&modelChanged=false&filtersModified=true&sortType=PRICE&sortDirection=ASC#resultsPage=1"
    
    pricemileCarGuru(url)
        
    
def pricemileCarGuru(url):
    page = urllib2.urlopen(url)
    
    soup = BeautifulSoup(page, 'html5lib')
    mydivs = soup.findAll("div", { "class" : "cg-dealFinder-result-stats" })
    
    values = {}
    for x in range(0,len(mydivs)):
        price = mydivs[x].find("span",{"itemprop" : "price"}).text
        mileage = mydivs[x].find_next("span",{"itemprop" : "price"}).parent.find_next_siblings()[0].find("span").text
        
        values[(float(price[1:].replace(",","")))] = float(mileage.replace(",",""))
        
    total = sorted(values.items(), key=operator.itemgetter(0))
    total1 = sorted(values.items(), key=operator.itemgetter(1))
    
    for x in range(0,len(total)):
        print "$" + str(total[x][0]) + " Miles: " + str(total[x][1]) + " ---------- Miles: " + str(total1[x][1]) + " $" + str(total1[x][0]) 
    
main()