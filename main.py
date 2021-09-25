from webbot import Browser
from cycle_handler.candy import *
import os, time

## Setup
web = Browser()

## Cycles Info
cycle_path = 'account_list/cache.cycle'
cycles_per = 5


## Upvote the Post
dc_plus.upvote('POST_URL', cycles_per)


