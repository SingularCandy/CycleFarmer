from main import web, cycle_path
from webbot import Browser

import time

class dc_plus:
  web = Browser()
  

  ## Post Information
  get_amount = 'jsx-1129441626 vote-control-count'

  ## Comment List 
  comment_class = "body"
  comment_post = "jsx-4184281861 primary"
  comments = ['Nice!', 'Awesome Post!', 'How many upvotes for the next update?', '@awesome_post Chain (sorry for pings by the way)']

  ## Logging Out
  logout_dropdown = 'jsx-3443991695'
  logout_button = 'Logout'


  ## Voting
  vote_classname = 'jsx-1129441626 vote-control vote-control-heavy vote-control-active vote-control-can-vote'
  vote_fails = 0

  ## Logging In
  login_name = 'username'
  login_pass = 'password'
  login_button = 'jsx-3019135774 primary'



  

  with open(cycle_path, 'a+') as handle:
    accounts = handle.read()

  def logout():
    dc_plus.web.click(classname=dc_plus.logout_dropdown)
    dc_plus.web.click('Logout')


  def comment(comment_data):
    dc_plus.web.type(comment_data, classname=dc_plus.comment_class)
    dc_plus.web.click(classname=dc_plus.comment_post)


    
  def upvote(post_url, amount):
    worked = 0
    failed = 0

    try:
      
     
      for account in dc_plus.accounts:
        dc_plus.web.go_to('https://replit.com/login')

        username = account.split(':')[0]
        password = account.split(':')[1]

        for i in range(0, int(amount)):
          dc_plus.web.type(username, name=dc_plus.login_name)
          dc_plus.web.type(password, name=dc_plus.login_pass)
          dc_plus.web.click(classname=dc_plus.login_button)
          dc_plus.web.go_to(post_url.lower()) 
          dc_plus.web.click(classname=dc_plus.vote_classname)

          print(f'Voted on {username} :: Worked {worked} :: Failed {failed}')
           
          dc_plus.logout()
      

    except:

      print('Failed to Launch Upvoter')

      failed += 1
      dc_plus.vote_fails += failed
