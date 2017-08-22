#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : pyTweetBot.py
# Description : pyTweetBot main execution file.
# Auteur : Nils Schaetti <n.schaetti@gmail.com>
# Date : 01.05.2017 17:59:05
# Lieu : Nyon, Suisse
#
# This file is part of the pyTweetBot.
# The pyTweetBot is a set of free software:
# you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyTweetBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with pyTweetBar.  If not, see <http://www.gnu.org/licenses/>.
#

# Import
import argparse
import logging
import os
import time
from config.BotConfig import BotConfig
from db.DBConnector import DBConnector
from executor.ActionScheduler import ActionScheduler
from friends.FriendsManager import FriendsManager
from tweet.RSSHunter import RSSHunter
from tweet.GoogleNewsHunter import GoogleNewsHunter
from tweet.TweetFinder import TweetFinder
from twitter.TweetBotConnect import TweetBotConnector
from twitter.TweetGenerator import TweetGenerator
from tweet.TweetFactory import TweetFactory
from stats.TweetStatistics import TweetStatistics

####################################################
# Main function
####################################################


# Execute actions
def execute_actions(action_scheduler):
    """
    Execute actions
    :param config:
    :param twitter_connector:
    :param action_scheduler:
    :return:
    """
    # Start executing action
    logging.getLogger(u"pyTweetBot").info(u"Start executing action with scheduler...")
    action_scheduler.daemon = True
    action_scheduler.start()

    # Waiting for the thread to terminate
    try:
        while action_scheduler.isAlive():
            action_scheduler.join(5)
        # end while
    except (KeyboardInterrupt, SystemExit):
        logging.getLogger(u"pyTweetBot").info(u"Stopping executing action with scheduler...")
    # end try

# end if