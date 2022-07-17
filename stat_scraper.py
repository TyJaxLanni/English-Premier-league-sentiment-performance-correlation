#!/usr/bin/env python

from lxml import html
import time
import requests
#from twitter_api_scraper import main as sentiment

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def getPlayers(clubSite, base_url):
	resp = requests.get(clubSite)
	tree = html.fromstring(resp.content)
	playerElements = tree.xpath('/html/body/main/div[3]/div/ul/li[*]/a')
	#stores a string of the player's link to their stats for each player

	playerSiteList = [base_url + "/".join(player.attrib['href'].split("/")[0:-1]) for player in playerElements]

	return(playerSiteList)


def getForward(tree, driver, player, yearExt):
	playerDict = dict()
	playerDict["position"] = "Forward"
	playerDict["name"] = player.split("/")[5]

	attackBlock = "/html/body/main/div[3]/div/div/div[2]/div/div/ul/li[1]/div"
	teamplayBlock = "/html/body/main/div[3]/div/div/div[2]/div/div/ul/li[2]/div"
	disciplineBlock = "/html/body/main/div[3]/div/div/div[2]/div/div/ul/li[3]/div"
	defenseBlock = "/html/body/main/div[3]/div/div/div[2]/div/div/ul/li[4]/div"	

	driver.get(player+yearExt)
	time.sleep(2)	
	goals = driver.find_element_by_xpath(attackBlock + "/div[2]/span/span").text
	penalties_scored = driver.find_element_by_xpath(attackBlock + "/div[7]/span/span").text
	freekicks_scored = driver.find_element_by_xpath(attackBlock + "/div[8]/span/span").text
	shots = driver.find_element_by_xpath(attackBlock + "/div[9]/span/span").text
	shots_on_target = driver.find_element_by_xpath(attackBlock + "/div[10]/span/span").text
	shooting_accuracy = driver.find_element_by_xpath(attackBlock + "/div[11]/span/span").text
	big_chances_missed = driver.find_element_by_xpath(attackBlock + "/div[13]/span/span").text

	#----------------------------------------------------------------------------------------------------	
	assists = driver.find_element_by_xpath(teamplayBlock + "/div[2]/span/span").text
	passes = driver.find_element_by_xpath(teamplayBlock + "/div[3]/span/span").text
	big_chances_created = driver.find_element_by_xpath(teamplayBlock + "/div[5]/span/span").text
	crosses = driver.find_element_by_xpath(teamplayBlock + "/div[6]/span/span").text
	
	#---------------------------------------------------------------------------------------------------------
	yellow_cards = driver.find_element_by_xpath(disciplineBlock + "/div[2]/span/span").text
	red_cards =  driver.find_element_by_xpath(disciplineBlock + "/div[3]/span/span").text

	#---------------------------------------------------------------------------------------------------
	tackles = driver.find_element_by_xpath(defenseBlock + "/div[2]/span/span").text
	blocked_shots = driver.find_element_by_xpath(defenseBlock + "/div[3]/span/span").text
	interceptions = driver.find_element_by_xpath(defenseBlock + "/div[4]/span/span").text
	clearances = driver.find_element_by_xpath(defenseBlock + "/div[5]/span/span").text

	playerDict["goals"] = goals.replace(',', '')
	playerDict["penalties_scored"] = penalties_scored.replace(',', '')
	playerDict["freekicks_scored"] = freekicks_scored.replace(',', '')
	playerDict["shots"] = shots.replace(',', '')
	playerDict["shots_on_target"] = shots_on_target.replace(',', '')
	playerDict["shooting_accuracy"] = shooting_accuracy.replace(',', '')
	playerDict["big_chances_missed"] = big_chances_missed.replace(',', '')
	playerDict["assists"] = assists.replace(',', '')
	playerDict["passes"] = passes.replace(',', '')
	playerDict["big_chances_created"] = big_chances_created.replace(',', '')
	playerDict["crosses"] = crosses.replace(',', '')
	playerDict["yellow_cards"] = yellow_cards.replace(',', '')
	playerDict["red_cards"] = red_cards.replace(',', '')
	playerDict["tackles"] =tackles.replace(',', '')
	playerDict["blocked_shots"] = blocked_shots.replace(',', '')
	playerDict["interceptions"] = interceptions.replace(',', '')
	playerDict["clearances"] = clearances.replace(',', '')

	return playerDict


