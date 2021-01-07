import sqlite3
import pandas as pd

def new_batting(year): #This function pulls the batting database for all players with over 0 ABs in a year
    conn = sqlite3.connect('lahmansbaseballdb.sqlite')
    c = conn.cursor()
    sql = """SELECT * from batting where AB > ? AND yearID = ?"""
    AB = "0"
    year = str(year)
    batting = pd.read_sql_query(sql, conn, params = (AB, year))
    c.close()
    return batting

def new_teams(year): #This function pulls the teams database for all teams in a year
    conn = sqlite3.connect('lahmansbaseballdb.sqlite')
    c = conn.cursor()
    sql = """SELECT * from teams where yearID = ?"""
    year = str(year)
    teams = pd.read_sql_query(sql, conn, params = (year,))
    c.close()
    return teams

def new_pitching(year): #This function pulls the pitching database for all players with over 0 IP in a year
    conn = sqlite3.connect('lahmansbaseballdb.sqlite')
    c = conn.cursor()
    sql = """SELECT * from pitching where IPouts > ? AND yearID = ?"""
    IP = "0"
    year = str(year)
    batting = pd.read_sql_query(sql, conn, params = (IP, year))
    c.close()
    return batting


def single_data(batting, pitching): #This function spits out team stats by pulling from player data
    batting = batting.groupby('teamID', as_index=False)[['R', 'H', 'HR', '2B', '3B', 'BB', 'SB', 'SO']].sum()
    pitching = pitching.groupby('teamID', as_index=False)[['ER', 'H', 'HR', 'BB', 'SO']].sum()
    pitching = pitching.rename(columns = {'H': 'HA', 'HR': 'HRA', 'BB': 'BBA', 'SO': 'SOA'})
    training = pd.merge(batting, pitching, how ='outer', on = 'teamID')
    return training


def prediction_data(old_batting, old_pitching, new_batting, new_pitching): #This function takes in the teams, batting, and pitching
    #dataframes, and spits out a dataframe that has their stats calculated for each team based on the player in that year

    new_batting = new_batting[['playerID', 'teamID']]
    new_pitching = new_pitching[['playerID', 'teamID']]

    old_batting = old_batting[['playerID', 'R', 'H', 'HR', '2B', '3B', 'BB', 'SB', 'SO']]
    old_pitching = old_pitching[['playerID', 'ER', 'H', 'HR', 'BB', 'SO']]

    batting = pd.merge(new_batting, old_batting, how ='left', on = 'playerID')
    pitching = pd.merge(new_pitching, old_pitching, how ='left', on = 'playerID')

    batting = batting.groupby('teamID', as_index=False)[['R', 'H', 'HR', '2B', '3B', 'BB', 'SB', 'SO']].sum()
    pitching = pitching.groupby('teamID', as_index=False)[['ER', 'H', 'HR', 'BB', 'SO']].sum()
    pitching = pitching.rename(columns = {'H': 'HA', 'HR': 'HRA', 'BB': 'BBA', 'SO': 'SOA'})
    prediction = pd.merge(batting, pitching, how ='outer', on = 'teamID')
    return prediction

def multi_year(i):
    batting_data = new_batting((i))
    pitching_data = new_pitching((i))
    teams_data = new_teams((i))
    combined = single_data(batting_data, pitching_data)
    teams_data = teams_data[['teamID', 'W']]
    single_training = pd.merge(teams_data, combined, how = 'left', on = "teamID")
    return single_training

    
    
