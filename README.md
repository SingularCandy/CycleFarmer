# Cycle Farmer
You a simple replit farmer for Cycles

## How to Use
You make accounts and import them into the `cache.cycle` file. That isn't much but we are working on an account maker for it. and a discord server for replit accounts and farmer bots.

1. Simple Handler which you can use!
```py
## Example for Upvoting Post

dc_plus.upvote("POST_URL", "AMOUNT")
```

## Making your own Script
Right now, you cant do much, other than make your own script and upvote posts. Making  your own script is easy. Follow the tutorials below

### Retrieving Accounts
Get accounts by using
```py
dc_plus.accounts
```

### Logging In
You can make them log in by using a `for` and `in`..
```py
for account in dc_plus.accounts:
  account.split(":")[0] # Retrives GMAIL
  account.split(":")[1] # Retrives PASSWORD
```

### Upvoting a Post
We have it already, there is a function to upvote (seen above)

### Commenting
There is a simple script to comment on a post with already logged in account, so you add it to your `for` and `in` script.

```
dc_plus.comment('COMMENT_DATA')
```

We also have a list (that you can edit)

```
from random import choice
from random import randint

dc_plus.comment(dc_plus.comments.choice(randint(1, 3)))
```

### Logging Out
Just use the basic logout script.
```py
dc_plus.logout()
```

## Changelog
- Added Comment List
- Added Comment Function