#===========================================================================================================================
def getMidfielder(tree, driver, player, yearExt):
	playerDict = dict()
	playerDict["position"] = "Midfielder"
	playerDict["name"] = player.split("/")[5]

	attackBlock = "/html/body/main/div[3]/div/div/div[2]/div/div/ul/li[1]/div"
	teamplayBlock = "/html/body/main/div[3]/div/div/div[2]/div/div/ul/li[2]/div"
	disciplineBlock = "/html/body/main/div[3]/div/div/div[2]/div/div/ul/li[3]/div"
	defenseBlock = "/html/body/main/div[3]/div/div/div[2]/div/div/ul/li[4]/div"	

	driver.get(player+yearExt)
	time.sleep(2)	
	goals = driver.find_element_by_xpath(attackBlock + "/div[2]/span/span").text
	penalties_scored = driver.find_element_by_xpath(attackBlock + "/div[7]/span/span").text
	freekicks_scored = driver.find_element_by_xpath(attackBlock + "/div[8]/span/span").text
	shots = driver.find_element_by_xpath(attackBlock + "/div[9]/span/span").text
	shots_on_target = driver.find_element_by_xpath(attackBlock + "/div[10]/span/span").text
	shooting_accuracy = driver.find_element_by_xpath(attackBlock + "/div[11]/span/span").text
	big_chances_missed = driver.find_element_by_xpath(attackBlock + "/div[13]/span/span").text

	#-------------------------------------------------------------------------------------------------
	assists = driver.find_element_by_xpath(teamplayBlock + "/div[2]/span/span").text
	passes = driver.find_element_by_xpath(teamplayBlock + "/div[3]/span/span").text
	big_chances_created = driver.find_element_by_xpath(teamplayBlock + "/div[5]/span/span").text
	crosses = driver.find_element_by_xpath(teamplayBlock + "/div[6]/span/span").text
	cross_accuracy = driver.find_element_by_xpath(teamplayBlock + "/div[7]/span/span").text
	through_balls = driver.find_element_by_xpath(teamplayBlock + "/div[8]/span/span").text
	accurate_long_balls = driver.find_element_by_xpath(teamplayBlock + "/div[9]/span/span").text

	#-------------------------------------------------------------------------------------------------
	yellow_cards = driver.find_element_by_xpath(disciplineBlock + "/div[2]/span/span").text
	red_cards =  driver.find_element_by_xpath(disciplineBlock + "/div[3]/span/span").text

	#---------------------------------------------------------------------------------------------------
	tackles = driver.find_element_by_xpath(defenseBlock + "/div[2]/span/span").text
	tackle_success = driver.find_element_by_xpath(defenseBlock + "/div[3]/span/span").text
	blocked_shots = driver.find_element_by_xpath(defenseBlock + "/div[4]/span/span").text
	interceptions = driver.find_element_by_xpath(defenseBlock + "/div[5]/span/span").text
	clearances = driver.find_element_by_xpath(defenseBlock + "/div[6]/span/span").text
	recoveries = driver.find_element_by_xpath(defenseBlock + "/div[8]/span/span").text
	duels_won = driver.find_element_by_xpath(defenseBlock + "/div[9]/span/span").text
	duels_lost = driver.find_element_by_xpath(defenseBlock + "/div[10]/span/span").text
	successful_50_50 = driver.find_element_by_xpath(defenseBlock + "/div[11]/span/span").text
	aerial_battles_won = driver.find_element_by_xpath(defenseBlock + "/div[12]/span/span").text
	aerial_battles_lost = driver.find_element_by_xpath(defenseBlock + "/div[13]/span/span").text
	errors = driver.find_element_by_xpath(defenseBlock + "/div[14]/span/span").text

	playerDict["goals"] = goals.replace(',', '')
	playerDict["penalties_scored"] = penalties_scored.replace(',', '')
	playerDict["freekicks_scored"] = freekicks_scored.replace(',', '')
	playerDict["shots"] = shots.replace(',', '')
	playerDict["shots_on_target"] = shots_on_target.replace(',', '')
	playerDict["shooting_accuracy"] = shooting_accuracy.replace(',', '')
	playerDict["big_chances_missed"] = big_chances_missed.replace(',', '')
	playerDict["assists"] = assists.replace(',', '')
	playerDict["passes"] = passes.replace(',', '')
	playerDict["big_chances_created"] = big_chances_created.replace(',', '')
	playerDict["crosses"] = crosses.replace(',', '')
	playerDict["cross_accuracy"] = cross_accuracy.replace(',', '')
	playerDict["through_balls"] = through_balls.replace(',', '')
	playerDict["accurate_long_balls"] = accurate_long_balls.replace(',', '')
	playerDict["yellow_cards"] = yellow_cards.replace(',', '')
	playerDict["red_cards"] = red_cards.replace(',', '')
	playerDict["tackles"] =tackles.replace(',', '')
	playerDict["tackle_success"] = tackle_success.replace(',', '')
	playerDict["blocked_shots"] = blocked_shots.replace(',', '')
	playerDict["interceptions"] = interceptions.replace(',', '')
	playerDict["clearances"] = clearances.replace(',', '')
	playerDict["recoveries"] = recoveries.replace(',', '')
	playerDict["duels_won"] =  duels_won.replace(',', '')
	playerDict["duels_lost"] = duels_lost.replace(',', '')
	playerDict["successful_50_50"] =  successful_50_50.replace(',', '')
	playerDict["aerial_battles_won"] = aerial_battles_won.replace(',', '')
	playerDict["aerial_battles_lost"] = aerial_battles_lost.replace(',', '')
	playerDict["errors"] = errors.replace(',', '')

	return playerDict

