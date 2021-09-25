from main import *
import time

class dc_plus:
  

  ## Post Information
  get_amount = 'jsx-1129441626 vote-control-count'

  ## Comment List 
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
    web.click(classname=logout_dropdown)
    web.click('Logout')

  def upvote(post_url, amount):
    worked = 0
    failed = 0

    try:
      
     
      for account in dc_plus.accounts:
        web.go_to('https://replit.com/login')

        username = account.split(':')[0]
        password = account.split(':')[1]

        for i in range(0, int(amount)):
          web.type(username, name=dc_plus.login_name)
          web.type(password, name=dc_plus.login_pass)
          web.click(classname=dc_plus.login_button)
          web.go_to(post_url.lower()) 
          web.click(classname=dc_plus.vote_classname)

          print(f'Voted on {username} :: Worked {worked} :: Failed {failed}')
           
          dc_plus.logout()
      

    except:

      print('Failed to Launch Upvoter')

      failed += 1
      dc_plus.vote_fails += failed
