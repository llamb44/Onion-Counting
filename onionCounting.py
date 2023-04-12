# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 08:51:03 2023

@author: Sweet
"""
import requests
from bs4 import BeautifulSoup

def onionCounting():
    pageUrl= "https://www.foodnetwork.com/recipes/recipes-a-z"
    page_r= requests.get(pageUrl)
    soup= BeautifulSoup(page_r.content, "lxml")
    
        
    onionRecipes = 0
    yellowOnionRecipes = 0
    powderOnionRecipes= 0
    totalRecipes = 0
    
    # onionRecipesList= []
    # yellowOnionRecipesList= []
    
    onionInc= False
    yellowOnionInc= False
    powderOnionRecipesInc= False
    
    indexList= ["http:"+pagination.get("href") for pagination in soup.find_all("a", class_= "o-IndexPagination__a-Button")]
    
    
    for indexPage in indexList:
        pageCount= 1
        
        page_r= requests.get(indexPage)
        page_soup= BeautifulSoup(page_r.content, "lxml")
        
        while pageCount != 0:
            recipeList= ["http:"+ tuple(recipe.children)[0].get("href") for recipe in page_soup.find_all("li", class_= "m-PromoList__a-ListItem")]
            
            if len(recipeList) == 0:
                pageCount=0
                break
            
            for recipe in recipeList:
                print(recipe)
                recipe_r= requests.get(recipe)
                recipe_soup= BeautifulSoup(recipe_r.content, "lxml")
                
                totalRecipes+=1
                
                for ingredient in recipe_soup.find_all("span", class_= "o-Ingredients__a-Ingredient--CheckboxLabel"):
                    if ("onion" in ingredient.text.lower() or "onions" in ingredient.text.lower()) and "powder" not in ingredient.text.lower():
                        onionRecipes+=1
                        #onionRecipesList.append(recipe)
                        with open(r"C:\Users\Sweet\OneDrive\Documents\College Stuff\Actual Class Things\spring2023\Bio\onionRecipeList.txt", "a") as outFile:
                            outFile.write(recipe+"\n")
                        
                        onionInc= True
                        #break
                    
                    if ("yellow onion" in ingredient.text.lower() or "yellow onions" in ingredient.text.lower()) and "powder" not in ingredient.text.lower():
                        yellowOnionRecipes+=1
                        #yellowOnionRecipesList.append(recipe)
                        with open(r"C:\Users\Sweet\OneDrive\Documents\College Stuff\Actual Class Things\spring2023\Bio\yellowOnionRecipeList.txt", "a") as outFile:
                            outFile.write(recipe+"\n")
                        
                        yellowOnionInc = True
                    
                    if (("powdered onion" in ingredient.text.lower()) or ("powdered onions" in ingredient.text.lower()) or ("onion powder" in ingredient.text.lower())):
                        powderOnionRecipes+=1
                        powderOnionRecipesInc
                    
                    if yellowOnionInc and onionInc and powderOnionRecipesInc:
                        yellowOnionInc= False
                        onionInc = False
                        powderOnionRecipesInc= False
                        break
                    
            pageCount+=1
            
            page_r= requests.get(indexPage+"p/"+str(pageCount))
            page_soup= BeautifulSoup(page_r.content, "lxml")
            print("\n\n")
            print(page_r.url)
            print("\n")
        #break
                
            
    print("onionCount=\t", onionRecipes)
    print("yellowOnionCount=\t", yellowOnionRecipes)
    print("powdered onion count=\t", powderOnionRecipes)
    print("totalRecipes=\t", totalRecipes)



    with open(r"C:\Users\Sweet\OneDrive\Documents\College Stuff\Actual Class Things\spring2023\Bio\onions.txt", "w")  as outFile:
        outFile.write("Onions:\t"+str(onionRecipes)+"\n")
        outFile.write("Yellow Onions:\t"+str(yellowOnionRecipes) +"\n")
        outFile.write("Powdered Onions:\t"+ str(powderOnionRecipes) +"\n")
        outFile.write("Total Recipes:\t"+str(totalRecipes)+"\n\n")
        outFile.write("Proportion of Onions:\t"+ str(onionRecipes/totalRecipes)+"\n")
        outFile.write("Proportion of Yellow Onions:\t"+ str(yellowOnionRecipes/totalRecipes)+"\n")
        outFile.write("Proportion of Powdered Onion:\t"+ str(powderOnionRecipes/totalRecipes)+"\n")
        
    # with open(r"C:\Users\Sweet\OneDrive\Documents\College Stuff\Actual Class Things\spring2023\Bio\onionRecipeList.txt", "w") as outFile:
    #     for recipe in onionRecipesList:
    #         outFile.write(recipe+"\n")
            
    # with open(r"C:\Users\Sweet\OneDrive\Documents\College Stuff\Actual Class Things\spring2023\Bio\yellowOnionRecipeList.txt", "w") as outFile:
    #     for recipe in yellowOnionRecipesList:
    #         outFile.write(recipe+"\n")
        
        
        
onionCounting()