#============================================================================================================================
def getDefender(tree, driver, player, yearExt):
	playerDict = dict()
	playerDict["position"] = "Defender"
	playerDict["name"] = player.split("/")[5]

	defenseBlock = "/html/body/main/div[3]/div/div/div[2]/div/div/ul/li[1]/div"
	teamplayBlock = "/html/body/main/div[3]/div/div/div[2]/div/div/ul/li[2]/div"
	disciplineBlock = "/html/body/main/div[3]/div/div/div[2]/div/div/ul/li[3]/div"
	attackBlock = "/html/body/main/div[3]/div/div/div[2]/div/div/ul/li[4]/div"

	driver.get(player+yearExt)
	time.sleep(2)	
	clean_sheets = driver.find_element_by_xpath(defenseBlock + "/div[2]/span/span").text
	goals_conceded = driver.find_element_by_xpath(defenseBlock + "/div[3]/span/span").text
	tackles = driver.find_element_by_xpath(defenseBlock + "/div[4]/span/span").text
	tackle_success = driver.find_element_by_xpath(defenseBlock + "/div[5]/span/span").text
	last_man_tackles = driver.find_element_by_xpath(defenseBlock + "/div[6]/span/span").text
	interceptions = driver.find_element_by_xpath(defenseBlock + "/div[8]/span/span").text
	clearances = driver.find_element_by_xpath(defenseBlock + "/div[9]/span/span").text
	recoveries = driver.find_element_by_xpath(defenseBlock + "/div[12]/span/span").text
	duels_won = driver.find_element_by_xpath(defenseBlock + "/div[13]/span/span").text
	duels_lost = driver.find_element_by_xpath(defenseBlock + "/div[14]/span/span").text
	successful_50_50 = driver.find_element_by_xpath(defenseBlock + "/div[15]/span/span").text
	aerial_battles_won = driver.find_element_by_xpath(defenseBlock + "/div[16]/span/span").text
	aerial_battles_lost = driver.find_element_by_xpath(defenseBlock + "/div[17]/span/span").text
	own_goals = driver.find_element_by_xpath(defenseBlock + "/div[18]/span/span").text
	errors = driver.find_element_by_xpath(defenseBlock + "/div[19]/span/span").text

	#---------------------------------------------------------------------------------------------
	assists = driver.find_element_by_xpath(teamplayBlock + "/div[2]/span/span").text
	passes = driver.find_element_by_xpath(teamplayBlock + "/div[3]/span/span").text
	big_chances_created = driver.find_element_by_xpath(teamplayBlock + "/div[5]/span/span").text
	crosses = driver.find_element_by_xpath(teamplayBlock + "/div[6]/span/span").text
	cross_accuracy = driver.find_element_by_xpath(teamplayBlock + "/div[7]/span/span").text
	through_balls = driver.find_element_by_xpath(teamplayBlock + "/div[8]/span/span").text
	accurate_long_balls = driver.find_element_by_xpath(teamplayBlock + "/div[9]/span/span").text

	#-------------------------------------------------------------------------------------------------
	yellow_cards = driver.find_element_by_xpath(disciplineBlock + "/div[2]/span/span").text
	red_cards =  driver.find_element_by_xpath(disciplineBlock + "/div[3]/span/span").text

	#---------------------------------------------------------------------------------------------------
	goals = driver.find_element_by_xpath(attackBlock + "/div[2]/span/span").text

	playerDict["clean_sheets"] = clean_sheets.replace(',', '')
	playerDict["goals_conceded"] = goals_conceded.replace(',', '')
	playerDict["tackles"] = tackles.replace(',', '')
	playerDict["tackle_success"] = tackle_success.replace(',', '')
	playerDict["last_man_tackles"] = last_man_tackles.replace(',', '')
	playerDict["interceptions"] = interceptions.replace(',', '')
	playerDict["clearances"] = clearances.replace(',', '')
	playerDict["recoveries"] = recoveries.replace(',', '')
	playerDict["duels_won"] = duels_won.replace(',', '')
	playerDict["duels_lost"] = duels_lost.replace(',', '')
	playerDict["successful_50_50"] = successful_50_50.replace(',', '')
	playerDict["aerial_battles_won"] = aerial_battles_won.replace(',', '')
	playerDict["aerial_battles_lost"] = aerial_battles_lost.replace(',', '')
	playerDict["own_goals"] = own_goals.replace(',', '')
	playerDict["errors"] = errors.replace(',', '')
	playerDict["assists"] = assists.replace(',', '')
	playerDict["passes"] = passes.replace(',', '')
	playerDict["big_chances_created"] = big_chances_created.replace(',', '')
	playerDict["crosses"] = crosses.replace(',', '')
	playerDict["cross_accuracy"] = cross_accuracy.replace(',', '')
	playerDict["through_balls"] = through_balls.replace(',', '')
	playerDict["accurate_long_balls"] = accurate_long_balls.replace(',', '')
	playerDict["yellow_cards"] = yellow_cards.replace(',', '')
	playerDict["red_cards"] = red_cards.replace(',', '')
	playerDict["goals"] = goals.replace(',', '') 	
	return playerDict



#==================================================================================================================
def getGoalkeeper(tree, driver, player, yearExt):
	#statContainer = "/html/body/main/div[3]/div/div/div[2]/div/div/ul"
	playerDict = dict()
	playerDict["position"] = "Goalkeeper"
	playerDict["name"] = player.split("/")[5]

	goalkeepingBlock = "/html/body/main/div[3]/div/div/div[2]/div/div/ul/li[1]/div"
	defenseBlock = "/html/body/main/div[3]/div/div/div[2]/div/div/ul/li[2]/div"
	disciplineBlock = "/html/body/main/div[3]/div/div/div[2]/div/div/ul/li[3]/div"
	#/html/body/main/div[3]/div/div/div[2]/div/div/ul/li[1]/div/div[3]/span/span
	#//*[@id="mainContent"]/div[3]/div/div/div[2]/div/div/ul/li[1]/div/div[3]/span/span
	#/div[2]/span/span extension for saves amount


	driver.get(player+yearExt)
	time.sleep(2)
	saves = driver.find_element_by_xpath(goalkeepingBlock + "/div[2]/span/span").text
	PK_saves = driver.find_element_by_xpath(goalkeepingBlock + "/div[3]/span/span").text
	punches = driver.find_element_by_xpath(goalkeepingBlock + "/div[4]/span/span").text
	high_claims = driver.find_element_by_xpath(goalkeepingBlock + "/div[5]/span/span").text
	catches = driver.find_element_by_xpath(goalkeepingBlock + "/div[6]/span/span").text
	sweeper_clearances = driver.find_element_by_xpath(goalkeepingBlock + "/div[7]/span/span").text
	#-------------------------------------------------------------------------------------------
	clean_sheets = driver.find_element_by_xpath(defenseBlock + "/div[2]/span/span").text
	goals_conceded = driver.find_element_by_xpath(defenseBlock + "/div[3]/span/span").text
	errors = driver.find_element_by_xpath(defenseBlock + "/div[4]/span/span").text
	own_goals = driver.find_element_by_xpath(defenseBlock + "/div[5]/span/span").text
	#------------------------------------------------------------------------------------------
	yellow_cards = driver.find_element_by_xpath(disciplineBlock + "/div[2]/span/span").text
	red_cards = driver.find_element_by_xpath(disciplineBlock + "/div[3]/span/span").text
	#//*[@id="mainContent"]/div[3]/div/div/div[2]/div/div/ul/li[2]/div/div[2]/span/span
	#saves = xpath(goalkeepingBlock + "/div[2]/span/span")

	playerDict["saves"] = saves.replace(',', '')
	playerDict["PK_saves"] = PK_saves.replace(',', '')
	playerDict["punches"] = punches.replace(',', '')
	playerDict["high_claims"] = high_claims.replace(',', '')
	playerDict["catches"] = catches.replace(',', '')
	playerDict["sweeper_clearances"] = sweeper_clearances.replace(',', '')
	playerDict["clean_sheets"] = clean_sheets.replace(',', '')
	playerDict["goals_conceded"] = goals_conceded.replace(',', '')
	playerDict["errors"] = errors.replace(',', '')
	playerDict["own_goals"] = own_goals.replace(',', '')
	playerDict["yellow_cards"] = yellow_cards.replace(',', '')
	playerDict["red_cards"] = red_cards.replace(',', '')

	return(playerDict)


	

def getStats(players, yearExt, driver):
	
	teamDict =dict()
	for player in players:
		#print(player+yearExt)
		resp = requests.get(player+yearExt)
		tree = html.fromstring(resp.content)

		position = tree.xpath('//*[@id="mainContent"]/div[3]/nav/div/section[1]/div[4]')
		if position[0].text == "Goalkeeper":
			#returns a dictionary for this particular player
			playerStats = getGoalkeeper(tree, driver, player, yearExt)
		elif position[0].text == "Defender":
			playerStats = getDefender(tree, driver, player, yearExt)
		elif position[0].text == "Midfielder":
			playerStats = getMidfielder(tree, driver, player, yearExt)
		elif position[0].text == "Forward":		#forward
			playerStats = getForward(tree, driver, player, yearExt)


		#playerInfo = tree.xpath('/html/body/main/div[3]/div/div/div[2]/div/div/ul')
		name = player.split("/")[5]
		
		#stores this dictionary in the team's dictionary for this particular player.
		teamDict[name] = playerStats

	return teamDict


def main():
	clubSite = "https://www.premierleague.com/clubs/7/Everton/squad"
	base_url = "https://www.premierleague.com"
	yearExt = "/stats?co=1&se=363"
	driver = webdriver.Chrome()
	
	#https://www.premierleague.com/clubs/7/Everton/squad/stats?co=1&se=363

	players = getPlayers(clubSite, base_url)
	teamDict = getStats(players, yearExt, driver)

	with open('stats.txt', 'w') as f:
		for player in teamDict.keys():
			print(teamDict[player], file=f)

	#for player in players:












	for i in teamDict.keys():
		print(teamDict[i])








	##site
	#url = "https://en.wikipedia.org/wiki/Outline_of_the_Marvel_Cinematic_Universe"
	##creating our requests object
	#resp = requests.get(url)
	##a tree of the entire site
	#tree = html.fromstring(resp.content)
	##all elements of the first column in our site. This holds all movies and links to their pages
	#elements = tree.xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr[*]/th/i/a')
	##printing all  elements
	#print(elements)
	##printing the first element
	#print(elements[0])
	##printing all info about hte first element
	#print(elements[0].attrib)
	##just printing the first element's link
	#print(elements[0].attrib['href'])
	##the base url we can use to iterate through all of them
	#base_url = "https://en.wikipedia.org"
	##list of all links for movies using base url and list comprehension.
	##we only want to capture hte first column where names are stored
	#links = [base_url + element.attrib['href'] for element in elements]
	#print (links)

if __name__ == "__main__":
    main()
